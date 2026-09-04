#!/usr/bin/env python3
"""Create a provider-safe variant of prompts/out2 without changing out2."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "prompts" / "out2"
DST = ROOT / "prompts" / "out2_safe"

REPLACEMENTS = [
    ("nude 19-year-old", "tastefully draped 19-year-old"),
    ("nude 20-year-old", "tastefully draped 20-year-old"),
    ("nude 21-year-old", "tastefully draped 21-year-old"),
    ("nude 22-year-old", "tastefully draped 22-year-old"),
    ("nude 23-year-old", "tastefully draped 23-year-old"),
    ("nude 24-year-old", "tastefully draped 24-year-old"),
    ("nude 25-year-old", "tastefully draped 25-year-old"),
    ("nude young", "tastefully draped young"),
    ("nude adult", "tastefully draped adult"),
    ("nude woman", "tastefully draped woman"),
    ("nude women", "tastefully draped women"),
    ("nude priestess", "tastefully draped priestess"),
    ("nude empress", "tastefully draped empress"),
    ("nude hermit", "tastefully draped hermit"),
    ("nude winged", "tastefully draped winged"),
    ("nude figure", "tastefully draped figure"),
    ("one breast bared", "tastefully draped upper body"),
    ("bare back", "draped back"),
    ("bare shoulders", "draped shoulders"),
    ("bare torso", "draped torso"),
    ("bare breast", "draped upper body"),
    ("Sensuality: render with heightened yet tasteful fine-art sensuality", "Sensuality: render with refined, non-explicit fine-art beauty"),
]

for src in sorted(SRC.glob("*.txt")):
    text = src.read_text(encoding="utf-8")
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    # Explicitly reinforce the provider-safe interpretation while retaining all locks.
    text += "\nSAFETY OVERRIDE: non-explicit fine-art depiction; all figures are fully tastefully draped; no exposed breasts, genitals, or sexual acts.\n"
    DST.mkdir(parents=True, exist_ok=True)
    (DST / src.name).write_text(text, encoding="utf-8")
(DST / "README.md").write_text(
    "# prompts/out2_safe\n\n"
    "Provider-safe derivatives of `prompts/out2`. Scene, count, anatomy, and output locks are retained; "
    "explicit nudity is converted to tasteful drapery so image generation can proceed. `prompts/out2` is unchanged.\n",
    encoding="utf-8",
)
print(f"wrote {len(list(SRC.glob('*.txt')))} safe prompts to {DST.relative_to(ROOT)}/")
