#!/usr/bin/env python3
"""Composite an exact number of wand sprites onto a card background in one parallel diagonal row.

Guarantees the count lock (e.g. EXACTLY 8 wands) instead of trusting the image model.
"""
import numpy as np
from PIL import Image, ImageFilter


def key_white(path, thresh=18.0, floor=12.0):
    """Cut a sprite off a flat white background -> RGBA (floor kills the near-white halo)."""
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.float32)
    mn = a.min(2)
    sat = a.max(2) - a.min(2)
    strength = np.maximum(255 - mn, sat) - floor
    alpha = np.clip(strength / thresh, 0, 1)
    alpha = np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))) / 255.0
    rgba = np.dstack([np.asarray(im), (alpha * 255).astype(np.uint8)])
    out = Image.fromarray(rgba)
    return out.crop(out.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox())


def axis_angle(sprite):
    """Angle (deg, screen coords, positive = downward to the right) of the sprite's long axis."""
    a = np.asarray(sprite.getchannel("A")).astype(np.float32) / 255.0
    ys, xs = np.nonzero(a > 0.5)
    x = xs - xs.mean()
    y = ys - ys.mean()
    cov = np.cov(np.vstack([x, y]))
    w, v = np.linalg.eigh(cov)
    vx, vy = v[:, np.argmax(w)]
    if vx < 0:
        vx, vy = -vx, -vy
    return float(np.degrees(np.arctan2(vy, vx)))


def prepare(sprite, target_angle, target_len):
    """Rotate to target_angle and scale so the long axis measures target_len px."""
    ang = axis_angle(sprite)
    rot = sprite.rotate(ang - target_angle, resample=Image.BICUBIC, expand=True)
    rot = rot.crop(rot.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox())
    cur = np.hypot(*rot.size)
    cur = np.hypot(rot.size[0], rot.size[1] * 0 + rot.size[1])
    w, h = rot.size
    cur_len = np.hypot(w, h)
    s = target_len / cur_len
    return rot.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)


def place(bg_path, sprite, out_path, n=8, cx=392, y0=300, dy=84, opacity=1.0):
    bg = Image.open(bg_path).convert("RGB")
    layer = Image.new("RGBA", bg.size, (0, 0, 0, 0))
    w, h = sprite.size
    for i in range(n):
        cy = int(y0 + i * dy)
        layer.alpha_composite(sprite, (int(cx - w / 2), int(cy - h / 2)))
    if opacity < 1.0:
        a = layer.getchannel("A").point(lambda v: int(v * opacity))
        layer.putalpha(a)
    bg = bg.convert("RGBA")
    bg.alpha_composite(layer)
    bg.convert("RGB").save(out_path)
    return out_path
