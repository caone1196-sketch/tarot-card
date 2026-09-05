#!/usr/bin/env python3
"""Tạo đúng văn bản prompt gửi cho model image = prompts/out/<slug>.txt NGUYÊN VĂN,
Mỗi chỗ thay là 1 chuỗi liền mạch, ghi lại trong SUBS để đối chiếu được.
Sau đó gắn thêm khối `MODESTY` (bước render) để mọi nhân vật nữ được khoác lụa
thanh thoát, giữ đúng chất fine-art gợi cảm nhưng không phản cảm.

Chạy:  python3 scripts/render_sent.py 00-fool 01-magician ...   -> cards/_regen/<slug>.sent.txt
(không truyền slug: chạy toàn bộ 78 lá)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "prompts", "out")
DST = os.path.join(ROOT, "cards", "_regen")

# slug -> [(chuỗi gốc trong cards.json/prompt, chuỗi thay thế)]
# Khớp đúng scene hiện tại trong `tarot prompt/cards.json` (build_prompts.py emit nguyên văn).
SUBS = {
    "00-fool": [(
        "a carefree nude 19-year-old woman wanderer",
        "a carefree 19-year-old woman wanderer in a flowing ivory silk gown that catches the wind",
    )],
    "01-magician": [(
        "a nude young woman magician",
        "a young woman magician in a sleeveless gold-and-ivory gown",
    )],
    "02-priestess": [(
        "a serene nude priestess",
        "a serene priestess in a pale blue floor-length gown",
    )],
    "03-empress": [(
        "a slender nude empress, one breast bared",
        "a slender empress in a softly draped ivory-and-gold silk gown with a low, covered neckline",
    )],
    "04-emperor": [(
        "a serene nude 25-year-old female emperor",
        "a serene 25-year-old female emperor in a gold-trimmed ivory flowing gown",
    )],
}


# Khối bước RENDER — gắn vào MỌI lá (giữ nguyên 2 bước: build_prompts -> render_sent).
# Đây là "bước render" mà AGENTS.md nói tới: cảnh `scene` giữ nguyên văn bản nguồn,
# việc khoác lụa/non-explicit do bước render xử lý.
MODESTY = (
    "\n\nSTYLE AND MODESTY LOCK (render step): render every female figure elegantly veiled in "
    "flowing sheer silk drapery suited to her scene — classical fine-art sensuality, tasteful, "
    "non-explicit. Match the provided reference image exactly for the frame: thin antique-gold "
    "gothic rule-line border, corner flourishes, full-bleed scene and the gold serif title "
    "placement; same card size and portrait aspect as the reference."
)


def build(slug: str) -> str:
    with open(os.path.join(SRC, f"{slug}.txt"), encoding="utf-8") as f:
        t = f.read().strip()
    for old, new in SUBS.get(slug, []):
        if old not in t:
            raise SystemExit(f"[loi] {slug}: khong tim thay cụm can thay trong prompts/out/{slug}.txt")
        t = t.replace(old, new, 1)
    return t + MODESTY


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
