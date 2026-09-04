#!/usr/bin/env python3
"""
finish_card.py — bước SAU khi model sinh cảnh.

Model chỉ vẽ CẢNH (full-bleed, không khung, không chữ). Script này:
  1. Crop/resize cover sang 784×1360 (7:12)
  2. Dán mực viền vàng ĐÚNG của The Star (extract từ cards/17-the-star.png)
  3. Viết tên lá bằng Cinzel Decorative, vàng cổ, không ruy băng
  4. Chấm QA theo standards/17-the-star (gating: size + ink_iou)

Như vậy ink_iou không còn phụ thuộc model vẽ khung — hết vòng vẽ-lại vì lệch viền.

Dùng:
    python3 scripts/finish_card.py <anh-tho.png> --slug 06-lovers
    python3 scripts/finish_card.py <anh-tho.png> --slug 06-lovers --install
    python3 scripts/finish_card.py --self-test
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from build_frame_standard import (  # noqa: E402
    composite_frame,
    extract_frame_overlay,
    gold_mask,
)

CARDS_JSON = os.path.join(ROOT, "tarot prompt", "cards.json")
ANCHOR = os.path.join(ROOT, "cards", "17-the-star.png")
STANDARD_JSON = os.path.join(ROOT, "standards", "17-the-star", "standard.json")
FRAME_MASK = os.path.join(ROOT, "standards", "17-the-star", "frame-mask.png")
REGEN_DIR = os.path.join(ROOT, "cards", "_regen")
FONT_PATHS = [
    os.path.join(ROOT, "variants", "fonts", "CinzelDecorative-Regular.ttf"),
    os.path.join(ROOT, "variants", "fonts", "CinzelDecorative-Bold.ttf"),
]

CARD_W, CARD_H = 784, 1360
TITLE_GOLD = (242, 216, 136)       # vàng sáng đo từ chữ The Star
TITLE_STROKE = (42, 28, 10)
TITLE_BASELINE_Y = 1286            # đáy glyph — trên nét kẻ đáy (~1337)
TITLE_MAX_WIDTH_FRAC = 0.70
TITLE_MAX_SIZE = 64
TITLE_MIN_SIZE = 26

_OVERLAY = None
_CARDS = None


def load_cards() -> dict[str, dict]:
    global _CARDS
    if _CARDS is None:
        with open(CARDS_JSON, encoding="utf-8") as f:
            _CARDS = {c["slug"]: c for c in json.load(f)["cards"]}
    return _CARDS


def card_size() -> tuple[int, int]:
    if os.path.exists(STANDARD_JSON):
        with open(STANDARD_JSON, encoding="utf-8") as f:
            wh = json.load(f).get("card_size_wh") or [CARD_W, CARD_H]
            return int(wh[0]), int(wh[1])
    return CARD_W, CARD_H


def load_overlay() -> np.ndarray:
    global _OVERLAY
    if _OVERLAY is None:
        anchor = cv2.imread(ANCHOR, cv2.IMREAD_COLOR)
        if anchor is None:
            raise FileNotFoundError(f"khong doc duoc la neo: {ANCHOR}")
        tw, th = card_size()
        if (anchor.shape[1], anchor.shape[0]) != (tw, th):
            anchor = cv2.resize(anchor, (tw, th), interpolation=cv2.INTER_AREA)
        _OVERLAY = extract_frame_overlay(anchor)
    return _OVERLAY


def fit_to_card(img_bgr: np.ndarray, size: tuple[int, int] | None = None,
                mode: str = "cover") -> np.ndarray:
    """Đưa ảnh về 784×1360. `cover` = cắt giữa (lệch nhẹ lên trên để giữ mặt);
    `letterbox` = thêm viền màu mép."""
    tw, th = size or card_size()
    h, w = img_bgr.shape[:2]
    if (w, h) == (tw, th):
        return img_bgr
    target_aspect = tw / th
    src_aspect = w / h
    if mode == "letterbox":
        scale = min(tw / w, th / h)
        nw, nh = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
        interp = cv2.INTER_AREA if scale < 1 else cv2.INTER_CUBIC
        resized = cv2.resize(img_bgr, (nw, nh), interpolation=interp)
        canvas = np.zeros((th, tw, 3), np.uint8)
        canvas[:] = img_bgr[h // 2, w // 2]
        canvas[(th - nh) // 2:(th - nh) // 2 + nh,
               (tw - nw) // 2:(tw - nw) // 2 + nw] = resized
        return canvas
    # cover: cắt cho đúng 7:12 rồi scale
    if src_aspect > target_aspect:
        nw = max(1, int(round(h * target_aspect)))
        x0 = (w - nw) // 2
        crop = img_bgr[:, x0:x0 + nw]
    else:
        nh = max(1, int(round(w / target_aspect)))
        y0 = max(0, (h - nh) // 6)          # thiên về phía trên (giữ đầu)
        y0 = min(y0, h - nh)
        crop = img_bgr[y0:y0 + nh, :]
    interp = cv2.INTER_AREA if crop.shape[0] > th else cv2.INTER_CUBIC
    return cv2.resize(crop, (tw, th), interpolation=interp)


def _font(path_ok: str | None, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if path_ok:
        return ImageFont.truetype(path_ok, size)
    return ImageFont.load_default()


def _font_file() -> str | None:
    for p in FONT_PATHS:
        if os.path.exists(p):
            return p
    return None


def fit_title_font(text: str, max_w: int, max_h: int = 70):
    path = _font_file()
    chosen, bbox = None, None
    for size in range(TITLE_MAX_SIZE, TITLE_MIN_SIZE - 1, -1):
        font = _font(path, size)
        bb = font.getbbox(text)
        w, h = bb[2] - bb[0], bb[3] - bb[1]
        if w <= max_w and h <= max_h:
            chosen, bbox = font, bb
            break
    if chosen is None:
        chosen = _font(path, TITLE_MIN_SIZE)
        bbox = chosen.getbbox(text)
    return chosen, bbox


def neutralize_frame_gold(scene_bgr: np.ndarray, overlay_bgra: np.ndarray) -> np.ndarray:
    """Hạ bão hoà pixel 'vàng' của cảnh trong dải khung (nơi overlay trong suốt).

    Trời hoàng hôn / tóc vàng ở mép lá bị `gold_mask` tính là mực viền → `ink_iou` tụt
    dù nét kẻ đã đúng. Chỉ đụng pixel trong `frame-mask` và alpha overlay thấp.
    """
    if not os.path.exists(FRAME_MASK):
        return scene_bgr
    fmask = cv2.imread(FRAME_MASK, cv2.IMREAD_GRAYSCALE)
    if fmask is None or fmask.shape[:2] != scene_bgr.shape[:2]:
        return scene_bgr
    a = overlay_bgra[:, :, 3]
    extra = (fmask > 127) & (a < 24) & (gold_mask(scene_bgr) > 0)
    if not extra.any():
        return scene_bgr
    hsv = cv2.cvtColor(scene_bgr, cv2.COLOR_BGR2HSV)
    s = hsv[:, :, 1].astype(np.int16)
    v = hsv[:, :, 2].astype(np.int16)
    s[extra] = np.minimum(s[extra], 28)
    v[extra] = np.minimum(v[extra], 200)
    hsv[:, :, 1] = np.clip(s, 0, 255).astype(np.uint8)
    hsv[:, :, 2] = np.clip(v, 0, 255).astype(np.uint8)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


def scrub_title_band(scene_bgr: np.ndarray) -> np.ndarray:
    """Inpaint mực vàng trong dải tên (xóa chữ AI vẽ) trước khi viết tên bằng code."""
    h, w = scene_bgr.shape[:2]
    y0, y1 = 1205, 1312
    x0, x1 = 70, w - 70
    roi = scene_bgr[y0:y1, x0:x1]
    g = gold_mask(roi)
    if int(g.sum()) < 200:
        return scene_bgr
    m = cv2.dilate(g, np.ones((9, 9), np.uint8))
    full = np.zeros(scene_bgr.shape[:2], np.uint8)
    full[y0:y1, x0:x1] = m
    return cv2.inpaint(scene_bgr, full, 5, cv2.INPAINT_TELEA)


def draw_title(scene_bgr: np.ndarray, title: str) -> np.ndarray:
    """Chữ vàng serif trực tiếp trên cảnh — không ruy băng / plaque."""
    if not title:
        return scene_bgr
    h, w = scene_bgr.shape[:2]
    text = title.strip().upper()
    font, bbox = fit_title_font(text, int(w * TITLE_MAX_WIDTH_FRAC))
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (w - tw) // 2 - bbox[0]
    y = TITLE_BASELINE_Y - bbox[3]
    # kẹp không đè nét kẻ đáy / hoa văn góc
    y = max(int(h * 0.82), min(y, h - 90 - th))
    pil = Image.fromarray(cv2.cvtColor(scene_bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    layer = Image.new("RGBA", pil.size, (0, 0, 0, 0))
    dr = ImageDraw.Draw(layer)
    # bóng nhẹ xuống-phải cho chữ nổi trên cảnh sáng lẫn tối
    dr.text((x + 2, y + 3), text, font=font, fill=(10, 6, 2, 140))
    dr.text((x, y), text, font=font, fill=TITLE_GOLD + (255,),
            stroke_width=2, stroke_fill=TITLE_STROKE + (230,))
    out = Image.alpha_composite(pil, layer).convert("RGB")
    return cv2.cvtColor(np.asarray(out), cv2.COLOR_RGB2BGR)


def score(path: str) -> dict | None:
    if not os.path.exists(STANDARD_JSON):
        return None
    try:
        from check_frame_standard import load_standard, score_card
        return score_card(path, load_standard(STANDARD_JSON))
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}", "failed": ["qa"], "checks": {}}


def finish_bgr(scene_bgr: np.ndarray, title: str = "", *,
               mode: str = "cover", frame: bool = True, letter: bool = True) -> np.ndarray:
    img = fit_to_card(scene_bgr, mode=mode)
    if frame:
        ov = load_overlay()
        img = neutralize_frame_gold(img, ov)
        img = composite_frame(img, ov)
    if letter and title:
        img = scrub_title_band(img)
        img = draw_title(img, title)
    return img


def finish_file(src: str, dst: str, slug: str | None = None, *,
                title: str | None = None, mode: str = "cover",
                frame: bool = True, letter: bool = True) -> dict:
    img = cv2.imread(src, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"khong doc duoc anh: {src}")
    if title is None:
        title = ""
        if slug:
            card = load_cards().get(slug)
            if card:
                title = card.get("title") or ""
    out = finish_bgr(img, title, mode=mode, frame=frame, letter=letter)
    os.makedirs(os.path.dirname(os.path.abspath(dst)) or ".", exist_ok=True)
    if not cv2.imwrite(dst, out):
        raise RuntimeError(f"khong ghi duoc: {dst}")
    qa = score(dst)
    return {
        "src": src, "dst": dst, "slug": slug, "title": title,
        "size_wh": [int(out.shape[1]), int(out.shape[0])],
        "ok": bool(qa and qa.get("ok")),
        "failed": (qa or {}).get("failed") or [],
        "ink_iou": ((qa or {}).get("checks") or {}).get("ink_iou", {}).get("measured"),
        "qa": qa,
    }


def infer_slug(path: str) -> str | None:
    base = os.path.splitext(os.path.basename(path))[0]
    for suffix in (".raw", "_raw", "-raw", "_scene", "-scene"):
        if base.endswith(suffix):
            base = base[: -len(suffix)]
    return base if base in load_cards() else None


def self_test() -> int:
    """Sinh cảnh giả (gradient), hoàn thiện, bắt buộc ĐẠT size+ink_iou."""
    tw, th = card_size()
    yy = np.linspace(0, 1, th)[:, None]
    grad = np.dstack([
        np.full((th, tw), 40 + 180 * yy),
        np.full((th, tw), 70 + 90 * yy),
        np.full((th, tw), 140 - 70 * yy),
    ]).astype(np.uint8)
    with tempfile.TemporaryDirectory(prefix="tarot-finish-") as td:
        src = os.path.join(td, "scene.png")
        dst = os.path.join(td, "card.png")
        cv2.imwrite(src, grad)
        r = finish_file(src, dst, slug="17-the-star")
        print(json.dumps({k: v for k, v in r.items() if k != "qa"}, ensure_ascii=False, indent=2))
        if not r["ok"]:
            print(f"[loi] self-test LECH: failed={r['failed']} iou={r['ink_iou']}", file=sys.stderr)
            return 1
        if r["size_wh"] != [tw, th]:
            print(f"[loi] size {r['size_wh']} != {[tw, th]}", file=sys.stderr)
            return 1
        if r["ink_iou"] is None or r["ink_iou"] < 0.55:
            print(f"[loi] ink_iou {r['ink_iou']} < 0.55", file=sys.stderr)
            return 1
        print(f"[ok] self-test DAT  {tw}x{th}  ink_iou={r['ink_iou']:.3f}")
        return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Hoàn thiện lá: crop 7:12 + khung The Star + tên.")
    ap.add_argument("src", nargs="?", help="ảnh cảnh thô (png/jpg)")
    ap.add_argument("--slug", default=None, help="slug lá (mặc định: đoán từ tên file)")
    ap.add_argument("--out", default=None, help="ảnh ra (mặc định: cards/_regen/<slug>.png)")
    ap.add_argument("--title", default=None, help="đè tên lá (mặc định: cards.json)")
    ap.add_argument("--mode", choices=["cover", "letterbox"], default="cover")
    ap.add_argument("--no-frame", action="store_true", help="bỏ dán khung (debug)")
    ap.add_argument("--no-title", action="store_true", help="bỏ viết tên (debug)")
    ap.add_argument("--install", action="store_true",
                    help="chép vào cards/<slug>.png và chạy build_gallery.py")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)

    if a.self_test:
        return self_test()
    if not a.src:
        ap.print_help()
        print("\nVí dụ:  python3 scripts/finish_card.py cards/_regen/06-lovers.raw.png --slug 06-lovers")
        return 2

    slug = a.slug or infer_slug(a.src)
    if a.install and not slug:
        print("[loi] --install can --slug (hoac ten file trung slug)", file=sys.stderr)
        return 2
    dst = a.out
    if not dst:
        name = (slug or os.path.splitext(os.path.basename(a.src))[0]) + ".png"
        dst = os.path.join(ROOT, "cards", name) if a.install else os.path.join(REGEN_DIR, name)

    r = finish_file(a.src, dst, slug=slug, title=a.title,
                    mode=a.mode, frame=not a.no_frame, letter=not a.no_title)
    tag = "DAT" if r["ok"] else "LECH"
    iou = "—" if r["ink_iou"] is None else f"{r['ink_iou']:.3f}"
    rel = os.path.relpath(dst, ROOT)
    print(f"[{tag}] {slug or '?'}  {r['size_wh'][0]}x{r['size_wh'][1]}  ink_iou={iou}  -> {rel}")
    if r["failed"]:
        print(f"       chi tieu lech: {', '.join(r['failed'])}")

    if a.install:
        if not slug:
            return 1
        dest = os.path.join(ROOT, "cards", slug + ".png")
        if os.path.abspath(dst) != os.path.abspath(dest):
            img = cv2.imread(dst, cv2.IMREAD_COLOR)
            cv2.imwrite(dest, img)
            print(f"[ok] da cai vao {os.path.relpath(dest, ROOT)}")
        import subprocess
        gallery = os.path.join(ROOT, "scripts", "build_gallery.py")
        subprocess.run([sys.executable, gallery], cwd=ROOT, check=False)

    return 0 if r["ok"] or r["qa"] is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
