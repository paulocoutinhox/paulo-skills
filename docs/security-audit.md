# Security Audit

Assess actual trust boundaries across web, API, mobile, desktop, and delivery paths.

## Invoke

Codex:

```text
$security-audit Audit the application for cross-user and cross-tenant access, including lists, mutations, files, exports, caches, jobs, and subscriptions.
```

Claude Code uses `/security-audit` with the same task details. Install the full skill directory first using [the installation guide](installation.md).

## Supply

- Provide the authorized repository/application scope and available controlled environment.
- Describe identities, tenants, privileged operations, sensitive assets, and platform targets.
- State whether remediation is requested or the work is assessment-only.

## What happens

The skill maps actors and boundaries, reads applicable catalogs, traces input to sensitive operations and output to readers, runs authorized checks, and verifies findings with concrete scenarios.

## Deliverables

Risk-prioritized report with code locations, prerequisites, evidence, controls, covered areas, checks, and material limitations.

## Decisions and limits

Opaque identifiers and slugs do not replace authorization. Bearer tokens do not belong in ordinary resource URLs. Standards are versioned and have distinct scopes. The result is an assessment, not proof that every vulnerability is absent.

## Detailed instructions

Read [the portable skill](../skills/security-audit/SKILL.md) for the workflow and links to its references, templates, helpers, and source notes. Supporting resources stay inside the skill so copying it independently preserves the guidance.
