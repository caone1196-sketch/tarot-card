#!/usr/bin/env python3
"""Create the next Star-reference prompt set from prompts/out5."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "prompts" / "out5"
DST = ROOT / "prompts" / "out6"
REFERENCE = (
    "REFERENCE STANDARD: use cards/17-the-star.png as the visual reference for the measured "
    "784×1360 composition, open-window scale, lighting, color atmosphere, depth and thin "
    "antique-gold line-art treatment. Replace the reference scene with this card's scene.\n\n"
)

for src in sorted(SRC.glob("*.txt")):
    text = src.read_text(encoding="utf-8")
    text = re.sub(r"^Create THE FOOL using.*?canvas edge to edge\.\n\n", "", text, flags=re.S) if src.name == "00-fool.txt" else text
    text = REFERENCE + text
    # Consistent neutral generation language for all cards.
    text += (
        "\nSTAR-REFERENCE OUTPUT: match the reference card's elegant atmosphere and measured frame "
        "without copying its objects. Keep the scene readable, realistic and non-explicit; use natural "
        "silhouette, pose, light and environment. Keep the card's original count locks and original scene "
        "objects only. Exact 784 × 1360 portrait PNG.\n"
    )
    (DST / src.name).parent.mkdir(parents=True, exist_ok=True)
    (DST / src.name).write_text(text, encoding="utf-8")
(DST / "README.md").write_text(
    "# prompts/out6\n\n"
    "78 prompts derived from `prompts/out5`, each explicitly using `cards/17-the-star.png` as the "
    "visual reference. Original scene descriptions and count/anatomy locks are retained.\n",
    encoding="utf-8",
)
print(f"wrote {len(list(SRC.glob('*.txt')))} prompts to {DST.relative_to(ROOT)}/")
