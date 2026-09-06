#!/usr/bin/env python3
"""Build the wardrobe-only Vietnamese render edition without modifying sources.

Inputs: tarot prompt/cards.json (card authority) and the static out6_vi translation.
Outputs: prompts/cardstarot_vi only. No image APIs, source synchronization or gallery
regeneration are performed by this script. --check is read-only.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
SOURCE_JSON = ROOT / "tarot prompt/cards.json"
SOURCE_VI = ROOT / "prompts/out6_vi"
DESTINATION = ROOT / "prompts/cardstarot_vi"
STYLE_ID = "waist-ribbon-v1"
STYLE_DATE = "2026-09-06"
REFERENCE = "cardstarot/variants/00-fool-waist-ribbon.png"
SYMBOL_ONLY = {
    "wands-ace", "wands-08", "cups-ace", "swords-ace", "swords-03", "pentacles-ace"
}
CHILD_WORDS = re.compile(r"\b(?:child(?:ren)?|baby|babies|infant|boy|girl|toddler|youngster)\b", re.I)
PROFILE_LABELS = {
    "adult_waist_ribbon": "Người trưởng thành — dải lụa eo/hông",
    "family_covered": "Có trẻ em — mọi nhân vật mặc kín",
    "symbol_only": "Biểu tượng/bàn tay — không thêm nhân vật",
}
STYLE = (
    "PHONG CÁCH: tranh Tarot cổ điển tả thực pha fantasy, chất liệu tinh xảo, "
    "chiều sâu khí quyển, màu ngà và các điểm nhấn vàng ấm trên nền có sắc độ sâu. "
    "Giữ thời điểm, thời tiết, không gian và cảm xúc của cảnh riêng; không tự đổi "
    "cảnh đêm, giông bão hoặc biển thành bình minh hay rừng."
)
ADULT_WARDROBE = (
    "TRANG PHỤC — CHỈ NHÂN VẬT TRƯỞNG THÀNH: một dải lụa chiffon ngà mỏng "
    "quấn ngang eo và hông, chiều rộng vừa đủ che kín mông và hạ thân, mép ở phần "
    "trên đùi, chỉ có một đầu ngắn rủ nhẹ. Không kéo lên thành áo, bodysuit, váy "
    "dài hoặc tà lớn; không quấn dày toàn thân. Lớp chiffon ngoài rất nhẹ theo "
    "quy ước thị giác 95%, nhưng các đoạn cần che có lớp lót màu da be ấm hoàn "
    "toàn kín, phẳng mịn, nhận ra là vải; không nhìn xuyên qua lớp lót và không "
    "mô phỏng chi tiết nhạy cảm trên đó. Tỷ lệ này là hướng dẫn thẩm mỹ, không "
    "phải độ xuyên sáng đo được của vật liệu hoặc của toàn bộ trang phục. "
    "Dải lụa giữ ổn định khi nhân vật chuyển động. Giữ các phụ kiện nhận diện "
    "thuộc cảnh gốc như vòng hoa, voan trên đầu, vương miện hoặc trang bị của "
    "ngựa; không tự thêm áo/váy mới cho nhân vật."
)
ADULT_CAMERA = (
    "GÓC NHÌN KÍN ĐÁO: ưu tiên góc nhìn từ sau vai hoặc 3/4 từ phía sau; chọn "
    "vị trí máy để không hiển thị chi tiết nhạy cảm ở mặt trước thân trên. Tóc, "
    "góc nhìn và phần khuất tự nhiên của tư thế gốc giữ độ che phủ, không thay "
    "bằng tư thế phô bày hoặc thêm đạo cụ để che. Không góc thấp, không cận cảnh "
    "cơ thể. Giữ tư thế và hành động đúng cảnh riêng, không thay vai trò nhân "
    "vật và không ép tất cả thành cùng một dáng đứng. Mặt nghiêng và bàn tay "
    "vẫn đọc được khi cần, mọi đồ vật có khóa số "
    "lượng phải tách biệt và nhìn thấy đủ."
)
FAMILY_WARDROBE = (
    "TRANG PHỤC GIA ĐÌNH: toàn bộ người lớn và trẻ em đều mặc trang phục thông "
    "thường bằng vải đục, che đầy đủ thân trên và thân dưới, phù hợp từng độ "
    "tuổi. Giữ bối cảnh gia đình hoặc chuyến đi tự nhiên, không nhấn hình thể. "
    "Trẻ em vẫn là trẻ em đúng cảnh, không đổi thành người lớn; thông số tuổi "
    "của nhân vật người lớn chính không được gán cho trẻ. Không dùng kiểu "
    "trang phục hoặc ảnh tham chiếu eo/hông của nhóm người lớn cho lá này."
)
FAMILY_CAMERA = (
    "BỐ CỤC GIA ĐÌNH: góc nhìn trung tính đủ rộng để đọc được quan hệ giữa các "
    "nhân vật, hành động và các đồ vật. Giữ mọi nhân vật mặc kín và đặt trọng "
    "tâm vào ý nghĩa gia đình/chuyến đi, không vào cơ thể."
)
SYMBOL_WARDROBE = (
    "PHẠM VI BIỂU TƯỢNG: cảnh này không có nhân vật toàn thân cần đổi trang "
    "phục. Không thêm phụ nữ, người toàn thân, quần áo hoặc dải vải. Nếu cảnh "
    "chỉ có một bàn tay thần thánh thì chỉ giữ đúng bàn tay đó; nếu cảnh chỉ "
    "có gậy, cốc, kiếm, đồng tiền hoặc trái tim thì chỉ dựng đúng các yếu tố "
    "đã mô tả. Giữ hình thức biểu tượng mỹ thuật, không thêm chi tiết máu me."
)
ANATOMY = (
    "GIẢI PHẪU: số nhân vật giữ đúng cảnh; mỗi người có một đầu, hai tay và "
    "hai chân, các khớp nối tự nhiên, bàn tay đúng cấu trúc. Tư thế được diễn "
    "đạt bằng phối cảnh, không cắt ghép thêm chi. Động vật giữ hình thể tự nhiên."
)
SYMBOL_ANATOMY = (
    "CẤU TRÚC BIỂU TƯỢNG: các vật thể tách biệt, không nhân đôi hoặc hòa lẫn. "
    "Bàn tay xuất hiện trong cảnh phải có cấu trúc tự nhiên; không tự thêm "
    "cánh tay hoặc cơ thể ngoài mô tả."
)
OUTPUT = (
    "ĐẦU RA: một tranh duy nhất, PNG dọc 784 × 1360, tỷ lệ 49:85, phủ kín bốn "
    "mép, không kéo giãn hình thể. Không khung, lề trắng, bảng tên, tiêu đề, "
    "số thứ tự lá, watermark hoặc chữ trang trí ngoài cảnh. Chỉ giữ những "
    "biểu tượng/chữ khắc là đạo cụ có trong cảnh gốc; không bổ sung huy hiệu "
    "hoặc vật trang trí của lá tham chiếu. Không hình ghép hay nhiều phiên bản "
    "trong cùng ảnh."
)
CAMERA_HINTS = {
    "00-fool": "GIỮ RIÊNG: một bông hồng trắng trên tay, mắt nhìn hoa, một chó trắng nhỏ ở gót chân; thấy mép vách đá, không biến hoa thành gậy phép.",
    "01-magician": "GIỮ RIÊNG: máy sau chếch trái, nhìn qua phía ngoài vai để thấy mặt bàn ở bên cạnh thân người. Một tay giơ gậy riêng lên trời, tay kia chỉ xuống đất. Trên bàn vẫn đúng bốn vật: cốc, kiếm, gậy nằm trên bàn, đồng tiền. Gậy trong tay không thay gậy trên bàn. Giữ đủ đầu gậy và các đồ vật, không biểu tượng tự thêm phía trên đầu.",
    "02-priestess": "GIỮ RIÊNG: nàng vẫn ngồi; máy sau chếch phải, hơi cao nhìn chéo vào lòng để thấy cuộn thư và hai bàn tay. Giữ hai cột đá và trăng bạc ở chân. Voan chỉ phủ đầu và tóc phía sau, không biến thành áo choàng dài. Không vòm trang trí bao khung ảnh.",
    "03-empress": "GIỮ RIÊNG: nàng vẫn ngồi trên ngai nhung, vòng hoa trên tóc vàng, khiên trái tim cạnh ngai, lúa mì và trái cây. Chọn góc sau chếch hoặc qua cạnh ngoài ngai để thấy vai/lưng, phần lụa ở hông và các đạo cụ; không chỉ xoay gương mặt trên một thân người còn chính diện. Không vương miện ngôi sao, không thêm quyền trượng và không giữ tà váy dài của phiên bản trước.",
    "12-hanged": "GIỮ RIÊNG: nhân vật vẫn treo ngược bằng một cổ chân, chân kia gập như nguồn; giữ độ che phủ ổn định theo trọng lực, không lật thành tư thế đứng.",
    "15-devil": "GIỮ RIÊNG: các sợi xích là biểu tượng của cảnh Tarot; thể hiện cảnh giả tưởng mang tính biểu tượng, không biến thành tình huống tình dục hoặc hành hạ cơ thể.",
    "swords-03": "GIỮ RIÊNG: trái tim và ba thanh kiếm là biểu tượng hội họa; không thêm người, không mô tả chấn thương y khoa hoặc máu me.",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def profile_for(card: dict) -> str:
    if CHILD_WORDS.search(card.get("scene", "")):
        return "family_covered"
    if card["slug"] in SYMBOL_ONLY:
        if card.get("age"):
            raise ValueError(f"Review symbol-only classification: {card['slug']}")
        return "symbol_only"
    age = re.search(r"\d+", card.get("age") or "")
    if age is None or int(age.group()) < 18:
        raise ValueError(f"Explicit adult age required before wardrobe styling: {card['slug']}")
    return "adult_waist_ribbon"


def extract_translation(text: str) -> dict:
    blocks = text.split("\n\n")
    scenes = [b for b in blocks if b.startswith("CẢNH:")]
    if len(scenes) != 1:
        raise ValueError("Expected exactly one translated scene")
    spec = re.search(
        r"THÔNG SỐ NHÂN VẬT.*?Tuổi: (.*?); Tóc: (.*?); Vóc dáng: (.*?); Vẻ gợi cảm:",
        text, re.S,
    )
    count = re.search(r"(KHÓA SỐ LƯỢNG.*?)(?= KHÓA GIẢI PHẪU|\n\n|$)", text, re.S)
    return {
        "scene": scenes[0][len("CẢNH: "):].strip(),
        "environment": next((b for b in blocks if b.startswith("MÔI TRƯỜNG VÀ BỐI CẢNH:")), None),
        "age": spec.group(1) if spec else None,
        "hair": spec.group(2) if spec else None,
        "build": spec.group(3) if spec else None,
        "count_lock": count.group(1).strip() if count else None,
    }


def neutral_scene(scene: str) -> str:
    """Remove obsolete exposure/fetish wording, not actors/actions/props/counts."""
    replacements = [
        (" khỏa thân", ""), (" khoả thân", ""),
        (", để lộ một bên ngực,", ","),
        ("đường cong một bên ngực nàng", "đường nét vai và tóc nàng"),
        ("thân trên để trần", "thân trên"),
        ("lưng trần", "lưng"), ("vai trần", "vai"),
        ("để lộ vai và lưng", "vai và lưng"),
        ("quyến rũ, ", ""), ("gợi cảm nhưng vẫn ", ""),
        ("xoay ba phần tư cơ thể về phía người xem", "xoay ba phần tư cơ thể"),
        ("xoay ba phần tư về phía người xem", "xoay ba phần tư"),
    ]
    for old, new in replacements:
        scene = scene.replace(old, new)
    scene = re.sub(r" +", " ", scene)
    scene = scene.replace(", ,", ",").strip()
    if re.search(r"khỏa thân|khoả thân|để lộ một bên ngực|gợi cảm|quyến rũ", scene):
        raise ValueError(f"Unreviewed source wording remains: {scene}")
    return scene


def make_prompt(card: dict, vi: dict, profile: str) -> str:
    title = f"LÁ {card['title']} — BẢN RENDER {STYLE_ID} (KHÔNG VẼ DÒNG NÀY VÀO ẢNH)."
    parts = [title, STYLE]
    if profile == "adult_waist_ribbon":
        parts.append(
            f"THAM CHIẾU: {REFERENCE} chỉ dùng cho chất tranh, dải lụa eo/hông và "
            "cách quan sát kín đáo. Không sao chép gương mặt, màu tóc, tư thế, hoa, "
            "chó, vách đá hoặc đồ vật của The Fool sang lá khác."
        )
    else:
        parts.append(
            "THAM CHIẾU: dùng mô tả màu sắc/chất tranh, không đính kèm ảnh nhân vật "
            "quấn lụa eo/hông của nhóm người lớn. Không sao chép cảnh hoặc nhân vật "
            "từ lá khác."
        )
    parts.append("CẢNH: " + neutral_scene(vi["scene"]))
    if profile != "symbol_only":
        age = int(re.search(r"\d+", card["age"]).group())
        if not vi["hair"] or int(re.search(r"\d+", vi["age"] or "").group()) != age:
            raise ValueError(f"Translation/age mismatch: {card['slug']}")
        if profile == "family_covered":
            parts.append(
                f"NHÂN VẬT NGƯỜI LỚN CHÍNH: {age} tuổi. Tóc: {vi['hair']}. "
                "Tuổi này không áp dụng cho trẻ em trong cảnh. Giữ số người, "
                "quan hệ gia đình và hành động ở phần cảnh."
            )
        else:
            parts.append(
                f"NHÂN VẬT CHÍNH: người trưởng thành {age} tuổi. Tóc: {vi['hair']}. "
                f"Vóc dáng: {vi['build']}. Giữ thông số nhân vật riêng; các nhân vật "
                "phụ mang hình người trong nhóm này cũng phải rõ ràng là người "
                "trưởng thành. Không dùng tỷ lệ trẻ em hoặc phong cách búp bê."
            )
    parts.append({
        "adult_waist_ribbon": ADULT_WARDROBE,
        "family_covered": FAMILY_WARDROBE,
        "symbol_only": SYMBOL_WARDROBE,
    }[profile])
    if profile != "symbol_only":
        parts.append(ADULT_CAMERA if profile == "adult_waist_ribbon" else FAMILY_CAMERA)
    if card["slug"] in CAMERA_HINTS:
        parts.append(CAMERA_HINTS[card["slug"]])
    if vi["count_lock"]:
        parts.append(vi["count_lock"])
    if vi["environment"]:
        parts.append(vi["environment"])
    parts.append(SYMBOL_ANATOMY if profile == "symbol_only" else ANATOMY)
    parts.append(OUTPUT)
    result = unicodedata.normalize("NFC", "\n\n".join(parts) + "\n")
    if profile == "family_covered":
        for banned in ["95%", "chiffon", "khỏa thân", "khoả thân", "Vẻ gợi cảm", "lót màu da"]:
            if banned in result:
                raise ValueError(f"Unsafe family-profile inheritance: {card['slug']}: {banned}")
    return result


def build_plan(root: Path = ROOT) -> tuple[dict[str, bytes], dict]:
    source_json = root / "tarot prompt/cards.json"
    cards = json.loads(source_json.read_text(encoding="utf-8"))["cards"]
    if len(cards) != 78 or len({c["slug"] for c in cards}) != 78:
        raise ValueError("Expected the complete canonical 78-card deck")
    files: dict[str, bytes] = {}
    entries = []
    for card in cards:
        source_path = root / "prompts/out6_vi" / f"{card['slug']}.txt"
        raw = source_path.read_bytes()
        vi = extract_translation(raw.decode("utf-8"))
        if bool(card.get("count")) != bool(vi["count_lock"]):
            raise ValueError(f"Canonical/translated count-lock mismatch: {card['slug']}")
        if vi["count_lock"]:
            count_number = re.search(r"CHÍNH XÁC\s+(\d+)", vi["count_lock"])
            if count_number is None or int(count_number.group(1)) != card["count"]["n"]:
                raise ValueError(f"Canonical/translated object count differs: {card['slug']}")
        profile = profile_for(card)
        name = f"{card['slug']}.txt"
        prompt = make_prompt(card, vi, profile)
        files[name] = prompt.encode("utf-8")
        entries.append({
            "slug": card["slug"], "title": card["title"], "group": card["group"],
            "profile": profile, "prompt": name, "prompt_sha256": digest(files[name]),
            "source_prompt": f"prompts/out6_vi/{name}", "source_sha256": digest(raw),
            "count_n": card["count"]["n"] if card.get("count") else None,
            "count_lock_sha256": digest(vi["count_lock"].encode()) if vi["count_lock"] else None,
            "image_reference": REFERENCE if profile == "adult_waist_ribbon" else None,
            "image_generation_status": "not_generated_by_this_script",
        })
    counts = dict(Counter(e["profile"] for e in entries))
    manifest = {
        "schema_version": 1, "style_id": STYLE_ID, "style_approved_on": STYLE_DATE,
        "card_count": 78, "profile_counts": counts,
        "group_counts": dict(Counter(c["group"] for c in cards)),
        "target_image_size": [784, 1360], "source_json": "tarot prompt/cards.json",
        "source_json_sha256": digest(source_json.read_bytes()),
        "source_translation_edition": "prompts/out6_vi",
        "image_api_called_by_builder": False,
        "image_batch_size": 3,
        "reference": REFERENCE,
        "reference_sha256": digest((root / REFERENCE).read_bytes()),
        "cards": entries,
    }
    files["manifest.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    style_doc = (
        f"# Quy chuẩn render {STYLE_ID}\n\nNgày xác nhận: 06/09/2026. "
        "Tài liệu dẫn xuất từ các hằng số trong `scripts/build_cardstarot_prompts_vi.py`; "
        "không phải nguồn dữ liệu nhân vật.\n\n"
        + STYLE + "\n\n## Nhóm người trưởng thành\n\n" + ADULT_WARDROBE
        + "\n\n" + ADULT_CAMERA
        + "\n\n## Những lá có trẻ em\n\n" + FAMILY_WARDROBE + "\n\n" + FAMILY_CAMERA
        + "\n\n## Những lá chỉ có biểu tượng/bàn tay\n\n" + SYMBOL_WARDROBE
        + "\n\n## Đầu ra\n\n" + OUTPUT
        + "\n\nCác khóa số lượng và nội dung riêng được ghép vào từng prompt, không lấy từ ảnh mẫu. "
        "Bộ dựng chỉ tạo văn bản; việc tạo/kiểm tra ảnh thực hiện riêng, tối đa 3 lá mỗi đợt.\n"
    )
    files["STYLE.md"] = style_doc.encode("utf-8")
    table = "\n".join(
        f"| {i + 1} | [{e['title']}]({e['prompt']}) | {e['group']} | {PROFILE_LABELS[e['profile']]} |"
        for i, e in enumerate(entries)
    )
    readme = f"""# 78 prompt tiếng Việt — dải lụa eo/hông

Quy chuẩn **{STYLE_ID}**, xác nhận ngày **06/09/2026**. Đây là bộ **render riêng**, không thay thế `cards.json`, `prompts/out6_vi` hoặc các ảnh gốc.

## Phạm vi

- **{counts['adult_waist_ribbon']} lá người trưởng thành:** dải lụa ngà chỉ quấn eo/hông, có lớp lót màu da kín; phần trước thân trên không phô bày nhờ góc nhìn/tóc/tư thế tự nhiên.
- **3 lá có trẻ em:** `cups-10`, `swords-06`, `pentacles-10`. Tất cả người lớn và trẻ em mặc kín, bối cảnh trung tính; không kế thừa mô tả trang phục mỏng. Không dùng ảnh tham chiếu người quấn lụa cho nhóm này.
- **6 lá không có nhân vật toàn thân:** Ace of Wands, Eight of Wands, Ace of Cups, Ace of Swords, Three of Swords, Ace of Pentacles. Không thêm người hoặc dải vải; giữ bàn tay/đạo cụ/biểu tượng theo cảnh.
- Đủ **22 lá Ẩn Chính + 56 lá Ẩn Phụ**. Chuẩn bị 78 prompt không đồng nghĩa đã tạo 78 ảnh; ảnh được thực hiện từng đợt **3 lá**, không có tác vụ tạo ảnh tự chạy ngầm.

## Bảo toàn nội dung

- Slug, tiêu đề, nhóm, tuổi và trường dữ liệu thẻ lấy từ `tarot prompt/cards.json`; cảnh, tóc, vóc dáng và khóa số lượng dùng bản dịch tĩnh `prompts/out6_vi` tương ứng.
- Các câu buộc phô bày cơ thể trong mô tả cũ được trung tính hóa ở **file render này**, để không mâu thuẫn trang phục/góc nhìn mới. Không ghi ngược thay đổi về nguồn.
- **62 khóa số lượng được giữ nguyên văn**, không tự tạo khóa cho 16 lá thiếu trường `count`. Giữ các hành động và đồ vật riêng, không ép mọi người đứng giống The Fool.
- Trên các lá có trẻ em, bỏ mô tả hình thể/gợi cảm của người lớn; chỉ giữ thông tin cần thiết và dùng trang phục gia đình kín đáo. Không thay tuổi trẻ em bằng tuổi nhân vật chính.
- “95%” ở nhóm người trưởng thành là **quy ước thị giác**, không phải phép đo độ xuyên sáng; lớp lót và các vùng cần che vẫn kín.
- Kích thước đích: **PNG 784 × 1360**, tranh phủ kín ảnh. Không khung hoặc tên lá; những biểu tượng thuộc cảnh gốc vẫn giữ, không bổ sung huy hiệu trang trí.
- Bản dịch là dữ liệu tĩnh. Nếu `cards.json` thay đổi, cần rà soát bản dịch tương ứng trước khi dựng lại bộ render; không có đồng bộ/biên dịch dịch thuật tự động.

## Tạo lại và kiểm tra

```bash
python3 scripts/build_cardstarot_prompts_vi.py
python3 scripts/build_cardstarot_prompts_vi.py --check
python3 -m unittest discover -s tests -p 'test_cardstarot_prompts_vi.py' -v
```

Script chỉ ghi `prompts/cardstarot_vi/`, không gọi API tạo ảnh, không sửa nguồn hoặc gallery. `--check` chỉ đọc và so sánh. Thông tin trạng thái ảnh thật nằm ở [`cardstarot/README.md`](../../cardstarot/README.md), không suy ra từ sự tồn tại của file prompt.

- [Toàn bộ 78 prompt](TAT-CA-78-PROMPT.md)
- [Quy chuẩn trang phục, góc nhìn và ngoại lệ](STYLE.md)
- [Manifest, hash nguồn và profile từng lá](manifest.json)
- [Ảnh mẫu dải lụa](../../{REFERENCE}) — chỉ dành cho nhóm người trưởng thành

## Danh sách

| STT | Lá / prompt | Nhóm | Profile |
|---|---|---|---|
{table}
"""
    files["README.md"] = readme.encode("utf-8")
    combined = ["# Toàn bộ 78 prompt — dải lụa eo/hông\n", "Xem README để biết ngoại lệ gia đình/biểu tượng và quy tắc nguồn. Đây là prompt, không phải báo cáo đã tạo đủ ảnh.\n"]
    for entry in entries:
        combined.append(
            f"## {entry['title']} — {entry['slug']}\n\n"
            f"Profile: {PROFILE_LABELS[entry['profile']]}\n\n"
            f"```text\n{files[entry['prompt']].decode('utf-8')}```\n"
        )
    files["TAT-CA-78-PROMPT.md"] = "\n".join(combined).encode("utf-8")
    return files, manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare generated outputs without writing")
    args = parser.parse_args()
    files, manifest = build_plan()
    if args.check:
        mismatches = [name for name, data in files.items() if not (DESTINATION / name).is_file() or (DESTINATION / name).read_bytes() != data]
        existing = {p.name for p in DESTINATION.glob("*.txt")}
        expected = {n for n in files if n.endswith(".txt")}
        if mismatches or existing != expected:
            raise SystemExit(f"Generated files need review/rebuild: {mismatches}; unexpected/missing prompts: {sorted(existing ^ expected)}")
        print("PASS: 78 prompts, docs and manifest match the read-only source plan.")
    else:
        DESTINATION.mkdir(parents=True, exist_ok=True)
        extras = {p.name for p in DESTINATION.glob("*.txt")} - {n for n in files if n.endswith(".txt")}
        if extras:
            raise SystemExit(f"Refusing to remove unexpected files: {sorted(extras)}")
        for name, data in files.items():
            (DESTINATION / name).write_bytes(data)
        print(f"Wrote {manifest['card_count']} prompts and {len(files)-manifest['card_count']} documentation/manifest files.")
    print(json.dumps(manifest["profile_counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
