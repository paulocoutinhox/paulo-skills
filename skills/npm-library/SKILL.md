---
name: npm-library
description: Create or modernize a Node.js npm library with explicit package exports, packed-artifact tests, and automatic CI publication through OIDC trusted publishing. Use when building a publishable npm package or replacing token-based release automation.
license: MIT
---

# npm Library

Implement a complete library and a release path that publishes from CI without a standing write token or per-release manual registry login. Read [package design](references/package-design.md) and [trusted publication](references/publishing.md).

1. Determine package name and scope, registry, repository, supported Node/browser targets, module system, public API, license, version strategy, and release trigger. Inspect current manifests and lockfiles.
2. Build the actual API and documentation. For a new package, prefer one current ESM contract unless another module target is explicitly required. Use compatible stable dependencies and the requested runtime target.
3. Define the publishable file allowlist, explicit exports, entrypoint types, runtime dependencies, and repository metadata. Keep credentials and private files outside the package.
4. Run lint, type checking, behavioral tests, and build. Create the actual tarball with `npm pack`, inspect its contents, and run a consumer smoke test against that tarball in an isolated directory.
5. Adapt [the release workflow template](assets/publish.yml) to the target repository. Implement every command it calls. Pin action revisions and the selected toolchain. Do not copy an incomplete workflow and claim it is ready.
6. Configure the exact registry trusted publisher: repository owner, repository name, workflow filename, optional environment, and allowed publish action. Use an existing authenticated administrative path only when authorized. Otherwise provide the precise one-time setup fields and state the dependency.
7. Verify that the release tag matches package metadata, the version is new, the publish job has `id-token: write`, and no fallback publishing token is configured. Build and test without registry write permission, then publish only the reviewed artifact in a separate job.
8. Deliver code, package documentation, tested tarball contents, CI configuration, publisher setup status, and the expected automated release behavior. Run a real publication only if the task authorizes it.

A first-time trust configuration, package namespace ownership, and account security setup may require the owner's authenticated session. Do not claim that a repository file alone configures registry trust or that every new package can bootstrap identically. After that setup, releases must not require an OTP, copied API token, or manual approval unless the user selected such protection. See [sources](references/sources.md).

## License

[MIT license and copyright notice](LICENSE.md).
