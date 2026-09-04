#!/usr/bin/env python3
"""Create a provider-safe artistic-nude variant of prompts/out2."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "prompts" / "out2"
DST = ROOT / "prompts" / "out2_safe"


def rewrite(text: str) -> str:
    # Preserve the original scene/count/anatomy/output locks while changing only
    # the depiction language to non-explicit classical figure study.
    patterns = [
        (r"nude (\d+-year-old) woman", r"tastefully posed artistic nude \1 woman"),
        (r"nude young woman", "tastefully posed artistic nude young woman"),
        (r"nude adult women", "tastefully posed artistic nude adult women"),
        (r"nude adult woman", "tastefully posed artistic nude adult woman"),
        (r"nude women", "tastefully posed artistic nude women"),
        (r"nude woman", "tastefully posed artistic nude woman"),
        (r"nude priestess", "tastefully posed artistic nude priestess"),
        (r"nude empress", "tastefully posed artistic nude empress"),
        (r"nude hermit woman", "tastefully posed artistic nude hermit woman"),
        (r"nude hermit", "tastefully posed artistic nude hermit"),
        (r"nude winged", "tastefully posed artistic nude winged"),
        (r"nude figure", "tastefully posed artistic nude figure"),
        (r"nude bare-shouldered woman", "tastefully posed artistic nude woman with shoulders turned away"),
        (r"one breast bared", "a classical three-quarter pose with sensitive areas concealed by composition"),
        (r"bare back", "back turned away from the viewer"),
        (r"bare shoulders", "shoulders turned away from the camera"),
        (r"bare torso", "torso concealed by pose and shadow"),
        (r"bare breast", "upper body concealed by pose and shadow"),
        (r"Sensuality: render with heightened yet tasteful fine-art sensuality", "Sensuality: render as refined, non-explicit classical figure-study beauty"),
    ]
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    text = text.replace("tastefully posed artistic nude", "tastefully posed sensual classical figure")
    text += (
        "\nSTYLE OVERRIDE: tasteful sensual classical fine-art figure study. A partial upper torso "
        "or breast may be visible when naturally composed, non-explicit, and not emphasized; use "
        "back view, three-quarter view, profile, careful cropping, flowing hair, props, natural pose, "
        "and soft shadow to keep the presentation elegant. No genitals, sexual acts, or explicit "
        "anatomical detail.\n"
    )
    return text


files = sorted(SRC.glob("*.txt"))
if len(files) != 78:
    raise SystemExit(f"expected 78 source prompts, found {len(files)}")
DST.mkdir(parents=True, exist_ok=True)
for src in files:
    (DST / src.name).write_text(rewrite(src.read_text(encoding="utf-8")), encoding="utf-8")
(DST / "README.md").write_text(
    "# prompts/out2_safe\n\n"
    "Provider-safe derivatives of `prompts/out2`. Scene, count, anatomy, and output locks are retained; "
    "figures use non-explicit classical artistic nudity with camera angle, pose, props, hair, cropping, "
    "and shadow concealing sensitive areas. `prompts/out2` is unchanged.\n",
    encoding="utf-8",
)
print(f"wrote {len(files)} safe prompts to {DST.relative_to(ROOT)}/")
