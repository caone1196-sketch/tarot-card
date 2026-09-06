#!/usr/bin/env python3
"""Copy the medallion emblem (oval interior) from one card onto another.

Useful when a freshly generated card comes back with an empty or wrong medallion:
the emblem artwork of the previous version is reused so the deck stays consistent.

Usage: python3 scripts/transplant_emblem.py <source_card.png> <target_card.png> [out.png]
"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROI = (300, 60, 490, 200)          # medallion interior in card coordinates
CENTRE, AX, BY = (92, 73), 85, 53  # oval interior (fitted), ROI coordinates


def transplant(src_path, dst_path, out_path=None, feather=3.0, shrink=2):
    out_path = out_path or dst_path
    x0, y0, x1, y1 = ROI
    src = Image.open(src_path).convert("RGB").crop((x0, y0, x1, y1))
    dst = Image.open(dst_path).convert("RGB")

    mask = Image.new("L", src.size, 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([CENTRE[0] - AX + shrink, CENTRE[1] - BY + shrink,
               CENTRE[0] + AX - shrink, CENTRE[1] + BY - shrink], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather))

    patch = Image.new("RGBA", src.size)
    patch.paste(src)
    patch.putalpha(mask)

    canvas = dst.convert("RGBA")
    canvas.alpha_composite(patch, (x0, y0))
    canvas.convert("RGB").save(out_path)
    return out_path


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else dst
    transplant(src, dst, out)
    print(f"emblem {src} -> {out}")
