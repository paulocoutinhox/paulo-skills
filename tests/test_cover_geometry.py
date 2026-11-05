import json
import unittest

from process_helper import ProcessHelper


class CoverGeometryTest(unittest.TestCase):
    SCRIPT = "skills/book-creator/scripts/cover-geometry.py"

    def test_cream_paper_wrap_dimensions(self):
        result = ProcessHelper.python(
            self.SCRIPT,
            "--pages",
            "240",
            "--trim-width-mm",
            "152.4",
            "--trim-height-mm",
            "228.6",
            "--paper",
            "cream-bw",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        geometry = json.loads(result.stdout)
        self.assertAlmostEqual(geometry["spine-mm"], 15.24)
        self.assertAlmostEqual(geometry["wrap-width-mm"], 326.39)
        self.assertAlmostEqual(geometry["wrap-height-mm"], 234.95)
        self.assertTrue(geometry["template-verification-required"])

    def test_explicit_template_spine_and_bleed(self):
        result = ProcessHelper.python(
            self.SCRIPT,
            "--pages",
            "120",
            "--trim-width-mm",
            "148",
            "--trim-height-mm",
            "210",
            "--spine-mm",
            "8",
            "--bleed-mm",
            "5",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["wrap-width-mm"], 314)

    def test_invalid_geometry_is_rejected(self):
        for pages, width in [("121", "148"), ("0", "148"), ("120", "nan"), ("120", "-1"), ("120", "1e308")]:
            with self.subTest(pages=pages, width=width):
                result = ProcessHelper.python(
                    self.SCRIPT,
                    "--pages",
                    pages,
                    "--trim-width-mm",
                    width,
                    "--trim-height-mm",
                    "210",
                    "--paper",
                    "white-bw",
                )
                self.assertNotEqual(result.returncode, 0)

    def test_conflicting_spine_sources_are_rejected(self):
        result = ProcessHelper.python(
            self.SCRIPT,
            "--pages",
            "120",
            "--trim-width-mm",
            "148",
            "--trim-height-mm",
            "210",
            "--paper",
            "white-bw",
            "--spine-mm",
            "8",
        )
        self.assertNotEqual(result.returncode, 0)
