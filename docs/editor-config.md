# Editor Config

Create effective editing rules for the repository's actual languages.

## Invoke

Codex:

```text
$editor-config Create a .editorconfig for this Python, Vue, YAML, and Markdown repository that matches its formatters.
```

Claude Code uses `/editor-config` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Provide the repository and any established formatter settings.
- Identify meaningful whitespace fixtures or generated paths needing special treatment.

## What happens

The skill inspects existing and nested configuration, adapts relevant sections of the polyglot template, preserves required tabs and Markdown hard breaks, and verifies representative matching behavior.

## Deliverables

An edited .editorconfig and a concise explanation of effective defaults and exceptions.

## Decisions and limits

EditorConfig is not a full formatter or linter. Closer files and later matching sections override earlier values. Configuration work does not implicitly authorize reformatting the whole repository.

## Detailed instructions

Read [the portable skill](../skills/editor-config/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
