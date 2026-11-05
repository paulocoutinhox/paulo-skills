# Python

## Layout and dependencies

Use the project's declared Python target. For a new project, verify the current supported stable version and dependency compatibility before pinning it. Use `pyproject.toml`, uv for dependency and environment management, and Ruff for linting and formatting. Use a `src/` layout for distributable packages when appropriate. Commit `uv.lock` for reproducible development. Libraries declare compatible dependency ranges separately from the locked development environment.

Importable module and package names use underscores because hyphens are not valid identifiers. Use one primary class or enum per file. Every `__init__.py` must be completely empty, without comments, docstrings, reexports, version declarations, or initialization code. Put public definitions and version constants in explicit modules. Do not use `TYPE_CHECKING` or `if TYPE_CHECKING`. Resolve import cycles by correcting dependencies and separating shared types. Use supported deferred or quoted annotations when needed by the selected runtime.

## Implementation

Use type annotations for meaningful interfaces. Prefer dataclasses or ordinary classes for explicit state and immutable value objects when appropriate. Avoid broad `Any`, mutable default arguments, global mutable configuration, dynamic imports, wildcard imports, and runtime annotation tricks. Use `pathlib`, context managers, parameterized database queries, and explicit text encodings. Keep exceptions specific and include useful context without secrets.

Async code must avoid blocking the event loop. Use structured task ownership, propagate cancellation, close clients and generators, and bound concurrency. Offload genuinely blocking work through the chosen framework's supported mechanism. Do not catch `BaseException` to hide cancellation or interpreter exit. Use argument arrays rather than shell concatenation for subprocesses and set timeouts for external operations.

## Tooling

```bash
uv sync --locked
uv run ruff check .
uv run ruff format --check .
uv run python -m unittest discover -s tests
```

Use pytest or a type checker when already adopted or justified by the project. Run tests against installed artifacts for packaging changes. Ruff is a linter and formatter, not a dependency manager or a type checker. Do not add every optional tool automatically.
