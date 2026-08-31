#!/usr/bin/env python3
"""
Wand counter v2 — cluster long shaft segments by spatial position.
For near-vertical wands: cluster by x-center.
For diagonal wands (8): cluster by perpendicular offset (rho).
Reports cluster count + saves annotated debug image.
"""
import cv2
import numpy as np
import sys, os

def detect(path, mode="vertical", min_len_ratio=0.18):
    img = cv2.imread(path)
    H, W = img.shape[:2]
    x0, x1 = int(W*0.09), int(W*0.91)
    y0, y1 = int(H*0.12), int(H*0.88)
    panel = img[y0:y1, x0:x1]
    gray = cv2.cvtColor(panel, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(cv2.GaussianBlur(gray,(5,5),0), 50, 150)
    minlen = int(min(panel.shape[0], panel.shape[1]) * min_len_ratio)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50,
                            minLineLength=minlen, maxLineGap=10)
    if lines is None:
        return 0, panel, []
    if lines.ndim == 3: lines = lines[:,0,:]

    segs = []
    for (x1,y1,x2,y2) in lines:
        dx, dy = x2-x1, y2-y1
        L = np.hypot(dx,dy)
        if L < minlen: continue
        ang = np.degrees(np.arctan2(dy, dx))  # -180..180
        a = abs(ang)
        if mode == "vertical":
            # near-vertical: |angle| in [55,125]
            if 55 <= a <= 125:
                segs.append(( (x1+x2)/2.0, (y1+y2)/2.0, L ))
        else:  # diagonal (positive slope, ~30-60deg)
            if 25 <= a <= 65:
                # perpendicular offset rho ~ y*cos - x*sin for line; use center projection
                cx, cy = (x1+x2)/2.0, (y1+y2)/2.0
                theta = np.radians(ang)
                rho = abs(cy*np.cos(theta) - cx*np.sin(theta))
                segs.append((rho, cx, L))
    if not segs:
        return 0, panel, []

    key = [s[0] for s in segs]
    key = sorted(key)
    # cluster by gap
    clusters = []
    cur = [key[0]]
    for k in key[1:]:
        if k - cur[-1] > 18:   # gap threshold (px)
            clusters.append(cur); cur = [k]
        else:
            cur.append(k)
    clusters.append(cur)

    # annotate: draw all accepted segments
    dbg = panel.copy()
    for (x1,y1,x2,y2) in lines:
        dx,dy=x2-x1,y2-y1
        L=np.hypot(dx,dy)
        if L<minlen: continue
        a=abs(np.degrees(np.arctan2(dy,dx)))
        ok = (55<=a<=125) if mode=="vertical" else (25<=a<=65)
        if ok:
            cv2.line(dbg,(x1,y1),(x2,y2),(0,0,255),2)
    return len(clusters), dbg, clusters

if __name__ == "__main__":
    jobs = [("wands-03","vertical"),("wands-09","vertical"),
            ("wands-08","diagonal"),("wands-knight","vertical")]
    root="/home/user/tarot-card/raw"
    for slug, mode in jobs:
        p=os.path.join(root,slug+".png")
        if not os.path.exists(p):
            print(f"{slug:14s} MISSING"); continue
        n, dbg, cl = detect(p, mode)
        out=f"/tmp/{slug}-clusters.png"; cv2.imwrite(out, dbg)
        print(f"{slug:14s} {mode:9s} -> {n} cluster(s)   [{out}]")
