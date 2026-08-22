#!/usr/bin/env python3
"""Create a non-destructive wedding-album working structure."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


DIRS = (
    "source_photos",
    "01_plan",
    "02_contact_sheets",
    "03_ai_design_pages",
    "04_review",
    "05_editable_ppt",
)

COLUMNS = (
    "asset_id",
    "filename",
    "width_px",
    "height_px",
    "orientation",
    "scene",
    "subject",
    "shot",
    "action",
    "light",
    "quality_flags",
    "spread_id",
    "role",
    "priority",
    "text",
    "notes",
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_directory", type=Path)
    args = parser.parse_args()
    root = args.project_directory.resolve()
    root.mkdir(parents=True, exist_ok=True)
    for name in DIRS:
        (root / name).mkdir(exist_ok=True)

    manifest = root / "01_plan" / "album_manifest.csv"
    if not manifest.exists():
        with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
            csv.writer(handle).writerow(COLUMNS)

    brief = root / "01_plan" / "design_brief.md"
    if not brief.exists():
        brief.write_text(
            "# Album design brief\n\n"
            "- Format:\n- Spread count:\n- Cover format:\n- Palette:\n"
            "- Typography:\n- Text policy:\n- Forbidden elements:\n- Delivery format:\n",
            encoding="utf-8",
        )

    print(root)


if __name__ == "__main__":
    main()

