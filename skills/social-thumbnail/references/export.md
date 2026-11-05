# JPEG export utility

The exporter converts a generated PNG or other supported raster master into a checked JPEG derivative. It does not generate or creatively edit imagery. Generate and repair artwork with the available image model before using it.

The utility requires Python 3.11+ and Pillow. Its inline dependency metadata supports:

```bash
uv run --script scripts/export-thumbnail.py master.png thumbnail.jpg --width 3840 --height 2160 --quality 99 --max-bytes 2000000
```

Alternatively, install Pillow in an isolated environment and run the script with that environment's Python. For a different approved composition, choose `--fit crop` or `--fit contain` explicitly. The default is `exact`, which rejects a mismatched aspect ratio. `contain` adds a deliberate background rather than stretching. The default background is white and can be set with `--background '#101820'`.

Upscaling is rejected unless `--allow-upscale` is explicitly selected. Existing output files are never overwritten. A byte-limit failure leaves no output file. The program does not secretly lower quality or resolution. Inspect the image after choosing a new approved setting. The original source is left intact.

Embedded color profiles are converted to sRGB when valid. An untagged image is treated as sRGB, which must be confirmed when the master came from a different color workflow. EXIF orientation is applied before resizing. The output embeds an sRGB profile and reports final pixel dimensions, quality, and bytes as JSON.
