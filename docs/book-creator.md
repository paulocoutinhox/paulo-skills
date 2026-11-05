# Book Creator

Produce a typeset book or workbook with the selected print and digital artifacts.

## Invoke

Codex:

```text
$book-creator Turn this manuscript into an A4 workbook for print and digital reading. Use the ABNT-based editorial defaults and ask me about cover stock, binding, ISBN, and internal parts.
```

Claude Code uses `/book-creator` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Supply the manuscript or agree on an outline, title, author, audience, and language.
- Choose print, digital, or both. Workbooks default to A4. Specify a book's trim dimensions.
- Select style, front matter, figure titles/lists, notes, pagination, cover inclusion, stock, ink, lamination, and binding.
- Provide the actual printer template and assigned ISBN when available.

## What happens

The skill establishes the brief before layout, keeps the interior white, generates illustration artwork with an available image model, typesets real navigation and references, freezes the actual page count, and calculates the final spine from the selected production path.

## Deliverables

Selected interior/reader PDFs, front/back/full-wrap PNG masters as applicable, a required manufacturing cover PDF, editable sources, and a production manifest.

## Decisions and limits

ABNT-based design differs from strict academic compliance. Arial 12 is the selected default. Crop marks depend on the printer. Hardcover, spiral, and saddle stitch need their own geometry. A final printer proof remains distinct from local preflight.

## Detailed instructions

Read [the portable skill](../skills/book-creator/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
