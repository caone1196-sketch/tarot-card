#!/usr/bin/env python3
"""
build_frame_standard.py — sinh BỘ CHUẨN KHUNG (frame standard) từ lá neo hiện tại.

Mặc định neo theo `cards/17-the-star.png` (THE STAR) như AGENTS.md mục 2–3, và xuất ra
`standards/<anchor>/` gồm:

  standard.json      chuẩn máy đọc được: độ dày dải viền, vị trí nét kẻ, vùng medallion/ruy băng,
                     tỉ lệ diện tích kim tuyến, ngưỡng đạt cho QA
  frame-mask.png     W×H, TRẮNG = vùng khung (được chấm điểm), ĐEN = cửa sổ nội dung (không chấm)
  anchor.sha256      hash của lá neo TẠI THỜI ĐIỂM sinh chuẩn — QA sẽ cảnh báo nếu lá neo
                     đã bị sửa mà chuẩn chưa regenerate (không copy ảnh để tránh nặng repo)
  profile-cols.csv   hồ sơ độ phủ kim tuyến theo từng cột x (0..MAX_SCAN-1)
  profile-rows.csv   hồ sơ độ phủ kim tuyến theo từng hàng y (0..MAX_SCAN-1)

Cách đo (mọi con số đều do đo mà ra, không hard-code "số đẹp"):
  1. Mask "kim tuyến" = HSV hue 12..48, sat>=35, val>=80 (bắt vàng đồng trên cả nền đêm tối
     lẫn parchment).
  2. Cột nào có độ phủ > LINE_COVER được coi là "nét kẻ dọc"; gom thành cụm liên tiếp -> vị trí nét.
     Hàng làm tương tự cho "nét kẻ ngang".
  3. Cửa sổ nội dung = hộp nằm giữa nét dọc trong cùng (trái/phải) và nét ngang trong cùng
     (trên/dưới), co thêm INSET px.
  4. Medallion/ribbon: ROI cố định theo tỉ lệ W,H; "có đĩa" nếu độ phủ kim tuyến trong ROI
     >= PLATE_COVER.

Chạy:
    python3 scripts/build_frame_standard.py                     # neo = 17-the-star
    python3 scripts/build_frame_standard.py --anchor cards/00-fool.png
    python3 scripts/build_frame_standard.py --out standards/the-star --force
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINE_COVER = 0.35    # độ phủ cột/hàng tối thiểu để coi là "nét kẻ"
PLATE_COVER = 0.35   # độ phủ kim tuyến trong ROI để coi là "có đĩa huy hiệu / ruy băng"
INSET = 4            # px thu thêm khi xác định cửa sổ nội dung
MAX_SCAN = 200       # chỉ quét trong 200px tính từ mép để tìm nét kẻ viền
GOLD_HSV = (12, 35, 80, 48, 255, 255)   # hmin,smin,vmin,hmax,smax,vmax


def gold_mask(img_bgr: np.ndarray) -> np.ndarray:
    """Mask 'kim tuyến': vàng đồng, đọc được trên cả nền đêm tối lẫn nền parchment."""
    h_lo, s_lo, v_lo, h_hi, s_hi, v_hi = GOLD_HSV
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, (h_lo, s_lo, v_lo), (h_hi, s_hi, v_hi))


def runs_of_true(flags) -> list[tuple[int, int]]:
    """[T,T,F,T] -> [(0,1),(3,3)]  (đoạn đóng [begin, end])."""
    out: list[tuple[int, int]] = []
    begin = None
    for i, f in enumerate(flags):
        if f and begin is None:
            begin = i
        elif not f and begin is not None:
            out.append((begin, i - 1))
            begin = None
    if begin is not None:
        out.append((begin, len(flags) - 1))
    return out


def measure(img_bgr: np.ndarray) -> dict:
    h, w = img_bgr.shape[:2]
    cov = gold_mask(img_bgr).astype(np.float32) / 255.0
    col = cov.mean(axis=0)          # độ phủ theo cột  (dài W)
    row = cov.mean(axis=1)          # độ phủ theo hàng (dài H)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)

    left_runs = runs_of_true(col[:MAX_SCAN] > LINE_COVER)
    right_runs = [(w - 1 - e, w - 1 - b)
                  for b, e in runs_of_true((col[w - MAX_SCAN:] > LINE_COVER)[::-1])]
    top_runs = runs_of_true(row[:MAX_SCAN] > LINE_COVER)
    bot_runs = [(h - 1 - e, h - 1 - b)
                for b, e in runs_of_true((row[h - MAX_SCAN:] > LINE_COVER)[::-1])]

    def inner_edge(runs, side):
        if not runs:
            return None
        return runs[-1][1] + 1 if side == "lo" else runs[-1][0] - 1

    x0 = inner_edge(left_runs, "lo")
    x1 = inner_edge(right_runs, "hi")
    y0 = inner_edge(top_runs, "lo")
    y1 = inner_edge(bot_runs, "hi")

    med_sl = (slice(int(h * 0.045), int(h * 0.190)), slice(int(w * 0.28), int(w * 0.72)))
    rib_sl = (slice(int(h * 0.855), int(h * 0.985)), slice(int(w * 0.18), int(w * 0.82)))

    def roi_stats(sl):
        m, g = cov[sl], gray[sl]
        return {
            "box_x0y0x1y1": [int(sl[1].start), int(sl[0].start), int(sl[1].stop), int(sl[0].stop)],
            "gold_coverage": round(float(m.mean()), 4),
            "luma_mean": round(float(g.mean()), 1),
            "luma_std": round(float(g.std()), 1),
        }

    med_s, rib_s = roi_stats(med_sl), roi_stats(rib_sl)

    # Lá nền sáng có viền liền mạch (không có "nét kẻ" rời) -> fallback theo ngưỡng độ phủ 0.9
    def first_cover(profile, thr=0.9):
        idx = np.flatnonzero(profile > thr)
        return int(idx[0]) if idx.size else None

    fallback = any(v is None for v in (x0, x1, y0, y1))
    if fallback:
        x0 = first_cover(col[:MAX_SCAN]) or 0
        x1 = w - (first_cover(col[w - MAX_SCAN:][::-1]) or 0)
        y0 = first_cover(row[:MAX_SCAN]) or 0
        y1 = h - (first_cover(row[h - MAX_SCAN:][::-1]) or 0)

    win = [int(x0) + INSET, int(y0) + INSET, int(x1) - INSET, int(y1) - INSET]
    win = [max(0, win[0]), max(0, win[1]), min(w, win[2]), min(h, win[3])]

    return {
        "size_wh": [int(w), int(h)],
        "aspect": round(w / h, 5),
        "gold_coverage_total": round(float(cov.mean()), 4),
        "lines": {
            "vertical_runs": [[int(a), int(b)] for a, b in left_runs],
            "vertical_runs_right": [[int(a), int(b)] for a, b in right_runs],
            "horizontal_runs": [[int(a), int(b)] for a, b in top_runs],
            "horizontal_runs_bottom": [[int(a), int(b)] for a, b in bot_runs],
        },
        "rule_offset_left_px": int(left_runs[0][0]) if left_runs else None,
        "rule_offset_top_px": int(top_runs[0][0]) if top_runs else None,
        "frame_band_px": {"left": int(win[0]), "right": int(w - win[2]),
                          "top": int(win[1]), "bottom": int(h - win[3])},
        "content_window_xyxy": win,
        "plates": {
            "medallion": {**med_s, "present": med_s["gold_coverage"] >= PLATE_COVER},
            "ribbon": {**rib_s, "present": rib_s["gold_coverage"] >= PLATE_COVER},
        },
        "_fallback_used": bool(fallback),
        "_profile_col_head": [round(float(v), 4) for v in col[:MAX_SCAN]],
        "_profile_row_head": [round(float(v), 4) for v in row[:MAX_SCAN]],
    }


def build_frame_mask(h: int, w: int, win: list[int]) -> np.ndarray:
    """TRẮNG = vùng khung (ngoài cửa sổ nội dung), ĐEN = nội dung."""
    m = np.full((h, w), 255, np.uint8)
    m[win[1]:win[3], win[0]:win[2]] = 0
    return m


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Sinh bộ chuẩn khung từ lá neo.")
    ap.add_argument("--anchor", default=os.path.join("cards", "17-the-star.png"),
                    help="đường dẫn lá dùng làm chuẩn (mặc định: cards/17-the-star.png)")
    ap.add_argument("--out", default=None, help="thư mục xuất (mặc định standards/<tên-lá-neo>)")
    ap.add_argument("--force", action="store_true", help="ghi đè nếu chuẩn đã tồn tại")
    ap.add_argument("--copy-anchor", action="store_true",
                    help="sao chép ảnh lá neo vào thư mục chuẩn (~2.6MB/lần; mặc định KHÔNG copy)")
    a = ap.parse_args(argv)

    anchor = a.anchor if os.path.isabs(a.anchor) else os.path.join(ROOT, a.anchor)
    if not os.path.exists(anchor):
        print(f"[loi] khong tim thay la neo: {anchor}", file=sys.stderr)
        return 2
    name = os.path.splitext(os.path.basename(anchor))[0]
    outdir = a.out or os.path.join("standards", name)
    outdir = outdir if os.path.isabs(outdir) else os.path.join(ROOT, outdir)

    img = cv2.imread(anchor, cv2.IMREAD_COLOR)
    if img is None:
        print(f"[loi] cv2 khong doc duoc anh: {anchor}", file=sys.stderr)
        return 2
    h, w = img.shape[:2]
    m = measure(img)

    if os.path.exists(os.path.join(outdir, "standard.json")) and not a.force:
        print(f"[loi] chuan da ton tai: {outdir} — dung --force de ghi de", file=sys.stderr)
        return 3

    os.makedirs(outdir, exist_ok=True)
    raw = open(anchor, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    with open(os.path.join(outdir, "anchor.sha256"), "w", encoding="utf-8") as f:
        f.write(f"{digest}  {os.path.relpath(anchor, ROOT).replace(os.sep, '/')}\n")
    if a.copy_anchor:                        # tuỳ chọn: lưu snapshot nếu muốn "đóng băng" chuẩn
        shutil.copy2(anchor, os.path.join(outdir, "anchor.png"))

    cv2.imwrite(os.path.join(outdir, "frame-mask.png"),
                build_frame_mask(h, w, m["content_window_xyxy"]))
    np.savetxt(os.path.join(outdir, "profile-cols.csv"), np.array(m["_profile_col_head"]),
               fmt="%.4f", delimiter=",", header=f"gold coverage per column x=0..{MAX_SCAN-1} ({name})",
               comments="# ")
    np.savetxt(os.path.join(outdir, "profile-rows.csv"), np.array(m["_profile_row_head"]),
               fmt="%.4f", delimiter=",", header=f"gold coverage per row y=0..{MAX_SCAN-1} ({name})",
               comments="# ")

    std = {
        "schema": 1,
        "anchor_card": {"slug": name, "file": os.path.relpath(anchor, ROOT).replace(os.sep, "/")},
        "anchor_sha256": digest,
        "anchor_bytes": len(raw),
        "derived_from": os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, "/"),
        "card_size_wh": [w, h],
        "aspect_ratio": round(w / h, 5),
        "aspect_ratio_target": round(7 / 12, 5),
        "frame": {
            "gold_coverage_total": m["gold_coverage_total"],
            "rule_offset_left_px": m["rule_offset_left_px"],
            "rule_offset_top_px": m["rule_offset_top_px"],
            "band_px": m["frame_band_px"],
            "content_window_xyxy": m["content_window_xyxy"],
            "lines": m["lines"],
        },
        "plates": m["plates"],
        "frame_style": "thin-line-art" if m["gold_coverage_total"] < 0.20 else "heavy-filigree",
        "tolerance": {
            "gold_coverage_abs": 0.05,      # |độ phủ kim tuyến − chuẩn| tối đa
            "rule_offset_px": 6,            # độ dày dải viền mỗi phía lệch tối đa
            "band_struct_corr_min": 0.90,   # tương quan hồ sơ viền (bất biến màu nền)
            "frame_ink_iou_min": 0.55,      # mức chồng khít của mực viền trong vùng khung
        },
        "measure_hints": {
            "fallback_used": m["_fallback_used"],
            "line_cover_thr": LINE_COVER,
            "plate_cover_thr": PLATE_COVER,
            "inset_px": INSET,
            "max_scan_px": MAX_SCAN,
            "gold_hsv": list(GOLD_HSV),
        },
    }
    with open(os.path.join(outdir, "standard.json"), "w", encoding="utf-8") as f:
        json.dump(std, f, indent=2, ensure_ascii=False)

    print(f"[ok] chuan khung da sinh tu `{name}` -> {os.path.relpath(outdir, ROOT)}/")
    print(f"     kich thuoc {w}x{h} (ty so {std['aspect_ratio']}) | kieu vien: {std['frame_style']}")
    print(f"     do phu kim tuyen toan la: {m['gold_coverage_total'] * 100:.1f}%")
    print(f"     net ke: trai x={m['rule_offset_left_px']}  tren y={m['rule_offset_top_px']}")
    print(f"     cua so noi dung: {m['content_window_xyxy']} (bang trai/phai/tren/duoi = {m['frame_band_px']})")
    print(f"     dia huy hieu: {'CO' if m['plates']['medallion']['present'] else 'KHONG'}"
          f" | ruy bang ten la: {'CO' if m['plates']['ribbon']['present'] else 'KHONG'}")
    if m["_fallback_used"]:
        print("     [!] khong nhan dien duoc net ke roi -> dung phuong an nguong 0.9 "
              "(xem measure_hints trong standard.json)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
