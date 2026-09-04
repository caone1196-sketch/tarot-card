#!/usr/bin/env python3
"""Tạo đúng văn bản prompt gửi cho model image = prompts/out/<slug>.txt NGUYÊN VĂN,
Mỗi chỗ thay là 1 chuỗi liền mạch, ghi lại trong SUBS để đối chiếu được.

Chạy:  python3 scripts/render_sent.py 00-fool 01-magician ...   -> cards/_regen/<slug>.sent.txt
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "prompts", "out")
DST = os.path.join(ROOT, "cards", "_regen")

def build(slug: str) -> str:
    with open(os.path.join(SRC, f"{slug}.txt"), encoding="utf-8") as f:
        t = f.read().strip()
    for old, new in SUBS.get(slug, []):
        if old not in t:
            raise SystemExit(f"[loi] {slug}: khong tim thay cụm can thay trong prompts/out/{slug}.txt")
        t = t.replace(old, new, 1)
    return t


def main() -> int:
    slugs = sys.argv[1:] or sorted(SUBS)
    os.makedirs(DST, exist_ok=True)
    for s in slugs:
        t = build(s)
        with open(os.path.join(DST, f"{s}.sent.txt"), "w", encoding="utf-8") as f:
            f.write(t + "\n")
        print(f"=== {s}  ({len(t)} ky tu) ===")
        print(t)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
