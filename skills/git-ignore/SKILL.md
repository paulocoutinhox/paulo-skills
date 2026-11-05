---
name: git-ignore
description: Create or audit a repository .gitignore for its languages and tools, excluding private local configuration, credentials, caches, builds, logs, virtual environments, and runtime output while preserving required source and reproducibility files. Use when configuring ignore rules or investigating accidentally tracked artifacts.
license: MIT
---

# Git Ignore

Inspect the actual repository and its tracked, untracked, and ignored paths. Use [the base template](assets/gitignore) and add only applicable [stack-specific patterns](references/stacks.md). Read [pattern and privacy rules](references/rules.md) before modifying tracked files.

1. Identify languages, build systems, package managers, editors, test outputs, runtime directories, deployment configuration, and local credentials.
2. Create or update `.gitignore` directly. Use scoped rules for real generated or sensitive paths. Prefer useful patterns over blindly concatenating every ecosystem template.
3. Preserve source assets, migrations, lockfiles, sanitized configuration examples, wrapper scripts, shared project settings, and explicitly versioned distribution artifacts where the repository requires them.
4. Validate representative paths with `git check-ignore -v --no-index -- <path>`. Check negative cases that must remain tracked as well as positive ignored cases.
5. Inspect already tracked generated or private paths separately. Ignore rules do not untrack files. Explain the issue and remove only authorized paths from the index when requested.
6. Review the final staged file list. Run the project's configured secret scan if available, without printing secret values. Report what was excluded and any actual tracked exposure requiring remediation.

Do not promise that ignore rules prevent every leak. They do not stop `git add -f`, remove history, redact logs, or protect secrets embedded in source. Credential rotation and history cleanup are separate authorized actions. Consult [sources](references/sources.md).

## License

[MIT license and copyright notice](LICENSE.md).
