---
name: book-creator
description: Design and typeset books and A4 workbooks for print, digital delivery, or both, including white-page interior PDFs, navigable contents, citations, bibliographies, illustrated covers, back covers, and page-count-aware spine geometry. Use when creating or preparing a complete book publication package.
license: MIT
---

# Book Creator

Produce a coherent publication package from the supplied manuscript or an agreed outline. Keep production guidance and finished book content provider-neutral. Do not name print providers in the book, cover, or delivery narrative.

## Establish the brief before layout

Read [the intake and deliverable contract](references/intake.md) and use [the publication brief](assets/publication-brief.json). Ask for unresolved consequential choices in compact groups:

- Print, digital, or both. Book or workbook. A workbook defaults to A4, 210 × 297 mm. Ask the trim size for a book rather than treating every book as A4.
- Title, subtitle, exact author name, language, audience, content, rights, edition, and ISBN if available.
- ABNT-based editorial profile, strict academic requirements, or another named style. Default to the ABNT-based profile with Arial 12 as an owner-selected convention. Ask about thematic typography and color.
- Desired front matter, internal cover sides, title page, copyright page, dedication, acknowledgments, preface, appendices, glossary, bibliography, and index.
- Whether a cover should appear in the same reader PDF as the interior. Keep manufacturing cover and interior files separate unless the printer explicitly requires otherwise.
- Caption titles above images and an automatic list of figures. Footnotes, author-date citations, and bibliography behavior.
- Pagination position: lower center, lower outer/right, or upper outer/right. Strict academic mode uses its applicable pagination rules rather than silently treating every option as compliant.
- For print: paper, weight, ink, cover stock and color, lamination, trim, binding, flaps, and the actual production template. See [print production](references/print-production.md).

## Build the publication

1. Validate the brief, manuscript, quotations, sources, illustration needs, and ISBN. Do not fabricate a bibliographic entry, quotation, legal notice, cataloging record, or identifier.
2. Apply [the editorial and ABNT profile](references/editorial.md). Keep rules of the chosen style distinct from configurable book-design choices.
3. Typeset a proof with named paragraph, heading, quotation, note, caption, table, list, code, and reference styles. [The A4 LuaLaTeX template](assets/main.tex) supplies a starting layout, not a complete compliance engine. Read [typesetting and preflight](references/typesetting.md) before using it.
4. Generate requested illustrative artwork with the available image model. Use [the image and cover design procedure](references/visual-design.md). Keep charts factual and data-driven. Preserve proportions and inspect generated anatomy, geometry, lettering, and detail.
5. Build a real linked table of contents for digital output, bibliography and citation cross-references, and selected lists. Resolve references after final pagination.
6. Freeze the actual final interior page count, including blank pages. Calculate the spine from the verified paper and binding template. Run `python3 scripts/cover-geometry.py --help` and consult [geometry rules](references/print-production.md). Recalculate whenever pagination changes.
7. Deliver front-cover PNG, back-cover PNG, and a complete back–spine–front PNG when requested. For print, also deliver the production cover PDF and interior PDF required by the selected template. PNG is an artwork master or preview, not a substitute for a press PDF.
8. Export digital and manufacturing variants separately. Keep every interior page white or unpainted. Color and imagery may cover the front and back covers. Never simulate cream paper by painting interior page backgrounds.
9. Run layout, navigation, font, image, color, barcode, page-count, and physical-geometry checks. Visually inspect every page and the assembled cover before declaring readiness.

## Completion

Deliver only the chosen modes with editable sources and a manifest of dimensions, page count, fonts, paper, ink, binding, spine, bleed, marks policy, ISBN status, and checks performed. Distinguish a proof awaiting a printer template from an approved production file. Never claim printer approval from a successful local export. Bibliographic and production verification guidance is in [source notes](references/sources.md).

## License

[MIT license and copyright notice](LICENSE.md).
