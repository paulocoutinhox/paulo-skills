import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import editorconfig
from process_helper import ProcessHelper


class ConfigurationTest(unittest.TestCase):
    def test_editorconfig_template_preserves_sensitive_whitespace(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            template = ProcessHelper.ROOT / "skills/editor-config/assets/editorconfig"
            shutil.copy(template, root / ".editorconfig")

            for name, expected in [("app.py", "4"), ("app.ts", "2"), ("config.yaml", "2")]:
                properties = editorconfig.get_properties(str(root / name))
                self.assertEqual(properties["indent_size"], expected)

            self.assertEqual(editorconfig.get_properties(str(root / "Makefile"))["indent_style"], "tab")
            self.assertEqual(editorconfig.get_properties(str(root / "main.go"))["indent_style"], "tab")
            markdown = editorconfig.get_properties(str(root / "guide.md"))
            self.assertEqual(markdown["trim_trailing_whitespace"], "false")

    def test_ignore_template_excludes_artifacts_but_keeps_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True, capture_output=True)
            shutil.copy(ProcessHelper.ROOT / "skills/git-ignore/assets/gitignore", root / ".gitignore")

            ignored = [
                ".env",
                ".env.production",
                ".venv/lib/module.py",
                "node_modules/pkg/index.js",
                "dist/bundle.js",
                "runtime.log",
                "credentials.json",
                ".DS_Store",
            ]
            retained = ["src/module.py", "uv.lock", "package-lock.json", ".env.example", "assets/logo.svg"]

            for path, expected in [(path, 0) for path in ignored] + [(path, 1) for path in retained]:
                result = subprocess.run(
                    ["git", "-C", str(root), "check-ignore", "--no-index", "-q", path],
                    check=False,
                    capture_output=True,
                )
                self.assertEqual(result.returncode, expected, path)
