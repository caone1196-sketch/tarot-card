#!/usr/bin/env python3
"""Build the 77-card neutral prompt set requested for the next image batch.

Source: prompts/out2. The Star is intentionally excluded. Ages are normalized to
20–23, and body descriptions use the neutral silhouette/pose/lighting approach
that succeeded for the generated Star image.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "prompts" / "out2"
DST = ROOT / "prompts" / "out4"


def age_20_23(value: int) -> int:
    return max(20, min(23, value))


def rewrite(text: str) -> str:
    # Normalize explicit age mentions and the source character age field.
    text = re.sub(
        r"(Age:\s*)(\d+)(\s*\(strictly young adult, aged 18 to 25\))",
        lambda m: f"{m.group(1)}{age_20_23(int(m.group(2)))} (adult, aged 20 to 23)",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"\b(18|19|20|21|22|23|24|25)-year-old\b",
        lambda m: f"{age_20_23(int(m.group(1)))}-year-old",
        text,
    )

    # Neutralize direct body/sexual vocabulary while retaining scene intent.
    replacements = [
        (r"\bnude\b", "adult classical figure"),
        (r"\bbreasts?\b", "upper torso"),
        (r"\bbare back\b", "back turned toward the viewer"),
        (r"\bbare shoulders\b", "shoulders turned away from the camera"),
        (r"\bbare torso\b", "torso shaped by pose and shadow"),
        (r"\bbare breast\b", "upper torso shaped by pose and shadow"),
        (r"Sensuality: render with heightened yet tasteful fine-art sensuality", "Sensuality: render as refined classical figure-study beauty"),
        (r"Sensual fine-art anatomy", "Classical figure-study silhouette and natural anatomy"),
        (r"\bgenitals\b", "explicit anatomy"),
        (r"sexual acts", "explicit content"),
        (r"\buncovered\b", "visible through classical composition"),
    ]
    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text, flags=re.I)

    text += (
        "\nSTYLE OVERRIDE: refined classical fine-art figure study with an adult 20–23-year-old subject. "
        "Describe the body through natural silhouette, pose, lighting, hair and atmosphere rather than "
        "explicit anatomy. Use one narrow strip of lightweight silk across the lower body only; keep the "
        "upper body elegant through classical composition. Do not add concealment props, extra accessories, "
        "or objects not already in the scene. No explicit anatomy or explicit content.\n"
    )
    return text


files = sorted(SRC.glob("*.txt"))
files = [p for p in files if p.name != "17-the-star.txt"]
if len(files) != 77:
    raise SystemExit(f"expected 77 non-Star source prompts, found {len(files)}")
DST.mkdir(parents=True, exist_ok=True)
for src in files:
    (DST / src.name).write_text(rewrite(src.read_text(encoding="utf-8")), encoding="utf-8")
(DST / "README.md").write_text(
    "# prompts/out4\n\n"
    "77 rewritten prompts derived from `prompts/out2`, excluding `17-the-star`. "
    "The successful neutral Star method is applied: body described through silhouette, pose, lighting "
    "and atmosphere; one narrow silk strip across the lower body; no explicit body vocabulary; ages "
    "normalized to 20–23. Original prompts are unchanged.\n",
    encoding="utf-8",
)
print(f"wrote {len(files)} prompts to {DST.relative_to(ROOT)}/")
