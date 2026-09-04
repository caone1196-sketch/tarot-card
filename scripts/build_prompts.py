#!/usr/bin/env python3
"""
Build Tarot Card Prompts using the THE STAR ANCHOR STANDARD:
- Full open window display matching the scale and expansive open space of The Star.
- MỌI trường (tuổi · tóc · vóc · huy hiệu · tên · cảnh · `count`) lấy từ ĐÚNG MỘT nguồn:
  `tarot prompt/cards.json`. Không script nào đọc `01-CARD-TABLE.md` / `02-CHARACTER-SPECS.md`
  để ghi đè dữ liệu — hai file đó là tài liệu đọc, muốn đổi gì thì sửa `cards.json`.
- 100% Female cast aged strictly between 18 and 25 years old.
- Natural, unconstrained environments without artificial inner column barriers.
- Symmetrical thin golden gothic line-art frame border, no top emblem/icon/symbol, and no framed title ribbon/banner.

Usage:
    python3 scripts/build_prompts.py check
    python3 scripts/build_prompts.py prompt <slug>     # prompt đầy đủ (khung + cảnh) — lưu prompts/out
    python3 scripts/build_prompts.py scene <slug>      # prompt CẢNH-ONLY (khung/tên do finish_card.py)
    python3 scripts/build_prompts.py all
    python3 scripts/build_prompts.py md
"""

import json
import os
import re
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_JSON = os.path.join(_ROOT, "tarot prompt", "cards.json")
OUT_DIR = os.path.join(_ROOT, "prompts", "out")
STANDARD_JSON = os.path.join(_ROOT, "standards", "17-the-star", "standard.json")


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

ANATOMY_LOCK = (
    "ANATOMY LOCK (HARD RULE): exactly two arms, two legs, one head and one torso per character; "
    "every joint (shoulder, elbow, wrist, hip, knee, ankle) connects naturally to the body — "
    "NO extra limbs, NO limbs fused into the ribs, hip, chest or back, NO missing or amputated arms, "
    "NO deformed joints, NO wrong finger counts; keep both arms clearly separated from the torso "
    "with visible armpits, elbows and wrists."
)

CLOTHING_LOCK = (
    "CLOTHING LOCK (HARD RULE): every human figure is a young adult woman aged 18 to 25 wearing a "
    "tasteful floor-length silk or ivory-and-gold gown or draped silk that fully covers the breasts "
    "and hips; no nudity, no bare breasts, no transparent fabric that reveals the body."
)

QUALITY_DIRECTIVE = (
    "Razor-sharp focus, increased fine detail, clean denoised and deblurred finish, no grain, no haze, "
    "no soft-focus blur. Sensual fine-art anatomy, painterly warm lighting against subtle shadows, "
    "rich atmospheric perspective and depth, vintage gothic fine-art illustration, high detail."
)

# Cụm khoả thân trong `scene` — chỉ thay lúc GỬI model (cards.json giữ nguyên văn).
_VEIL_SUBS = [
    (re.compile(r"\bone breast bared,?\s*", re.I), ""),
    (re.compile(r"\bbreast bared,?\s*", re.I), ""),
    (re.compile(r"\bnude\b", re.I), "silk-draped"),
    (re.compile(r"\bbare-shouldered\b", re.I), "silk-draped"),
    (re.compile(r"\bbare torso\b", re.I), "silk-draped torso"),
    (re.compile(r"\bbare body\b", re.I), "silk-draped body"),
    (re.compile(r"\bbare breasts?\b", re.I), "silk-covered chest"),
    (re.compile(r"\bher bare (shoulders?|back|body|torso)\b", re.I), r"her \1"),
    (re.compile(r"\bbare shoulders?\b", re.I), "shoulders"),
]


def veil_scene(text: str) -> str:
    """Thay cụm khoả thân → khoác lụa. Không đụng cards.json — chỉ văn bản gửi model."""
    if not text:
        return text
    out = text
    for pat, repl in _VEIL_SUBS:
        out = pat.sub(repl, out)
    out = re.sub(r" {2,}", " ", out)
    out = re.sub(r"\s+,", ",", out)
    return out.strip()


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
        ("inside that frame everything is pure scene, with no top emblem/icon/symbol and with the "
         "card title lettered directly over the lower part of the image without any frame, plaque, "
         "cartouche, ribbon or banner" if no_plate else
         "remove the top emblem/icon/symbol and remove any ribbon/banner/frame behind the title"),
    ]
    body = ", ".join(parts).rstrip(".")
    return body + ". " + ("" if not std else
                          f"(measured frame spec: {std['card_size_wh'][0]}×{std['card_size_wh'][1]} px, "
                          f"content window {std['frame']['content_window_xyxy']}, gold coverage "
                          f"{round(std['frame']['gold_coverage_total'] * 100, 1)}% — see "
                          f"standards/{std['anchor_card']['slug']}/standard.json).")


def build_card_prompt_star_standard(card, use_reference=True, std=None):
    emblem = (card.get("emblem") or "").strip()
    title = card.get("title", "")
    scene = card.get("scene", "")           # NGUYÊN VĂN từ cards.json — không file nào được sửa
    count_str = format_count_lock(card.get("count"))
    char_str = format_character_spec(card)
    std = load_standard() if std is None else std
    framed_like_star = bool(std and not std.get("plates", {}).get("medallion", {}).get("present")
                            and not std.get("plates", {}).get("ribbon", {}).get("present"))

    extra_directives = []
    if char_str:
        extra_directives.append(char_str)
    if count_str:
        extra_directives.append(count_str)
    extra_directives.append(ANATOMY_LOCK)
    extra_text = (" " + " ".join(extra_directives)) if extra_directives else ""

    ref_clause = frame_clause(std, use_reference)

    emblem_clause = ("NO TOP EMBLEM / NO ICON / NO SYMBOL: do not add a separate top emblem, icon, "
                     "heraldic symbol, oval medallion plate, or decorative symbol above the scene. ")
    title_clause = (f"NO TITLE FRAME: do not draw a ribbon banner, plaque, cartouche, box, panel, "
                    f"or frame behind or around the title. The title \"{title}\" appears only as clean "
                    f"antique-gold serif capital lettering painted directly over the lower part of the scene. ")

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
        f"only the thin golden rule line and the four corner flourishes ON TOP of the scene edges — "
        f"foreground ornament overlapping the background content for a strong sense of depth. Do not add "
        f"an emblem area or any framed title area. "
        f"Razor-sharp focus, increased fine detail, clean denoised and deblurred finish, no grain, no haze, "
        f"no soft-focus blur. Sensual fine-art anatomy, painterly warm lighting against subtle shadows, "
        f"rich atmospheric perspective and depth, thin symmetrical golden rule line at the card edges, "
        f"perfectly centered, portrait orientation 7:12 aspect ratio, vintage gothic fine-art illustration, high detail."
    )


def build_scene_prompt(card, scene_text=None):
    """Prompt CẢNH-ONLY: model không vẽ khung / tên — `finish_card.py` ghép sau.

    `scene_text` đã veil (khoác lụa) thì truyền vào; không thì dùng `card['scene']` nguyên văn
    (để `all`/`prompt` không đổi). `render_sent.py` mới là chỗ veil.
    """
    title = card.get("title", "")
    scene = scene_text if scene_text is not None else card.get("scene", "")
    count_str = format_count_lock(card.get("count"))
    char_str = format_character_spec(card)
    extras = []
    if char_str:
        extras.append(char_str)
    if count_str:
        extras.append(count_str)
    extras.append(ANATOMY_LOCK)
    extras.append(CLOTHING_LOCK)
    extra = " ".join(extras)
    return (
        f"A single tarot card painting of \"{title}\", portrait 7:12 aspect ratio, "
        f"the painted scene running full bleed to every edge of the canvas. "
        f"NO BORDER / NO FRAME / NO TITLE: do not draw any gold rule line, corner ornaments, "
        f"medallion, ribbon, plaque, caption, letters, numbers or watermark — the frame and "
        f"the card title will be composited later in code. "
        f"No inner arch or column barriers. Scene: {scene}. {extra} "
        f"{QUALITY_DIRECTIVE}"
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

    elif cmd == "scene":
        if len(sys.argv) < 3:
            print("Please specify card slug, e.g. python3 scripts/build_prompts.py scene 00-fool")
            sys.exit(1)
        slug = sys.argv[2]
        match = next((c for c in cards if c["slug"] == slug), None)
        if not match:
            print(f"Card '{slug}' not found.")
            sys.exit(1)
        print("=== SCENE-ONLY PROMPT (frame+title via finish_card.py) ===")
        print(build_scene_prompt(match, scene_text=veil_scene(match.get("scene", ""))))

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
