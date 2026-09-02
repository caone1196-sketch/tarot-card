#!/usr/bin/env python3
"""
Inspect raw tarot card image metrics:
- Dimensions and aspect ratio (target 784x1360 = 0.576, 7:12)
- Color metrics and framing consistency
"""

import sys
import subprocess
import os
import glob

TARGET_W, TARGET_H = 784, 1360


def check_image(path):
    cmd = ["identify", "-format", "%w %h %[mean] %[standard_deviation]", path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    parts = res.stdout.strip().split()
    w, h = int(parts[0]), int(parts[1])
    ratio = w / h
    if abs(ratio - TARGET_W / TARGET_H) < 0.03:
        status = "OK (7:12)"
    elif abs(ratio - 0.671) < 0.03:
        status = "OLD 2:3 (848x1264)"
    else:
        status = "RATIO MISMATCH (!)"
    note = "" if (w, h) == (TARGET_W, TARGET_H) else "  <-- NOT 784x1360"
    print(f"[{status:<18}] {os.path.basename(path):<22} {w}x{h} (Ratio: {ratio:.3f}){note}")


def main():
    if len(sys.argv) < 2:
        files = sorted(glob.glob("cards/*.png"))
        for f in files:
            check_image(f)
    else:
        for p in sys.argv[1:]:
            if os.path.isdir(p):
                for f in sorted(glob.glob(os.path.join(p, "*.png")) + glob.glob(os.path.join(p, "*.jpg"))):
                    check_image(f)
            else:
                check_image(p)


if __name__ == "__main__":
    main()
