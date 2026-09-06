#!/usr/bin/env python3
"""Engrave a distinctive emblem motif into a card's top medallion.

The motif is supplied as artwork on a flat white background (gold engraving); it is keyed
out, scaled to fit inside the oval plate and blended in MULTIPLY mode so it reads like part
of the printed plate instead of a pasted sticker.

Usage: python3 scripts/set_emblem.py <motif.png> <card.png> [out.png]
"""
import sys
import cv2
import numpy as np
from PIL import Image, ImageFilter

ROI = (300, 60, 490, 200)          # medallion interior in card coordinates
CENTRE, AX, BY = (92, 73), 85, 53  # oval interior (fitted), ROI coordinates


def clean_plate(roi):
    """Erase whatever is drawn inside the oval and restore the smooth plate."""
    h, w = roi.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    inside = (((xx - CENTRE[0]) / (AX - 2)) ** 2 + ((yy - CENTRE[1]) / (BY - 2)) ** 2) < 1
    g = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    bg = cv2.medianBlur(g, 41).astype(np.int32)
    m = (((bg - g.astype(np.int32)) > 8) & inside).astype(np.uint8)
    m = cv2.dilate(m, np.ones((5, 5), np.uint8))
    plate = cv2.inpaint(roi, m, 10, cv2.INPAINT_NS)
    sm = cv2.medianBlur(plate, 41)
    a = cv2.GaussianBlur(cv2.dilate(m, np.ones((11, 11), np.uint8)).astype(np.float32), (0, 0), 7)
    a = np.clip(a, 0, 1) * inside
    return (sm * a[..., None] + plate * (1 - a[..., None])).astype(np.uint8)


def key_motif(path, floor=10.0, thresh=26.0):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    mn = a.min(2)
    sat = a.max(2) - a.min(2)
    alpha = np.clip((np.maximum(255 - mn, sat) - floor) / thresh, 0, 1)
    alpha = np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.5))) / 255.0
    rgba = np.dstack([np.asarray(im), (alpha * 255).astype(np.uint8)])
    out = Image.fromarray(rgba)
    bbox = out.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
    return out.crop(bbox)


def engrave(motif_path, card_path, out_path=None, margin=8, strength=1.0, scale=1.0):
    out_path = out_path or card_path
    x0, y0, x1, y1 = ROI
    card = Image.open(card_path).convert("RGB")
    roi = cv2.cvtColor(np.asarray(card)[y0:y1, x0:x1], cv2.COLOR_RGB2BGR)
    plate = clean_plate(roi)
    base = Image.fromarray(cv2.cvtColor(plate, cv2.COLOR_BGR2RGB)).convert("RGB")

    motif = key_motif(motif_path)
    maxw, maxh = int((AX - margin) * 2 * scale), int((BY - margin) * 2 * scale)
    k = min(maxw / motif.width, maxh / motif.height)
    motif = motif.resize((max(1, int(motif.width * k)), max(1, int(motif.height * k))), Image.LANCZOS)

    layer = Image.new("RGB", base.size, (255, 255, 255))
    mask = Image.new("L", base.size, 0)
    pos = (CENTRE[0] - motif.width // 2, CENTRE[1] - motif.height // 2)
    layer.paste(motif.convert("RGB"), pos)
    mask.paste(motif.getchannel("A"), pos)

    b = np.asarray(base).astype(np.float32)
    l = np.asarray(layer).astype(np.float32)
    m = (np.asarray(mask).astype(np.float32) / 255.0 * strength)[..., None]
    mult = b * (l / 255.0)                      # multiply blend -> engraved on the plate
    outroi = (b * (1 - m) + mult * m).clip(0, 255).astype(np.uint8)

    canvas = card.copy()
    canvas.paste(Image.fromarray(outroi), (x0, y0))
    canvas.save(out_path)
    return out_path


if __name__ == "__main__":
    motif, card = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else card
    engrave(motif, card, out)
    print(f"emblem {motif} -> {out}")
