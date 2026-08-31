#!/usr/bin/env python3
"""
Enrich tarot prompt/cards.json with distinct character attributes:
- Age: strictly between 18 and 25 years old
- Hair: distinct style, cut, texture, and color for every character
- Build: distinct silhouette, proportions, and physical stature
"""

import json

CARD_SPECS = {
    # Major Arcana
    "00-fool": {
        "age": "19 years old",
        "hair": "loose wind-tossed honey-blonde waves down to her shoulder blades, sunlit and carefree",
        "build": "petite and lithe, slender waist, youthful energy and light, springy step"
    },
    "01-magician": {
        "age": "22 years old",
        "hair": "jet-black straight hair falling past her waist like a sleek silk curtain, center-parted",
        "build": "statuesque and commanding, elegant elongated proportions with poised posture"
    },
    "02-priestess": {
        "age": "23 years old",
        "hair": "deep auburn hair with soft natural waves, cascading beneath a sheer gossamer veil",
        "build": "serene, slender and graceful, long neck and soft classical feminine curves"
    },
    "03-empress": {
        "age": "24 years old",
        "hair": "thick ripe-wheat golden blonde hair, spilling over both shoulders in soft ropey curls garlanded with flowers",
        "build": "voluptuous and curvaceous, full feminine bust and hips, warm radiant goddess presence"
    },
    "04-emperor": {
        "age": "25 years old",
        "hair": "short textured dark bronze-brown hair with a clean sharp jawline and focused gaze",
        "build": "broad-shouldered, athletic muscular chest, commanding warrior-king physique"
    },
    "05-hierophant": {
        "age": "24 years old",
        "hair": "neatly groomed dark espresso-brown hair with gentle waves at the temples",
        "build": "tall, noble and dignified, poised scholar physique with upright posture"
    },
    "06-lovers": {
        "age": "21 years old",
        "hair": "warm chestnut-brown hair gathered in a loose romantic knot with soft wisps framing her cheeks",
        "build": "slender hourglass silhouette, supple waist, graceful gentle curves beside her partner"
    },
    "07-chariot": {
        "age": "22 years old",
        "hair": "dark sable-brown hair tightly plaited in a single thick warrior braid over one shoulder",
        "build": "athletic and toned, sculpted shoulders and taut waist, resolute and heroic stance"
    },
    "08-strength": {
        "age": "23 years old",
        "hair": "burnished copper-red long wavy hair flowing down like a lion's mane",
        "build": "lithe yet strong, defined muscular tone along the back, soft graceful curves"
    },
    "09-hermit": {
        "age": "23 years old",
        "hair": "ethereal silver-ash long hair, veiled beneath sheer white cowl gauze",
        "build": "slender, mysterious and delicate silhouette, quiet meditative poise"
    },
    "10-wheel": {
        "age": "22 years old",
        "hair": "golden-amber braided hair crowned with mystic celestial laurels",
        "build": "statuesque, poised mythological figure with balanced proportions"
    },
    "11-justice": {
        "age": "24 years old",
        "hair": "sleek raven-black hair drawn back sharply into a high polished half-ponytail",
        "build": "statuesque and regal, prominent collarbones, straight spine and austere balanced posture"
    },
    "12-hanged": {
        "age": "21 years old",
        "hair": "sandy-brown tousled locks hanging down with gravity, catching ambient glow",
        "build": "lean, wiry and flexible dancer physique, calm relaxed musculature"
    },
    "13-death": {
        "age": "22 years old",
        "hair": "pale bone-platinum straight hair flowing behind the visor",
        "build": "tall, lean and solemn warrior silhouette in black ornamental armor"
    },
    "14-temperance": {
        "age": "22 years old",
        "hair": "pale fine ash-blonde hair floating weightlessly in the air",
        "build": "ethereal and willowy, long slender limbs, arched supple spine, graceful angelic poise"
    },
    "15-devil": {
        "age": "21 years old",
        "hair": "midnight-black wavy hair with deep wine-red undertones, wild and untamed",
        "build": "sultry and curvaceous, arched back and soft full hips, magnetic alluring presence"
    },
    "16-tower": {
        "age": "20 years old",
        "hair": "storm-dark chestnut hair blown dynamically backward by lightning winds",
        "build": "taut and athletic, dynamic acrobatic physique arched mid-fall"
    },
    "17-the-star": {
        "age": "20 years old",
        "hair": "very long pale shimmering gold hair, wet and silky, cascading down past one bare shoulder",
        "build": "slender and lithe, narrow waist, long graceful legs, luminous maiden proportions"
    },
    "18-moon": {
        "age": "21 years old",
        "hair": "ink-blue-black hair with cool silvery highlights, cascading like water to her hips",
        "build": "slender, mysterious water-nymph silhouette, delicate waist and soft curving hips"
    },
    "19-sun": {
        "age": "19 years old",
        "hair": "radiant sunflower-blonde hair, bouncing loose curls garlanded in red blossoms",
        "build": "youthful and vibrant, sun-kissed skin, energetic and joyful feminine curves"
    },
    "20-judgement": {
        "age": "22 years old",
        "hair": "rich amber-honey hair in thick luminous waves catching golden rays",
        "build": "statuesque, open-armed posture, noble and reborn classical anatomy"
    },
    "21-world": {
        "age": "22 years old",
        "hair": "dark chocolate-chestnut hair swirling freely with violet silk ribbons",
        "build": "dancer's perfected physique, long toned legs, narrow waist, supple celebratory poise"
    },

    # Wands Suit
    "wands-ace": {"age": None, "hair": None, "build": None},
    "wands-02": {
        "age": "22 years old",
        "hair": "deep auburn hair falling in long loose ringlets over one shoulder",
        "build": "slender and contemplative, upright posture looking out from the parapet"
    },
    "wands-03": {
        "age": "23 years old",
        "hair": "warm caramel-brown hair loosely braided with golden cord",
        "build": "tall and statuesque, long back line facing toward the horizon"
    },
    "wands-04": {
        "age": "20 years old",
        "hair": "blue-black hair piled high in a floral-pinned braided updo",
        "build": "lithe and celebratory, joyful dancer waist and raised graceful arms"
    },
    "wands-05": {
        "age": "21 years old",
        "hair": "short tousled copper-brown hair damp with exertion",
        "build": "athletic, toned agile muscles, dynamic sparring stance"
    },
    "wands-06": {
        "age": "22 years old",
        "hair": "honey-gold hair billowing triumphantly in the wind",
        "build": "commanding and proud, tall equestrian posture on horseback"
    },
    "wands-07": {
        "age": "21 years old",
        "hair": "dark espresso hair cropped close at sides with messy curls on top",
        "build": "lean, wiry and determined, athletic defensive stance"
    },
    "wands-08": {"age": None, "hair": None, "build": None},
    "wands-09": {
        "age": "24 years old",
        "hair": "dark brown hair pulled back with a simple leather tie",
        "build": "broad, muscular and battle-tested, watchful stance"
    },
    "wands-10": {
        "age": "23 years old",
        "hair": "damp chestnut hair clinging to brow from labor",
        "build": "strong athletic back, powerful shoulders bearing the bundle"
    },
    "wands-page": {
        "age": "18 years old",
        "hair": "short tousled ginger-auburn hair cut in a playful textured bob",
        "build": "petite and spirited, lithe youthful frame with eager stance"
    },
    "wands-knight": {
        "age": "22 years old",
        "hair": "wind-whipped golden-brown curls peeking under helm",
        "build": "dashing athletic warrior build, lean muscular core on rearing steed"
    },
    "wands-queen": {
        "age": "24 years old",
        "hair": "a magnificent mane of rich russet-red waves crowning her head",
        "build": "voluptuous, commanding and fiery, proud posture on lion throne"
    },
    "wands-king": {
        "age": "25 years old",
        "hair": "dark bronze hair swept back neatly with a short trimmed beard line",
        "build": "powerful broad-chested monarch physique, authoritative presence"
    },

    # Cups Suit
    "cups-ace": {"age": None, "hair": None, "build": None},
    "cups-02": {
        "age": "21 years old",
        "hair": "soft ash-brown hair worn in a low intertwined romantic braid",
        "build": "slender and graceful, gentle curving silhouette leaning in communion"
    },
    "cups-03": {
        "age": "20 years old",
        "hair": "rich chocolate-brown, golden-blonde, and copper hair among the three maidens",
        "build": "harmonious, curvaceous, dancing together with joyful feminine grace"
    },
    "cups-04": {
        "age": "22 years old",
        "hair": "dark wavy hair falling over eyes in contemplative mood",
        "build": "lean, relaxed seated posture against the tree trunk"
    },
    "cups-05": {
        "age": "22 years old",
        "hair": "long mahogany hair unbound and draping over cloaked shoulders",
        "build": "slender, somber silhouette with delicate bowed neck"
    },
    "cups-06": {
        "age": "19 years old",
        "hair": "pale golden hair styled in a delicate maiden crown knot",
        "build": "petite, innocent and delicate, sweet gentle posture"
    },
    "cups-07": {
        "age": "21 years old",
        "hair": "dark raven curls drifting in visionary haze",
        "build": "slender, mesmerized posture with hands slightly raised"
    },
    "cups-08": {
        "age": "23 years old",
        "hair": "deep brown hair tucked under pilgrim hood",
        "build": "lean traveler physique, resolute back turned toward the mountains"
    },
    "cups-09": {
        "age": "24 years old",
        "hair": "warm honey-brown hair in a relaxed loose chignon",
        "build": "luxurious, soft feminine curves, content and smiling seated posture"
    },
    "cups-10": {
        "age": "22 years old",
        "hair": "warm hazel-brown hair cascading in silky ripples",
        "build": "graceful, tender motherly poise with slender loving frame"
    },
    "cups-page": {
        "age": "18 years old",
        "hair": "dark glossy hair in a single side fishtail braid over the collarbone",
        "build": "petite, curious and dreamy, delicate limbs holding the chalice"
    },
    "cups-knight": {
        "age": "22 years old",
        "hair": "fair sandy-blonde hair falling in soft waves across his forehead",
        "build": "romantic, slender and noble athletic poise offering the cup"
    },
    "cups-queen": {
        "age": "23 years old",
        "hair": "long shimmering platinum-blonde hair falling straight like water to her thighs",
        "build": "slender and ethereal, narrow waist, serene and mystical queenly beauty"
    },
    "cups-king": {
        "age": "25 years old",
        "hair": "deep wave dark brown hair crowned in sea-gold",
        "build": "calm, broad-shouldered, steady noble presence seated on sea throne"
    },

    # Swords Suit
    "swords-ace": {"age": None, "hair": None, "build": None},
    "swords-02": {
        "age": "21 years old",
        "hair": "jet-black hair drawn back into a sleek, flawless high knot",
        "build": "slender, perfectly balanced, taut core and crossed arms holding dual blades"
    },
    "swords-03": {"age": None, "hair": None, "build": None},
    "swords-04": {
        "age": "22 years old",
        "hair": "deep sable hair spread neatly around her resting head on stone",
        "build": "slender, peaceful reclined effigy silhouette in sacred stillness"
    },
    "swords-05": {
        "age": "22 years old",
        "hair": "wind-blown dark brown hair with cynical smirk",
        "build": "lean, agile and sharp-shouldered, turning with collected blades"
    },
    "swords-06": {
        "age": "21 years old",
        "hair": "light ash-brown hair gathered softly in a misty veil",
        "build": "slender, quiet passenger silhouette seated in the ferry boat"
    },
    "swords-07": {
        "age": "20 years old",
        "hair": "mischievous tousled dark chestnut hair",
        "build": "light-footed, slender agile rogue build tiptoeing away"
    },
    "swords-08": {
        "age": "20 years old",
        "hair": "dark brown hair bound loosely with a crimson ribbon",
        "build": "slender, delicate and vulnerable silhouette surrounded by upright blades"
    },
    "swords-09": {
        "age": "22 years old",
        "hair": "long black hair falling in sorrowful waves over her weeping hands",
        "build": "slender, delicate nightgown silhouette seated in emotional release"
    },
    "swords-10": {
        "age": "23 years old",
        "hair": "dark hair strewn across the shoreline sand",
        "build": "lean peaceful fallen figure bathed in morning horizon light"
    },
    "swords-page": {
        "age": "18 years old",
        "hair": "windswept honey-brown hair cut in a sharp feathered pixie cut",
        "build": "lithe, sharp and vigilant, athletic spring in her stance on rocky hill"
    },
    "swords-knight": {
        "age": "21 years old",
        "hair": "dark hair streaming wildly back from beneath open helmet",
        "build": "fierce, muscular athletic charge, leaning into the wind on galloping charger"
    },
    "swords-queen": {
        "age": "24 years old",
        "hair": "deep mahogany-red hair in an intricate woven crown braid",
        "build": "statuesque, sharp profile, austere elegant collarbones, stern intellectual beauty"
    },
    "swords-king": {
        "age": "25 years old",
        "hair": "clean-cut raven hair with sharp aristocratic temples",
        "build": "tall, imposing, sharp-eyed judicial ruler with blade upright"
    },

    # Pentacles Suit
    "pentacles-ace": {"age": None, "hair": None, "build": None},
    "pentacles-02": {
        "age": "19 years old",
        "hair": "tousled sandy-gold curls moving with the juggling dance",
        "build": "agile, lithe and flexible entertainer physique balancing the coins"
    },
    "pentacles-03": {
        "age": "22 years old",
        "hair": "dark auburn hair coiled in a practical braided crown",
        "build": "focused, toned artisan shoulders, sculpted hands crafting the cathedral"
    },
    "pentacles-04": {
        "age": "24 years old",
        "hair": "neatly combed dark brown hair holding gold tight",
        "build": "solid, grounded seated posture guarding his accumulated coins"
    },
    "pentacles-05": {
        "age": "20 years old",
        "hair": "long windswept dark-brown hair catching falling snow",
        "build": "slender, shivering yet enduring silhouette under church window"
    },
    "pentacles-06": {
        "age": "23 years old",
        "hair": "well-groomed golden-brown hair in merchant styling",
        "build": "prosperous, upright dignified posture distributing coins"
    },
    "pentacles-07": {
        "age": "22 years old",
        "hair": "sweat-touched warm chestnut hair resting on hoe handle",
        "build": "lean, hardworking farm-toned musculature, patient contemplative stance"
    },
    "pentacles-08": {
        "age": "21 years old",
        "hair": "chestnut hair bound in a neat, focused low chignon",
        "build": "slender and meticulous, steady hands engraving coins at the workbench"
    },
    "pentacles-09": {
        "age": "23 years old",
        "hair": "long vine-dark espresso hair loosely curled with gold thread",
        "build": "graceful, refined aristocratic hourglass build in blooming grape vineyard"
    },
    "pentacles-10": {
        "age": "22 years old",
        "hair": "warm honey-brown hair in a thick braided crown",
        "build": "content, gentle matriarchal beauty surrounded by familial wealth"
    },
    "pentacles-page": {
        "age": "18 years old",
        "hair": "golden-blonde hair falling loose past shoulders, catching meadow sun",
        "build": "petite, earnest scholar-student frame, holding coin aloft with reverence"
    },
    "pentacles-knight": {
        "age": "23 years old",
        "hair": "dark bronze hair under heavy helm, steadfast gaze",
        "build": "sturdy, broad-shouldered athletic knight on stationary heavy warhorse"
    },
    "pentacles-queen": {
        "age": "24 years old",
        "hair": "deep chocolate hair with a ruddy golden sheen, crowned in blooming vines",
        "build": "voluptuous, maternal, generous warm feminine curves on carved beast throne"
    },
    "pentacles-king": {
        "age": "25 years old",
        "hair": "dark wavy hair woven with golden laurel leaves",
        "build": "robust, wealthy monarch physique seated comfortably amidst vine-covered castle"
    }
}

with open("tarot prompt/cards.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for card in data["cards"]:
    slug = card["slug"]
    if slug in CARD_SPECS:
        spec = CARD_SPECS[slug]
        if spec["age"]:
            card["age"] = spec["age"]
        if spec["hair"]:
            card["hair"] = spec["hair"]
        if spec["build"]:
            card["build"] = spec["build"]

with open("tarot prompt/cards.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully enriched cards.json with unique character attributes (Age 18-25, Hairstyle/Color, Body Build)!")
