# Authoring and maintenance

## Discovery

Collect a representative request and the output a user would accept. Identify which inputs can come from repository context and which need questions. Describe explicit assumptions. Exclude adjacent capabilities when otherwise likely to trigger incorrectly. A thumbnail skill creates an image. It should not publish a social campaign just because both involve social media.

## Research record

For each consequential external rule, keep a primary source URL, access date, applicable mode or version, and the decision it supports. Record inaccessible material as inaccessible. When sources disagree, prefer the source for the exact target surface or account and disclose the conflict. Do not turn a recommendation into an official requirement. Do not reproduce paid or copyrighted standards in full.

## Instruction design

Lead with the outcome. Route by the user's selected mode. Describe required inputs, meaningful defaults, validation, failure handling, output names, and completion checks. Prefer action verbs and concrete acceptance conditions over persona claims. Explain when to read a reference. Do not load every language or platform manual for a narrow task.

Use a script when numeric rules, parsing, export limits, or repeated transformations benefit from deterministic handling. Give the command, input schema, dependency installation, error cases, and output location. Fail explicitly on invalid inputs. Keep outputs separate from source assets. Do not overwrite user files silently. Run the script before claiming it works.

Templates must be usable starting points. Clearly mark values the user needs to supply, and make the workflow replace them before release. Do not publish unresolved template tokens as a finished implementation. Keep executable examples safe to inspect without contacting production systems.

## Evaluation

| Scenario | Observable acceptance |
| --- | --- |
| Normal task | Produces the requested artifact with correct structure and mode. |
| Missing decisive input | Asks a focused question and continues independent work when useful. |
| Out-of-scope request | Does not apply unrelated procedures or mutate unrelated files. |
| Boundary | Handles exact size, page, character, permission, or path boundaries. |
| Missing dependency | Names the missing dependency and does not fabricate execution. |
| Failure | Returns actionable diagnostics and preserves existing user artifacts. |
| Update | Preserves relevant resources and replaces superseded instructions. |

Use independent evaluation only when available and authorized. Never make delegation a mandatory capability of a portable skill. Keep fixture files temporary and avoid live publication during evaluations.

## Maintenance

Change the source of truth once, then update routes, templates, documentation, and checks that depend on it. Remove broken links and unused files. Revalidate every affected skill. Keep architecture guidance current rather than appending a change diary. Avoid adding permanent global rules for isolated failures that a narrow correction can solve.
