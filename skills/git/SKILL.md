---
name: git
description: Organize Git branches, stage reviewed files, and create one concise commit using an existing issue identifier or conventional prefixes. Use when preparing a branch, commit, or Git delivery and checking that temporary files and secrets are excluded.
license: MIT
---

# Git

Prepare a clear, reviewable Git delivery with the real configured author and no generated attribution. Read [the workflow and naming rules](references/workflow.md).

1. Inspect repository instructions, `git status --short --branch`, remotes, the current branch, and the relevant diff. Preserve unrelated work.
2. Determine whether a GitHub, Bitbucket, or other task identifier exists in the request, branch, or linked task. If unknown, ask once. Do not invent one.
3. Use `<IDENTIFIER>-<short-lowercase-description>` for a task branch and `<IDENTIFIER> <short lowercase action>` for its commit. Preserve the exact identifier, including uppercase letters. Otherwise use `<type>-<short-description>` and `<type>: <short lowercase action>`.
4. Run relevant checks. Inspect untracked, ignored, generated, and sensitive files before staging. Check builds, logs, local credentials, caches, test output, archives, and runtime state.
5. Stage only the paths belonging to this delivery. Inspect `git diff --cached --stat`, `git diff --cached --check`, and the complete staged diff. Verify the staged set contains no unrelated files or private material.
6. Create one commit unless the user explicitly requests a different arrangement. Use the configured human author. Do not add co-author trailers, tool or agent names, source references, or generated-by footers.
7. Report the commit hash, subject, checks, and remaining working-tree state. Push or publish only when the task authorizes it.

If the Git directory is not writable, request the required execution permission. Do not work around permissions by moving Git metadata elsewhere. Never reset, clean, rewrite published history, force-push, or remove user changes as routine cleanup. A `.gitignore` does not remove already tracked files or erase leaked history. Read [the sources](references/sources.md) when Git semantics are uncertain.

## License

[MIT license and copyright notice](LICENSE.md).
