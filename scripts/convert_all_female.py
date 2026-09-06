#!/usr/bin/env python3
"""
Convert all characters in tarot deck to all-female cast (Aged 18-25).
"""

import json

ALL_FEMALE_UPDATES = {
    "04-emperor": {
        "femme": True,
        "age": "25 years old",
        "hair": "sleek dark bronze-brown hair in a sharp warrior braid, crowned with a golden ram-horn circlet",
        "build": "powerful, broad-shouldered, athletic and commanding female sovereign with sculpted physique",
        "scene": "a commanding 25-year-old bare-shouldered female emperor in an ornate golden cuirass and crimson velvet mantle, seated resolutely on a stone throne carved with ram heads, holding an ankh scepter in one hand, barren rugged mountains behind her"
    },
    "05-hierophant": {
        "femme": True,
        "age": "24 years old",
        "hair": "thick espresso-brown waves falling over embroidered ceremonial vestments",
        "build": "tall, noble and serene female high priestess with graceful dignified poise",
        "scene": "a serene 24-year-old female high mystic priestess in rich red-and-gold ceremonial robes, raising one blessing hand, two kneeling female acolytes before her, sacred temple pillars behind"
    },
    "10-wheel": {
        "femme": True,
        "age": "22 years old",
        "hair": "golden-amber braided hair crowned with mystic celestial laurels",
        "build": "statuesque winged female guardian with poised mythological silhouette",
        "scene": "a great spinning wheel of fortune inscribed with mystic letters, a winged female sphinx holding an upright sword atop it, a rising golden serpent on one side and a jackal deity on the other, four winged female watchers at the corners"
    },
    "12-hanged": {
        "femme": True,
        "age": "21 years old",
        "hair": "golden-brown tousled locks cascading downward with gravity, glowing in ethereal light",
        "build": "lean, lithe and supple young woman dancer physique, serene and peaceful poise",
        "scene": "a serene nude 21-year-old young woman suspended upside-down by one ankle from a living tree shaped like a cross, one leg bent gracefully, a radiant halo of golden light glowing around her head"
    },
    "13-death": {
        "femme": True,
        "age": "22 years old",
        "hair": "long bone-platinum hair flowing behind an ornate gothic helm",
        "build": "tall, slender and formidable female dark knight silhouette in polished black armor",
        "scene": "a striking 22-year-old pale female knight in ornate black armor riding a calm pale charger, holding a black banner adorned with a five-petaled white rose, a golden sunrise glowing between twin distant towers"
    },
    "15-devil": {
        "femme": True,
        "age": "21 years old",
        "hair": "midnight-black wavy hair with deep wine-red undertones, wild and untamed",
        "build": "sultry and curvaceous, arched back and soft full hips, magnetic alluring presence",
        "scene": "a horned winged female arch-devil upon a dark pedestal; beside her two alluring nude young women arched in golden chains, their bodies glowing in candlelit shadow inside an obsidian cavern"
    },
    "16-tower": {
        "femme": True,
        "age": "20 years old",
        "hair": "storm-dark chestnut hair blown dynamically backward by lightning winds",
        "build": "taut and athletic, dynamic acrobatic physique arched mid-fall",
        "scene": "a tall stone tower struck by a jagged bolt of lightning, its golden crown toppling in flames, two graceful young women falling through the storm and ash, their bodies illuminated by the brilliant flash"
    },
    "20-judgement": {
        "femme": True,
        "age": "22 years old",
        "hair": "rich amber-honey hair in thick luminous waves catching golden rays",
        "build": "statuesque, open-armed posture, noble and reborn classical anatomy",
        "scene": "a radiant winged female angel blowing a golden trumpet with a white banner; below, rising from calm waters, three beautiful nude young women with open arms turning toward the divine light"
    },
    "wands-05": {
        "femme": True,
        "age": "21 years old",
        "hair": "short tousled copper-brown hair damp with exertion",
        "build": "athletic, toned agile muscles, dynamic sparring stance",
        "scene": "five athletic young women in light linen wraps engaged in dynamic friendly sparring with five living wands"
    },
    "wands-07": {
        "femme": True,
        "age": "21 years old",
        "hair": "dark espresso hair cropped close at sides with messy curls on top",
        "build": "lean, wiry and determined, athletic defensive stance",
        "scene": "a determined young woman standing atop a high crag, holding one great wand with both hands to defend her position against six wands rising from below"
    },
    "wands-09": {
        "femme": True,
        "age": "24 years old",
        "hair": "dark brown hair pulled back with a simple leather tie",
        "build": "broad, toned and battle-ready, watchful stance",
        "scene": "a vigilant young woman warrior resting hands on one standing wand, eight wands upright behind her like a palisade"
    },
    "wands-10": {
        "femme": True,
        "age": "23 years old",
        "hair": "damp chestnut hair clinging to brow from labor",
        "build": "strong athletic back, powerful shoulders bearing the bundle",
        "scene": "a strong young woman carrying a heavy bundle of ten wands toward a distant sunlit castle"
    },
    "wands-knight": {
        "femme": True,
        "age": "22 years old",
        "hair": "wind-whipped golden-brown curls peeking beneath a feathered diadem",
        "build": "dashing athletic female knight, lean muscular core on a rearing golden steed",
        "scene": "a daring 22-year-old bare-shouldered female knight in golden armor on a rearing horse, raising one flourishing living wand high"
    },
    "wands-king": {
        "femme": True,
        "age": "25 years old",
        "hair": "dark bronze hair swept back in an ornate crown braid with fiery orange ribbons",
        "build": "commanding, statuesque high queen with broad noble shoulders and authoritative presence",
        "scene": "a powerful 25-year-old female sovereign with a lion-carved crown seated on a flame-carved throne, holding one blossoming wand"
    },
    "cups-04": {
        "femme": True,
        "age": "22 years old",
        "hair": "dark wavy hair falling over her shoulder in contemplative thought",
        "build": "slender, relaxed seated posture against a flowering tree",
        "scene": "a contemplative young woman seated beneath a tree, arms crossed, regarding three cups on the grass while a celestial hand offers a fourth cup from a cloud"
    },
    "cups-07": {
        "femme": True,
        "age": "21 years old",
        "hair": "dark raven curls drifting in mystical haze",
        "build": "slender, mesmerized posture with hands slightly raised",
        "scene": "a mesmerized young woman seen from behind, marveling at seven floating cups within glowing clouds containing mystical treasures"
    },
    "cups-08": {
        "femme": True,
        "age": "23 years old",
        "hair": "deep brown hair tucked under a travel cloak",
        "build": "lean wanderer silhouette, resolute back turned toward mountains",
        "scene": "a solitary young woman in a deep crimson cloak walking away with a staff, leaving eight stacked cups behind to journey toward misty moonlit peaks"
    },
    "cups-knight": {
        "femme": True,
        "age": "22 years old",
        "hair": "fair sandy-blonde hair falling in soft romantic waves across her brow",
        "build": "poetic, slender and noble athletic female knight offering the chalice",
        "scene": "a graceful 22-year-old female knight in winged silver armor riding a calm white steed beside a stream, extending a golden chalice of peace"
    },
    "cups-king": {
        "femme": True,
        "age": "25 years old",
        "hair": "deep-wave dark espresso hair crowned in sea-gold and pearls",
        "build": "calm, statuesque oceanic sovereign with serene noble presence",
        "scene": "a serene 25-year-old oceanic queen on a throne floating upon rolling waves, holding a lotus scepter and a golden cup, a dolphin leaping in the distance"
    },
    "swords-05": {
        "femme": True,
        "age": "22 years old",
        "hair": "wind-blown dark brown hair with a subtle confident smirk",
        "build": "lean, agile and sharp-shouldered, turning with collected blades",
        "scene": "a confident young woman holding three swords over her shoulder and watching two retreating female companions on a stormy coastline, two swords lying in the sand"
    },
    "swords-07": {
        "femme": True,
        "age": "20 years old",
        "hair": "mischievous tousled dark chestnut hair",
        "build": "light-footed, slender agile rogue build tiptoeing away",
        "scene": "a nimble young woman stealthily carrying five swords in her arms while looking back at a military encampment where two swords remain upright"
    },
    "swords-10": {
        "femme": True,
        "age": "23 years old",
        "hair": "dark silky hair strewn across shoreline sand",
        "build": "lean peaceful reclining maiden silhouette bathed in golden morning horizon light",
        "scene": "a peaceful young woman lying draped in crimson silk on a shoreline at dawn beneath ten upright swords, golden sunlight breaking across dark waters"
    },
    "swords-knight": {
        "femme": True,
        "age": "21 years old",
        "hair": "dark hair streaming wildly back from beneath an open winged helmet",
        "build": "fierce, athletic female knight in full gallant charge",
        "scene": "a fierce 21-year-old female knight in gleaming steel armor charging on a galloping horse, sword held high into the storm winds"
    },
    "swords-king": {
        "femme": True,
        "age": "25 years old",
        "hair": "clean-cut raven hair crowned with sharp golden circlet",
        "build": "tall, imposing, sharp-eyed judicial female ruler with blade upright",
        "scene": "a stern and majestic 25-year-old female supreme judge on a high stone throne, holding an upright sword of truth, clear blue skies behind"
    },
    "pentacles-02": {
        "femme": True,
        "age": "19 years old",
        "hair": "tousled sandy-gold curls bouncing with her dance",
        "build": "agile, lithe and flexible young dancer balancing two coins in an infinity ribbon",
        "scene": "a joyful 19-year-old young woman dancing on a seaside terrace, juggling two golden pentacles looped inside an infinity ribbon with ships in rolling surf behind"
    },
    "pentacles-04": {
        "femme": True,
        "age": "24 years old",
        "hair": "neatly combed dark brown hair holding gold close",
        "build": "solid, grounded seated posture guarding her wealth",
        "scene": "a wealthy young woman seated on a stone bench, holding one golden pentacle tight to her chest, one on her crown, and two under her feet"
    },
    "pentacles-06": {
        "femme": True,
        "age": "23 years old",
        "hair": "well-groomed golden-brown hair in merchant styling",
        "build": "prosperous, upright dignified posture distributing coins",
        "scene": "a prosperous young woman in rich robes holding scales in one hand, distributing golden coins to two kneeling maidens"
    },
    "pentacles-07": {
        "femme": True,
        "age": "22 years old",
        "hair": "sweat-touched warm chestnut hair resting on hoe handle",
        "build": "lean, hardworking farm-toned musculature, patient contemplative stance",
        "scene": "a patient young woman leaning on her garden staff, contemplating seven golden pentacles blooming on a lush green vine"
    },
    "pentacles-knight": {
        "femme": True,
        "age": "23 years old",
        "hair": "dark bronze hair braided under an oak-leaf crested helmet",
        "build": "sturdy, athletic female knight on a calm heavy warhorse",
        "scene": "a steadfast 23-year-old female knight in dark armor holding a golden pentacle with calm reverence in a plowed field"
    },
    "pentacles-king": {
        "femme": True,
        "age": "25 years old",
        "hair": "dark wavy hair woven with golden laurel leaves and ripe grapes",
        "build": "robust, wealthy sovereign seated comfortably in lush castle gardens",
        "scene": "a wealthy 25-year-old female queen of wealth seated on a bull-carved throne amid blooming grapevines and castle walls, holding a golden pentacle in her lap"
    }
}

with open("tarot prompt/cards.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for card in data["cards"]:
    slug = card["slug"]
    if slug in ALL_FEMALE_UPDATES:
        up = ALL_FEMALE_UPDATES[slug]
        for k, v in up.items():
            card[k] = v
    else:
        # If card has characters, ensure femme is True
        if card.get("age"):
            card["femme"] = True

with open("tarot prompt/cards.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully converted all characters across all 78 tarot cards to 100% all-female cast (Aged 18-25)!")
