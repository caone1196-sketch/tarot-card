#!/usr/bin/env python3
"""
fix_crown_stars.py — kiểm tra & ghép đủ **12 ngôi sao** cho vương miện `03-empress` bằng code.

Vì sao cần: `AGENTS.md` §3 — *"Không tin AI đếm — ghép bằng code"*. `cards.json` chỉ
mô tả `emblem: a twelve-star crown`; model sinh ảnh vẽ số sao theo cảm hứng (bản 2026-09-03
vẽ 9), nên số sao phải đếm lại và补齐 bằng code, không viết thêm vào prompt.

Cách làm:
 1) cắt template = blob vàng lớn nhất trong vùng vương miện, `matchTemplate` để định vị
    từng ngôi sao (chỉ tính trong 35% chiều cao đầu ảnh, loại bụi vàng ở cảnh dưới);
 2) khớp đường tròn đi qua các tâm sao -> suy ra tâm + bán kính + bước góc;
 3) thiếu bao nhiêu sao thì dán thêm sprite (chính là một ngôi sao cắt từ ảnh, alpha =
    mặt nạ vàng + feather) tiếp tục vòng cung, so le trái/phải — hoặc đúng vị trí
    truyền bằng `--at x,y,x,y,...`;
 4) đếm lại và in kết quả (exit 1 nếu vẫn thiếu).

Dùng:
    python3 scripts/fix_crown_stars.py <anh-vao> <anh-ra> [want=12] [--at x,y,...]
"""
from __future__ import annotations
import sys
import numpy as np
import cv2


def gold(img):
    q = img.astype(int)
    r, g, b = q[..., 2], q[..., 1], q[..., 0]
    return (((r > 185) & (g > 145) & (b < 205) & (r - b > 45))).astype(np.uint8)


def locate_stars(img, S=34, ybox=0.35, thresh=0.40):
    """Trả về (danh sách tâm sao, mask vàng, template ảnh sao, vị trí cắt template)."""
    H, W = img.shape[:2]
    m = gold(img)
    top = int(H * ybox)
    sub = m[:top, :]
    n, lab, st, _ = cv2.connectedComponentsWithStats(sub, 8)
    if n <= 1:
        return [], m, None, None
    # chon blob "giong ngoi sao" nhat trong dai vuong mien: vuong vach, dien tich vua,
    # va phan tram lap day 0.28-0.62 (sao 5 canh ~ 0.4-0.5; khoi sang/nen ~ >0.7)
    yband = int(H * 0.28)
    cand = []
    for k in range(1, n):
        bx, by, bw, bh, ba = st[k]
        if not (70 <= ba <= 500 and 12 <= bw <= 44 and 12 <= bh <= 44 and by < yband):
            continue
        if not (int(W * 0.12) <= bx <= int(W * 0.85)):
            continue
        fill = ba / float(bw * bh)
        if 0.26 <= fill <= 0.64:
            cand.append((ba * min(bw / bh, bh / bw), k))
    if not cand:
        return [], m, None, None
    i = max(cand)[1]
    x, y, w, h, _ar = st[i]
    x0 = int(max(0, min(W - S, x - (S - w) // 2)))
    y0 = int(max(0, min(top - S, y - (S - h) // 2)))
    # giu nguyen kich thuoc: template = dung o S x S chua blob (KHONG resize -> sai ti le)
    tmpl = m[y0:y0 + S, x0:x0 + S].astype(np.float32)
    if tmpl.shape != (S, S):
        return [], m, None, None
    res = cv2.matchTemplate(m[:top, :].astype(np.float32), tmpl, cv2.TM_CCOEFF_NORMED)
    work = res.copy()
    pts = []
    while True:
        idx = int(np.argmax(work))
        vy, vx = np.unravel_index(idx, work.shape)
        if work[vy, vx] < thresh:
            break
        pts.append((vx + S // 2, vy + S // 2, float(work[vy, vx])))
        work[max(0, vy - S // 2):vy + S // 2, max(0, vx - S // 2):vx + S // 2] = -1
    pts.sort(key=lambda t: (t[1], t[0]))
    sprite = img[y0:y0 + S, x0:x0 + S].copy()
    return pts, m, sprite, (x0, y0, S)


def fit_circle(pts):
    P = np.asarray([(a, b) for a, b, _ in pts], float)
    A = np.c_[2 * P[:, 0], 2 * P[:, 1], np.ones(len(P))]
    s, *_ = np.linalg.lstsq(A, (P ** 2).sum(1), rcond=None)
    cx, cy = float(s[0]), float(s[1])
    return cx, cy, float(np.sqrt(s[2] + cx * cx + cy * cy))


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--at"]
    at = []
    if "--at" in sys.argv:
        i = sys.argv.index("--at") + 1
        if i < len(sys.argv):
            at = [tuple(map(int, t.split(","))) for t in sys.argv[i].split() if "," in t]
            args = [a for a in args if "," not in a]
    src = args[0] if args else "cards/_regen/03-empress_v3fit.png"
    dst = args[1] if len(args) > 1 else "cards/_regen/03-empress_12.png"
    want = int(args[2]) if len(args) > 2 else 12

    img = cv2.imread(src)
    H, W = img.shape[:2]
    pts, m, sprite, cut = locate_stars(img)
    print(f"[1] thay {len(pts)} ngoi sao tren vong vuong mien: "
          + ", ".join(f"({x},{y})" for x, y, _ in pts))
    if len(pts) < 3:
        print("[loi] khong du moc de khop vong", file=sys.stderr)
        return 2

    cx, cy, R = fit_circle(pts)
    angs = np.array([np.degrees(np.arctan2(y - cy, x - cx)) for x, y, _ in pts])
    step = float(np.median(np.diff(np.sort(angs)))) if len(angs) > 1 else 20.0
    print(f"[2] vong tam=({cx:.0f},{cy:.0f}) R={R:.0f} buoc goc~{step:.1f} deg")

    need = want - len(pts)
    if need <= 0 and not at:
        print(f"[3] du {len(pts)}/{want} — khong ghep gi")
        cv2.imwrite(dst, img)
        return 0

    S = cut[2]
    x0, y0 = cut[0], cut[1]
    sp = img[y0:y0 + S, x0:x0 + S].copy()
    am = cv2.dilate(gold(sp), np.ones((3, 3), np.uint8), 1)
    alpha = (cv2.GaussianBlur(am * 255, (0, 0), 1.7) / 255.0)[..., None]

    def stamp(nx, ny):
        px, py = int(round(nx)) - S // 2, int(round(ny)) - S // 2
        if not (2 < py and py + S < H - 2 and 2 < px and px + S < W - 2):
            return False
        reg = img[py:py + S, px:px + S].astype(float)
        img[py:py + S, px:px + S] = (sp.astype(float) * alpha + reg * (1 - alpha)).astype(np.uint8)
        return True

    added = []
    if at:
        for nx, ny in at:
            if stamp(nx, ny):
                added.append((nx, ny))
    else:
        have = set(np.round(angs / step).astype(int))
        k = 1
        while len(added) < need and k < 60:
            for sgn in (-1, 1):
                idx = int(round(np.median(np.array(angs) / step))) + sgn * k
                if idx in have:
                    continue
                a = np.deg2rad(idx * step)
                if stamp(cx + R * np.cos(a), cy + R * np.sin(a)):
                    have.add(idx); added.append((int(cx + R * np.cos(a)), int(cy + R * np.sin(a))))
                    if len(added) >= need:
                        break
            k += 1
    print(f"[3] ghep them {len(added)}: {', '.join(f'({x},{y})' for x, y in added)}")

    pts2, *_ = locate_stars(img)
    cv2.imwrite(dst, img)
    print(f"[4] kiem lai: {len(pts2)}/{want} sao -> {dst}")
    return 0 if len(pts2) >= want else 1


if __name__ == "__main__":
    raise SystemExit(main())
