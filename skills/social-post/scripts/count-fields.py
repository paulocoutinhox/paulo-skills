#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


class TextCountHelper:
    @staticmethod
    def count(content: str, unit: str) -> int:
        if unit == "codepoints":
            return len(content)

        if unit == "utf8":
            return len(content.encode("utf-8"))

        if unit == "utf16":
            return len(content.encode("utf-16-le")) // 2

        tags = json.loads(content)

        if not isinstance(tags, list) or not all(isinstance(tag, str) and tag.strip() for tag in tags):
            raise ValueError("YouTube tags must be a JSON array of nonempty strings.")

        return sum(len(tag) + (2 if " " in tag else 0) for tag in tags) + max(len(tags) - 1, 0)

    @classmethod
    def run(cls) -> None:
        parser = argparse.ArgumentParser(
            description="Count final social publishing text in an explicit unit."
        )
        parser.add_argument("path", type=Path)
        parser.add_argument("--unit", required=True, choices=["codepoints", "utf8", "utf16", "youtube-tags"])
        parser.add_argument("--limit", required=True, type=int)
        arguments = parser.parse_args()

        if arguments.limit < 1:
            parser.error("The limit must be positive.")

        try:
            with arguments.path.open(encoding="utf-8", newline="") as text_file:
                content = text_file.read()

            count = cls.count(content, arguments.unit)
        except (OSError, ValueError, UnicodeError) as error:
            parser.exit(2, f"Cannot validate the input: {error}\n")

        valid = count <= arguments.limit
        print(json.dumps({"unit": arguments.unit, "count": count, "limit": arguments.limit, "valid": valid}))
        raise SystemExit(0 if valid else 1)


if __name__ == "__main__":
    TextCountHelper.run()
