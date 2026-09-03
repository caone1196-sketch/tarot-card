#!/usr/bin/env python3
"""
check_frame_standard.py — chấm điểm khung viền của từng lá SO VỚI BỘ CHUẨN đã sinh
bằng `scripts/build_frame_standard.py` (mặc định: standards/17-the-star/standard.json).

Khác với thước đo cũ (RMSE dải 60px thô, bị chi phối bởi màu nền của lá), ở đây mọi
phép đo đều CHỈ lấy vùng khung theo `frame-mask.png` và được chuẩn hoá theo từng ảnh,
nên "nền đêm tối" hay "nền parchment" không còn tự động gây lệch.

Chỉ số (dùng để quyết định ĐẠT/KHÔNG):
  size          784x1360 đúng chuẩn
  coverage      |độ phủ kim tuyến toàn lá − chuẩn| <= tolerance.gold_coverage_abs
  struct_corr   Pearson giữa hồ sơ độ phủ theo cột+hàng (đã chuẩn hoá) và của chuẩn
                >= tolerance.band_struct_corr_min     -> "viền đặt đúng chỗ chưa"
  ink_iou       độ chồng khít phần MỰC VIỀN (mask nhị phân, nới ±3px) trong vùng khung
                >= tolerance.frame_ink_iou_min        -> "đúng hình dạng viền chưa"
  band          độ dày dải viền trái/phải/trên/dưới lệch <= tolerance.rule_offset_px
  plates        đĩa huy hiệu trên + ruy băng tên dưới: có/không phải khớp chuẩn

Chạy:
    python3 scripts/check_frame_standard.py                 # quét cả bộ, xuất report
    python3 scripts/check_frame_standard.py --slug wands-08 # 1 lá, in chi tiết
    python3 scripts/check_frame_standard.py --json          # kết quả máy đọc được
Exit code: 0 nếu 100% lá đạt, 1 nếu có lá lệch (dùng được trong CI), 2 nếu thiếu chuẩn.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from build_frame_standard import gold_mask, measure  # noqa: E402

DILATE = 3     # px nới mask mực viền trước khi tính mức chồng khít (tha lỗi 1-2px dịch)


def load_standard(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        std = json.load(f)
    pc = np.loadtxt(os.path.join(os.path.dirname(path), "profile-cols.csv"),
                    delimiter=",", comments="# ")
    pr = np.loadtxt(os.path.join(os.path.dirname(path), "profile-rows.csv"),
                    delimiter=",", comments="# ")
    mask = cv2.imread(os.path.join(os.path.dirname(path), "frame-mask.png"), cv2.IMREAD_GRAYSCALE)
    # Ảnh neo: ưu tiên snapshot `anchor.png` trong thư mục chuẩn; nếu không có thì đọc đúng
    # lá gốc ghi trong standard.json (mặc định build_frame_standard KHÔNG copy ảnh để nhẹ repo).
    d = os.path.dirname(path)
    anchor_img, anchor_src = None, None
    for cand in (os.path.join(d, "anchor.png"), os.path.join(ROOT, std["anchor_card"]["file"])):
        if os.path.exists(cand):
            anchor_img, anchor_src = cv2.imread(cand, cv2.IMREAD_COLOR), cand
            break
    stale = None
    hf = os.path.join(d, "anchor.sha256")
    if anchor_src and anchor_src.endswith("anchor.png") is False and os.path.exists(hf):
        want = open(hf, encoding="utf-8").read().split()[0]
        got = hashlib.sha256(open(anchor_src, "rb").read()).hexdigest()
        if want != got:
            stale = (f"lá neo `{std['anchor_card']['slug']}` đã đổi sau khi sinh chuẩn — "
                     f"chạy lại: python3 scripts/build_frame_standard.py --force")
    return {"std": std, "prof_cols": pc, "prof_rows": pr, "frame_mask": mask,
            "anchor_img": anchor_img, "anchor_src": anchor_src, "stale": stale, "dir": d}


def _std01(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, np.float32)
    return (v - v.mean()) / (v.std() + 1e-6)


def score_card(img_path: str, L: dict) -> dict:
    """Chấm 1 lá. Dùng lại đúng `measure()` của build_frame_standard để định nghĩa số liệu
    giống hệt nhau giữa chuẩn và lá được chấm (khỏi lệch 'ngoài mép' vs 'trong nét kẻ')."""
    std = L["std"]
    tol = std["tolerance"]
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img is None:
        return {"ok": False, "error": "cv2 khong doc duoc anh", "checks": {}}

    h, w = img.shape[:2]
    m = measure(img)
    cov = gold_mask(img).astype(np.float32) / 255.0
    checks: dict[str, dict] = {}

    # 1) kich thuoc
    size_ok = [w, h] == std["card_size_wh"]
    checks["size"] = {"pass": bool(size_ok), "measured": [w, h], "expected": std["card_size_wh"]}

    # 2) do phu kim tuyen toan la — CHI LA THONG TIN (bi mau canh chi phoi)
    cover = m["gold_coverage_total"]
    d = abs(cover - std["frame"]["gold_coverage_total"])
    checks["coverage"] = {"pass": bool(d <= tol["gold_coverage_abs"]), "gating": False,
                          "measured": round(cover, 4), "expected": std["frame"]["gold_coverage_total"],
                          "delta": round(d, 4), "tolerance": tol["gold_coverage_abs"]}

    # 3) tuong quan cau truc ho so vien (bat bien voi mau nen)
    corr = 0.0
    pc, pr = L["prof_cols"], L["prof_rows"]
    my_pc, my_pr = m["_profile_col_head"], m["_profile_row_head"]
    if len(my_pc) == pc.size and len(my_pr) == pr.size:
        a = np.concatenate([_std01(my_pc), _std01(my_pr)])
        b = np.concatenate([_std01(pc), _std01(pr)])
        corr = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9))
    checks["struct_corr"] = {"pass": bool(corr >= tol["band_struct_corr_min"]), "gating": False,
                             "measured": round(corr, 4), "min": tol["band_struct_corr_min"]}

    # 4) muc vien chong khit (chi trong vung khung cua chuan)
    fmask = (L["frame_mask"] > 127).astype(np.uint8)
    ref_img = L["anchor_img"]
    if ref_img is not None and ref_img.shape[:2] == (h, w):
        k = np.ones((2 * DILATE + 1, 2 * DILATE + 1), np.uint8)
        mine = cv2.dilate((cov > 0.35).astype(np.uint8), k)
        ref = cv2.dilate((gold_mask(ref_img) > 0).astype(np.uint8), k)
        both = np.logical_and(mine, ref)[fmask > 0].sum()
        any_ = np.logical_or(mine, ref)[fmask > 0].sum()
        iou = float(both / any_) if any_ else 0.0
    else:
        # lá neo thiếu ảnh / khác kích thước → không đo được mức chồng khít, ép về 0
        # (main() đã cảnh báo riêng bằng shape của frame-mask và sha256 của lá neo)
        iou = 0.0
    thr = tol["frame_ink_iou_min"]
    checks["ink_iou"] = {"pass": bool(iou >= thr), "measured": round(iou, 4), "min": thr}

    # 5a) VỊ TRÍ NÉT KẺ — chỉ số bất biến với màu cảnh: đỉnh |đạo hàm| của hồ sơ kim tuyến
    peak_ref = (std["frame"].get("rule_peak_px") or {})
    peak_mine = {"left": m.get("rule_peak_left_px"), "top": m.get("rule_peak_top_px"),
                 "right": m.get("rule_peak_right_px"), "bottom": m.get("rule_peak_bottom_px")}
    if peak_ref:
        pd_ = {kk: (abs(peak_mine[kk] - peak_ref[kk]) if peak_mine[kk] is not None and peak_ref[kk] is not None
                    else 999) for kk in peak_ref}
        checks["rule_peak"] = {"pass": bool(max(pd_.values()) <= tol["rule_peak_px"]),
                               "measured": peak_mine, "expected": peak_ref,
                               "delta_px": {kk: int(v) for kk, v in pd_.items()},
                               "tolerance": tol["rule_peak_px"]}
    else:
        checks["rule_peak"] = {"pass": False, "note": "chuan schema 1 — chay lai build_frame_standard.py --force"}

    # 5b) do dai dai vien (chi la thong tin: phu thuoc canh tran mép hay khong)
    band_ref = std["frame"]["band_px"]
    deltas = {kk: int(abs(m["frame_band_px"][kk] - band_ref[kk])) for kk in band_ref}
    checks["band"] = {"pass": bool(max(deltas.values()) <= tol["rule_offset_px"]), "gating": False,
                      "measured": m["frame_band_px"], "expected": band_ref,
                      "delta_px": deltas, "tolerance": tol["rule_offset_px"]}

    # 6) dia huy hieu + ruy bang ten la
    plates_ref = std["plates"]
    plates_mine = m["plates"]
    plates_ok = all(plates_mine[kk]["present"] == plates_ref[kk]["present"] for kk in plates_ref)
    checks["plates"] = {"pass": bool(plates_ok),
                        "measured": {kk: plates_mine[kk]["present"] for kk in plates_mine},
                        "expected": {kk: plates_ref[kk]["present"] for kk in plates_ref}}

    gating = std.get("gating_checks") or [k for k in checks if not k.startswith("_")]
    failed = sorted(k for k, c in checks.items()
                    if k in gating and not c.get("pass") and not k.startswith("_"))
    return {"ok": bool(not failed), "size_wh": [w, h], "checks": checks, "failed": failed}


def load_deck() -> list[dict]:
    with open(os.path.join(ROOT, "cards", "deck.json"), "r", encoding="utf-8") as f:
        return json.load(f)["cards"]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="QA khung viền theo bộ chuẩn đã sinh.")
    ap.add_argument("--standard", default=os.path.join("standards", "17-the-star", "standard.json"))
    ap.add_argument("--slug", default=None, help="chỉ chấm 1 lá (theo slug)")
    ap.add_argument("--json", action="store_true", help="in ket qua may doc duoc")
    ap.add_argument("--no-write-report", action="store_true", help="khong ghi file report")
    a = ap.parse_args(argv)

    spath = a.standard if os.path.isabs(a.standard) else os.path.join(ROOT, a.standard)
    if not os.path.exists(spath):
        print(f"[loi] chua bo chuan: {spath}\n"
              f"      chay:  python3 scripts/build_frame_standard.py --force", file=sys.stderr)
        return 2
    L = load_standard(spath)
    if L.get("stale"):
        print(f"[canh bao] {L['stale']}", file=sys.stderr)
    if L["anchor_img"] is None:
        print(f"[loi] khong doc duoc la neo ({L['std']['anchor_card']['file']}) — khong the so sanh", file=sys.stderr)
        return 2

    if L["anchor_img"] is not None and L["frame_mask"].shape[:2] != L["anchor_img"].shape[:2]:
        print("[canh bao] frame-mask.png khong cung kich thuoc la neo — chay lai build_frame_standard.py",
              file=sys.stderr)

    cards = load_deck()
    if a.slug:
        cards = [c for c in cards if c["slug"] == a.slug]
        if not cards:
            print(f"[loi] khong co slug `{a.slug}` trong cards/deck.json", file=sys.stderr)
            return 2

    rows = []
    for c in cards:
        r = score_card(os.path.join(ROOT, "cards", c["image"]), L)
        r["slug"] = c["slug"]
        r["title"] = c.get("title", "")
        rows.append(r)

    rows.sort(key=lambda r: (r["ok"], ",".join(r.get("failed", []))))
    n_ok = sum(1 for r in rows if r["ok"])

    if a.json:
        print(json.dumps({"standard": os.path.relpath(spath, ROOT), "total": len(rows),
                          "pass": n_ok, "results": rows}, ensure_ascii=False, indent=2))
    else:
        anchor = L["std"]["anchor_card"]["slug"]
        print(f"Chuan khung: `{anchor}`  ({os.path.relpath(spath, ROOT)})")
        print(f"Kich thuoc chuan {L['std']['card_size_wh']} | kieu vien: {L['std']['frame_style']} | "
              f"do phu kim tuyen {L['std']['frame']['gold_coverage_total'] * 100:.1f}%")
        print(f"Dai vien chuan: {L['std']['frame']['band_px']} | dia huy: "
              f"{L['std']['plates']['medallion']['present']} | ruy bang: {L['std']['plates']['ribbon']['present']}")
        print("-" * 96)
        print(f"{'slug':14s} {'kq':4s} {'phu%':7s} {'corr':7s} {'iou':7s} {'peak_lech(px)':13s} "
              f"{'plate':6s} cac chi tieu LECH")
        for r in rows:
            if "error" in r and not r.get("checks"):
                print(f"{r['slug']:14s} LOI  -  -  -  -  -  {r['error']}")
                continue
            c = r["checks"]
            rp = c.get("rule_peak", {}).get("delta_px", {"x": 0})
            print(f"{r['slug']:14s} {'DAT' if r['ok'] else 'LECH':4s} "
                  f"{c['coverage']['measured'] * 100:6.1f}  {c['struct_corr']['measured']:6.3f}  "
                  f"{c['ink_iou']['measured']:6.3f}  "
                  f"{max(rp.values()):13d}  "
                  f"{'ok' if c['plates']['pass'] else 'lech':6s} "
                  f"{','.join(r['failed']) if r['failed'] else '—'}")
        print("-" * 96)
        print(f"DAT {n_ok}/{len(rows)}  |  LECH {len(rows) - n_ok}/{len(rows)}")

    if not a.no_write_report and not a.slug and not a.json:
        rep_dir = os.path.dirname(spath)
        with open(os.path.join(rep_dir, "frame-report.json"), "w", encoding="utf-8") as f:
            json.dump({"standard": os.path.relpath(spath, ROOT), "anchor": anchor,
                       "total": len(rows), "pass": n_ok, "results": rows},
                      f, ensure_ascii=False, indent=2)
        lines = [f"# Báo cáo QA khung viền — chuẩn `{anchor}`", "",
                 f"- Sinh bởi: `scripts/check_frame_standard.py` · chuẩn: `{os.path.relpath(spath, ROOT)}`",
                 f"- Chuẩn: {L['std']['card_size_wh'][0]}×{L['std']['card_size_wh'][1]} · "
                 f"{L['std']['frame_style']} · độ phủ kim tuyến "
                 f"{L['std']['frame']['gold_coverage_total'] * 100:.1f}%",
                 f"- Kết quả: **{n_ok}/{len(rows)} ĐẠT**, {len(rows) - n_ok} lá lệch chuẩn", "",
                 "| Lá | Kết quả | Phủ kim tuyến | Tương quan cấu trúc | chồng khít mực viền | "
                 "Lệch dải viền (px) | Plate | Chỉ tiêu lệch |",
                 "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            c = r.get("checks") or {}
            if not c:
                lines.append(f"| `{r['slug']}` | LỖI | — | — | — | — | — | {r.get('error', '')} |")
                continue
            lines.append(
                f"| `{r['slug']}` | {'✅ ĐẠT' if r['ok'] else '⚠️ lệch'} | "
                f"{c['coverage']['measured'] * 100:.1f}% | {c['struct_corr']['measured']:.3f} | "
                f"{c['ink_iou']['measured']:.3f} | {max(c['band']['delta_px'].values())} | "
                f"{'khớp' if c['plates']['pass'] else 'lệch'} | "
                f"{', '.join(r['failed']) or '—'} |")
        with open(os.path.join(rep_dir, "frame-report.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"[ok] da ghi report: {os.path.relpath(rep_dir, ROOT)}/frame-report.{{json,md}}")

    return 0 if n_ok == len(rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
