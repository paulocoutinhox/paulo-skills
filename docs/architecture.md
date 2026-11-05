# Architecture and authoring

Each of the twelve directories under `skills/` is independently distributable. Its `SKILL.md` contains portable discovery metadata and workflow instructions. Detailed guidance stays in its own `references/`, reusable output templates in `assets/`, and deterministic helpers in `scripts/` where needed.

The collection uses only shared frontmatter fields in its entrypoints. No client-specific runtime, dynamic command injection, mandatory model ID, or cross-skill dependency is required. Runtime tools and authorization still belong to the client and the user's task. Compatible formatting does not make every client expose identical capabilities.

## Main boundaries

- Skill authoring owns format and maintenance. The repository's `AGENTS.md` owns contributor architecture and commands.
- Code development owns implementation. Code review owns read-only assessment unless fixes are separately requested. Security audit owns deeper trust-boundary analysis when requested.
- Git owns branch and commit preparation. It does not infer permission to push, force-rewrite, or publish.
- Library skills own package implementation and CI preparation. Registry trust and publication remain explicit external account actions.
- Social copy and thumbnail skills prepare artifacts. They do not infer permission to post them.
- Book production separates reader navigation from printer-specific manufacturing requirements and white interior layout from cover artwork.

## Extending a skill

Research first. Update the relevant source note, workflow, references, templates, helper behavior, usage guide, and checks as needed. Remove obsolete instructions and resources. Keep every required resource inside the skill and linked from the entrypoint. Do not duplicate lengthy rules in the README.

Add new language or platform references only when a real task warrants them. State which rules are official requirements, chosen conventions, recommendations, or unresolved. Avoid presenting a preferred architecture as the only valid industry practice.

## Collection tooling

`scripts/install-skills.sh` preflights names and destination collisions before copying complete directories. `scripts/validate-skills.sh` invokes the official validator for every immediate skill directory. `scripts/check-repository.py` verifies packaging and local documentation links. Tests exercise utility boundaries in temporary directories. CI uses the same commands and no model execution.

The dependency lock records the exact `skills-ref` revision and tool versions. The SVG logo is editable source under `extras/images/`. The `.github/` folder follows the project's existing hosting conventions with validation, issue forms, a PR template, a release template, funding, and dependency updates.
