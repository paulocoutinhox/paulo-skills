# Code Review

Review a change and trace its system impact with concrete evidence.

## Invoke

Codex:

```text
$code-review Review this branch against main. Trace affected callers, data contracts, permissions, background jobs, and deployment. Do not edit files.
```

Claude Code uses `/code-review` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Provide the base/head or intended staged/working-tree scope and task intent.
- Make relevant source, tests, and integration context available.
- Specify whether the request is review-only or also authorizes fixes.

## What happens

The skill reads complete changes and surrounding code, builds an impact map, checks integration and failure paths, validates suspicious behavior, and reports actionable findings.

## Deliverables

Severity-ordered findings with locations, triggers, impact and evidence, plus reviewed scope, checks, and coverage gaps.

## Decisions and limits

A passing suite does not prove unchanged callers are correct. Findings distinguish introduced defects from baseline issues. No findings is a valid result when supported. Review-only does not authorize PR comments, source edits, or commits.

## Detailed instructions

Read [the portable skill](../skills/code-review/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
