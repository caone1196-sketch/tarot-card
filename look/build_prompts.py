#!/usr/bin/env python3
"""Sinh 78 prompt chuẩn hóa theo "look" THẾ STAR (không đè ảnh cards/).

Mỗi prompt nhúng cùng một khối STYLE LOCK (phong cách vẽ + bảng màu + khung viền
+ tỉ lệ 7:12) trích xuất từ cards/17-the-star.png, để cả 78 lá khi tạo lại đều
ra cùng một phong cách vẽ và tỉ lệ đồng nhất.

Cách dùng:
    python3 look/build_prompts.py          # ghi đè 78 file vào look/prompts/
    python3 look/build_prompts.py <slug>   # in prompt 1 lá ra stdout
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_JSON = os.path.join(ROOT, "tarot prompt", "cards.json")
OUT_DIR = os.path.join(ROOT, "look", "prompts")

STYLE_LOCK = (
    "STYLE LOCK (unified deck look, anchored to THE STAR): fine-art oil-painting "
    "illustration with painterly brushwork and softly blended forms; warm directional "
    "light against soft cool shadows; rich atmospheric perspective with deep spatial "
    "recession; aged parchment/vellum base with a thin, razor-sharp, perfectly "
    "symmetrical golden gothic line-art border of antique gold filigree with corner "
    "flourishes; palette anchored to The Star (cream #ecd5a9, antique gold #d6b988, "
    "gold line #e0c595, bronze #c5a674 to #9f7e59 to umber #674b2e, deep slate "
    "#343944 to near-black #1a1c25, muted steel blue #76888f); sensual fine-art "
    "anatomy, tasteful classical rendering, painterly skin in warm golden light; "
    "perfectly centered, portrait orientation 7:12 aspect ratio (784x1360), high detail."
)

ANATOMY_LOCK = (
    "ANATOMY LOCK (HARD RULE): exactly two arms, two legs, one head and one torso per "
    "character; every joint (shoulder, elbow, wrist, hip, knee, ankle) connects "
    "naturally to the body — NO extra limbs, NO limbs fused into the ribs, hip, chest "
    "or back, NO missing or amputated arms, NO deformed joints, NO wrong finger counts; "
    "keep both arms clearly separated from the torso with visible armpits, elbows and "
    "wrists."
)


def format_count_lock(count_info):
    if not count_info:
        return ""
    n = count_info.get("n")
    obj = count_info.get("obj")
    layout = count_info.get("layout")
    return f"COUNT LOCK (EXACTLY {n} {obj}): {layout}."


def format_character_spec(card):
    parts = []
    if card.get("age"):
        parts.append(f"Age: {card['age']} (strictly young adult, aged 18 to 25)")
    if card.get("hair"):
        parts.append(f"Hair: {card['hair']}")
    if card.get("build"):
        parts.append(f"Physique: {card['build']}")
    parts.append(
        "Sensuality: render with heightened yet tasteful fine-art sensuality — "
        "confident, poised, soft classical anatomy, painterly skin in warm golden lighting"
    )
    return "CHARACTER SPECIFICATION: " + "; ".join(parts) + "."


def build_prompt(card):
    title = card.get("title", "")
    emblem = card.get("emblem", "an ornate heraldic symbol")
    scene = card.get("scene", "")
    char = format_character_spec(card)
    count = format_count_lock(card.get("count"))

    blocks = [
        f'A single tarot card "{title}", built inside the reference frame matching the '
        f"EXACT open-window display, scale and lighting style of THE STAR.",
        STYLE_LOCK,
        f"At the TOP: inside the oval medallion plate, {emblem} in glowing antique gold.",
        f'At the BOTTOM: inside the ribbon banner, the title "{title}" in clean antique '
        f"gold lettering.",
        "In the large open center panel (filling the entire inner window edge to edge "
        "and bleeding slightly beneath the golden border, matching the open space of "
        f"The Star without heavy inner arch barriers): {scene}.",
        char,
        count,
        ANATOMY_LOCK,
        "Depth layering: enlarge the scene so its edges extend slightly beneath the "
        "inner edge of the golden border, then paint the thin golden line-art border, "
        "corner flourishes, oval medallion and ribbon banner ON TOP of the scene edges "
        "— foreground ornament overlapping the background content for a strong sense "
        "of depth.",
    ]
    return "\n".join(b for b in blocks if b) + "\n"


def main():
    with open(CARDS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    cards = data["cards"]

    if len(sys.argv) > 1:
        slug = sys.argv[1]
        match = next((c for c in cards if c["slug"] == slug), None)
        if not match:
            sys.exit(f"Không tìm thấy lá '{slug}'")
        print(build_prompt(match))
        return

    os.makedirs(OUT_DIR, exist_ok=True)
    for c in cards:
        path = os.path.join(OUT_DIR, f"{c['slug']}.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build_prompt(c))
    print(f"Đã sinh {len(cards)} prompt chuẩn look vào {os.path.relpath(OUT_DIR, ROOT)}/")


if __name__ == "__main__":
    main()
