#!/usr/bin/env python3
"""
Build Tarot Card Prompts — KHUNG BÀI MỚI (4 LỚP · KHÔNG HUY HIỆU).

Quét dữ liệu từ:
- `tarot prompt/02-CHARACTER-SPECS.md` — bảng thông số 72 nhân vật
  (mắt · tóc · vóc dáng A–D · màu da · nét riêng · không khí) — nguồn chuẩn.
- `tarot prompt/cards.json` — title / scene / count / emblem (huy hiệu KHÔNG
  còn dùng trong khung, chỉ giữ dữ liệu lịch sử).

Mỗi prompt theo mẫu khung 4 lớp:
  1. NỀN            — giấy da cổ phủ kín lá
  2. NỘI DUNG TRÀN VIỀN — cảnh phủ sát mép, chui xuống dưới khung vàng
  3. KHUNG HỌA TIẾT MẢNH — viền vàng mảnh sát lề, vẽ ĐÈ lên nội dung
  4. KHUNG TÊN       — dải băng vàng ở đáy chứa tên lá (KHÔNG medallion/huy hiệu)

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
SPECS_MD = "tarot prompt/02-CHARACTER-SPECS.md"
OUT_DIR = "prompts/out"

# ---------------------------------------------------------------- data
def load_data():
    with open(CARDS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def parse_character_specs() -> dict[str, dict]:
    """Đọc bảng chính trong 02-CHARACTER-SPECS.md thành dict theo slug.

    Cột: Lá | Tuổi | Đôi mắt | Kiểu tóc (chuẩn) | Vóc dáng | Màu da | Nét riêng | Không khí
    """
    specs = {}
    with open(SPECS_MD, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("|") or line.startswith("|--"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != 8:
                continue
            m = re.search(r"`([a-z0-9\-]+)`", cells[0])
            if not m:
                continue
            slug = m.group(1)

            # Vóc dáng: tháo grade A/B/C/D khỏi mô tả
            build_cell = cells[4]
            g = re.match(r"\*\*([A-D])\*\*\s*(.*)", build_cell)
            grade, build = (g.group(1), g.group(2).strip()) if g else ("", build_cell)

            specs[slug] = {
                "age": int(cells[1]),
                "eyes": cells[2],
                "hair": cells[3],
                "grade": grade,
                "build": build,
                "skin": cells[5],
                "signature": cells[6],
                "aura": cells[7],
            }
    return specs


GRADE_EN = {
    "A": "A — slender / delicate",
    "B": "B — lean / toned",
    "C": "C — average soft",
    "D": "D — average shapely (ceiling: never plus-size)",
}
SKIN_RULE = (
    "SKIN TONES LOCK: only the 10 light-to-warm tones (porcelain, ivory, fair, "
    "warm peach, light olive, sand, warm tan, honey, light bronze, amber-gold); "
    "NEVER dark, brown-black or black skin, even in shadow."
)
# QUẦNG MỀM GẦN VẬT THỂ — giữ gợn mờ / halo mềm quanh đồ vật, nguồn sáng (không phải nhiễu)
SOFT_OBJECT_HALO = (
    "SOFT OBJECT HALO: keep a gentle blurred halo / subtle haze close to objects — water ripples "
    "around jugs and vessels, soft glow around lamps, candles and gold, light bloom near stars and "
    "flames, faint soft reflection where objects meet water; these soft ambient ripples near objects "
    "are INTENTIONAL — do not remove them, but keep them smooth, painterly and localized (NOT noise, "
    "NOT grain, NOT sharp blur)."
)
# Thông số chất lượng: độ bóng · chi tiết · khử hạt/nhiễu · độ sắc nét
QUALITY_LOCK = (
    "QUALITY & SURFACE LOCK (HARD RULE): "
    "GLOSSY — luminous oil-paint sheen on skin, wet-glass specular highlights on shoulders, "
    "collarbones, hips and lips, no flat matte finish; "
    "DETAIL — ultra-high fine detail on hair strands, skin pores, jewellery and background textures; "
    "NOISE — perfectly clean image: NO film grain, NO sensor noise, NO speckles, NO dither artifacts, "
    "NO jpeg artefacts, NO chromatic fringing; smooth buttery gradients everywhere; "
    "SHARPNESS — razor-sharp crisp edges, high-contrast micro detail, tack-sharp focus on the figure "
    "and title, no soft blur, no motion blur on the figure."
)

# ---------------------------------------------------------------- card locks
# Cách diễn đạt ĐÃ THÀNH CÔNG (từ các phương án render được chấp nhận) — giữ
# nguyên văn để các lần generate sau đi đúng quỹ đạo này.
STAR_SCENE_LOCK = (
    "the scene is painted as a CLASSICAL ALLEGORICAL OIL PAINTING of a water nymph at night, "
    "in the manner of Victorian allegorical art / tasteful luminous style of old master paintings; "
    "a graceful young woman standing waist-deep in a calm moonlit lake, long pale gold wet hair "
    "flowing down her back, S-CURVE stance — hips swayed, torso softly leaning, one leg lightly bent; "
    "her face tilted slightly BACK, chin raised toward the stars; "
    "her right arm raised high overhead, hand gripping a golden pitcher, a silvery stream pouring "
    "from its spout ONTO her neck, gliding down her collarbone and torso like liquid glass, falling "
    "from her waist into the lake; "
    "her left arm hangs relaxed down and BEHIND her back, hand holding a second golden pitcher "
    "tilted slightly — NO water flows from it."
)
STAR_SKY_RIPPLE_LOCK = (
    "SKY LOCK: one large radiant EIGHT-POINTED gold star directly above her head, with SEVEN "
    "smaller stars arranged around it, ONLY these eight stars — NO moon, NO crescent. "
    "RIPPLE RULE (HARD): ripples appear ONLY in two zones — a circle of gentle ripples where her "
    "body meets the water surface, and a circle where the falling stream meets the water surface; "
    "NO other ripples anywhere, no ripple rings on her body."
)
CARD_LOCKS = {"17-the-star": (STAR_SCENE_LOCK, STAR_SKY_RIPPLE_LOCK)}


# ---------------------------------------------------------------- formatting
def format_count_lock(count_info):
    if not count_info:
        return ""
    n = count_info.get("n")
    obj = count_info.get("obj")
    layout = count_info.get("layout")
    return f"COUNT LOCK (EXACTLY {n} {obj}): {layout}."


def format_character_spec(card: dict, spec: dict | None) -> str:
    """CHARACTER SPEC từ 02-CHARACTER-SPECS.md (fallback: cards.json)."""
    if spec:
        grade = GRADE_EN.get(spec["grade"], spec["grade"])
        return (
            f"CHARACTER SPECIFICATION (source: 02-CHARACTER-SPECS.md): "
            f"a female figure, {spec['age']} years old (strictly 18-25, 100% female); "
            f"EYES: {spec['eyes']}; "
            f"HAIR: {spec['hair']}; "
            f"PHYSIQUE ({grade}): {spec['build']}; "
            f"SKIN: {spec['skin']}; "
            f"UNIQUE SIGNATURE (exactly one): {spec['signature']}; "
            f"ATMOSPHERE: {spec['aura']}. "
            f"{SKIN_RULE}"
        )

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


# ---------------------------------------------------------------- template
def build_card_prompt_new_frame(card: dict, spec: dict | None):
    title = card.get("title", "")
    scene = card.get("scene", "")
    scene_locks = CARD_LOCKS.get(card.get("slug"), ())
    if scene_locks:
        scene = " ".join(scene_locks)
    count_str = format_count_lock(card.get("count"))
    char_str = format_character_spec(card, spec)

    anatomy_lock = (
        "ANATOMY LOCK (HARD RULE): exactly two arms, two legs, one head and one torso per character; "
        "every joint (shoulder, elbow, wrist, hip, knee, ankle) connects naturally to the body — "
        "NO extra limbs, NO limbs fused into the ribs, hip, chest or back, NO missing or amputated arms, "
        "NO deformed joints, NO wrong finger counts; keep both arms clearly separated from the torso "
        "with visible armpits, elbows and wrists."
    )

    # luôn giữ "gợn mờ gần vật thể" (soft object halo) — mọi lá
    extras = " ".join(x for x in (char_str, SOFT_OBJECT_HALO, count_str, anatomy_lock) if x)

    return (
        f'A single tarot card "{title}" in vintage gothic fine-art style, portrait 7:12 aspect ratio, '
        f"high detail, perfectly centered.\n\n"
        f"PAINT IT AS 4 LAYERS, background to foreground:\n"
        f"LAYER 1 — BACKGROUND: an aged parchment / vellum texture covering the WHOLE card, "
        f"sepia-warm, subtle stains and fibres.\n"
        f'LAYER 2 — CONTENT (FULL BLEED): {scene}. {extras} '
        f"The scene is enlarged FULL-BLEED so its edges reach the card edges and slip slightly "
        f"beneath the thin golden frame.\n"
        f"LAYER 3 — FRAME: a very thin, delicate METALLIC ANTIQUE-GOLD line-art gothic frame sitting "
        f"close to the card edge, symmetrical, with small filigree corner flourishes — rich deep gold "
        f"stroke with dark rim, bright core and a faint warm halo — painted ON TOP of the scene edges "
        f"(foreground ornament over background content); stays THIN. NO medallion, NO emblem, NO icon, "
        f"NO crest anywhere on the card.\n"
        f"LAYER 4 — TITLE: at the BOTTOM, the title \"{title}\" in antique blackletter gold lettering "
        f"whose baseline gently CURVES (letters rise at the ends, sag in the middle), placed DIRECTLY on "
        f"the scene — NO title frame, NO plate, NO ribbon, NO cartouche, NO border around the text; "
        f"clean carved edges with a thin shadow.\n\n"
        f"{QUALITY_LOCK}\n"
        f"Sensual fine-art anatomy, painterly warm lighting against subtle shadows, rich atmospheric "
        f"perspective and depth, no heavy inner arch barriers, vintage gothic fine-art illustration, "
        f"ultra-high detail."
    )


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    data = load_data()
    cards = data.get("cards", [])
    specs = parse_character_specs()

    if cmd == "check":
        print(f"Loaded {len(cards)} cards from cards.json.")
        print(f"Loaded {len(specs)} character specs from 02-CHARACTER-SPECS.md.")
        missing = [c["slug"] for c in cards if c["slug"] not in specs]
        print(f"Cards without character spec (object-only, expected 6): {missing}")
        print("All frame templates now use the 4-layer structure WITHOUT emblem medallion.")

    elif cmd == "prompt":
        if len(sys.argv) < 3:
            print("Usage: python3 scripts/build_prompts.py prompt <slug>")
            sys.exit(1)
        slug = sys.argv[2]
        match = next((c for c in cards if c["slug"] == slug), None)
        if not match:
            print(f"Card '{slug}' not found.")
            sys.exit(1)
        print(build_card_prompt_new_frame(match, specs.get(slug)))

    elif cmd == "all":
        os.makedirs(OUT_DIR, exist_ok=True)
        for c in cards:
            slug = c["slug"]
            p = build_card_prompt_new_frame(c, specs.get(slug))
            with open(os.path.join(OUT_DIR, f"{slug}.txt"), "w", encoding="utf-8") as f:
                f.write(p + "\n")
        print(f"Generated {len(cards)} prompts (4-layer frame, no emblem) in {OUT_DIR}/")

    elif cmd == "md":
        print("| Slug | Title | Age | Eyes | Hair | Physique | Skin | Signature | Aura |")
        print("|---|---|---|---|---|---|---|---|---|")
        for c in cards:
            s = specs.get(c["slug"])
            if not s:
                continue
            print(f"| `{c['slug']}` | **{c['title']}** | {s['age']} | {s['eyes'][:38]}… "
                  f"| {s['hair'][:38]}… | {s['grade']} {s['build'][:30]}… | {s['skin']} "
                  f"| {s['signature'][:34]}… | {s['aura'][:34]}… |")

    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
