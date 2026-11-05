#!/usr/bin/env python3
import argparse
import json
import math


class CoverGeometryHelper:
    THICKNESS_MM = {
        "white-bw": 0.0572008,
        "cream-bw": 0.0635,
        "standard-color": 0.0572008,
        "premium-color": 0.0596138,
    }

    @staticmethod
    def positive_number(value: str) -> float:
        number = float(value)

        if not math.isfinite(number) or number <= 0:
            raise argparse.ArgumentTypeError("The value must be a positive finite number.")

        return number

    @staticmethod
    def page_count(value: str) -> int:
        pages = int(value)

        if pages < 1 or pages % 2:
            raise argparse.ArgumentTypeError("The final paperback page count must be positive and even.")

        return pages

    @classmethod
    def run(cls) -> None:
        parser = argparse.ArgumentParser(
            description="Calculate flat paperback cover geometry in millimeters."
        )
        parser.add_argument("--pages", required=True, type=cls.page_count)
        parser.add_argument("--trim-width-mm", required=True, type=cls.positive_number)
        parser.add_argument("--trim-height-mm", required=True, type=cls.positive_number)
        parser.add_argument("--bleed-mm", default=3.175, type=cls.positive_number)
        spine_source = parser.add_mutually_exclusive_group(required=True)
        spine_source.add_argument("--paper", choices=cls.THICKNESS_MM)
        spine_source.add_argument("--spine-mm", type=cls.positive_number)
        arguments = parser.parse_args()

        spine = arguments.spine_mm

        if arguments.paper is not None:
            spine = arguments.pages * cls.THICKNESS_MM[arguments.paper]

        wrap_width = 2 * arguments.trim_width_mm + spine + 2 * arguments.bleed_mm
        wrap_height = arguments.trim_height_mm + 2 * arguments.bleed_mm

        if not all(math.isfinite(value) for value in [spine, wrap_width, wrap_height]):
            parser.error("The supplied dimensions exceed the supported numeric range.")

        result = {
            "binding": "paperback",
            "pages": arguments.pages,
            "trim-width-mm": arguments.trim_width_mm,
            "trim-height-mm": arguments.trim_height_mm,
            "bleed-mm": arguments.bleed_mm,
            "spine-mm": round(spine, 6),
            "wrap-width-mm": round(wrap_width, 6),
            "wrap-height-mm": round(wrap_height, 6),
            "template-verification-required": True,
        }
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    CoverGeometryHelper.run()
