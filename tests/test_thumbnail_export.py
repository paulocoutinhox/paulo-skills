import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image
from process_helper import ProcessHelper


class ThumbnailExportTest(unittest.TestCase):
    SCRIPT = "skills/social-thumbnail/scripts/export-thumbnail.py"

    def test_export_preserves_source_and_checks_dimensions(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "master.png"
            output = Path(directory) / "thumb.jpg"
            Image.new("RGBA", (640, 360), (20, 100, 180, 100)).save(source)
            original = source.read_bytes()
            result = ProcessHelper.python(
                self.SCRIPT, str(source), str(output), "--width", "320", "--height", "180"
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(json.loads(result.stdout)["bytes"], output.stat().st_size)

            with Image.open(output) as image:
                self.assertEqual(image.size, (320, 180))
                self.assertEqual(image.format, "JPEG")
                self.assertIn("icc_profile", image.info)

    def test_byte_failure_leaves_no_output(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "master.png"
            output = Path(directory) / "thumb.jpg"
            Image.new("RGB", (640, 360), "blue").save(source)
            result = ProcessHelper.python(
                self.SCRIPT,
                str(source),
                str(output),
                "--width",
                "320",
                "--height",
                "180",
                "--max-bytes",
                "10",
            )
            self.assertEqual(result.returncode, 1)
            self.assertFalse(output.exists())

    def test_palette_transparency_is_flattened_onto_selected_background(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "master.png"
            output = Path(directory) / "thumb.jpg"
            image = Image.new("P", (320, 180), 0)
            image.putpalette([255, 0, 0] + [0, 0, 0] * 255)
            image.save(source, transparency=0)
            result = ProcessHelper.python(
                self.SCRIPT,
                str(source),
                str(output),
                "--width",
                "160",
                "--height",
                "90",
                "--background",
                "#ffffff",
            )
            self.assertEqual(result.returncode, 0, result.stderr)

            with Image.open(output) as exported:
                red, green, blue = exported.getpixel((80, 45))
                self.assertGreater(min(red, green, blue), 250)

    def test_wrong_ratio_and_upscale_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "master.png"
            Image.new("RGB", (320, 180), "blue").save(source)

            for width, height in [("100", "100"), ("640", "360")]:
                with self.subTest(width=width, height=height):
                    output = Path(directory) / "thumb.jpg"
                    result = ProcessHelper.python(
                        self.SCRIPT, str(source), str(output), "--width", width, "--height", height
                    )
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse(output.exists())

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "master.png"
            output = Path(directory) / "thumb.jpg"
            Image.new("RGB", (320, 180), "blue").save(source)
            output.write_bytes(b"User content.")
            result = ProcessHelper.python(
                self.SCRIPT, str(source), str(output), "--width", "320", "--height", "180"
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_bytes(), b"User content.")

    def test_explicit_containment_keeps_canvas_dimensions(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "master.png"
            output = Path(directory) / "thumb.jpg"
            Image.new("RGB", (320, 180), "blue").save(source)
            result = ProcessHelper.python(
                self.SCRIPT, str(source), str(output), "--width", "160", "--height", "160", "--fit", "contain"
            )
            self.assertEqual(result.returncode, 0, result.stderr)

            with Image.open(output) as image:
                self.assertEqual(image.size, (160, 160))
