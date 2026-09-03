#!/usr/bin/env python3
"""
Build Tarot Card Prompts using the THE STAR ANCHOR STANDARD:
- Full open window display matching the scale and expansive open space of The Star.
- MỌI trường (tuổi · tóc · vóc · huy hiệu · tên · cảnh · `count`) lấy từ ĐÚNG MỘT nguồn:
  `tarot prompt/cards.json`. Không script nào đọc `01-CARD-TABLE.md` / `02-CHARACTER-SPECS.md`
  để ghi đè dữ liệu — hai file đó là tài liệu đọc, muốn đổi gì thì sửa `cards.json`.
- 100% Female cast aged strictly between 18 and 25 years old.
- Natural, unconstrained environments without artificial inner column barriers.
- Symmetrical golden gothic line-art frame border, top medallion emblem, bottom ribbon title.

Usage:
    python3 scripts/build_prompts.py check
    python3 scripts/build_prompts.py prompt <slug>
    python3 scripts/build_prompts.py all
    python3 scripts/build_prompts.py md
"""

import json
import os
import re
import sys

CARDS_JSON = "tarot prompt/cards.json"
OUT_DIR = "prompts/out"
STANDARD_JSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "standards", "17-the-star", "standard.json")


def load_standard():
    """Bộ chuẩn khung đo được (standards/17-the-star/standard.json) — có thì dùng, không thì bỏ."""
    try:
        with open(STANDARD_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def load_data():
    with open(CARDS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def format_count_lock(count_info):
    if not count_info:
        return ""
    n = count_info.get("n")
    obj = count_info.get("obj")
    layout = count_info.get("layout")
    return f"COUNT LOCK (EXACTLY {n} {obj}): {layout}."

def format_character_spec(card):
    """Khối CHARACTER SPECIFICATION — CHỈ đọc `cards.json` (age · hair · build)."""
    bits = []
    if card.get("age"):
        age = re.sub(r"[^0-9]", "", str(card["age"])) or str(card["age"]).strip()
        bits.append(f"Age: {age} (strictly young adult, aged 18 to 25)")
    if card.get("hair"):
        bits.append(f"Hair: {str(card['hair']).strip()}")
    if card.get("build"):
        bits.append(f"Physique: {str(card['build']).strip()}")
    if not bits:
        return ""
    bits.append("Sensuality: render with heightened yet tasteful fine-art sensuality — "
                "confident, poised, soft classical anatomy, painterly skin in warm golden lighting")
    return "CHARACTER SPECIFICATION (source: cards.json): " + "; ".join(bits) + "."

def frame_clause(std, use_reference=True):
    """Mô tả khung = đúng những gì đo được ở lá neo (standards/…/standard.json)."""
    if not use_reference:
        return ("ornate vintage gothic tarot card composition matching the open window style "
                "of THE STAR.")
    if not std:
        return ("built inside the reference frame, matching the EXACT open window display, scale, "
                "and lighting style of THE STAR: keep the intricate thin golden line-art border "
                "in vintage gothic style and aged parchment background texture.")
    rule_l = std["frame"].get("rule_offset_left_px")
    band = std["frame"]["band_px"]
    style = std.get("frame_style", "thin-line-art")
    plates = std.get("plates", {})
    no_plate = (not plates.get("medallion", {}).get("present")) and (not plates.get("ribbon", {}).get("present"))
    parts = [
        (f"built INSIDE the measured reference frame of THE STAR (style: {style}): the painted scene "
         f"runs full bleed to all four edges of the card, and only a thin antique-gold rule line "
         f"inset about {rule_l} px from each edge plus small gothic corner flourishes are painted on "
         f"top of it — no outer parchment margin, no wide decorative border, no oval medallion plate, "
         f"no ribbon banner"
         if (no_plate and rule_l is not None) else
         "built inside the measured reference frame of THE STAR, matching its open window display, "
         "scale and lighting"),
        ("inside that frame everything is pure scene, with the card title lettered directly over the "
         "lower part of the image" if no_plate else
         "keep the oval medallion plate at the top and the ribbon banner at the bottom"),
    ]
    body = ", ".join(parts).rstrip(".")
    return body + ". " + ("" if not std else
                          f"(measured frame spec: {std['card_size_wh'][0]}×{std['card_size_wh'][1]} px, "
                          f"content window {std['frame']['content_window_xyxy']}, gold coverage "
                          f"{round(std['frame']['gold_coverage_total'] * 100, 1)}% — see "
                          f"standards/{std['anchor_card']['slug']}/standard.json).")


QUALITY_DIRECTIVE = (
    "RENDER QUALITY (HARD): produce the final image in crisp 4K ultra-high resolution with every edge, "
    "filament and texture razor sharp; completely remove film grain and sensor noise for a clean, smooth "
    "fine-art surface; maximize fine micro-detail in hair strands, water droplets, foliage, lace and gold "
    "embossing; professional studio-grade clarity, saturation and contrast, no artifacts, no speckle."
)

def build_card_prompt_star_standard(card, use_reference=True, std=None):
    emblem = card.get("emblem", "an ornate heraldic symbol")
    title = card.get("title", "")
    scene = card.get("scene", "")           # NGUYÊN VĂN từ cards.json — không file nào được sửa
    count_str = format_count_lock(card.get("count"))
    char_str = format_character_spec(card)
    std = load_standard() if std is None else std
    framed_like_star = bool(std and not std.get("plates", {}).get("medallion", {}).get("present")
                            and not std.get("plates", {}).get("ribbon", {}).get("present"))

    anatomy_lock = (
        "ANATOMY LOCK (HARD RULE): exactly two arms, two legs, one head and one torso per character; "
        "every joint (shoulder, elbow, wrist, hip, knee, ankle) connects naturally to the body — "
        "NO extra limbs, NO limbs fused into the ribs, hip, chest or back, NO missing or amputated arms, "
        "NO deformed joints, NO wrong finger counts; keep both arms clearly separated from the torso "
        "with visible armpits, elbows and wrists."
    )

    extra_directives = []
    if char_str:
        extra_directives.append(char_str)
    if count_str:
        extra_directives.append(count_str)
    extra_directives.append(anatomy_lock)
    extra_directives.append(QUALITY_DIRECTIVE)
    extra_text = (" " + " ".join(extra_directives)) if extra_directives else ""

    ref_clause = frame_clause(std, use_reference)

    if framed_like_star:
        emblem_clause = (f"High in the composition, painted directly over the scene, {emblem} rendered "
                         f"as a small glowing antique-gold line-art motif (no plate, no frame around it). ")
        title_clause = (f"The title \"{title}\" is painted directly over the lower part of the scene in "
                        f"clean antique-gold serif capitals, with no banner behind it. ")
    else:
        emblem_clause = f"At the TOP: inside the oval medallion plate, {emblem} in glowing antique gold. "
        title_clause = (f"At the BOTTOM: inside the ribbon banner, the title \"{title}\" in clean "
                        f"antique gold lettering. ")

    return (
        f"A single tarot card \"{title}\" {ref_clause} "
        f"{emblem_clause}{title_clause}" +
        (f"The scene occupies the whole card edge to edge, passing beneath the thin gold rule line, "
         f"with no inner arch or column barriers: " if framed_like_star else
         f"In the large open center panel (filling the entire inner window edge to edge and bleeding "
         f"slightly beneath the golden border, matching the open space of The Star without heavy inner "
         f"arch barriers): ")
        + f"{scene}.{extra_text} "
        f"Depth layering: enlarge the scene so its edges bleed to the very outer edge of the card, then paint "
        f"{'the thin golden rule line and the four corner flourishes' if framed_like_star else 'the thin golden line-art border, corner flourishes, oval medallion and ribbon banner'} ON TOP of the scene edges — foreground ornament overlapping the background content for a strong sense of depth. "
        f"Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, "
        f"{'thin symmetrical golden rule line at the card edges' if framed_like_star else 'symmetrical golden frame border'}, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail."
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/build_prompts.py [check | prompt <slug> | all | md]")
        sys.exit(1)

    cmd = sys.argv[1]
    data = load_data()
    cards = data.get("cards", [])

    if cmd == "check":
        print(f"Loaded {len(cards)} cards successfully.")
        print("- Nguon duy nhất: tarot prompt/cards.json (khong doc 01/02 de ghi de)")
        std = load_standard()
        print("- Chuan khung: " + (f"{std['anchor_card']['slug']} · {std['frame_style']} · "
              f"rule line {std['frame']['rule_offset_left_px']}px · medallion={std['plates']['medallion']['present']} · "
              f"ribbon={std['plates']['ribbon']['present']}" if std else "KHONG CO (fallback noi dung cu)"))
        with_age = sum(1 for c in cards if c.get("age"))
        with_hair = sum(1 for c in cards if c.get("hair"))
        with_build = sum(1 for c in cards if c.get("build"))
        print(f"- Cards with defined Age (18-25): {with_age}")
        print(f"- Cards with defined Hair: {with_hair}")
        print(f"- Cards with defined Build: {with_build}")
        print("All card character definitions are valid.")

    elif cmd == "prompt":
        if len(sys.argv) < 3:
            print("Please specify card slug, e.g. python3 scripts/build_prompts.py prompt 00-fool")
            sys.exit(1)
        slug = sys.argv[2]
        match = next((c for c in cards if c["slug"] == slug), None)
        if not match:
            print(f"Card '{slug}' not found.")
            sys.exit(1)
        print("=== THE STAR ANCHOR STANDARD PROMPT ===")
        print(build_card_prompt_star_standard(match, use_reference=True))

    elif cmd == "all":
        os.makedirs(OUT_DIR, exist_ok=True)
        for c in cards:
            slug = c["slug"]
            p = build_card_prompt_star_standard(c, use_reference=True)
            with open(os.path.join(OUT_DIR, f"{slug}.txt"), "w", encoding="utf-8") as f:
                f.write(p + "\n")
        print(f"Generated {len(cards)} Star-standard prompt files in {OUT_DIR}/")

    elif cmd == "md":
        print("| Slug | Title | Age | Hair Style & Color | Physique / Build |")
        print("|---|---|---|---|---|")
        for c in cards:
            if c.get("age"):
                print(f"| `{c['slug']}` | **{c['title']}** | {c.get('age')} | {c.get('hair', '')[:40]}... | {c.get('build', '')[:40]}... |")

if __name__ == "__main__":
    main()
