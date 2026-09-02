#!/usr/bin/env python3
"""
Compose artwork onto the NEW 4-LAYER CARD FRAME (no emblem medallion).

Quy trình: ảnh raw (từ AI) được scale kiểu "cover" ra toàn lá 784x1360
-> dán lên NỀN giấy da cổ -> KHUNG hoạ tiết mảnh sát lề đè lên nội dung
-> KHUNG TÊN (dải băng + tên lá bằng GrenzeGotisch-Bold).

Nguồn asset: variants/frame-kit/ (xem scripts/apply_new_frame.py).

Usage:
    python3 scripts/compose_card.py <raw_image.png> [out.png] [--title "THE FOOL"]
    python3 scripts/compose_card.py --check
"""

import json
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from apply_new_frame import (  # noqa: E402
    CARDS_DIR,
    CARDS_JSON,
    compose,
    cover_resize,
    render_title,
)

W, H = 784, 1360


def load_title(slug_hint: str) -> str:
    try:
        with open(CARDS_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        for c in data["cards"]:
            if slug_hint in (c["slug"], c["slug"] + ".png"):
                return c["title"]
    except Exception:
        pass
    return os.path.splitext(os.path.basename(slug_hint))[0].replace("-", " ").upper()


def compose_card(raw_path: str, out_path: str, title: str | None = None) -> None:
    raw = Image.open(raw_path).convert("RGB")
    content = cover_resize(raw, W, H)
    out = compose(content=content, title=title)
    out.save(out_path)
    print(f"Composed card: {raw_path} -> {out_path} ({out.size})")


def check_rmse() -> None:
    """So sánh khung hoạ tiết mảnh của từng lá với mốc The Star (theo mask)."""
    import cv2
    import numpy as np
    from apply_new_frame import KIT_FRAME

    # chỉ nét vàng đặc (alpha>=240); rìa/quầng sáng bán trong suốt blend với nền
    # nội dung (mỗi lá khác nhau) nên không đưa vào phép đo.
    mask = np.asarray(Image.open(KIT_FRAME).convert("RGBA"))[..., 3] >= 240
    ref = cv2.imread(os.path.join(CARDS_DIR, "17-the-star.png"), cv2.IMREAD_GRAYSCALE)
    for f in sorted(os.listdir(CARDS_DIR)):
        if not f.endswith(".png") or f in ("card-blank.png",):
            continue
        p = os.path.join(CARDS_DIR, f)
        a = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
        if a is None or a.shape != ref.shape:
            continue
        d = a[mask].astype(np.float64) - ref[mask].astype(np.float64)
        print(f"Card {f:<22} frame RMSE: {float(np.sqrt(np.mean(d ** 2)) / 255.0):.4f}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == "--check":
        check_rmse()
        return
    raw_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("--") else \
        os.path.join(CARDS_DIR, os.path.splitext(os.path.basename(raw_path))[0] + ".png")
    title = None
    if "--title" in sys.argv:
        title = sys.argv[sys.argv.index("--title") + 1]
    else:
        title = load_title(raw_path)
    compose_card(raw_path, out_path, title)


if __name__ == "__main__":
    main()
