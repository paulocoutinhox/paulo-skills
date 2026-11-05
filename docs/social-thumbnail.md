# Social Thumbnail

Create original thumbnail artwork and proportionally exported derivatives.

## Invoke

Codex:

```text
$social-thumbnail Create a thumbnail for this tutorial. Use 16:9, a large PNG master, and a JPEG starting at quality 99 under 2 MB.
```

Claude Code uses `/social-thumbnail` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Supply the content promise, audience, language, exact text, theme, and references.
- Choose platform/surface, upload device, ratio, dimensions, file format, and byte ceiling.
- Provide brand assets and approved font direction when applicable.

## What happens

The skill generates image-model artwork, sets precise readable typography, inspects proportions and small-size legibility, preserves the master, and exports only the chosen derivative settings.

## Deliverables

Large PNG master, requested JPEG or other derivatives, actual dimensions/bytes/settings, and visual inspection notes.

## Decisions and limits

16:9 is the generic default, but Shorts and vertical covers need another composition. Current YouTube desktop and mobile limits differ. The exporter fails rather than silently lowering quality, changing composition, or overwriting output.

## Detailed instructions

Read [the portable skill](../skills/social-thumbnail/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
