# Editable PowerPoint reconstruction

Use the `presentations` skill for this stage and follow its required render-and-verify process.

## Build rules

- Use the approved AI page as a visual reference beside the source-photo manifest.
- Add every source photo as an independent picture object with `cover` or `contain` cropping appropriate to the frame.
- Recreate text as native textboxes and decoration as native shapes.
- Use simple white mats, pale color fields, and thin rules instead of rasterized frame graphics when possible.
- Put the exact source filename in image alt text or slide speaker notes.
- Keep the original source files untouched. If originals are extremely large, create derived high-quality JPEGs for embedding and document the resize policy.
- Do not use an AI design page as the slide background except for temporary tracing during construction; remove it before export.

## Replacement-friendly behavior

The user should be able to select one photo and choose `Picture Format → Change Picture` without rebuilding the spread. Avoid grouped raster collages. If grouping is useful for movement, group editable objects only after verifying each picture remains independently reachable.

## Aspect ratios

Do not distort a square cover to fit landscape spreads. Prefer separate decks when the cover and interior formats differ. Record the intended output size in the README or handoff notes.

## Visual QA checklist

- Correct original filename in every frame.
- No generated face or generated typography remains.
- No unintended crop removes a face, bouquet, dress, or ceremony focal point.
- Adjacent spreads have meaningful layout variation.
- Text matches the approved copy exactly and is not repeated unnecessarily.
- No dark or forbidden borders were reintroduced.
- Small photos remain readable; delete redundant tiny frames.
- Gutter-sensitive faces and text remain away from the fold.
- All slide content stays inside bounds with no overflow.
- Every slide is rendered and inspected; presentation validation passes.

