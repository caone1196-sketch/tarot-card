#!/usr/bin/env python3
"""
card_specs.py — bộ ĐỌC `tarot prompt/02-CHARACTER-SPECS.md` và gộp vào dữ liệu lá.

Từ 2026-09-03, **02-CHARACTER-SPECS.md là chuẩn thông số nhân vật** (thay cho
01-CARD-TABLE.md). Quy tắc gộp:

  • 02 cung cấp: tuổi · mắt · tóc · vóc dáng (thang A–D) · màu da · nét riêng · không khí
  • cards.json cung cấp (và GIỮ NGUYÊN VĂN, không file nào được sửa):
        title · emblem · scene · count · group · n
  • Ngoại lệ: nếu cards.json mô tả tóc/dáng dạng "distinct per …" (nhiều nhân vật
    trong một lá, 02 chỉ có một nhân vật) thì GIỮ cards.json cho trường đó.
  • 6 lá vật-thuần (wands-ace, wands-08, cups-ace, swords-ace, swords-03,
    pentacles-ace) không có trong 02 → giữ nguyên như cards.json (tức là không có
    khối CHARACTER SPECIFICATION).

Chạy để kiểm tra lệch:
    python3 scripts/card_specs.py check
    python3 scripts/card_specs.py show 00-fool
"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS_MD = os.path.join(ROOT, "tarot prompt", "02-CHARACTER-SPECS.md")
CARDS_JSON = os.path.join(ROOT, "tarot prompt", "cards.json")

# 02: "| **[A]** **THE FOOL** `00-fool` | 19 | mắt | tóc | vóc | da | nét riêng | không khí |"
ROW_RE = re.compile(r"^\|\s*\*\*.+?\*\*\s+`(?P<slug>[a-z0-9-]+)`\s*\|")
GRADE_WORDS = {
    "A": "slender and delicate, light as wind, small waist",
    "B": "lean and graceful, soft natural tone, dancer's lines",
    "C": "softly average, balanced, natural curves within an average frame",
    "D": "average but slightly fuller, still within an average frame, no exaggeration",
}


def _clean(cell: str) -> str:
    """Bỏ markdown đậm/nghiêng, gộp khoảng trắng."""
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", cell)
    t = re.sub(r"\*([^*]+)\*", r"\1", t)
    return re.sub(r"\s+", " ", t).strip().strip("·").strip()


def load_specs(path: str = SPECS_MD) -> dict[str, dict]:
    """Đọc bảng BẢNG CHÍNH trong 02-CHARACTER-SPECS.md -> {slug: spec}."""
    if not os.path.exists(path):
        return {}
    out: dict[str, dict] = {}
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.startswith("|"):
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8:
            continue
        slug = m.group("slug")
        badge = ""
        bm = re.match(r"^\*\*(?:\[(.+?)\])?", cells[0])
        if bm and bm.group(1):
            badge = bm.group(1)
        build = cells[4]
        gm = re.match(r"^\*\*([ABCD])\*\*", build)
        grade = gm.group(1) if gm else None
        out[slug] = {
            "badge": badge,
            "age": _clean(cells[1]),
            "eyes": _clean(cells[2]),
            "hair": _clean(cells[3]),
            "build": _clean(build),
            "grade": grade,
            "skin": _clean(cells[5]),
            "signature": _clean(cells[6]),
            "aura": _clean(cells[7]),
            "source": os.path.basename(path),
        }
    return out


def merge(card: dict, specs: dict[str, dict]) -> tuple[dict, list[str]]:
    """Trả (spec hiệu dụng cho prompt, danh sách ghi chú nguồn)."""
    slug = card.get("slug", "")
    sp = specs.get(slug)
    notes: list[str] = []
    eff = {
        "title": card.get("title", ""),
        "emblem": card.get("emblem", ""),
        "scene": card.get("scene", ""),
        "count": card.get("count"),
        "age": card.get("age", ""),
        "hair": card.get("hair", ""),
        "build": card.get("build", ""),
    }
    if not sp:
        notes.append("khong co dong trong 02 (la vat-the-thuan) -> dung cards.json")
        return eff, notes

    for field in ("age", "hair", "build"):
        cur = str(card.get(field) or "").strip()
        if cur.lower().startswith("distinct"):
            notes.append(f"giu cards.json cho `{field}` (la co nhieu nhan vat, 02 chi mo ta 1)")
            continue
        if sp.get(field):
            eff[field] = sp[field]
            if cur and cur != sp[field]:
                notes.append(f"{field}: lay tu 02 (cards.json ghi khac)")
    for field in ("eyes", "skin", "signature", "aura"):
        eff[field] = sp.get(field, "")
    eff["grade"] = sp.get("grade")
    return eff, notes


def character_block(eff: dict) -> str:
    """Khối CHARACTER SPECIFICATION cho prompt (tiếng Anh, tiếng Việt giữ nguyên văn 02)."""
    if not (eff.get("age") or eff.get("hair") or eff.get("build")):
        return ""
    bits = []
    if eff.get("age"):
        age = re.sub(r"[^0-9]", "", str(eff["age"])) or eff["age"]
        bits.append(f"Age: {age} (strictly young adult, aged 18 to 25)")
    if eff.get("eyes"):
        bits.append(f"Eyes: {eff['eyes']}")
    if eff.get("hair"):
        bits.append(f"Hair: {eff['hair']}")
    if eff.get("build"):
        tier = f" (physique tier {eff['grade']}: {GRADE_WORDS[eff['grade']]})" if eff.get("grade") in GRADE_WORDS else ""
        bits.append(f"Physique: {eff['build']}{tier}")
    if eff.get("skin"):
        bits.append(f"Skin tone: {eff['skin']} — light range only, never deepened to brown or black even in shadow")
    if eff.get("signature"):
        bits.append(f"Signature detail: {eff['signature']}")
    if eff.get("aura"):
        bits.append(f"Mood / aura: {eff['aura']}")
    bits.append("Sensuality: render with heightened yet tasteful fine-art sensuality — "
                "confident, poised, soft classical anatomy, painterly skin in warm golden lighting")
    return "CHARACTER SPECIFICATION (source: 02-CHARACTER-SPECS.md): " + "; ".join(bits) + "."


def check() -> int:
    cards = json.load(open(CARDS_JSON, encoding="utf-8"))["cards"]
    specs = load_specs()
    if not specs:
        print(f"[loi] khong doc duoc bang nao tu {SPECS_MD}", file=sys.stderr)
        return 2
    by = {c["slug"]: c for c in cards}
    missing = [s for s in by if s not in specs]
    extra = [s for s in specs if s not in by]
    hair_diff, age_diff, build_only_02 = [], [], 0
    for s, sp in specs.items():
        c = by.get(s) or {}
        if str(c.get("hair", "")).strip() != sp["hair"] and not str(c.get("hair", "")).strip().lower().startswith("distinct"):
            hair_diff.append(s)
        if re.sub(r"\D", "", str(c.get("age", ""))) != re.sub(r"\D", "", sp["age"]):
            age_diff.append((s, c.get("age"), sp["age"]))
        if str(c.get("build", "")).strip() != sp["build"]:
            build_only_02 += 1
    print(f"02-CHARACTER-SPECS.md : {len(specs)} dong  |  cards.json : {len(cards)} la")
    print(f"- la cards.json co nhung 02 khong co : {len(missing)} -> {', '.join(sorted(missing)) or '—'}")
    print(f"- la 02 co nhung cards.json khong co : {len(extra)} -> {', '.join(sorted(extra)) or '—'}")
    print(f"- TUOI lech giua 02 va cards.json    : {len(age_diff)} {age_diff if age_diff else ''}")
    print(f"- TOC  lech (02 thang, cards.json ghi khac): {len(hair_diff)}")
    for s in hair_diff:
        print(f"    · {s}: 02 = \"{specs[s]['hair'][:78]}…\"  |  json = \"{str(by[s].get('hair',''))[:78]}…\"")
    print(f"- DANG khac nhau ve he thong (02 dung thang A-D): {build_only_02}/{len(specs)}  -> 02 duoc dung trong prompt")
    grades = {}
    for sp in specs.values():
        grades[sp.get("grade") or "?"] = grades.get(sp.get("grade") or "?", 0) + 1
    print(f"- phan bo A-D: {grades}")
    print(f"- truong moi chi 02 co (mat · da · net rieng · khong khi): "
          f"{sum(1 for sp in specs.values() if all(sp.get(k) for k in ('eyes','skin','signature','aura')))}/{len(specs)} la day du")
    return 0


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    cmd = argv[0] if argv else "check"
    if cmd == "check":
        return check()
    if cmd == "show":
        if len(argv) < 2:
            print("Usage: card_specs.py show <slug>", file=sys.stderr)
            return 2
        cards = {c["slug"]: c for c in json.load(open(CARDS_JSON, encoding="utf-8"))["cards"]}
        specs = load_specs()
        s = argv[1]
        if s not in cards:
            print(f"[loi] khong co slug {s}", file=sys.stderr)
            return 2
        eff, notes = merge(cards[s], specs)
        print(json.dumps(eff, ensure_ascii=False, indent=2))
        print("\nGHI CHU NGUON:")
        for n in notes:
            print("  -", n)
        print("\n" + character_block(eff))
        return 0
    print("Usage: card_specs.py [check | show <slug>]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
