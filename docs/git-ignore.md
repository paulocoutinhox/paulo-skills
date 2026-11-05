# Git Ignore

Exclude generated and private local files while preserving reproducibility inputs.

## Invoke

Codex:

```text
$git-ignore Audit this repository and create a .gitignore for its Python and Node tooling. Check tracked files separately.
```

Claude Code uses `/git-ignore` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Provide the repository and its real build/runtime tools.
- Identify intentionally tracked generated artifacts, shared editor settings, and sanitized examples.

## What happens

The skill adapts scoped patterns, checks ignored and preserved paths, reviews existing tracked artifacts, and separates credential exposure from ordinary ignore hygiene.

## Deliverables

An updated .gitignore, representative rule checks, and any concrete tracked-file or secret concerns.

## Decisions and limits

Keep lockfiles, source assets, migrations, and wrappers. Ignore rules do not protect already tracked files, erase history, revoke secrets, or stop forced staging. Rotation and history changes are separate actions.

## Detailed instructions

Read [the portable skill](../skills/git-ignore/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
