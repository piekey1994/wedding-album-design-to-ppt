# End-to-end workflow

## 1. Intake and discovery

Inspect the workspace before making changes. Locate source photos, prior copy, client feedback, approved designs, and output constraints. Confirm the intended album dimensions, page count, spread order, cover format, and whether the final PPT is for screen review or print-oriented handoff.

Do not ask questions that can be answered from local files. Ask only when a missing choice would materially alter selection, sequencing, format, privacy, or external publication.

## 2. Inventory and tagging

Create or update `01_plan/album_manifest.csv`. Assign stable spread IDs and exact filenames. Derive dimensions, orientation, and basic technical flags programmatically when possible; assign semantic and design-role tags through visual inspection.

Generate contact sheets with filenames visible. Contact sheets are review tools, not final art.

## 3. Story and spread plan

Group images into a coherent progression such as arrival, landscape, intimacy, ceremony, and closing night details. For each spread, record exact photo filenames and roles, a short layout intention, optional native text, palette constraints, and crop or replacement concerns.

Prefer variation across adjacent spreads. If several spreads share the same grid, change hierarchy, edge behavior, scale, overlap, whitespace, or crossing of the gutter.

## 4. AI layout mockups

Use image generation to explore or render the spread composition. Supply only the necessary contact sheet or references for that spread. State that the output is a design mockup and that exact faces and photo details need not become final assets.

Store generated pages separately from originals. Maintain an explicit mapping from each generated page back to the manifest.

## 5. Feedback loop

Convert feedback into a change log keyed by spread ID. Distinguish global rules from local changes:

- Global: palette, borders, typography density, decoration language.
- Local: add a sentence to `S04`, redesign `S06`, reduce images in `S12`.

Regenerate affected pages, update the manifest if the photo set changes, and keep the latest approved version clearly named. Do not silently reinterpret approved selections.

## 6. Editable PPT reconstruction

Rebuild the approved composition with source photographs. The generated design page may be used side by side as a visual reference, but must not be embedded as the finished spread.

Recreate text, mats, rules, washes, and panels as native PowerPoint objects. Keep each photo independently selectable and replaceable. Use separate decks for incompatible aspect ratios when appropriate.

## 7. Verification and handoff

Render every slide. Check cropping, sequence, text, overflow, margins, visual variety, and the requested corrections. Run the presentation validator. Deliver the PPTX files, a concise replacement instruction, and any manifest or source map that helps later editing.

Stop after delivering the requested local artifacts unless the user also authorizes an external mutation such as publishing a repository or sharing a file.

