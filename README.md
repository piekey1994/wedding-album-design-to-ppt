# Wedding Album Design to Editable PPT

A reusable Codex skill for turning wedding or portrait-session originals into:

1. a filename-safe photo inventory and spread manifest;
2. labeled contact sheets for selection and review;
3. AI-generated album layout mockups;
4. an editable PowerPoint rebuilt with the real source photographs.

The central rule is simple: AI-generated pages are layout references, not final photographic assets. The exported PPT restores the real photos and keeps every picture, text block, mat, line, and color field editable.

## What the skill standardizes

- `COVER`, `S01`, `S02`, … spread IDs and exact filename mapping
- photo roles such as hero, support, detail, and transition
- iterative feedback recorded per spread
- prompts for restrained editorial wedding-album mockups
- replacement-friendly PPT construction and slide-by-slide QA
- separation of client originals from derived previews and reusable code

## Install locally

Copy this folder to your Codex skills directory:

```text
%CODEX_HOME%/skills/wedding-album-design-to-ppt
```

If `CODEX_HOME` is unset on Windows, the usual location is:

```text
%USERPROFILE%/.codex/skills/wedding-album-design-to-ppt
```

Invoke it with:

```text
$wedding-album-design-to-ppt
```

## Optional project scaffold

```bash
python scripts/init_album_project.py path/to/new-album
```

Fill `01_plan/album_manifest.csv`, place originals in `source_photos`, then create labeled boards:

```bash
python scripts/make_contact_sheets.py --project path/to/new-album
```

## Privacy

This repository contains workflow instructions and helper scripts only. Do not commit client photographs, generated album pages, review exports, or PPT deliverables.


