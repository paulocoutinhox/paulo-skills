# PyPI Library

Build tested Python distributions and automate token-free publication.

## Invoke

Codex:

```text
$pypi-library Create a Python library for this API using uv and Ruff, with tested wheel/sdist artifacts and automatic PyPI trusted publishing.
```

Claude Code uses `/pypi-library` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Supply distribution/import names, API, license, repository, supported Python version, and version policy.
- Choose production or a separately configured TestPyPI rehearsal.
- Provide registry ownership and the trusted-publisher tuple or identify pending setup.

## What happens

The skill builds an explicit source layout with empty initializers, validates metadata, tests both distribution types in clean consumers, and separates read-only build work from OIDC publication.

## Deliverables

Library code, pyproject/lockfile, usage documentation, wheel/sdist smoke test, release workflow, and actual setup/validation status.

## Decisions and limits

The template expects a release dependency group and a meaningful tests/smoke-distribution.py. A pending publisher can create a new project but does not reserve its name. Real publication needs authorization and configured registry trust.

## Detailed instructions

Read [the portable skill](../skills/pypi-library/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
