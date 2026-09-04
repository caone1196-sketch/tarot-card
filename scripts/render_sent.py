#!/usr/bin/env python3
"""Tạo văn bản prompt GỬI model.

Mặc định: prompt CẢNH-ONLY (không khung, không tên) — `scripts/finish_card.py`
ghép khung The Star + chữ tên sau khi sinh ảnh. `cards.json` giữ nguyên văn;
khoác lụa chỉ xảy ra ở bước này.

    python3 scripts/render_sent.py 06-lovers
    python3 scripts/render_sent.py 00-fool 01-magician
    python3 scripts/render_sent.py --full 00-fool     # prompt đầy đủ từ prompts/out (cũ)
    python3 scripts/render_sent.py --all              # ghi cả 78 file .sent.txt

File ra: cards/_regen/<slug>.sent.txt
"""
from __future__ import annotations

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from build_prompts import (  # noqa: E402
    build_card_prompt_star_standard,
    build_scene_prompt,
    load_data,
    veil_scene,
)

SRC = os.path.join(ROOT, "prompts", "out")
DST = os.path.join(ROOT, "cards", "_regen")

# slug -> [(chuỗi gốc trong cards.json/prompt, chuỗi thay thế)]
# Áp nếu tìm thấy; không có thì bỏ qua (scene đã rút gọn vẫn được veil_scene xử lý).
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
        "a slender nude empress, breast bared",
        "a slender empress in a softly draped ivory-and-gold silk gown with a low, covered neckline",
    )],
    "04-emperor": [(
        "draped only in a diaphanous transparent silk veil so fine it clings to her soft curves and "
        "glows with warm light against her skin, the gossamer fabric slipping from one shoulder",
        "draped in a diaphanous silk over-veil over a gold-trimmed ivory gown, the fabric glowing with "
        "warm light, slipping from one shoulder",
    )],
}


def apply_subs(slug: str, text: str) -> str:
    t = text
    for old, new in SUBS.get(slug, []):
        if old in t:
            t = t.replace(old, new, 1)
    return t


def build_scene(slug: str, card: dict) -> str:
    scene = apply_subs(slug, card.get("scene") or "")
    scene = veil_scene(scene)
    return build_scene_prompt(card, scene_text=scene)


def build_full(slug: str, card: dict) -> str:
    path = os.path.join(SRC, f"{slug}.txt")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            t = f.read().strip()
    else:
        t = build_card_prompt_star_standard(card, use_reference=True)
    t = apply_subs(slug, t)
    return veil_scene(t)


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    full = "--full" in argv
    dump_all = "--all" in argv
    argv = [a for a in argv if a not in ("--full", "--all")]

    data = load_data()
    cards = {c["slug"]: c for c in data.get("cards", [])}
    slugs = argv if argv else (sorted(cards) if dump_all else [])
    if not slugs:
        print("Usage: python3 scripts/render_sent.py [--full] <slug> [slug ...]")
        print("       python3 scripts/render_sent.py --all")
        print("Mặc định: prompt cảnh-only (khung + tên do scripts/finish_card.py).")
        return 2

    os.makedirs(DST, exist_ok=True)
    missing = [s for s in slugs if s not in cards]
    if missing:
        print(f"[loi] khong co slug: {', '.join(missing)}", file=sys.stderr)
        return 2

    for s in slugs:
        t = build_full(s, cards[s]) if full else build_scene(s, cards[s])
        with open(os.path.join(DST, f"{s}.sent.txt"), "w", encoding="utf-8") as f:
            f.write(t + "\n")
        kind = "full" if full else "scene-only"
        print(f"=== {s}  ({kind}, {len(t)} ky tu) ===")
        print(t)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
