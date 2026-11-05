---
name: editor-config
description: Create or update a repository .editorconfig from its actual languages, file types, formatters, and whitespace-sensitive files. Use when standardizing editor indentation, encoding, newlines, and trailing-whitespace behavior.
license: MIT
---

# Editor Config

Inspect the repository's files, nested `.editorconfig` files, formatter settings, and generated paths. Create or update `.editorconfig` directly using [the polyglot template](assets/editorconfig) and [the language and precedence guide](references/rules.md).

1. Identify actual file types and existing conventions. Preserve coherent formatter settings and required syntax.
2. Establish root-level UTF-8, LF, final newline, and whitespace defaults. Add only relevant language overrides from the template.
3. Preserve hard tabs for Make recipes and the language's required tab behavior. Preserve intentional Markdown hard breaks and significant fixture whitespace.
4. Order broad sections before narrow exceptions. Verify that later matching sections and closer configuration files resolve as intended.
5. Explain any deliberate change that could reformat existing files. Creating configuration does not authorize a repository-wide formatting rewrite.
6. Check representative real files with the configured EditorConfig integration or an appropriate checker when available. Use the existing formatter for language-specific style enforcement.

EditorConfig supplies editor properties, not a complete formatter, linter, or security boundary. Keep its values consistent with Ruff, Prettier, gofmt, rustfmt, or the chosen language tool. Verify support before adding nonstandard properties. Consult [sources](references/sources.md).

## License

[MIT license and copyright notice](LICENSE.md).
