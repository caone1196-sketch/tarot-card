"""Read-only checks for the all-card waist-ribbon render edition."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import unittest
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("render_builder", ROOT / "scripts/build_cardstarot_prompts_vi.py")
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class CardstarotPromptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files, cls.manifest = builder.build_plan(ROOT)
        cls.cards = json.loads((ROOT / "tarot prompt/cards.json").read_text())["cards"]
        cls.by_slug = {c["slug"]: c for c in cls.cards}

    def test_full_deck_and_groups(self):
        self.assertEqual({p[:-4] for p in self.files if p.endswith(".txt")}, set(self.by_slug))
        self.assertEqual(self.manifest["card_count"], 78)
        self.assertEqual(self.manifest["group_counts"], {"major": 22, "wands": 14, "cups": 14, "swords": 14, "pentacles": 14})
        self.assertEqual(self.manifest["profile_counts"], {"adult_waist_ribbon": 69, "symbol_only": 6, "family_covered": 3})

    def test_family_profiles_do_not_inherit_adult_costume(self):
        family = {e["slug"] for e in self.manifest["cards"] if e["profile"] == "family_covered"}
        self.assertEqual(family, {"cups-10", "swords-06", "pentacles-10"})
        for entry in self.manifest["cards"]:
            if entry["slug"] not in family:
                continue
            text = self.files[entry["prompt"]].decode()
            self.assertIn("toàn bộ người lớn và trẻ em đều mặc", text)
            self.assertIsNone(entry["image_reference"])
            for word in ["khỏa thân", "khoả thân", "95%", "chiffon", "Vẻ gợi cảm", "lót màu da"]:
                self.assertNotIn(word, text)

    def test_symbol_cards_have_no_invented_people_or_human_body_lock(self):
        for entry in self.manifest["cards"]:
            if entry["profile"] != "symbol_only":
                continue
            text = self.files[entry["prompt"]].decode()
            self.assertIn("không có nhân vật toàn thân cần đổi trang phục", text)
            self.assertNotIn("NHÂN VẬT CHÍNH:", text)
            self.assertNotIn("mỗi người có một đầu, hai tay", text)
            self.assertNotIn("95%", text)
            self.assertIsNone(entry["image_reference"])

    def test_count_locks_are_verbatim(self):
        total = 0
        for entry in self.manifest["cards"]:
            source = (ROOT / entry["source_prompt"]).read_text()
            parsed = builder.extract_translation(source)
            rendered = self.files[entry["prompt"]].decode()
            if parsed["count_lock"]:
                total += 1
                self.assertEqual(rendered.count(parsed["count_lock"]), 1, entry["slug"])
                self.assertEqual(builder.digest(parsed["count_lock"].encode()), entry["count_lock_sha256"])
                self.assertEqual(entry["count_n"], self.by_slug[entry["slug"]]["count"]["n"])
                self.assertEqual(int(re.search(r"CHÍNH XÁC\s+(\d+)", parsed["count_lock"]).group(1)), entry["count_n"])
            else:
                self.assertNotIn("KHÓA SỐ LƯỢNG", rendered)
        self.assertEqual(total, 62)

    def test_original_scene_digits_and_hair_preserved(self):
        for entry in self.manifest["cards"]:
            source = builder.extract_translation((ROOT / entry["source_prompt"]).read_text())
            clean = builder.neutral_scene(source["scene"])
            self.assertEqual(re.findall(r"\d+", clean), re.findall(r"\d+", source["scene"]))
            rendered = self.files[entry["prompt"]].decode()
            self.assertIn("CẢNH: " + clean, rendered)
            if source["hair"]:
                self.assertIn(source["hair"], rendered)
            if source["environment"]:
                self.assertIn(source["environment"], rendered)

    def test_adult_profile_requires_confirmed_adult_age(self):
        card = copy.deepcopy(self.by_slug["01-magician"])
        card["age"] = "17 years old"
        with self.assertRaises(ValueError):
            builder.profile_for(card)
        card["age"] = None
        with self.assertRaises(ValueError):
            builder.profile_for(card)

    def test_child_scene_overrides_adult_main_character_age(self):
        card = copy.deepcopy(self.by_slug["01-magician"])
        card["scene"] += ", a child walking beside her"
        self.assertEqual(builder.profile_for(card), "family_covered")

    def test_no_stale_exposure_directives(self):
        for entry in self.manifest["cards"]:
            text = self.files[entry["prompt"]].decode()
            for token in ["khỏa thân", "khoả thân", "để lộ một bên ngực", "Vẻ gợi cảm"]:
                self.assertNotIn(token, text, entry["slug"])
            self.assertIn("PNG dọc 784 × 1360", text)
            self.assertIn("Không khung", text)

    def test_combined_document_and_encoding(self):
        combined = self.files["TAT-CA-78-PROMPT.md"].decode()
        blocks = re.findall(r"```text\n(.*?)```", combined, flags=re.S)
        self.assertEqual(blocks, [self.files[e["prompt"]].decode() for e in self.manifest["cards"]])
        second_build, _ = builder.build_plan(ROOT)
        for name, data in self.files.items():
            text = data.decode("utf-8")
            self.assertEqual(text, unicodedata.normalize("NFC", text), name)
            self.assertEqual(second_build[name], data)

    def test_manifest_hashes_and_source_integrity(self):
        self.assertEqual(self.manifest["source_json_sha256"], builder.digest((ROOT / "tarot prompt/cards.json").read_bytes()))
        for entry in self.manifest["cards"]:
            self.assertEqual(entry["prompt_sha256"], builder.digest(self.files[entry["prompt"]]))
            self.assertEqual(entry["source_sha256"], builder.digest((ROOT / entry["source_prompt"]).read_bytes()))
        self.assertFalse(self.manifest["image_api_called_by_builder"])
        self.assertEqual(self.manifest["image_batch_size"], 3)


if __name__ == "__main__":
    unittest.main()
