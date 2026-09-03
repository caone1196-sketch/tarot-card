#!/usr/bin/env python3
"""
compose_fullbleed.py — ghép lá bài theo họ khung FULL-BLEED của lá neo `cards/17-the-star.png`
(chuẩn 2026-09-03: cảnh tràn sát 4 mép, chỉ có nét kẻ vàng mảnh cách mép ~18 px + 4 hoa văn góc
vẽ ĐÈ lên cảnh, tên lá viết thẳng lên tranh, KHÔNG medallion / KHÔNG ruy băng / KHÔNG lề giấy da).

3 lớp (theo thứ tự vẽ):
  1. SCENE  — ảnh cảnh do model vẽ, phóng/cắt về đúng 784×1360 (full-bleed).
  2. FRAME  — mực viền vàng tách bằng code từ chính lá neo (nét kẻ + 4 góc), nên khung của lá
              mới chồng khít 100 % pixel với lá neo (`check_frame_standard.py` → ink_iou ≈ 1).
  3. TITLE  — tên lá (đúng `title` trong `tarot prompt/cards.json`) bằng chữ serif vàng cổ,
              có bóng mờ để đọc được trên mọi nền; vị trí/kích thước mặc định đo từ lá neo
              (chữ THE STAR: y ≈ 1218..1268, cao ≈ 50 px, giữa lá).

Chạy:
    python3 scripts/compose_fullbleed.py <slug> <scene.png> [--out cards/<slug>.png]
        [--anchor cards/17-the-star.png] [--font variants/fonts/CinzelDecorative-Regular.ttf]
        [--title-y 1243] [--title-h 50] [--no-title] [--dump-layers DIR]

Ví dụ:
    python3 scripts/compose_fullbleed.py 17-the-star cards/_regen/17-the-star.scene.png
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_JSON = os.path.join(ROOT, "tarot prompt", "cards.json")
DEFAULT_ANCHOR = os.path.join(ROOT, "cards", "17-the-star.png")
DEFAULT_FONT = os.path.join(ROOT, "variants", "fonts", "CinzelDecorative-Regular.ttf")
SIZE_WH = (784, 1360)

# Cùng ngưỡng "kim tuyến" với build_frame_standard.py (GOLD_HSV) để khung tách ra == khung được đo.
GOLD_HSV_LO = (12, 35, 80)
GOLD_HSV_HI = (48, 255, 255)

# Vị trí nét kẻ của lá neo (đo bởi build_frame_standard.py → standards/17-the-star/standard.json,
# mục frame.lines): mỗi cạnh có 2 nét song song. Chỉ lấy mực vàng ĐÚNG tại các nét này (±1 px),
# cộng với hoa văn 4 góc = các thành phần liên thông DÍNH VÀO nét kẻ, nằm gọn trong ô góc.
RULE_RUNS_X = [(18, 20), (26, 27), (756, 758), (764, 767)]        # nét dọc (trái, phải)
RULE_RUNS_Y = [(21, 23), (29, 30), (1329, 1330), (1337, 1339)]    # nét ngang (trên, dưới)
RULE_PAD = 1
CORNER = 260            # ô vuông ở 4 góc chứa hoa văn (TL kéo vào tới ~x=207/y=159)
MIN_COMP_AREA = 40      # bỏ hạt nhiễu nhỏ dính nét kẻ
TITLE_BOX = (150, 1200, 634, 1290)   # hộp chữ "THE STAR" trên lá neo (chữ đo được y≈1218..1268)


def gold_mask(img_bgr: np.ndarray) -> np.ndarray:
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, GOLD_HSV_LO, GOLD_HSV_HI)


def rule_region(h: int, w: int) -> np.ndarray:
    """Mask các dải mảnh đúng vị trí nét kẻ (dọc + ngang)."""
    reg = np.zeros((h, w), np.uint8)
    for x0, x1 in RULE_RUNS_X:
        reg[:, max(0, x0 - RULE_PAD):min(w, x1 + RULE_PAD + 1)] = 1
    for y0, y1 in RULE_RUNS_Y:
        reg[max(0, y0 - RULE_PAD):min(h, y1 + RULE_PAD + 1), :] = 1
    return reg


def corner_region(h: int, w: int) -> np.ndarray:
    reg = np.zeros((h, w), np.uint8)
    for ys, xs in ((slice(0, CORNER), slice(0, CORNER)), (slice(0, CORNER), slice(w - CORNER, w)),
                   (slice(h - CORNER, h), slice(0, CORNER)), (slice(h - CORNER, h), slice(w - CORNER, w))):
        reg[ys, xs] = 1
    return reg


def extract_frame_layer(anchor_bgr: np.ndarray) -> Image.Image:
    """Lớp RGBA chỉ chứa mực viền vàng của lá neo (nét kẻ + hoa văn 4 góc), alpha mềm 1 px.

    Cách lọc (không tin màu đơn thuần, vì cảnh của lá neo cũng có pixel vàng):
      1. Nét kẻ = kim tuyến tại đúng toạ độ nét kẻ đã đo (dải ±1 px).
      2. Hoa văn góc = thành phần liên thông của kim tuyến trong ô góc mà có pixel chạm nét kẻ.
         Sao/chữ/vật thể của cảnh không chạm nét kẻ → bị loại.
    """
    h, w = anchor_bgr.shape[:2]
    gold = gold_mask(anchor_bgr)
    rules = rule_region(h, w)
    corners = corner_region(h, w)

    ink_rules = cv2.bitwise_and(gold, gold, mask=rules)
    cand = cv2.bitwise_and(gold, gold, mask=cv2.bitwise_or(rules, corners))
    n, lab, st, _ = cv2.connectedComponentsWithStats(cand, 8)
    keep = ink_rules.copy()
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] < MIN_COMP_AREA:
            continue
        comp = lab == i
        if (ink_rules[comp] > 0).any():          # có dính nét kẻ
            keep[comp] = 255
    # nới 1 px + làm mềm để nét vàng không bị răng cưa khi đè lên cảnh tối
    alpha = cv2.dilate(keep, np.ones((3, 3), np.uint8))
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0)
    rgba = np.dstack([anchor_bgr[:, :, 2], anchor_bgr[:, :, 1], anchor_bgr[:, :, 0], alpha])
    return Image.fromarray(rgba, "RGBA")


def extract_title_layer(anchor_bgr: np.ndarray) -> Image.Image:
    """Lấy nguyên dòng chữ vàng của lá neo trong TITLE_BOX (dùng khi lá đang ghép CHÍNH LÀ lá neo
    hoặc cùng tên) — chữ khớp 100 % với chuẩn, không phụ thuộc font có sẵn."""
    h, w = anchor_bgr.shape[:2]
    x0, y0, x1, y1 = TITLE_BOX
    gold = gold_mask(anchor_bgr)
    box = np.zeros((h, w), np.uint8)
    box[y0:y1, x0:x1] = 1
    ink = cv2.bitwise_and(gold, gold, mask=box)
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink, 8)
    keep = np.zeros_like(ink)
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] >= 25:
            keep[lab == i] = 255
    alpha = cv2.GaussianBlur(cv2.dilate(keep, np.ones((3, 3), np.uint8)), (3, 3), 0)
    # bóng tối mềm phía sau chữ để đọc được trên nền sáng
    shadow_a = cv2.GaussianBlur(cv2.dilate(keep, np.ones((5, 5), np.uint8)), (0, 0), 4)
    shadow = np.dstack([np.zeros((h, w, 3), np.uint8), (shadow_a * 0.8).astype(np.uint8)])
    shadow = np.roll(shadow, (3, 2), axis=(0, 1))
    text = np.dstack([anchor_bgr[:, :, 2], anchor_bgr[:, :, 1], anchor_bgr[:, :, 0], alpha])
    return Image.alpha_composite(Image.fromarray(shadow, "RGBA"), Image.fromarray(text, "RGBA"))


def fit_scene(scene_path: str) -> Image.Image:
    """Phóng/cắt cảnh về đúng 784×1360 (cover, giữ tâm)."""
    im = Image.open(scene_path).convert("RGB")
    W, H = SIZE_WH
    sw, sh = im.size
    scale = max(W / sw, H / sh)
    nw, nh = max(W, round(sw * scale)), max(H, round(sh * scale))
    im = im.resize((nw, nh), Image.LANCZOS)
    left, top = (nw - W) // 2, (nh - H) // 2
    return im.crop((left, top, left + W, top + H))


def title_layer(title: str, font_path: str, cap_h: int, y_center: int, w: int, h: int,
                letter_spacing: int = 6) -> Image.Image:
    """Chữ vàng cổ có bóng tối mềm + viền sáng nhẹ, vẽ giữa lá; cap_h = chiều cao chữ in hoa."""
    # tìm cỡ font sao cho chiều cao chữ hoa đúng cap_h
    size = cap_h
    for _ in range(12):
        f = ImageFont.truetype(font_path, size)
        bb = f.getbbox("H")
        got = bb[3] - bb[1]
        if abs(got - cap_h) <= 1:
            break
        size = max(8, round(size * cap_h / max(1, got)))
    font = ImageFont.truetype(font_path, size)

    # đo bề rộng có letter-spacing
    widths = [font.getlength(ch) for ch in title]
    total = sum(widths) + letter_spacing * (len(title) - 1)
    x = (w - total) / 2
    bb = font.getbbox("H")
    y = y_center - (bb[1] + bb[3]) / 2

    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ds, dl = ImageDraw.Draw(shadow), ImageDraw.Draw(layer)
    cx = x
    for ch, cw in zip(title, widths):
        ds.text((cx + 2, y + 3), ch, font=font, fill=(0, 0, 0, 215))
        cx += cw + letter_spacing
    shadow = shadow.filter(ImageFilter.GaussianBlur(4))
    cx = x
    for ch, cw in zip(title, widths):
        # viền tối mảnh
        dl.text((cx, y), ch, font=font, fill=(60, 38, 8, 255), stroke_width=2, stroke_fill=(60, 38, 8, 255))
        cx += cw + letter_spacing
    cx = x
    for ch, cw in zip(title, widths):
        dl.text((cx, y), ch, font=font, fill=(232, 196, 96, 255))
        cx += cw + letter_spacing
    # ánh kim: gradient nhẹ từ sáng (trên) xuống đậm (dưới) trong từng dòng chữ
    arr = np.array(layer).astype(np.float32)
    ys = np.arange(h, dtype=np.float32)[:, None]
    grad = np.clip(1.0 - (ys - (y_center - cap_h / 2)) / max(1.0, cap_h) * 0.35, 0.6, 1.0)
    arr[:, :, :3] *= grad[:, :, None]
    layer = Image.fromarray(arr.clip(0, 255).astype(np.uint8), "RGBA")
    return Image.alpha_composite(shadow, layer)


def load_title(slug: str) -> str:
    with open(CARDS_JSON, "r", encoding="utf-8") as f:
        for c in json.load(f)["cards"]:
            if c["slug"] == slug:
                return c["title"]
    raise SystemExit(f"[loi] khong thay slug `{slug}` trong cards.json")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Ghép lá full-bleed: cảnh + khung The Star + tên lá.")
    ap.add_argument("slug")
    ap.add_argument("scene")
    ap.add_argument("--out", default=None)
    ap.add_argument("--anchor", default=DEFAULT_ANCHOR)
    ap.add_argument("--font", default=DEFAULT_FONT)
    ap.add_argument("--title-y", type=int, default=1243, help="tâm dòng chữ theo trục y (lá neo: 1243)")
    ap.add_argument("--title-h", type=int, default=50, help="chiều cao chữ in hoa px (lá neo: ~50)")
    ap.add_argument("--no-title", action="store_true")
    ap.add_argument("--title-from-anchor", choices=("auto", "yes", "no"), default="auto",
                    help="lấy nguyên dòng chữ của lá neo (auto: khi title trùng với title lá neo)")
    ap.add_argument("--dump-layers", default=None, help="ghi 3 lớp rời vào thư mục này")
    a = ap.parse_args(argv)

    out = a.out or os.path.join(ROOT, "cards", f"{a.slug}.png")
    anchor = cv2.imread(a.anchor, cv2.IMREAD_COLOR)
    if anchor is None:
        raise SystemExit(f"[loi] khong doc duoc la neo {a.anchor}")
    if anchor.shape[1::-1] != SIZE_WH:
        raise SystemExit(f"[loi] la neo phai {SIZE_WH}, dang la {anchor.shape[1::-1]}")

    scene = fit_scene(a.scene).convert("RGBA")
    frame = extract_frame_layer(anchor)
    card = Image.alpha_composite(scene, frame)
    title_img, title_src = None, None
    if not a.no_title:
        title = load_title(a.slug)
        anchor_slug = os.path.splitext(os.path.basename(a.anchor))[0]
        same_title = False
        try:
            same_title = load_title(anchor_slug) == title
        except SystemExit:
            pass
        use_anchor = a.title_from_anchor == "yes" or (a.title_from_anchor == "auto" and same_title)
        if use_anchor:
            title_img, title_src = extract_title_layer(anchor), f"chữ tách từ {os.path.relpath(a.anchor, ROOT)}"
        else:
            title_img, title_src = title_layer(title, a.font, a.title_h, a.title_y, *SIZE_WH), \
                f"font {os.path.basename(a.font)} @ y={a.title_y} h={a.title_h}"
        card = Image.alpha_composite(card, title_img)

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    card.convert("RGB").save(out, "PNG", optimize=True)

    if a.dump_layers:
        os.makedirs(a.dump_layers, exist_ok=True)
        scene.convert("RGB").save(os.path.join(a.dump_layers, f"{a.slug}.01-scene.png"))
        frame.save(os.path.join(a.dump_layers, f"{a.slug}.02-frame.png"))
        if title_img is not None:
            title_img.save(os.path.join(a.dump_layers, f"{a.slug}.03-title.png"))

    ink_px = int((np.array(frame)[:, :, 3] > 127).sum())
    print(f"[ok] {out}  ({SIZE_WH[0]}x{SIZE_WH[1]})  khung: {ink_px} px mực vàng lấy từ {os.path.relpath(a.anchor, ROOT)}"
          + ("" if a.no_title else f"  tên lá: '{load_title(a.slug)}' ({title_src})"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
