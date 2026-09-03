#!/usr/bin/env python3
"""
Regenerate tarot prompt/01-CARD-TABLE.md — BẢNG TRA NHANH (không còn là chuẩn).

Từ 2026-09-03:
  • Chuẩn thông số nhân vật = `tarot prompt/02-CHARACTER-SPECS.md` (72 nhân vật,
    có thêm mắt · màu da · nét riêng · không khí · thang vóc A–D).
  • `01-CARD-TABLE.md` chỉ còn là **bảng tra 78 lá** do script này sinh ra:
    cột nhân vật lấy từ 02 (qua scripts/card_specs.py), cột bố cục/huy hiệu/tên
    lấy NGUYÊN VĂN từ `cards.json`. Không sửa tay file này — sửa nguồn rồi chạy lại.

Chạy: python3 scripts/generate_card_table.py
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import card_specs  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tarot prompt", "01-CARD-TABLE.md")

HEAD = """# Bảng 78 Lá — TRA NHANH (sinh tự động, KHÔNG phải chuẩn)

> ⚠️ **File này do `scripts/generate_card_table.py` sinh ra — đừng sửa tay.**
> Chuẩn thông số nhân vật hiện là **`02-CHARACTER-SPECS.md`** (72 nhân vật; 6 lá
> thuần vật thể không có người). Cột Tuổi/Mắt/Tóc/Vóc/Da/Nét/Không khí dưới đây
> được lấy từ 02; cột Huy hiệu/Tên/Bố cục lấy **nguyên văn** từ `cards.json`
> (`cards.json` là nguồn prompt duy nhất và không file nào được quyền sửa nó).

Cấu trúc hình ảnh: 4 lớp chiều sâu + COUNT LOCK theo `cards.json`.
Nhân vật luôn trong khoảng **18–25 tuổi**. Thang vóc: **A** thanh mảnh → **D** đầy đặn vừa.
"""

COLS = ("| # | Slug | Tuổi | Mắt | Tóc | Vóc (02) | Da | Nét riêng | Không khí | Huy hiệu | Tên lá |",
        "|---|---|---|---|---|---|---|---|---|---|---|")


def row(label, c, eff, sp):
    """Một dòng bảng: cột nhân vật từ 02, cột bố cục từ cards.json."""
    def cell(x, dash="—"):
        return (x or "").strip() or dash
    physique = eff.get("build", "")
    if sp and sp.get("grade"):
        if physique.startswith(sp["grade"] + " "):          # "A mảnh, ..." -> cấp A + mô tả
            physique = f"**{sp['grade']}** · " + physique[len(sp["grade"]) + 1:].strip(" ·")
        else:                                                # cards.json thắng (lá nhiều nhân vật)
            physique = f"**{sp['grade']}** · " + physique
    from02 = "" if sp else " *(cards.json)*"
    return (f"| {label} | `{c.get('slug','')}` | {cell(str(eff.get('age') or ''))} | "
            f"{cell(eff.get('eyes'))} | {cell(eff.get('hair'))}{from02} | {cell(physique)} | "
            f"{cell(eff.get('skin'))} | {cell(eff.get('signature'))} | {cell(eff.get('aura'))} | "
            f"{cell(c.get('emblem'))} | **{c.get('title','')}** |")


def main():
    with open(os.path.join(ROOT, "tarot prompt", "cards.json"), "r", encoding="utf-8") as f:
        cards = json.load(f)["cards"]
    specs = card_specs.load_specs()

    lines = [HEAD, "", "## 1. MAJOR ARCANA — 22 Lá Ẩn Chính", "", *COLS]
    for c in cards:
        if c.get("group") != "major":
            continue
        eff, _ = card_specs.merge(c, specs)
        lines.append(row(c.get("n", ""), c, eff, specs.get(c["slug"])))

    lines += ["", "## 2. MINOR ARCANA — 56 Lá Ẩn Phụ", "", *COLS]
    for c in cards:
        if c.get("group") == "major":
            continue
        eff, _ = card_specs.merge(c, specs)
        lines.append(row(c.get("group", "").capitalize(), c, eff, specs.get(c["slug"])))

    covered = sum(1 for c in cards if c["slug"] in specs)
    lines += ["", "---", "",
              f"*{covered}/{len(cards)} lá lấy thông số nhân vật từ `02-CHARACTER-SPECS.md`; "
              f"{len(cards) - covered} lá thuần vật thể giữ theo `cards.json`. "
              "Muốn đổi thông số nhân vật → sửa **02** rồi chạy lại script này; "
              "muốn đổi bố cục/cảnh → sửa `cards.json`.*", ""]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Regenerated {os.path.relpath(OUT, ROOT)} — {covered}/{len(cards)} nhân vật từ 02, "
          f"{len(cards)-covered} lá giữ cards.json.")


if __name__ == "__main__":
    main()
