#!/usr/bin/env python3
"""Ghép ảnh nội dung mới (tranh vẽ lại) lên khung chuẩn của lá hiện có.

- Ảnh mới được crop giữa về đúng tỉ lệ 7:12 rồi resize 784x1360.
- Chỉ vùng "content mask" (xem build_mask.py) được thay; khung viền + huy hiệu
  medallion + ribbon tên giữ nguyên từ lá hiện có => tỉ lệ & viền đồng nhất.

Cách dùng:
    python3 look/redraw/compose.py <slug> <raw_image.png>
    python3 look/redraw/compose.py all            # ghép mọi ảnh trong look/redraw/raw/
"""
import os, sys, glob
import numpy as np
import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARDS = os.path.join(ROOT, "cards")
RAW = os.path.join(ROOT, "look", "redraw", "raw")
OUT = os.path.join(ROOT, "look", "redraw", "out")
MASK_PATH = os.path.join(ROOT, "look", "redraw", "content_mask.npy")
W, H = 784, 1360


def to_card(img):
    """Center-crop to 7:12 then resize to 784x1360."""
    h, w = img.shape[:2]
    target = W / H
    cur = w / h
    if cur > target:  # too wide -> crop width
        nw = int(round(h * target))
        x0 = (w - nw) // 2
        img = img[:, x0:x0 + nw]
    elif cur < target:  # too tall -> crop height
        nh = int(round(w / target))
        y0 = (h - nh) // 2
        img = img[y0:y0 + nh]
    return cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)


def compose(slug, raw_path, out_path):
    alpha = np.load(MASK_PATH)  # (1360,784) float 0..1
    existing = cv2.imread(os.path.join(CARDS, slug + ".png"))
    if existing is None:
        sys.exit(f"không tìm thấy cards/{slug}.png")
    art = cv2.imread(raw_path)
    if art is None:
        sys.exit(f"không đọc được {raw_path}")
    art = to_card(art)
    a = alpha[..., None]
    out = (art.astype(np.float64) * a + existing.astype(np.float64) * (1 - a)).clip(0, 255).astype(np.uint8)
    cv2.imwrite(out_path, out)
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    if sys.argv[1] == "all":
        files = sorted(glob.glob(os.path.join(RAW, "*.png")) + glob.glob(os.path.join(RAW, "*.jpg")))
        for f in files:
            slug = os.path.splitext(os.path.basename(f))[0]
            compose(slug, f, os.path.join(OUT, slug + ".png"))
            print("composed", slug)
        return
    slug, raw_path = sys.argv[1], sys.argv[2]
    compose(slug, raw_path, os.path.join(OUT, slug + ".png"))
    print("composed", slug)


if __name__ == "__main__":
    main()
