---
name: wedding-album-design-to-ppt
description: Turn wedding or portrait-session source photos into a tagged album plan, AI-generated layout mockups, and editable PowerPoint album pages that restore the real source photos. Use when a user wants contact sheets, spread-level image selection, iterative album design, or a replaceable-photo PPT rather than flattened AI artwork.
---

# Wedding Album Design to Editable PPT

Build an auditable path from original photographs to approved design mockups and then to editable PowerPoint pages. Preserve the user's chosen photos and copy; do not treat generated faces, generated typography, or generated photo details as final assets.

## Route the work

1. Inventory and tag the original photographs.
2. Plan the album at spread level and create labeled contact sheets when visual review helps.
3. Use the `imagegen` skill and image-generation tool for layout mockups only.
4. Record feedback as explicit spread-level changes and regenerate only affected designs when practical.
5. Use the `presentations` skill to rebuild approved layouts with original photographs and native PowerPoint objects.
6. Render and inspect every exported page before delivery.

Read [references/workflow.md](references/workflow.md) for the complete artifact flow and stopping points. Read only the relevant specialized reference when entering that stage:

- Tagging or photo selection: [references/tagging-and-manifest.md](references/tagging-and-manifest.md)
- Image-generation prompts or design revisions: [references/imagegen-layout-mockups.md](references/imagegen-layout-mockups.md)
- Editable PowerPoint construction and QA: [references/editable-ppt.md](references/editable-ppt.md)

## Non-negotiable invariants

- Never overwrite, move, rename, or recompress the user's originals without explicit authorization. Derived previews belong in separate folders.
- Keep a manifest mapping every spread to the exact original filenames. Filename labels must remain visible on contact sheets.
- Treat AI pages as layout references. Do not reuse their rendered people, scenery, flowers, or text in the final deliverable.
- In the final PPT, each photograph is an independent picture object. Text and decoration are native editable textboxes and shapes.
- Do not flatten a spread into a single background image unless the user explicitly requests a non-editable export.
- Preserve approved sparse-copy decisions. Generated typography is advisory; recreate all final copy as native text.
- Keep client photographs and generated client work out of a reusable skill repository.

## Sensible defaults

- Spread IDs: `COVER`, then `S01`, `S02`, …
- Roles: `cover`, `hero`, `support`, `detail`, `transition`.
- Favor one clear hero image per spread, with fewer supporting images as the spread becomes visually dense.
- Use high-quality derived JPEGs for a practical PPT size while keeping the originals untouched and replaceable. Record the original filename in alt text or speaker notes.
- When cover and spreads use different aspect ratios, export separate PPTX files instead of distorting one format.

## Reusable helpers

- Run `scripts/init_album_project.py <project-directory>` to create a clean working structure and manifest template.
- Run `scripts/make_contact_sheets.py --project <project-directory>` after filling the manifest to create filename-labeled spread boards.

These scripts create derived project files only; they do not modify source photographs.

