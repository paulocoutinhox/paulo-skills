# Sources

Verified: 2026-11-05.

- [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/): OIDC identity, minimum client versions, hosted-runner support, current allowed-action configuration, and provenance conditions.
- [npm trust CLI](https://docs.npmjs.com/cli/v11/commands/npm-trust/): current administrative interface, subject to authentication and ownership.
- [Package manifest](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/): exports, files, engines, dependency metadata, and publication configuration.
- [npm pack](https://docs.npmjs.com/cli/v11/commands/npm-pack/): package archive inspection.
- [GitHub workflow security](https://docs.github.com/en/actions/reference/security/secure-use): least permissions, pinned actions, and untrusted input.

The archive smoke-test script, release version policy, protected tags, and direct-publish selection must be implemented for the actual project. The template does not configure a registry account or create package ownership.
