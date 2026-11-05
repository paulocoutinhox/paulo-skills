---
name: pypi-library
description: Create or modernize a Python library with uv, Ruff, explicit packaging metadata, tested wheel and source distributions, and automatic PyPI publication through OIDC trusted publishing. Use for Python package authoring and token-free CI release workflows.
license: MIT
---

# PyPI Library

Implement a usable Python library and fully automated CI publication after the registry trust relationship is established. Read [packaging](references/packaging.md) and [publishing](references/publishing.md).

1. Determine distribution and import names, supported Python version, API, license, registry, repository, version source, and release trigger.
2. Implement the library using a focused source layout and modern `pyproject.toml` metadata. Use uv for dependencies and Ruff for formatting and lint. Keep every `__init__.py` completely empty and avoid `TYPE_CHECKING` imports.
3. Test real behavior and public module imports. Build both the source distribution and wheel, inspect their contents, validate metadata, and install the built artifacts into isolated consumers.
4. Adapt [the release workflow](assets/publish.yml). Pin actions and tooling. Implement every referenced test command and release dependency group. Validate that the release tag matches the actual package version.
5. Configure the exact trusted publisher. For an unpublished project, use a supported pending publisher to create the project at first publication. TestPyPI and production are separate identities and registries.
6. Build without registry write capability. Publish only the validated distributions from a dedicated job with `id-token: write`. Keep long-lived upload tokens out of the workflow.
7. Deliver source, documentation, build and install evidence, CI, publisher setup status, and expected automated release behavior. Actual publication requires task authorization.

One-time account ownership and trust setup may require an authenticated owner. Do not claim repository YAML configures the registry by itself. After setup, routine releases must not require copying credentials or manually uploading packages. Consult [sources](references/sources.md) for supported flows.

## License

[MIT license and copyright notice](LICENSE.md).
