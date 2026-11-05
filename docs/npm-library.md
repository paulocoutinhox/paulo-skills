# npm Library

Build an npm library and automate release publication with trusted identity.

## Invoke

Codex:

```text
$npm-library Create a typed ESM library for this API and a GitHub Actions pipeline that publishes automatically through npm trusted publishing.
```

Claude Code uses `/npm-library` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Supply package name/scope, repository, public API, license, supported runtime, and module target.
- Choose the version source and automated release trigger.
- Provide the exact trusted-publisher identity or identify the required one-time account setup.

## What happens

The skill implements the library, defines explicit exports and publishable files, tests the packed tarball as a consumer, and adapts the pinned CI template with separate build and publish jobs.

## Deliverables

Library source, manifest/lockfile, API documentation, packed-artifact test, release workflow, and publisher-setup status.

## Decisions and limits

The template expects real lint, typecheck, test, build, and test:package commands. New-package bootstrap differs from PyPI. Enable direct publish in current publisher settings when a staging step is unwanted. Do not claim the registry is configured without account evidence.

## Detailed instructions

Read [the portable skill](../skills/npm-library/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
