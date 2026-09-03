#!/usr/bin/env python3
"""
Scan cards/ directory and build an interactive gallery viewer (index.html) and deck.json.
"""

import json
import os
import glob

CARDS_DIR = "cards"
CARDS_JSON = "tarot prompt/cards.json"
OUT_HTML = "cards/index.html"
OUT_JSON = "cards/deck.json"

def build_gallery():
    with open(CARDS_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    cards_map = {c["slug"]: c for c in data["cards"]}
    image_files = sorted(glob.glob(os.path.join(CARDS_DIR, "*.png")))

    deck_entries = []
    for img_path in image_files:
        base = os.path.basename(img_path)
        slug = os.path.splitext(base)[0]
        if slug in ("card-blank", "card-back"):
            continue

        card_info = cards_map.get(slug, {
            "title": slug.replace("-", " ").title(),
            "emblem": "N/A",
            "age": "18-25",
            "scene": ""
        })

        deck_entries.append({
            "slug": slug,
            "title": card_info.get("title", ""),
            "image": base,
            "emblem": card_info.get("emblem") or "",
            "age": card_info.get("age", ""),
            "hair": card_info.get("hair", ""),
            "build": card_info.get("build", ""),
            "scene": card_info.get("scene", "")
        })

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump({"total": len(deck_entries), "cards": deck_entries}, f, indent=2, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Sensual Gothic Tarot Gallery (78 Cards)</title>
    <style>
        body {{
            background-color: #12100e;
            color: #e6d7b8;
            font-family: 'Cinzel', 'Georgia', serif;
            margin: 0;
            padding: 24px;
        }}
        h1 {{
            text-align: center;
            color: #d4af37;
            letter-spacing: 2px;
            margin-bottom: 8px;
        }}
        .subtitle {{
            text-align: center;
            color: #a39274;
            margin-bottom: 32px;
            font-size: 1.1rem;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 28px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .card-item {{
            background: #1e1b18;
            border: 1px solid #4a3f2c;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 8px 24px rgba(0,0,0,0.6);
            transition: transform 0.25s ease, border-color 0.25s ease;
        }}
        .card-item:hover {{
            transform: translateY(-6px);
            border-color: #d4af37;
        }}
        .card-item img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        .card-details {{
            padding: 16px;
        }}
        .card-title {{
            font-size: 1.25rem;
            color: #d4af37;
            font-weight: bold;
            margin-bottom: 6px;
            text-transform: uppercase;
        }}
        .card-meta {{
            font-size: 0.9rem;
            color: #a8987e;
            margin-bottom: 8px;
        }}
        .card-scene {{
            font-size: 0.85rem;
            color: #c2b293;
            line-height: 1.4;
        }}
    </style>
</head>
<body>
    <h1>SENSUAL GOTHIC TAROT 78 LÁ</h1>
    <div class="subtitle">Bố cục 4 Lớp Chiều Sâu &bull; Khóa Bố Cục The Magician &bull; 100% Nữ Giới (18–25 Tuổi)</div>
    <div class="grid">
"""

    for item in deck_entries:
        html += f"""        <div class="card-item">
            <img src="{item['image']}" alt="{item['title']}">
            <div class="card-details">
                <div class="card-title">{item['title']}</div>
                <div class="card-meta"><strong>Độ tuổi:</strong> {item['age']}</div>
                <div class="card-scene">{item['scene']}</div>
            </div>
        </div>\n"""

    html += """    </div>
</body>
</html>"""

    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated gallery with {len(deck_entries)} cards in {OUT_HTML} and {OUT_JSON}")

if __name__ == "__main__":
    build_gallery()
