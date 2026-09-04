#!/usr/bin/env python3
"""Rewrite prompts/out into frame-free prompts/out2 prompts.

The original prompt files remain untouched. This derived set keeps each original
scene, character, count, and anatomy specification while removing instructions for
borders, titles, emblems, and other card-frame decoration.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "prompts" / "out"
DST = ROOT / "prompts" / "out2"

TITLE_RE = re.compile(r'A single tarot card "([^"]+)"')
SCENE_RE = re.compile(r"The scene occupies the whole card edge to edge,.*?: (.*?) CHARACTER SPECIFICATION ", re.S)


def rewrite(text: str) -> str:
    title_m = TITLE_RE.search(text)
    scene_m = SCENE_RE.search(text)
    if not title_m or not scene_m:
        raise ValueError("prompt does not match expected generated format")
    title = title_m.group(1)
    scene = scene_m.group(1).strip()
    rest = text[scene_m.end() - len("CHARACTER SPECIFICATION "):]
    # Keep all character/count/anatomy rules, but discard the old frame-specific tail.
    rest = rest.split("Depth layering:", 1)[0].strip()
    rest = rest.replace("none cropped by the frame", "none cropped by the canvas")
    rest = rest.replace("inside the frame", "inside the artwork")
    result = (
        f'Create the artwork for "{title}" using the original scene specification. '
        "This is an artwork-only illustration, not a finished tarot card. "
        "The scene must fill the entire canvas edge to edge with no reserved header or footer.\n\n"
        f"SCENE: {scene}\n\n"
        f"{rest}\n\n"
        "OUTPUT LOCK: exact portrait canvas 784 by 1360 pixels, 7:12 composition. "
        "Pure edge-to-edge painted artwork only. No outer margin, no border, no frame, "
        "no gold line, no corner flourishes, no inner panel, no medallion, no emblem, "
        "no icon, no heraldic symbol, no card suit symbol, no ribbon, no plaque, "
        "no title, no letters, no numbers, no watermark, and no typography anywhere. "
        "Do not render the card name or any text in the image."
    )
    return result + "\n"


def main() -> None:
    files = sorted(SRC.glob("*.txt"))
    if len(files) != 78:
        raise SystemExit(f"expected 78 source prompts, found {len(files)}")
    DST.mkdir(parents=True, exist_ok=True)
    for src in files:
        (DST / src.name).write_text(rewrite(src.read_text(encoding="utf-8")), encoding="utf-8")
    (DST / "README.md").write_text(
        "# prompts/out2\n\n"
        "78 prompts rewritten from `prompts/out/` for artwork-only generation.\n\n"
        "The scene, character, count, and anatomy specifications are retained from the original prompts. "
        "Frame, border, title, emblem, symbol, and typography instructions are replaced by an explicit "
        "784×1360 frame-free output lock.\n",
        encoding="utf-8",
    )
    print(f"wrote {len(files)} prompts to {DST.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
