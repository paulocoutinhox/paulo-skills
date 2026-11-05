#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["Pillow>=11,<14"]
# ///
import argparse
import io
import json
from pathlib import Path

from PIL import Image, ImageCms, ImageColor, ImageOps


class ThumbnailExportHelper:
    @staticmethod
    def positive_integer(value: str) -> int:
        number = int(value)

        if number < 1:
            raise argparse.ArgumentTypeError("The value must be positive.")

        return number

    @classmethod
    def run(cls) -> None:
        parser = argparse.ArgumentParser(description="Export a proportional JPEG without overwriting files.")
        parser.add_argument("source", type=Path)
        parser.add_argument("output", type=Path)
        parser.add_argument("--width", required=True, type=cls.positive_integer)
        parser.add_argument("--height", required=True, type=cls.positive_integer)
        parser.add_argument("--quality", type=int, default=99, choices=range(1, 101), metavar="1-100")
        parser.add_argument("--max-bytes", type=cls.positive_integer, default=2_000_000)
        parser.add_argument("--fit", choices=["exact", "crop", "contain"], default="exact")
        parser.add_argument("--background", default="#ffffff")
        parser.add_argument("--allow-upscale", action="store_true")
        arguments = parser.parse_args()

        if arguments.output.suffix.lower() not in {".jpg", ".jpeg"}:
            parser.error("The output must use a .jpg or .jpeg extension.")

        if arguments.source.resolve() == arguments.output.resolve() or arguments.output.exists():
            parser.error("The output must be a new file distinct from the source.")

        target = (arguments.width, arguments.height)

        try:
            background = ImageColor.getrgb(arguments.background)
            srgb = ImageCms.createProfile("sRGB")
            profile_bytes = ImageCms.ImageCmsProfile(srgb).tobytes()

            with Image.open(arguments.source) as source:
                image = ImageOps.exif_transpose(source)
                image.load()

                if image.mode == "P":
                    image = image.convert("RGBA" if "transparency" in image.info else "RGB")

                alpha = image.getchannel("A") if "A" in image.getbands() else None
                embedded_profile = image.info.get("icc_profile")

                if embedded_profile:
                    source_profile = ImageCms.ImageCmsProfile(io.BytesIO(embedded_profile))
                    image = ImageCms.profileToProfile(image, source_profile, srgb, outputMode="RGB")
                else:
                    image = image.convert("RGB")

                if alpha is not None:
                    canvas = Image.new("RGB", image.size, background)
                    canvas.paste(image, mask=alpha)
                    image = canvas

            if arguments.fit == "exact" and image.width * target[1] != image.height * target[0]:
                parser.error("Aspect ratios differ. Select an approved crop or contain operation.")

            width_scale = target[0] / image.width
            height_scale = target[1] / image.height
            scale = (
                min(width_scale, height_scale)
                if arguments.fit == "contain"
                else max(width_scale, height_scale)
            )

            if scale > 1 and not arguments.allow_upscale:
                parser.error("The requested export would upscale the source.")

            if arguments.fit == "crop":
                image = ImageOps.fit(image, target, method=Image.Resampling.LANCZOS)
            elif arguments.fit == "contain":
                resized = ImageOps.contain(image, target, method=Image.Resampling.LANCZOS)
                canvas = Image.new("RGB", target, background)
                offset = ((target[0] - resized.width) // 2, (target[1] - resized.height) // 2)
                canvas.paste(resized, offset)
                image = canvas
            else:
                image = image.resize(target, Image.Resampling.LANCZOS)

            buffer = io.BytesIO()
            image.save(
                buffer,
                format="JPEG",
                quality=arguments.quality,
                subsampling=0,
                optimize=True,
                icc_profile=profile_bytes,
            )
            encoded = buffer.getvalue()

            if len(encoded) > arguments.max_bytes:
                parser.exit(1, f"Export needs {len(encoded)} bytes. Choose approved dimensions or quality.\n")

            with arguments.output.open("xb") as output_file:
                output_file.write(encoded)
        except (OSError, ValueError, ImageCms.PyCMSError) as error:
            parser.exit(2, f"Export failed: {error}\n")

        print(
            json.dumps(
                {
                    "width": target[0],
                    "height": target[1],
                    "quality": arguments.quality,
                    "bytes": len(encoded),
                    "format": "JPEG",
                }
            )
        )


if __name__ == "__main__":
    ThumbnailExportHelper.run()
