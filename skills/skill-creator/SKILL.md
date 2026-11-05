---
name: skill-creator
description: Create, update, and validate portable Agent Skills with researched workflows, standard frontmatter, focused references, reusable templates, and behavioral acceptance criteria. Use when authoring a SKILL.md or maintaining a skill collection.
license: MIT
---

# Skill Creator

Create a skill another capable agent can use independently. Research the requested domain before writing instructions. Preserve the user's actual task, choices, and authorization.

## Workflow

1. Identify the deliverable, trigger phrases, required inputs, exclusions, and meaningful completion criteria. Ask only for information that changes the result.
2. Consult current primary documentation. Record official requirements, selected conventions, recommendations, conflicts, and unknowns separately. Read [the format contract](references/format.md) before choosing structure.
3. Select a single capability and a lowercase hyphenated folder name. Use [the authoring workflow](references/authoring.md) to design decisions, resource routing, failures, and output.
4. Create `SKILL.md` from [the entrypoint template](assets/skill-template.md). Replace every instructional placeholder. Add only resources the workflow actually uses.
5. Put detailed mode-specific rules in references. Put reusable output files in assets. Put deterministic transformations in scripts. Link every resource directly from the entrypoint with its purpose and invocation.
6. Validate the folder with `skills-ref validate ./path/to/skill`. When working in a collection, validate every skill. Fix failures before delivery.
7. Exercise a realistic normal request, a missing-input request, an out-of-scope request, and a material boundary or failure. Execute new helpers against representative inputs. Inspect outputs and error behavior.
8. Deliver the complete skill directory, usage example, dependencies, validation results, and any unresolved limits. For an existing repository, update its current architecture guidance and user documentation.

## Installation and portability

Author in the location the user requested. Installing is a separate requested action. When installation is requested, confirm the client from context or ask: Codex uses `~/.agents/skills/<name>/`, and Claude Code uses `~/.claude/skills/<name>/`. Repository scopes use `.agents/skills/` and `.claude/skills/` respectively. Copy the complete directory, including its resources. Inspect conflicts before replacing an installed skill.

Keep the shared entrypoint free of client-only argument substitutions, dynamic command execution, hard-coded tool names, hidden network operations, or mandatory vendor metadata. Optional client adapters may augment the shared format but cannot be prerequisites. Do not depend on another installed skill unless it is genuinely necessary and available. State a missing tool clearly instead of claiming its output.

## Acceptance

The description must make selection reliable. The body must be useful after activation. Resource links must resolve after independent installation. A format validator confirms syntax and naming, not factual quality or successful behavior. Keep researched details maintainable and recheck volatile claims before use. Consult [the source notes](references/sources.md) for specification and client documentation.

## License

[MIT license and copyright notice](LICENSE.md).
