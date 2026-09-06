#!/usr/bin/env python3
"""Dựng "content mask" — vùng nội dung (tranh) cần thay thế khi vẽ lại.

Mask được xây từ độ lệch chuẩn pixel của 78 lá hiện có (khung viền/huy hiệu/tên
giống nhau -> std thấp; nội dung khác nhau -> std cao), giới hạn trong cửa sổ nội
dung đo được của khung chuẩn. Kết quả lưu look/redraw/content_mask.npy (alpha 0..1).

Cách dùng: python3 look/redraw/build_mask.py
"""
import os, glob, sys
import numpy as np
import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARDS = os.path.join(ROOT, "cards")
OUT = os.path.join(ROOT, "look", "redraw")

# Cửa sổ nội dung (bên trong đường viền vàng, dưới medallion, trên ribbon)
X0, X1 = 112, 672
Y0, Y1 = 136, 1234
STD_T = 25.0     # ngưỡng std: chrome < 25, content > 25
BLUR = 5         # feather (px)


def main():
    files = [
        f for f in sorted(glob.glob(os.path.join(CARDS, "*.png")))
        if os.path.splitext(os.path.basename(f))[0] not in ("card-back", "card-blank")
    ]
    if len(files) != 78:
        print("WARN: expected 78 cards, got", len(files))
    imgs = [cv2.imread(f, cv2.IMREAD_GRAYSCALE).astype(np.float64) for f in files]
    stack = np.stack(imgs, 0)
    std = stack.std(0)

    rect = np.zeros_like(std, bool)
    rect[Y0:Y1, X0:X1] = True
    mask = (std > STD_T) & rect
    print(f"content mask: {mask.sum()} px ({mask.mean()*100:.1f}% of card)")

    # sanity: mask must not reach medallion (<Y0) or ribbon (>=Y1) or outer border
    ys, xs = np.nonzero(mask)
    print(f"mask bbox x {xs.min()}..{xs.max()}, y {ys.min()}..{ys.max()}")

    alpha = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), BLUR)
    os.makedirs(OUT, exist_ok=True)
    np.save(os.path.join(OUT, "content_mask.npy"), alpha)
    cv2.imwrite(os.path.join(OUT, "content_mask_preview.png"), (alpha * 255).astype(np.uint8))
    # also cache raw mask
    np.save(os.path.join(OUT, "content_mask_bin.npy"), mask)
    print("saved look/redraw/content_mask.npy + preview")


if __name__ == "__main__":
    main()
