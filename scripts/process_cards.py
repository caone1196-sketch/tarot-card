#!/usr/bin/env python3
"""
Process raw tarot card images:
- Auto-trim outer margins with threshold
- Resize and normalize to 848x1264 (7:12 / 2:3 aspect ratio)
- Compress to JPEG / PNG under target file size
"""

import os
import sys
import subprocess
import glob

TARGET_W = 848
TARGET_H = 1264
MAX_KB = 800

def process_image(img_path, out_path=None, trim=True, trim_thr="18%"):
    if out_path is None:
        out_path = img_path

    cmd = ["convert", img_path]
    if trim:
        cmd.extend(["-fuzz", trim_thr, "-trim"])
    cmd.extend([
        "-resize", f"{TARGET_W}x{TARGET_H}!",
        "-quality", "92",
        out_path
    ])
    subprocess.run(cmd, check=True)
    print(f"Processed: {img_path} -> {out_path} ({TARGET_W}x{TARGET_H})")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/process_cards.py <file_or_dir> [--trim] [--trim-thr <fuzz>]")
        sys.exit(1)

    target = sys.argv[1]
    trim = "--trim" in sys.argv
    trim_thr = "18%"
    if "--trim-thr" in sys.argv:
        idx = sys.argv.index("--trim-thr")
        if idx + 1 < len(sys.argv):
            trim_thr = sys.argv[idx + 1]

    if os.path.isdir(target):
        files = glob.glob(os.path.join(target, "*.png")) + glob.glob(os.path.join(target, "*.jpg"))
        for f in files:
            process_image(f, trim=trim, trim_thr=trim_thr)
    else:
        process_image(target, trim=trim, trim_thr=trim_thr)

if __name__ == "__main__":
    main()
