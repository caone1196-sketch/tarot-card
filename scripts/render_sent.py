#!/usr/bin/env python3
"""Tạo đúng văn bản prompt gửi cho model image = prompts/out/<slug>.txt NGUYÊN VĂN,
Mỗi chỗ thay là 1 chuỗi liền mạch, ghi lại trong SUBS để đối chiếu được.
Sau đó gắn thêm khối `SENSUAL SHEER SILK` (bước render) — chất đặc trưng của bộ bài:
nhân vật nữ khoác LỤA MỎNG TRONG SUỐT ôm sát, lộ rõ đường cong, fine-art gợi cảm
(không phải váy dày che kín, không phản cảm).

Chạy:  python3 scripts/render_sent.py 00-fool 01-magician ...   -> cards/_regen/<slug>.sent.txt
(không truyền slug: chạy toàn bộ 78 lá)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "prompts", "out")
DST = os.path.join(ROOT, "cards", "_regen")

# slug -> [(chuỗi gốc trong cards.json/prompt, chuỗi thay thế)]
# Khớp đúng scene hiện tại trong `tarot prompt/cards.json` (build_prompts.py emit nguyên văn).
# Quy ước bộ bài: "nude" được bước render đổi thành khoác LỤA MỎNG TRONG SUỐT (sheer silk)
# — chất gợi cảm đặc trưng, lộ đường cong, không bao giờ thay bằng váy dày che kín.
SUBS = {
    "00-fool": [(
        "a carefree nude 19-year-old woman wanderer",
        "a carefree 19-year-old woman wanderer draped only in a diaphanous translucent silk veil "
        "that clings softly to her curves",
    )],
    "01-magician": [(
        "a nude young woman magician",
        "a young woman magician draped only in a diaphanous translucent silk veil, "
        "a length of sheer gossamer silk slung low across her hips",
    )],
    "02-priestess": [(
        "a serene nude priestess",
        "a serene priestess draped in a pale blue translucent silk veil so sheer it veils while "
        "revealing her soft figure",
    )],
    "03-empress": [(
        "a slender nude empress, one breast bared",
        "a slender empress draped in a diaphanous translucent gold silk veil that clings to and "
        "reveals her voluptuous curves",
    )],
    "04-emperor": [(
        "a serene nude 25-year-old female emperor",
        "a serene 25-year-old female emperor draped in a diaphanous translucent gold-trimmed silk "
        "veil that clings to and reveals her soft curves",
    )],
}


# Khối bước RENDER — gắn vào MỌI lá (giữ nguyên 2 bước: build_prompts -> render_sent).
# Đây là "bước render" mà AGENTS.md nói tới: cảnh `scene` giữ nguyên văn bản nguồn,
# việc khoác LỤA MỎNG TRONG SUỐT / non-explicit do bước render xử lý.
SENSUAL_SHEER_SILK = (
    "\n\nSENSUAL SHEER SILK (render step, deck signature): render every female figure draped "
    "only in diaphanous TRANSLUCENT sheer silk gossamer — fabric is soft, transparent and "
    "clinging, gently veiling the body while letting the elegant feminine silhouette and warm "
    "skin show through; classical fine-art sensuality, tasteful, non-explicit. Never dress her in "
    "opaque clothing, full gowns, armor or closed bodices. Match the provided reference image "
    "exactly for the frame: thin antique-gold gothic rule-line border, corner flourishes, "
    "full-bleed scene and the gold serif title placement; same card size and portrait aspect as "
    "the reference."
)


# Cụm nhạy cảm (nguy cơ content moderation) cần làm mềm cho MỌI lá.
GLOBAL_SANITIZE = [
    ("one breast bared", "the sheer drape slipping from one shoulder"),
    ("her bare back and the curve of one breast revealed by the golden lantern light",
     "her silk-veiled figure glowing softly in the golden lantern light"),
    ("her bare torso turned toward the light", "her silk-veiled torso turned toward the light"),
]

# Cụm nhạy cảm cho từng lá.
SANITIZE = {}


def build(slug: str) -> str:
    with open(os.path.join(SRC, f"{slug}.txt"), encoding="utf-8") as f:
        t = f.read().strip()
    for old, new in SUBS.get(slug, []):
        if old not in t:
            raise SystemExit(f"[loi] {slug}: khong tim thay cụm can thay trong prompts/out/{slug}.txt")
        t = t.replace(old, new, 1)
    # Quy ước bộ bài (áp dụng cho MỌI lá): "nude" trong scene -> KHÔNG đổi thành váy kín,
    # mà thành "sheer-silk draped" (lụa mỏng), khối SENSUAL_SHEER_SILK bên dưới sẽ
    # ép chất trong suốt/ôm sát của vải.
    t = re.sub(r"\bnude\b", "sheer-silk draped", t)
    for old, new in GLOBAL_SANITIZE:
        t = t.replace(old, new)
    for old, new in SANITIZE.get(slug, []):
        if old in t:
            t = t.replace(old, new, 1)
    return t + SENSUAL_SHEER_SILK


def all_slugs() -> list[str]:
    """Danh sách 78 lá lấy từ cards.json (nguồn duy nhất)."""
    import json
    with open(os.path.join(ROOT, "tarot prompt", "cards.json"), encoding="utf-8") as f:
        data = json.load(f)
    return [c["slug"] for c in data["cards"]]


def main() -> int:
    slugs = sys.argv[1:] or all_slugs()
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
