---
name: security-audit
description: Audit web, API, mobile, and desktop code for authorization, tenant isolation, authentication, injection, data exposure, storage, cryptography, native-memory, platform, dependency, and CI security defects. Use for a requested security assessment or hardening review of the full application or a defined change.
license: MIT
---

# Security Audit

Assess the actual trust boundaries and reachable behavior. Cover the whole requested scope, including unchanged consumers and deployment paths, rather than scanning only the diff. Do not claim an exhaustive absence of vulnerabilities.

## Workflow

1. Establish the authorized repository/application scope and available test environment. Inspect architecture, entrypoints, identities, tenants, assets, data flows, dependencies, storage, build, and release paths. Read [the assessment procedure](references/procedure.md).
2. Map every protected operation to its authoritative authorization boundary. Read [authorization and isolation](references/authorization.md) for all connected applications, regardless of client platform.
3. Read the relevant platform catalogs: [web and API](references/web-api.md), [mobile](references/mobile.md), and [desktop/native](references/desktop.md). Read [delivery and operational security](references/operations.md) for dependency, secrets, CI, and runtime risks.
4. Trace input from its entrypoint to sensitive sinks, and sensitive output to its reader. Check negative paths, alternate endpoints, batch operations, files, exports, jobs, and subscriptions.
5. Use static analysis, dependency and secret scans, focused tests, and controlled runtime probes where available and authorized. A scanner result is evidence, not a complete verdict. Do not send private code externally without authorization or test a live target destructively.
6. Verify findings with a concrete trigger, affected source, prerequisites, impact, and a minimal safe reproduction or static proof. Record uncertainty explicitly. Prioritize actual risk.
7. If fixes are requested, implement the authoritative control, migrate affected paths, and add meaningful regression checks. Retest both allowed and denied access and inspect remaining consumers.
8. Deliver [the assessment report](assets/security-report.md) with findings, coverage, checks, remediation priorities, and limitations. Do not publish findings or contact others without authorization.

Prefer opaque public identifiers or slugs over exposing internal sequential keys where the product supports it. Neither opaque identifiers nor slugs replace server-side authorization. Bearer credentials must not be put into ordinary resource URLs. See [source notes](references/sources.md) for standards, versions, and scope distinctions.

## License

[MIT license and copyright notice](LICENSE.md).
