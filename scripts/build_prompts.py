#!/usr/bin/env python3
"""
Build Tarot Card Prompts using the THE STAR ANCHOR STANDARD:
- Full open window display matching the scale and expansive open space of The Star.
- Rich, sensual fine-art character poses based on 01-CARD-TABLE.md (The Empress standard).
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
import sys

CARDS_JSON = "tarot prompt/cards.json"
OUT_DIR = "prompts/out"

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
    age = card.get("age")
    hair = card.get("hair")
    build = card.get("build")

    specs = []
    if age:
        specs.append(f"Age: {age} (strictly young adult, aged 18 to 25)")
    if hair:
        specs.append(f"Hair: {hair}")
    if build:
        specs.append(f"Physique: {build}")

    specs.append(
        "Sensuality: render with heightened yet tasteful fine-art sensuality — "
        "confident, poised, soft classical anatomy, painterly skin in warm golden lighting"
    )

    return "CHARACTER SPECIFICATION: " + "; ".join(specs) + "."

def build_card_prompt_star_standard(card, use_reference=True):
    emblem = card.get("emblem", "an ornate heraldic symbol")
    title = card.get("title", "")
    scene = card.get("scene", "")
    count_str = format_count_lock(card.get("count"))
    char_str = format_character_spec(card)

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
    extra_text = (" " + " ".join(extra_directives)) if extra_directives else ""

    ref_clause = (
        "built inside the reference frame, matching the EXACT open window display, scale, and lighting style of THE STAR: "
        "keep the intricate thin golden line-art border in vintage gothic style and aged parchment background texture."
        if use_reference
        else "ornate vintage gothic tarot card composition matching the open window style of THE STAR."
    )

    return (
        f"A single tarot card \"{title}\" {ref_clause} "
        f"At the TOP: inside the oval medallion plate, {emblem} in glowing antique gold. "
        f"At the BOTTOM: inside the ribbon banner, the title \"{title}\" in clean antique gold lettering. "
        f"In the large open center panel (filling the entire inner window edge to edge and bleeding slightly beneath the golden border, matching the open space of The Star without heavy inner arch barriers): "
        f"{scene}.{extra_text} "
        f"Depth layering: enlarge the scene so its edges extend slightly beneath the inner edge of the golden border, then paint the thin golden line-art border, corner flourishes, oval medallion and ribbon banner ON TOP of the scene edges — foreground ornament overlapping the background content for a strong sense of depth. "
        f"Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric perspective and depth, "
        f"symmetrical golden frame border, perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail."
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
