#!/usr/bin/env python3
"""Tạo đúng văn bản prompt gửi cho model image = prompts/out/<slug>.txt NGUYÊN VĂN,
chỉ thay các cụm mô tả khoả thân thành khoác lụa (chính sách nội dung).
Mỗi chỗ thay là 1 chuỗi liền mạch, ghi lại trong SUBS để đối chiếu được.

Chạy:  python3 scripts/render_sent.py 00-fool 01-magician ...   -> cards/_regen/<slug>.sent.txt
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "prompts", "out")
DST = os.path.join(ROOT, "cards", "_regen")

# slug -> [(chuỗi gốc trong cards.json/prompt, chuỗi thay thế)]
SUBS = {
    "00-fool": [(
        "draped only in a transparent silk veil so fine it clings and reveals her bare body beneath, "
        "the veil slipping from one shoulder",
        "draped in a diaphanous silk over-veil over a floor-length ivory gown, the over-veil slipping "
        "from one shoulder",
    )],
    "01-magician": [(
        "a nude young woman magician, bare torso with a length of silk slung low across her hips",
        "a young woman magician wearing a sleeveless ivory-and-gold gown with a length of silk slung "
        "low across her hips",
    )],
    "02-priestess": [(
        "a serene nude priestess, bare shoulders and the soft line of her breasts veiled only by a "
        "drift of sheer gauze",
        "a serene priestess in a pale blue floor-length gown, her shoulders and neckline veiled by a "
        "drift of sheer gauze",
    )],
    "03-empress": [(
        "a slender nude empress, one breast bared",
        "a slender empress in a softly draped ivory-and-gold silk gown with a low, covered neckline",
    )],
    "04-emperor": [(
        "draped only in a diaphanous transparent silk veil so fine it clings to her soft curves and "
        "glows with warm light against her skin, the gossamer fabric slipping from one shoulder",
        "draped in a diaphanous silk over-veil over a gold-trimmed ivory gown, the fabric glowing with "
        "warm light, slipping from one shoulder",
    )],
    "05-hierophant": [(
        "draped only in a diaphanous transparent red silk veil so fine it clings to her curves and "
        "glows with warm candlelight against her skin, the gossamer-thin fabric slipping from one "
        "shoulder",
        "draped in layered crimson-and-gold ceremonial vestments beneath a diaphanous red silk "
        "over-veil glowing with warm candlelight, the gossamer-thin over-veil slipping from one "
        "shoulder",
    )],
}


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
