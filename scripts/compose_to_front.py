#!/usr/bin/env python3
"""compose_to_front.py — ghép lá đã sinh lên KHUNG CHUẨN để viền đồng nhất.

Lý do: khi model tự vẽ khung thì mỗi lá ra một khung khác nhau (độ dày nét vàng,
hoa văn góc, ngả màu giấy da). Thay vào đó, chỉ dùng PHẦN NỘI DUNG bên trong cửa sổ
chuẩn (content_window) của lá đã sinh, dán lên `cards/card-blank.png` (khung cố định
của The Star) tại đúng toạ độ → MỌI LÁ có khung giống hệt nhau, chỉ khác nội dung.

Khung chuẩn lấy từ `standards/<anchor>/standard.json` (content_window_xyxy + card_size_wh).

Dùng:
    python3 scripts/compose_to_front.py            # ghép TẤT CẢ ảnh .png trong src/ -> dst/
    python3 scripts/compose_to_front.py <src.png> <dst.png>

Kết quả là ảnh đúng cỡ khung chuẩn, nội dung khớp toạ độ cửa sổ chuẩn.
"""
from __future__ import annotations

import json
import os
import sys
import glob

import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STANDARD_JSON = os.path.join(ROOT, "standards", "17-the-star", "standard.json")
FRAME_IMG = os.path.join(ROOT, "cards", "card-blank.png")   # khung cố định (viền chuẩn)
SRC_DIR = os.path.join(ROOT, "cards1")
DST_DIR = os.path.join(ROOT, "cards1")

# Chừa thêm ~ vài px đè lên mép trong khung để không lộ đường nối (feather).
PAD = 8


def load_standard() -> dict:
    with open(STANDARD_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def compose(src_path: str, dst_path: str, std: dict, frame_img: str) -> dict:
    size = tuple(std["card_size_wh"])                       # (w, h) = (784, 1360)
    x0, y0, x1, y1 = std["frame"]["content_window_xyxy"]    # [32, 35, 751, 1324]

    frame = cv2.imread(frame_img, cv2.IMREAD_COLOR)
    if frame is None:
        raise FileNotFoundError(f"khong doc duoc khung: {frame_img}")
    frame = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)

    src = cv2.imread(src_path, cv2.IMREAD_COLOR)
    if src is None:
        raise FileNotFoundError(f"khong doc duoc anh nguon: {src_path}")
    src = cv2.resize(src, size, interpolation=cv2.INTER_AREA)

    # Cửa sổ nội dung chuẩn, chừa thêm PAD để đè kín mép khung (feather cho mượt).
    cx0, cy0 = max(0, x0 - PAD), max(0, y0 - PAD)
    cx1, cy1 = min(size[0], x1 + PAD), min(size[1], y1 + PAD)
    panel = src[cy0:cy1, cx0:cx1].copy()

    # Feather mép panel để không lộ chữ nhật khi dán.
    mask = np.zeros(panel.shape[:2], np.uint8)
    mask[:] = 255
    f = 4
    mask[:f, :] = 0
    mask[-f:, :] = 0
    mask[:, :f] = 0
    mask[:, -f:] = 0
    mask = cv2.GaussianBlur(mask, (0, 0), 2)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR).astype(np.float32) / 255.0

    region = frame[cy0:cy1, cx0:cx1].astype(np.float32)
    region = region * (1 - mask) + panel.astype(np.float32) * mask
    frame[cy0:cy1, cx0:cx1] = region.astype(np.uint8)

    os.makedirs(os.path.dirname(dst_path) or ".", exist_ok=True)
    cv2.imwrite(dst_path, frame)
    return {"src": os.path.basename(src_path), "dst": os.path.basename(dst_path),
            "window": [cx0, cy0, cx1, cy1]}


def main() -> int:
    std = load_standard()
    args = sys.argv[1:]
    if len(args) == 2:
        # <src.png> <dst.png>
        r = compose(args[0], args[1], std, FRAME_IMG)
        print(f"ok: {r['src']} -> {r['dst']} (window {r['window']})")
        return 0

    # Mặc định: ghép tất cả ảnh .png trong SRC_DIR (không đụng khung).
    os.makedirs(DST_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(SRC_DIR, "*.png")))
    done = 0
    for f in files:
        base = os.path.basename(f)
        if base == "card-blank.png":
            continue
        dst = os.path.join(DST_DIR, base)
        compose(f, dst, std, FRAME_IMG)
        done += 1
    print(f"composed {done} cards in {DST_DIR} onto standard frame.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
