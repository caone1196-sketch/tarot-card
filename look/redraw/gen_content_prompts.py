#!/usr/bin/env python3
"""Sinh 78 prompt "chỉ nội dung" (không khung/không chữ) để vẽ lại phần tranh.

Prompt này dành cho trình tạo ảnh: vẽ đúng cảnh + nhân vật của từng lá, full-bleed,
không viền, không medallion, không ribbon, không chữ — phần khung sẽ được ghép sau
bằng look/redraw/compose.py.

ĐỒNG NHẤT TRANG PHỤC: mọi lá dùng cùng một "wardrobe" — nhân vật chỉ khoác voan lụa
mỏng trong suốt (diaphanous transparent silk veil). Các lá lệch phong cách (khỏa thân
hoàn toàn, hoặc giáp/áo choàng/đầm) được ghi đè cảnh trong WARDROBE_FIX.

Cách dùng: python3 look/redraw/gen_content_prompts.py [slug]
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CARDS_JSON = os.path.join(ROOT, "tarot prompt", "cards.json")
OUT = os.path.join(ROOT, "look", "redraw", "prompts")

STYLE = (
    "fine-art oil-painting illustration with painterly brushwork and softly blended "
    "forms; warm directional light against soft cool shadows; rich atmospheric "
    "perspective with deep spatial recession; palette anchored to THE STAR (cream "
    "#ecd5a9, antique gold #d6b988, gold #e0c595, bronze #c5a674 to #9f7e59 to umber "
    "#674b2e, deep slate #343944 to near-black #1a1c25, muted steel blue #76888f); "
    "sensual fine-art anatomy, tasteful classical rendering, painterly skin in warm "
    "golden light; high detail."
)

ANATOMY = (
    "ANATOMY LOCK: exactly two arms, two legs, one head and one torso per character; "
    "every joint connects naturally; no extra limbs, no limbs fused to the body, no "
    "deformed joints, no wrong finger counts; both arms clearly separated from the "
    "torso with visible elbows and wrists."
)

HANDS = (
    "HANDS LOCK: every hand perfectly formed with exactly five fingers, fingers "
    "naturally separated and un-fused, no extra or missing digits, no twisted, "
    "clawed, melted or deformed hands; hands gripping any object with a relaxed, "
    "natural grasp."
)

POSE = (
    "POSE LOCK (artistic, sensual pose): an expressive, graceful pose with a soft "
    "S-curve through the spine, the back gently arched and the shoulders relaxed, "
    "weight shifted onto one leg or one hip in a flowing contrapposto; arms and "
    "hands rise into natural, elegant gestures instead of hanging stiffly at the "
    "sides; where the scene allows, lean or recline into a relaxed, languid "
    "attitude; the sheer veil trails, wraps and flows across the body to trace and "
    "emphasize the silhouette; no rigid symmetrical upright standing, no stiff "
    "mannequin posture."
)

WARDROBE = (
    "WARDROBE LOCK (uniform deck costume): every FEMALE figure draped only in a "
    "diaphanous transparent silk veil — gossamer-thin, softly clinging to and gently "
    "revealing the figure beneath; every MALE figure wearing only a simple loincloth "
    "(khố), bare-chested, nothing else; no opaque garments, no armor, no robes, no "
    "dresses, no modern clothing; the identical sheer silk drapery on women and "
    "loincloth on men for a consistent deck look."
)

# Ghi đè cảnh cho các lá lệch phong cách trang phục (khỏa thân / giáp / áo choàng / đầm)
WARDROBE_FIX = {
    "01-magician": "a young woman magician draped only in a diaphanous transparent silk veil that clings to and softly reveals her figure, one hand raising a wand to the sky and the other pointing down to the earth, the altar table before her laid with a cup, a sword, a wand and a pentacle, a garden of black roses behind her",
    "02-priestess": "a serene priestess draped only in a diaphanous transparent silk veil that softly veils her figure, seated between two stone pillars, a scroll of mystery resting in her lap, a silver crescent moon at her feet",
    "03-empress": "an empress draped only in a diaphanous transparent silk veil that clings to her soft curves, a crown of flowers in loosened hair, reclining on a velvet throne amid ripe golden wheat and fruits, a heart-shaped shield of Venus leaning beside her",
    "06-lovers": "a man wearing only a simple loincloth and a woman draped only in a diaphanous transparent silk veil, standing hand in hand beneath a great winged angel, her body turned three-quarters toward the viewer and his hand at the small of her back, the tree of knowledge with a serpent behind her, the tree of flames behind him",
    "08-strength": "a woman garlanded with roses, draped only in a diaphanous transparent silk veil, one knee raised, leaning in close to calmly close the jaws of a great golden lion, warm low sunlight, an infinity sign glowing above her head",
    "09-hermit": "a hermit woman standing on a bare mountain peak under a deep star-filled night sky, holding up a lit lantern with warm golden light pouring out of it, draped only in a diaphanous transparent silk veil that slips from one shoulder and clings softly to her figure, the golden lantern light glowing through the sheer silk",
    "11-justice": "a statuesque queen draped only in a diaphanous transparent silk veil slipping from one shoulder, a sword upright in one hand and balanced scales in the other, seated on a stone throne between pillars",
    "12-hanged": "a serene 21-year-old young woman draped only in a diaphanous transparent silk veil, suspended upside-down by one ankle from a living tree shaped like a cross, one leg bent gracefully, a radiant halo of golden light glowing around her head",
    "15-devil": "a horned winged female arch-devil draped in sheer black silk upon a dark pedestal; beside her two alluring young women draped in diaphanous sheer silk veils, posed in golden chains, their figures glowing in candlelit shadow inside an obsidian cavern",
    "17-the-star": "a young woman standing waist-deep in a clear pool at night, draped only in a diaphanous silk veil that clings wet to her body, her body arched back and turned three-quarters toward the viewer, wet hair falling down her back, both arms raised pouring water from two jugs, one knee lifted, a great eight-pointed star and seven smaller stars above",
    "18-moon": "a pale moon with a serene face dropping dew, two towers and a winding path, a water nymph draped only in a diaphanous transparent silk veil rising from the dark pool with water streaming over her shoulders, a wolf and a dog howling, a crayfish in the water",
    "19-sun": "a joyful young woman with a wreath of red flowers riding a calm white horse, draped only in a diaphanous transparent silk veil streaming in the wind, a red banner streaming, a radiant sun with a gentle face, a low sunflower wall",
    "wands-10": "a serene 23-year-old woman reclining gracefully on soft grass, draped only in a diaphanous transparent silk veil across her form, resting beside a boulder; leaning against the boulder behind her is one natural bundle of ten long wooden wands tied loosely at the middle with a thin cord, their upper ends spreading apart in a natural fan like an open hand fan, every wand the same length and thickness, evenly spaced with a clear gap of sky between each shaft, all ten tips clearly separated and countable, the lower ends gathered together in the grass, none crossing, none hidden, a distant sunlit castle beyond",
    "cups-02": "a young woman draped in a diaphanous transparent silk veil and a young man wearing only a simple loincloth facing one another, her body turned three-quarters toward the viewer, each raising one chalice in a toast, a caduceus with a lion head above them",
    "cups-03": "three maidens with flower wreaths dancing in a circle, each draped only in a diaphanous transparent silk veil, their bodies turned to the light, each raising one chalice, fruits on the ground",
    "cups-05": "a graceful adult woman draped only in a diaphanous transparent silk veil slipping from one shoulder, standing bowed with her back to the light by the river, three spilled chalices lying emptied and overturned in the foreground at her feet, two full chalices still standing upright on the bank behind her",
    "cups-06": "two graceful young women draped only in diaphanous transparent silk veils in an old courtyard garden, exchanging one flower-filled chalice, five more set along the wall behind them",
    "cups-08": "a solitary young woman draped only in a diaphanous transparent silk veil walking away with a staff, leaving eight stacked cups behind to journey toward misty moonlit peaks",
    "cups-09": "a content adult woman draped only in a diaphanous transparent silk veil slipping from one shoulder, seated at a banquet table before nine golden chalices proudly arranged in a neat grid on a shelf behind her",
    "cups-page": "a graceful young woman page by the sea draped only in a diaphanous transparent silk veil sliding off one shoulder, holding one chalice from which a curious fish looks out",
    "cups-knight": "a graceful 22-year-old female knight draped only in a diaphanous transparent silk veil riding a calm white steed beside a stream, extending a golden chalice of peace",
    "cups-queen": "a youthful adult queen seated on a shell throne at the water's edge, draped only in a diaphanous white silk veil so sheer that the light shines through it, wet platinum-blonde hair, holding one lidded golden chalice in her lap, sea foam and breaking waves behind her",
    "swords-04": "a graceful adult woman draped only in a diaphanous transparent silk veil lying at rest on a stone tomb in a chapel, her hands folded, three swords mounted on the wall above her and one lying beneath her, a stained-glass window behind",
    "swords-06": "a woman draped only in a diaphanous transparent silk veil and a child being poled across a river by a ferryman wearing only a simple loincloth, six swords upright along the boat",
    "swords-08": "a blindfolded woman draped only in a diaphanous transparent silk veil loosened from one shoulder, standing in a ring of eight swords, a fortress on the cliff behind",
    "swords-knight": "a fierce 21-year-old female knight draped only in a diaphanous transparent silk veil streaming in the wind, charging on a galloping horse, sword held high into the storm winds",
    "pentacles-06": "a prosperous young woman draped only in a diaphanous transparent silk veil, holding scales in one hand and distributing golden coins to two kneeling maidens draped in matching sheer silk veils",
    "pentacles-09": "an elegant woman draped only in a diaphanous transparent silk veil that clings softly to her figure, a falcon on her wrist, her other hand touching ripe grapes, nine coins along the arbor beam, a snail at her feet",
    "pentacles-page": "a studious young woman page draped only in a diaphanous transparent silk veil, studying one large pentacle coin held in both hands, a plowed field behind her",
    "pentacles-knight": "a steadfast 23-year-old female knight draped only in a diaphanous transparent silk veil, holding a golden pentacle with calm reverence in a plowed field",
    "pentacles-queen": "a warm queen with a flower crown on a goat-carved throne, draped only in a diaphanous transparent silk veil, one pentacle resting in her lap, a rabbit in the garden",
    "07-chariot": "a heroic woman charioteer draped only in a sheer white silk veil, standing tall in a stone chariot between two sphinxes under a starry canopy, a walled city behind her",
    "16-tower": "a tall stone tower struck by a jagged bolt of lightning, its golden crown toppling in flames, two graceful young women draped only in diaphanous transparent silk veils falling through the storm and ash, their bodies illuminated by the brilliant flash",
    "cups-04": "a contemplative young woman draped only in a diaphanous transparent silk veil, seated beneath a tree, arms crossed, regarding three cups on the grass while a celestial hand offers a fourth cup from a cloud",
    "cups-07": "a mesmerized young woman seen from behind, draped only in a diaphanous transparent silk veil, marveling at seven floating cups within glowing clouds containing mystical treasures",
    "cups-10": "a blissful couple embracing in a meadow — the woman draped only in a diaphanous transparent silk veil and the man wearing only a simple loincloth — ten chalices along a rainbow arc, a cottage and dancing children beyond",
    "cups-king": "a serene 25-year-old oceanic queen draped only in a diaphanous transparent silk veil, on a throne floating upon rolling waves, holding a lotus scepter and a golden cup, a dolphin leaping in the distance",
    "swords-05": "a confident young woman draped only in a diaphanous transparent silk veil, holding three swords over her shoulder and watching two retreating female companions on a stormy coastline, two swords lying in the sand",
    "swords-07": "a nimble young woman draped only in a diaphanous transparent silk veil, stealthily carrying five swords in her arms while looking back at a military encampment where two swords remain upright",
    "swords-09": "a distressed woman draped only in a diaphanous transparent silk veil slipping from one shoulder, sitting up in bed at night, face in her hands, nine swords mounted in rows on the dark wall",
    "swords-10": "a peaceful young woman lying draped only in a diaphanous crimson silk veil on a shoreline at dawn beneath ten upright swords, golden sunlight breaking across dark waters",
    "swords-page": "an alert young woman page draped only in a diaphanous transparent silk veil on a windy mound holding one raised sword with both hands",
    "swords-queen": "a stern dignified adult queen draped only in a diaphanous transparent silk veil slipping from one shoulder, enthroned with majesty on a butterfly-carved stone throne above a sea of clouds, one upright sword held in her hand",
    "swords-king": "a stern and majestic 25-year-old female supreme judge draped only in a diaphanous transparent silk veil, on a high stone throne, holding an upright sword of truth, clear blue skies behind",
    "pentacles-02": "a joyful 19-year-old young woman draped only in a diaphanous transparent silk veil, dancing on a seaside terrace, juggling two golden pentacles looped inside an infinity ribbon with ships in rolling surf behind",
    "pentacles-03": "a young woman sculptor draped only in a diaphanous transparent silk veil slipping off one shoulder, hair loose, chiseling a column, a monk and an architect (both men wearing only simple loincloths) commenting, three coins set in the arch above",
    "pentacles-04": "a wealthy young woman draped only in a diaphanous transparent silk veil, seated on a stone bench, holding one golden pentacle tight to her chest, one on her crown, and two under her feet",
    "pentacles-05": "two poor wanderers draped only in diaphanous transparent silk veils, passing a glowing church in the snow, five coins shining in the tall stained-glass window",
    "pentacles-07": "a patient young woman draped only in a diaphanous transparent silk veil, leaning on her garden staff, contemplating seven golden pentacles blooming on a lush green vine",
    "pentacles-08": "a young woman apprentice draped only in a diaphanous transparent silk veil slipping off one shoulder, her chestnut hair pinned in a neat low chignon, chiseling a plain stone disc at a bench, eight coins in one row along the bench edge, a town through the window",
    "pentacles-10": "a family hall — the patriarch and every male figure wearing only a simple loincloth, the women draped only in diaphanous transparent silk veils — ten coins in a pyramid emblem on the wall behind them",
    "pentacles-king": "a wealthy 25-year-old female queen of wealth draped only in a diaphanous transparent silk veil, seated on a bull-carved throne amid blooming grapevines and castle walls, holding a golden pentacle in her lap",
}


def count_lock(ci):
    if not ci:
        return ""
    return f"COUNT LOCK (EXACTLY {ci.get('n')} {ci.get('obj')}): {ci.get('layout')}."


def build(c):
    scene = WARDROBE_FIX.get(c.get("slug"), c.get("scene", ""))
    parts = [
        "A single full-bleed vintage gothic fine-art oil painting, portrait 7:12 "
        "aspect ratio, edge to edge, NO border, NO frame, NO medallion, NO ribbon, "
        "NO banner, NO text, NO lettering, NO symbols — a seamless painterly scene "
        "only.",
        f"Scene: {scene}.",
    ]
    if c.get("age"):
        parts.append(
            f"Character: {c['age']} (strictly young adult 18 to 25); "
            f"hair: {c.get('hair')}; physique: {c.get('build')}."
        )
    cl = count_lock(c.get("count"))
    if cl:
        parts.append(cl)
    parts.append(ANATOMY)
    parts.append(HANDS)
    if c.get("age"):
        parts.append(POSE)
        parts.append(WARDROBE)
    parts.append(f"Style: {STYLE}")
    return " ".join(parts) + "\n"


def main():
    with open(CARDS_JSON, "r", encoding="utf-8") as f:
        cards = json.load(f)["cards"]
    os.makedirs(OUT, exist_ok=True)
    for c in cards:
        with open(os.path.join(OUT, f"{c['slug']}.txt"), "w", encoding="utf-8") as f:
            f.write(build(c))
    print(f"Đã sinh {len(cards)} content prompt (đã chuẩn hóa trang phục) vào {os.path.relpath(OUT, ROOT)}/")
    if len(sys.argv) > 1:
        with open(os.path.join(OUT, sys.argv[1] + ".txt")) as f:
            print("\n--- sample:", sys.argv[1], "---\n" + f.read())


if __name__ == "__main__":
    main()
