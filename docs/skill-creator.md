# Skill Creator

Create or revise a portable skill from a real repeatable task.

## Invoke

Codex:

```text
$skill-creator Create a skill for monthly sales reports from CSV inputs, with validation and a usage guide.
```

Claude Code uses `/skill-creator` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Describe the user outcome and representative input/output.
- State the target repository and installation client only if installation is requested.
- Provide domain requirements, authoritative sources, tool availability, and boundaries.

## What happens

The skill researches the domain, distinguishes mandatory format fields from optional resources, writes a portable entrypoint, creates useful supporting files, validates the directory with skills-ref, and checks realistic behavior.

## Deliverables

A complete skill directory, source notes, usage example, dependency notes, and actual validation results.

## Decisions and limits

Review metadata, resource paths, missing-input behavior, out-of-scope behavior, and any executable helpers. Installation into user directories occurs only when requested.

## Detailed instructions

Read [the portable skill](../skills/skill-creator/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
