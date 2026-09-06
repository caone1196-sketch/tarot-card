#!/usr/bin/env python3
"""Rebuild the EIGHT OF WANDS medallion emblem so it shows EXACTLY 8 gold wands.

The plate is inpainted clean, one original stroke is lifted as a sprite, and n copies are
fanned as ellipse chords inside the oval -> the count is guaranteed by construction.

Usage: python3 scripts/rebuild_emblem.py <card.png> [out.png] [n]
"""
import sys
import cv2
import numpy as np
from PIL import Image

ROI = (300, 60, 490, 200)     # medallion interior in card coordinates
CENTRE, AX, BY = (92, 73), 85, 53   # oval interior (fitted), ROI coordinates
SRC = "cards/wands-08.png"    # artwork the stroke sprite is lifted from


def clean_plate(roi):
    h, w = roi.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    inside = (((xx - CENTRE[0]) / (AX - 2)) ** 2 + ((yy - CENTRE[1]) / (BY - 2)) ** 2) < 1
    g = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY).astype(np.int32)
    bg = cv2.medianBlur(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY), 41).astype(np.int32)
    m = (((bg - g) > 8) & inside).astype(np.uint8)
    m = cv2.dilate(m, np.ones((5, 5), np.uint8))
    plate = cv2.inpaint(roi, m, 10, cv2.INPAINT_NS)
    sm = cv2.medianBlur(plate, 41)
    a = cv2.GaussianBlur(cv2.dilate(m, np.ones((11, 11), np.uint8)).astype(np.float32), (0, 0), 7)
    a = np.clip(a, 0, 1) * inside
    return (sm * a[..., None] + plate * (1 - a[..., None])).astype(np.uint8)


def stroke_sprite():
    img = cv2.imread(SRC)
    x0, y0, x1, y1 = ROI
    roi = img[y0:y1, x0:x1]
    g = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY).astype(np.int32)
    bg = cv2.medianBlur(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY), 31).astype(np.int32)
    m = ((bg - g) > 18).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    cand = sorted((st[i][2], i) for i in range(1, n) if st[i][3] > 60)
    i = cand[0][1]
    x, y, w, h, _ = st[i]
    plate = clean_plate(roi)
    pad = 3
    sub = roi[y - pad:y + h + pad, x - pad:x + w + pad].astype(np.float32)
    pl = plate[y - pad:y + h + pad, x - pad:x + w + pad].astype(np.float32)
    alpha = np.clip((pl - sub).mean(2) / 34.0, 0, 1)
    alpha = cv2.GaussianBlur(alpha, (0, 0), 0.5)
    # keep only the main stroke blob
    mm = (alpha > 0.16).astype(np.uint8)
    nn, lab2, st2, _ = cv2.connectedComponentsWithStats(mm, 8)
    k = 1 + int(np.argmax(st2[1:, cv2.CC_STAT_AREA]))
    keep = cv2.GaussianBlur(cv2.dilate((lab2 == k).astype(np.float32), np.ones((3, 3), np.uint8)), (0, 0), 0.6)
    alpha = alpha * np.clip(keep, 0, 1)
    rgba = np.dstack([cv2.cvtColor(sub.astype(np.uint8), cv2.COLOR_BGR2RGB), (alpha * 255).astype(np.uint8)])
    sp = Image.fromarray(rgba)
    sp = sp.crop(sp.getchannel("A").point(lambda v: 255 if v > 30 else 0).getbbox())
    # straighten
    al = np.asarray(sp.getchannel("A")).astype(np.float32) / 255
    ys, xs = np.nonzero(al > 0.5)
    cov = np.cov(np.vstack([xs - xs.mean(), ys - ys.mean()]))
    wv, v = np.linalg.eigh(cov)
    vx, vy = v[:, np.argmax(wv)]
    ang = float(np.degrees(np.arctan2(vy, vx)))
    sp = sp.rotate(ang - 90 if ang > 0 else ang + 90, resample=Image.BICUBIC, expand=True)
    return sp.crop(sp.getchannel("A").point(lambda v: 255 if v > 30 else 0).getbbox())


def rebuild(card_path, out_path=None, n=8, spread=22.0, spanx=58.0, margin=5.0, thick=1.3):
    out_path = out_path or card_path
    card = Image.open(card_path).convert("RGBA")
    x0, y0, x1, y1 = ROI
    roi = cv2.cvtColor(np.asarray(card.convert("RGB"))[y0:y1, x0:x1], cv2.COLOR_RGB2BGR)
    plate = clean_plate(roi)
    base = Image.fromarray(cv2.cvtColor(plate, cv2.COLOR_BGR2RGB)).convert("RGBA")
    sp = stroke_sprite()
    sw, sh = sp.size
    ae, be = AX - 6, BY - 6
    for i in range(n):
        f = (i - (n - 1) / 2) / ((n - 1) / 2)
        th = np.radians(spread * f)
        u = np.array([np.sin(th), -np.cos(th)])
        q = np.array([spanx * f, 0.0])
        qa, qb, ua, ub = q[0] / ae, q[1] / be, u[0] / ae, u[1] / be
        aa, bb, cc = ua * ua + ub * ub, 2 * (qa * ua + qb * ub), qa * qa + qb * qb - 1
        disc = bb * bb - 4 * aa * cc
        if disc <= 0:
            continue
        t1 = (-bb - np.sqrt(disc)) / (2 * aa) + margin
        t2 = (-bb + np.sqrt(disc)) / (2 * aa) - margin
        L = t2 - t1
        s = sp.resize((max(3, int(round(sw * thick))), max(6, int(round(L)))), Image.LANCZOS)
        box = int(np.hypot(*s.size)) + 10
        canv = Image.new("RGBA", (box, box), (0, 0, 0, 0))
        canv.alpha_composite(s, (box // 2 - s.width // 2, box // 2 - s.height // 2))
        rot = canv.rotate(-np.degrees(th), resample=Image.BICUBIC, center=(box // 2, box // 2))
        mid = np.array(CENTRE) + q + u * (t1 + t2) / 2
        base.alpha_composite(rot, (int(round(mid[0] - box / 2)), int(round(mid[1] - box / 2))))
    card.alpha_composite(base, (x0, y0))
    card.convert("RGB").save(out_path)
    return out_path


if __name__ == "__main__":
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else src
    k = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    rebuild(src, dst, n=k)
    print(f"emblem rebuilt with exactly {k} wands -> {dst}")
