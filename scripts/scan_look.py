#!/usr/bin/env python3
"""Scan the look kit while excluding redraw working/output files.

The scanner deliberately walks only ``look/`` and ignores directories named
``out`` anywhere below it. Other directories inside ``look/redraw/`` are
included. It is intended for inspection and never modifies the source files.

Usage:
    python3 scripts/scan_look.py
    python3 scripts/scan_look.py --json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOOK_DIR = ROOT / "look"
EXCLUDED_DIRS = {"out"}


def scan_look() -> list[dict[str, object]]:
    """Return metadata for files in look/, excluding redraw and out folders."""
    results: list[dict[str, object]] = []
    for path in sorted(LOOK_DIR.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(LOOK_DIR)
        # Exclude by path component, not by a substring, so look/prompts/outside
        # remains valid. Other folders under look/redraw remain included.
        if EXCLUDED_DIRS.intersection(relative.parts):
            continue
        results.append(
            {
                "path": relative.as_posix(),
                "type": path.suffix.lower().lstrip(".") or "file",
                "bytes": path.stat().st_size,
            }
        )
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print JSON instead of a summary")
    args = parser.parse_args()
    files = scan_look()
    if args.json:
        print(json.dumps({"root": "look", "excluded": sorted(EXCLUDED_DIRS), "files": files}, ensure_ascii=False, indent=2))
        return
    print(f"look/: {len(files)} files")
    for item in files:
        print(f"{item['path']}\t{item['type']}\t{item['bytes']} bytes")


if __name__ == "__main__":
    main()
