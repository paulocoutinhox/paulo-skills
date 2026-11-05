# Installation and updates

Clone this repository and run its installer from any working directory. Bash is required. The skills themselves do not require a permanent running service.

```bash
bash scripts/install-skills.sh codex all
bash scripts/install-skills.sh claude social-post
```

Codex user skills live under `~/.agents/skills/`. Claude Code user skills live under `~/.claude/skills/`. Project installations use `.agents/skills/` and `.claude/skills/` respectively. Choose one destination per command. Installing for one client does not install for the other.

```bash
bash scripts/install-skills.sh codex code-review --destination /absolute/project/.agents/skills
```

For manual installation, copy the entire `skills/<name>/` directory into the chosen skills root, retaining `SKILL.md`, references, scripts, and assets together. Do not copy only the entrypoint. The generic `skills/` directory in this source repository is a catalog, not itself a client discovery location.

## Verify discovery

Use the client's skill selector or explicit invocation. Codex uses `$code-review`, and Claude Code uses `/code-review`. If a changed installation does not appear, refresh the client or restart its session according to its current documentation. A client can already provide a same-name skill, particularly `skill-creator`, `code-review`, or `git`. Inspect the actual selected path and client name-resolution behavior. The installer refuses a conflicting local destination rather than overwriting it.

## Updates and removal

Fetch the desired repository revision through your normal Git workflow. Inspect its changes and validation results. Back up the existing installed skill directory outside the discovery root, remove only that exact installed copy, and reinstall it. Keeping two copies with the same metadata name can make discovery ambiguous. Do not rename only the folder: the frontmatter name must continue to match it.

To uninstall, remove only the installed skill directory you selected. This does not remove generated user artifacts or revoke registry permissions configured while using a publishing skill.

## Dependencies

Most instructions need only the tools appropriate to the user's task. The cover-geometry and general text-count scripts use Python 3.11+ standard libraries. Thumbnail export additionally uses Pillow, installable through its inline uv metadata. Weighted X validation uses Node and `twitter-text`. Book typesetting needs a real supported renderer and selected fonts. Registry publication needs account ownership and a one-time trusted-publisher configuration.

The installer does not install these optional tools, execute the skills, configure registries, or publish content. See [validation](validation.md) for the repository's development environment.
