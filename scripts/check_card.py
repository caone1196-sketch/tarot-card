#!/usr/bin/env python3
"""
Inspect raw tarot card image metrics:
- Dimensions and aspect ratio (target 848x1264 = 0.671)
- Color metrics and framing consistency
"""

import sys
import subprocess
import os
import glob

def check_image(path):
    cmd = ["identify", "-format", "%w %h %[mean] %[standard_deviation]", path]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, check=True)
    parts = res.stdout.strip().split()
    w, h = int(parts[0]), int(parts[1])
    ratio = w / h
    status = "OK (7:12)" if abs(ratio - 0.583) < 0.03 else ("OK (2:3)" if abs(ratio - 0.671) < 0.03 else "RATIO MISMATCH (!)")
    print(f"[{status:<18}] {os.path.basename(path):<22} {w}x{h} (Ratio: {ratio:.3f})")

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
