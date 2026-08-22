# Tagging and manifest

## Stable identifiers

Use `COVER`, `S01`, `S02`, … for album pages or spreads. Keep the ID stable through revisions. Version the rendered design file, not the logical spread ID.

## Recommended manifest columns

| Column | Purpose |
|---|---|
| `asset_id` | Stable local identifier; may equal the filename stem |
| `filename` | Exact source filename including extension and case |
| `width_px`, `height_px`, `orientation` | Technical placement data |
| `scene` | Forest, mountain, ceremony, night, interior, etc. |
| `subject` | Couple, bride, groom, bouquet, rings, decor, landscape |
| `shot` | Wide, full, medium, closeup, detail |
| `action` | Walking, embracing, ceremony, toast, still-life |
| `light` | Soft, backlit, harsh, dusk, night |
| `quality_flags` | Blur, blink, duplicate, clipped highlight, crop risk |
| `spread_id` | `COVER` or `S##` |
| `role` | Cover, hero, support, detail, transition |
| `priority` | `1` strongest through `3` optional |
| `text` | Approved native text for this spread, if any |
| `notes` | Crop guidance, feedback, replacement warning |

Use consistent comma-free tag tokens or quote CSV fields correctly.

## Selection principles

- Lead with visual and emotional clarity, not only technical sharpness.
- Avoid near-duplicates unless they form an intentional sequence.
- Balance wide environmental views, portraits, interactions, and details.
- Give small frames images with readable silhouettes or details; reserve complex scenes for larger frames.
- A crowded spread should lose weak or redundant images before adding decoration.
- Treat natural green in photographs separately from an added green design palette.

## Contact sheets

Contact sheets must show the exact filename next to each thumbnail and group images by spread. Use them to confirm mappings and prevent later substitution errors. Keep boards in a derived folder; never annotate the source files themselves.

