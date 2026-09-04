#!/usr/bin/env python3
"""
LEGACY — bố cục cũ 848×1264 (panel.json, parchment window).

Chuẩn hiện tại là The Star full-bleed 784×1360: dùng `scripts/finish_card.py`
(dán mực viền The Star lên cảnh, không dán nội dung vào card-blank).

Usage:
    python3 scripts/compose_card.py raw/
    python3 scripts/compose_card.py --check
"""

import json
import os
import sys
import subprocess
import glob

PANEL_JSON = "tarot prompt/panel.json"
TEMPLATE_FRAME = "cards/card-blank.png"
OUT_DIR = "cards"

def load_panel_config():
    with open(PANEL_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def compose_card(raw_path, out_path, config):
    panel = config["panel"]      # [x, y, w, h]
    emblem = config.get("emblem")  # [x, y, w, h] or null when the deck has no top emblem/icon
    title = config.get("title")    # [x, y, w, h] or null when title is not composited separately
    feather = config.get("feather", 3)
    size = config.get("size", [848, 1264])

    # Ensure source card is normalized to target dimensions
    temp_raw = f"/tmp/norm_{os.path.basename(raw_path)}"
    subprocess.run([
        "convert", raw_path,
        "-resize", f"{size[0]}x{size[1]}!",
        temp_raw
    ], check=True)

    # Crop configured regions from the raw card.
    # `emblem: null` means the updated deck should NOT transplant any top icon/symbol.
    # `title` is still allowed: it is only the plain title lettering directly on the scene,
    # not a ribbon/banner/plaque/frame.
    temp_panel = f"/tmp/panel_{os.path.basename(raw_path)}"
    temp_emblem = f"/tmp/emblem_{os.path.basename(raw_path)}" if emblem else None
    temp_title = f"/tmp/title_{os.path.basename(raw_path)}" if title else None

    subprocess.run(["convert", temp_raw, "-crop", f"{panel[2]}x{panel[3]}+{panel[0]}+{panel[1]}", "+repage", temp_panel], check=True)
    if emblem:
        subprocess.run(["convert", temp_raw, "-crop", f"{emblem[2]}x{emblem[3]}+{emblem[0]}+{emblem[1]}", "+repage", temp_emblem], check=True)
    if title:
        subprocess.run(["convert", temp_raw, "-crop", f"{title[2]}x{title[3]}+{title[0]}+{title[1]}", "+repage", temp_title], check=True)

    # Composite configured regions onto the base template frame.
    cmd = ["convert", TEMPLATE_FRAME,
           temp_panel, "-geometry", f"+{panel[0]}+{panel[1]}", "-composite"]
    if emblem:
        cmd.extend([temp_emblem, "-geometry", f"+{emblem[0]}+{emblem[1]}", "-composite"])
    if title:
        cmd.extend([temp_title, "-geometry", f"+{title[0]}+{title[1]}", "-composite"])
    cmd.extend(["-quality", "92", out_path])
    subprocess.run(cmd, check=True)

    # Cleanup temp files
    for p in [temp_raw, temp_panel, temp_emblem, temp_title]:
        if p and os.path.exists(p):
            os.remove(p)

    print(f"Composed card: {raw_path} -> {out_path}")

def check_rmse():
    print("Checking frame consistency across cards...")
    cards = sorted(glob.glob("cards/*.png"))
    for c in cards:
        if os.path.basename(c) in ["card-blank.png", "card-blank.jpg"]:
            continue
        # Compare left frame border against standard template
        cmd = [
            "compare", "-metric", "RMSE",
            "-crop", "80x1264+0+0",
            c, TEMPLATE_FRAME,
            "null:"
        ]
        res = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
        print(f"Card {os.path.basename(c):<20} Frame RMSE: {res.stderr.strip()}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/compose_card.py [raw/ | <raw_image.png> | --check]")
        sys.exit(1)

    config = load_panel_config()

    if sys.argv[1] == "--check":
        check_rmse()
        return

    target = sys.argv[1]
    if os.path.isdir(target):
        files = sorted(glob.glob(os.path.join(target, "*.png")) + glob.glob(os.path.join(target, "*.jpg")))
        for f in files:
            out_name = os.path.basename(f)
            out_path = os.path.join(OUT_DIR, out_name)
            compose_card(f, out_path, config)
    else:
        out_name = os.path.basename(target)
        out_path = os.path.join(OUT_DIR, out_name)
        compose_card(target, out_path, config)

if __name__ == "__main__":
    main()
