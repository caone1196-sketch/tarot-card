"""Validate the real collection index separately from the 78 text-only plans."""
import hashlib
import json
from pathlib import Path
import re
import struct
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
COLLECTION = ROOT / "cardstarot"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CardstarotCollectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.collection = json.loads((COLLECTION / "manifest.json").read_text())
        cls.plans = json.loads((ROOT / "prompts/cardstarot_vi/manifest.json").read_text())
        cls.by_slug = {c["slug"]: c for c in cls.plans["cards"]}

    def test_complete_plan_and_honest_image_progress(self):
        cards = self.collection["cards"]
        self.assertEqual(len(cards), 78)
        self.assertEqual({c["slug"] for c in cards}, set(self.by_slug))
        available = [c for c in cards if c.get("image")]
        pending = [c for c in cards if not c.get("image")]
        self.assertEqual(self.collection["images_available"], len(available))
        self.assertEqual(self.collection["images_pending"], len(pending))
        self.assertEqual(self.collection["images_matching_requested_style"], sum(c.get("style_status") == "applied" for c in cards))
        self.assertEqual({p.name for p in COLLECTION.glob("*.png")}, {c["image"] for c in available})
        self.assertFalse(self.collection["generation_in_progress"])
        for c in pending:
            self.assertEqual(c["style_status"], "not_started")
            self.assertFalse((COLLECTION / f"{c['slug']}.png").exists())

    def test_image_files_prompts_and_origins(self):
        for c in self.collection["cards"]:
            plan = self.by_slug[c["slug"]]
            self.assertEqual(c["wardrobe_profile"], plan["profile"])
            requested = COLLECTION / c["requested_render_prompt"]
            self.assertTrue(requested.is_file())
            self.assertEqual(sha(requested), c["requested_render_prompt_sha256"])
            self.assertEqual(sha(requested), plan["prompt_sha256"])
            if not c.get("image"):
                continue
            image = COLLECTION / c["image"]
            data = image.read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
            self.assertEqual(struct.unpack(">II", data[16:24]), (784, 1360))
            self.assertEqual((data[24], data[25]), (8, 2))
            pos = 8
            while pos < len(data):
                size = struct.unpack(">I", data[pos:pos + 4])[0]
                chunk = data[pos + 4:pos + 8 + size]
                crc = struct.unpack(">I", data[pos + 8 + size:pos + 12 + size])[0]
                self.assertEqual(zlib.crc32(chunk) & 0xffffffff, crc)
                kind = data[pos + 4:pos + 8]
                pos += size + 12
                if kind == b"IEND":
                    break
            self.assertEqual(pos, len(data))
            self.assertEqual(sha(image), c["image_sha256"])
            self.assertEqual(sha(COLLECTION / c["render_prompt"]), c["render_prompt_sha256"])
            mirror = COLLECTION / f"{c['slug']}.next.txt"
            if mirror.exists():
                self.assertEqual(mirror.read_bytes(), requested.read_bytes())
            if c.get("image_origin"):
                origin = c["image_origin"]
                self.assertEqual(sha(COLLECTION / origin["image"]), origin["image_sha256"])
                self.assertEqual(image.read_bytes(), (COLLECTION / origin["image"]).read_bytes())
                self.assertEqual(sha(COLLECTION / origin["render_prompt"]), origin["render_prompt_sha256"])
            if c.get("render_reference"):
                self.assertTrue((COLLECTION / c["render_reference"]).is_file())
            for ref in c.get("render_references", []):
                self.assertEqual(sha(COLLECTION / ref["path"]), ref["sha256"])

    def test_family_and_symbol_plans_do_not_use_adult_body_reference(self):
        for c in self.collection["cards"]:
            plan = self.by_slug[c["slug"]]
            if c["wardrobe_profile"] in {"family_covered", "symbol_only"}:
                self.assertIsNone(plan["image_reference"])
                if c.get("image") and c["wardrobe_profile"] == "family_covered":
                    self.assertTrue(c["visual_review"]["all_people_fully_clothed"])

    def test_document_links_and_main_source_preservation(self):
        for p in [COLLECTION / "README.md", ROOT / "prompts/cardstarot_vi/README.md"]:
            for href in re.findall(r"\]\(([^)]+)\)", p.read_text()):
                if not href.startswith(("http", "#")):
                    self.assertTrue((p.parent / href.split("#")[0]).exists(), (p, href))
        self.assertEqual(self.plans["source_json_sha256"], sha(ROOT / "tarot prompt/cards.json"))
        for plan in self.plans["cards"]:
            self.assertEqual(plan["source_sha256"], sha(ROOT / plan["source_prompt"]))
        self.assertEqual(self.collection["style_profile"]["reference_sha256"], sha(ROOT / self.collection["style_profile"]["reference"]))


if __name__ == "__main__":
    unittest.main()
