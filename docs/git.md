# Git

Prepare a branch and one reviewed commit with task-aware naming.

## Invoke

Codex:

```text
$git Review the current changes and create one commit. There is no task identifier. Do not push.
```

Claude Code uses `/git` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Identify the intended changes and whether a task key exists.
- State whether branch creation, committing, or pushing is authorized.
- Keep the configured human Git identity available.

## What happens

The skill inspects current and staged changes, identifies the task key or asks once, runs relevant checks, excludes private/generated files, stages explicit paths, and creates one concise commit.

## Deliverables

A branch when requested, one commit hash and subject, check results, and the remaining working-tree state.

## Decisions and limits

An identifier preserves its case, as in UBKMI-1234 fix player. Otherwise use a lowercase conventional subject. No generated attribution or co-author trailer is added. Ignoring a file does not remove an existing tracked exposure.

## Detailed instructions

Read [the portable skill](../skills/git/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
