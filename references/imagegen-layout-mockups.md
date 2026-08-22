# Image-generation layout mockups

Use the `imagegen` skill for this stage.

## Purpose

The generated page is a composition reference: hierarchy, crop intention, spacing, color, text placement, decoration, and spread rhythm. It is not the final photographic asset.

## Prompt structure

Include:

1. Canvas format and whether it is a single page or cross-page spread.
2. Exact number and roles of reference photos.
3. Primary hierarchy: hero photo, supporting frames, whitespace, gutter behavior.
4. Palette and materials: e.g. warm ivory, pale mist blue, restrained champagne gold.
5. Typography: exact approved English sentence or no text.
6. Decoration limits and forbidden colors/elements.
7. A request for clean editorial geometry and clearly separated photo frames.

Example skeleton:

```text
Create a refined editorial wedding-album spread mockup in a 3:2 landscape canvas.
Use the attached labeled contact sheet as the only photo-selection reference.
Layout: one dominant hero frame across the left page, three varied supporting frames on the right, generous warm-ivory negative space, one pale mist-blue translucent block, and a very thin champagne-gold rule.
Native copy to place: “...”. No other text.
Avoid dark-green borders, heavy ornament, repeated equal grids, tiny unreadable photos, or invented extra photos.
This is a layout mockup; exact photographic fidelity will be restored later from the originals.
```

## Iteration discipline

- Keep global feedback in a shared brief and local feedback under the spread ID.
- Regenerate the smallest affected scope.
- When a client deletes photos, update the manifest before regenerating.
- When adjacent spreads feel repetitive, change the composition logic rather than only adding ornaments.
- If generated text is misspelled, do not waste iterations perfecting it when the final PPT will use native text; preserve only its placement and scale.

