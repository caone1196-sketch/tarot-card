#!/usr/bin/env python3
"""
Regenerate tarot prompt/01-CARD-TABLE.md with full character specifications.
"""

import json

with open("tarot prompt/cards.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cards = data["cards"]

lines = [
    "# Bảng 78 Lá — Đặc Điểm Nhân Vật (Độ Tuổi 18–25, Mái Tóc, Thân Hình) & Bố Cục Chuẩn",
    "",
    "Tất cả các lá bài được chuẩn hóa theo khung **The Star** (full-bleed, thin-line-art, không medallion/ruy băng).",
    "Nhân vật trên mỗi lá bài đều có nhận diện độc bản với độ tuổi cố định trong khoảng **18 đến 25 tuổi**.",
    "",
    "## 1. MAJOR ARCANA — 22 Lá Ẩn Chính",
    "",
    "| # | Slug | Độ tuổi | Mái tóc (Kiểu dáng & Màu sắc) | Thân hình / Vóc dáng | Huy hiệu (Top) | Tên lá (Bottom) |",
    "|---|---|---|---|---|---|---|"
]

for c in cards:
    if c.get("group") == "major":
        num = c.get("n", "")
        slug = c.get("slug", "")
        age = c.get("age", "—")
        hair = c.get("hair", "—")
        build = c.get("build", "—")
        emblem = c.get("emblem") or "—"
        title = c.get("title", "")
        lines.append(f"| {num} | `{slug}` | **{age}** | {hair} | {build} | {emblem} | **{title}** |")

lines.extend([
    "",
    "## 2. MINOR ARCANA — 56 Lá Ẩn Phụ",
    "",
    "| Nhóm | Slug | Độ tuổi | Mái tóc (Kiểu dáng & Màu sắc) | Thân hình / Vóc dáng | Huy hiệu (Top) | Tên lá (Bottom) |",
    "|---|---|---|---|---|---|---|"
])

for c in cards:
    if c.get("group") != "major":
        group = c.get("group", "").capitalize()
        slug = c.get("slug", "")
        age = c.get("age", "—")
        hair = c.get("hair", "—")
        build = c.get("build", "—")
        emblem = c.get("emblem") or "—"
        title = c.get("title", "")
        lines.append(f"| {group} | `{slug}` | **{age}** | {hair} | {build} | {emblem} | **{title}** |")

with open("tarot prompt/01-CARD-TABLE.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("Successfully regenerated tarot prompt/01-CARD-TABLE.md with complete character specifications!")
