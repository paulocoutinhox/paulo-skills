# Code Developer

Implement the final requested behavior in the actual repository and validate its consumers.

## Invoke

Codex:

```text
$code-developer Implement this issue directly. Follow the Python profile, update AGENTS.md, and validate affected callers.
```

Claude Code uses `/code-developer` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Provide the repository and desired behavior, with examples or acceptance criteria.
- State required language/runtime versions or public contract constraints.
- Use an existing architecture when coherent. A new Swift or Android application defaults to MVVM when no architecture exists.

## What happens

The skill reads project instructions and relevant language profiles, updates current architecture guidance, implements explicit behavior with readable responsibility blocks, removes superseded code within scope, and verifies integration.

## Deliverables

Edited source, current AGENTS.md, affected documentation where needed, and a factual validation report.

## Decisions and limits

Profiles cover Python, Swift, Kotlin, C++, Rust, Lua, Markdown, JavaScript/TypeScript, Vue, React, and Angular. Other languages require current official research. Owner preferences are separate from language requirements. Data destruction or external release is not implied by refactoring.

- [Rust](../skills/code-developer/references/rust.md): Cargo and toolchain constraints, ownership, errors, unsafe boundaries, concurrency, and workspace verification.
- [Lua](../skills/code-developer/references/lua.md): interpreter/host selection, modules, table and false/nil behavior, resources, and compatible static tooling.
- [Markdown](../skills/code-developer/references/markdown.md): dialect selection, document structure, links, code examples, metadata, and rendered-output checks.

## Detailed instructions

Read [the portable skill](../skills/code-developer/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
