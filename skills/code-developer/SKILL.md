---
name: code-developer
description: Implement and refactor production code and technical documentation with explicit behavior, readable structure, current architecture guidance, and language-specific standards. Use for development tasks in existing or new repositories, including Python, Swift, Kotlin, C++, Rust, Lua, Markdown, JavaScript, TypeScript, Vue, React, and Angular.
license: MIT
---

# Code Developer

Edit the actual source files and complete the requested behavior. Apply [the general engineering contract](references/general.md) and read only the profiles for languages and frameworks being changed.

| Target | Required profile |
| --- | --- |
| Python | [Python](references/python.md) |
| Swift and Apple apps | [Swift](references/swift.md) |
| Kotlin and Android | [Kotlin](references/kotlin.md) |
| C++ | [C++](references/cpp.md) |
| Rust | [Rust](references/rust.md) |
| Lua | [Lua](references/lua.md) |
| Markdown documentation | [Markdown](references/markdown.md), plus the relevant language profile for changed code examples |
| JavaScript or TypeScript | [JavaScript and TypeScript](references/javascript-typescript.md) |
| Vue | [Vue](references/vue.md), plus JavaScript or TypeScript |
| React | [React](references/react.md), plus JavaScript or TypeScript |
| Angular | [Angular](references/angular.md), plus TypeScript |
| Another language | [Adding a language profile](references/other-languages.md), then research that language before implementing |

## Workflow

1. Read repository instructions and inspect the current architecture, manifests, toolchain, call sites, and tests. Establish the required language standard, platform, and supported runtime.
2. Identify the intended final behavior and affected consumers. Follow existing coherent architecture. For a new Swift or Android application with no architecture, select MVVM with separate models, views, and view models.
3. Create or update root `AGENTS.md` using [the project guidance template](assets/agents-template.md). Describe the current purpose, capabilities, structure, architecture, commands, and rules. Do not append implementation history.
4. Implement directly. Refactor affected callers to the new final contract. Remove superseded code, compatibility branches, and dead paths within the requested scope. Do not retain legacy behavior by default.
5. Keep functions easy to scan and debug. Separate different responsibilities with blank lines. Use descriptive intermediate variables and early returns. Extract a helper only for meaningful shared support logic.
6. Validate impact beyond changed lines: callers, schemas, state, persistence, permissions, lifecycle, concurrency, packaging, and deployment. Run the relevant formatter, linter, compiler, and behavioral checks.
7. Report the result, integration changes, checks actually executed, and material limitations. Never claim that tests guarantee the absence of memory, concurrency, or security defects.

Use current compatible dependencies for new work unless the user pins versions. Check official sources before choosing versions. Respect the repository's target standard and lockfile. Never silently upgrade the whole dependency tree or rewrite unrelated modules. Ask when a missing decision changes the public contract or risks data loss. Sources and distinctions between user conventions and language requirements are in [source notes](references/sources.md).

## License

[MIT license and copyright notice](LICENSE.md).
