import json
import tempfile
import unittest
from pathlib import Path

from process_helper import ProcessHelper


class TextCountTest(unittest.TestCase):
    SCRIPT = "skills/social-post/scripts/count-fields.py"

    def test_unicode_units_and_limit_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "caption.txt"
            source.write_bytes("Aé😀\r\n".encode())

            for unit, expected in [("codepoints", 5), ("utf8", 9), ("utf16", 6)]:
                with self.subTest(unit=unit):
                    result = ProcessHelper.python(
                        self.SCRIPT, str(source), "--unit", unit, "--limit", str(expected)
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(json.loads(result.stdout)["count"], expected)

                    over = ProcessHelper.python(
                        self.SCRIPT, str(source), "--unit", unit, "--limit", str(expected - 1)
                    )
                    self.assertEqual(over.returncode, 1)

    def test_youtube_tags_include_spaces_quotes_and_commas(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "tags.json"
            source.write_text(json.dumps(["python", "clean code"]))
            result = ProcessHelper.python(self.SCRIPT, str(source), "--unit", "youtube-tags", "--limit", "19")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["count"], 19)

    def test_invalid_tag_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "tags.json"

            for value in ['{"tag": "test"}', '["valid", ""]', "not JSON"]:
                source.write_text(value)
                result = ProcessHelper.python(
                    self.SCRIPT, str(source), "--unit", "youtube-tags", "--limit", "500"
                )
                self.assertEqual(result.returncode, 2)
