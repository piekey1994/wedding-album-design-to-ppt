#!/usr/bin/env python3
"""Build filename-labeled contact sheets grouped by spread_id."""

from __future__ import annotations

import argparse
import csv
import math
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


def font(size: int) -> ImageFont.ImageFont:
    candidates = (
        "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--columns", type=int, default=3)
    args = parser.parse_args()

    project = args.project.resolve()
    manifest = project / "01_plan" / "album_manifest.csv"
    photos = project / "source_photos"
    output = project / "02_contact_sheets"
    output.mkdir(parents=True, exist_ok=True)

    groups: dict[str, list[str]] = defaultdict(list)
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            spread = (row.get("spread_id") or "UNASSIGNED").strip()
            filename = (row.get("filename") or "").strip()
            if filename:
                groups[spread].append(filename)

    thumb_w, thumb_h, label_h, gap, margin = 540, 390, 48, 28, 38
    title_h = 82
    title_font, label_font = font(34), font(22)

    for spread, filenames in sorted(groups.items()):
        cols = max(1, args.columns)
        rows = math.ceil(len(filenames) / cols)
        canvas_w = margin * 2 + cols * thumb_w + (cols - 1) * gap
        canvas_h = margin * 2 + title_h + rows * (thumb_h + label_h) + (rows - 1) * gap
        canvas = Image.new("RGB", (canvas_w, canvas_h), "#F6F2EA")
        draw = ImageDraw.Draw(canvas)
        draw.text((margin, margin), spread, fill="#403A34", font=title_font)

        for index, filename in enumerate(filenames):
            row, col = divmod(index, cols)
            x = margin + col * (thumb_w + gap)
            y = margin + title_h + row * (thumb_h + label_h + gap)
            source = photos / filename
            if source.exists():
                with Image.open(source) as image:
                    image = ImageOps.exif_transpose(image).convert("RGB")
                    tile = ImageOps.contain(image, (thumb_w, thumb_h))
                    px = x + (thumb_w - tile.width) // 2
                    py = y + (thumb_h - tile.height) // 2
                    canvas.paste(tile, (px, py))
            else:
                draw.rectangle((x, y, x + thumb_w, y + thumb_h), outline="#B85C5C", width=4)
                draw.text((x + 18, y + 18), "MISSING", fill="#B85C5C", font=label_font)
            draw.text((x, y + thumb_h + 10), filename, fill="#403A34", font=label_font)

        canvas.save(output / f"{spread}_contact_sheet.jpg", quality=92, subsampling=0)


if __name__ == "__main__":
    main()

