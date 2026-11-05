# Paulo Skills

## Purpose and current architecture

This repository distributes twelve independent Agent Skills in English for Codex, Claude Code, and other clients implementing the Agent Skills format. It contains instructions, reusable references, templates, and a small set of deterministic utilities. It is not an application, a model runtime, or a package publishing service.

## Repository map

- `skills/<skill-name>/SKILL.md` is the portable entrypoint for one capability.
- `skills/<skill-name>/references/` contains detailed guidance loaded only for the relevant task.
- `skills/<skill-name>/assets/` contains templates copied into user projects.
- `skills/<skill-name>/scripts/` contains deterministic, documented utilities.
- `docs/` contains installation, architecture, research policy, and one usage guide per skill.
- `extras/images/logo.svg` is the editable vector brand asset.
- `scripts/` contains repository installation and validation utilities.
- `tests/` checks utility behavior and safety boundaries using temporary directories.
- `.github/` contains validation CI, contribution templates, funding, and dependency updates.

## Authoring contract

Use the shared Agent Skills specification. Every skill directory must contain `SKILL.md` with YAML frontmatter containing `name` and `description`. The name matches the directory, uses lowercase ASCII letters, digits, and single hyphens, and is at most 64 characters. The description states the capability and activation conditions, is nonempty, and is at most 1,024 characters. Use only standard frontmatter for portable entrypoints. Optional standard fields must satisfy the specification. Client-specific metadata is optional and must never be required for the workflow.

Keep the entrypoint focused on routing, workflow, decisions, constraints, and delivery criteria. Keep it below 500 lines and preferably below 5,000 tokens. These are project limits and specification recommendations, not additional mandatory format fields. Link every reference, script, and template from the entrypoint. Do not create empty directories or placeholder files. A skill must work when copied independently. Never link outside its directory for required runtime guidance.

Research before creating or materially updating a skill. Prefer current primary documentation. Record links, verification date, applicability, and unresolved limitations in a source reference. Explain conflicts instead of silently mixing incompatible requirements. Separate official requirements, project conventions, and recommendations. Do not copy entire standards, manuals, prompts, or third-party source files. Recheck volatile platform limits, registry requirements, tool versions, and print templates before operational use. Never describe inaccessible documentation as verified.

## Creating and updating skills

1. Identify the user outcome, inputs, exclusions, authorization boundaries, and realistic usage examples.
2. Research the domain and determine which rules are mandatory, configurable, or recommendations.
3. Choose a narrow hyphenated name and a discriminating description.
4. Write the entrypoint. Extract substantial conditional details into focused references.
5. Add templates or executable helpers only when they materially improve repeatability.
6. Document required dependencies, commands, errors, output files, and known limits.
7. Add or update `docs/<skill-name>.md` and the README catalog in the same change.
8. Run `skills-ref` validation and the relevant utility checks. Inspect local links and installability.
9. Review realistic success, missing-input, boundary, and failure scenarios. Format validation does not prove domain correctness.
10. Inspect the final diff and create one concise commit when committing is requested.

Updates describe the final behavior. Remove superseded guidance, unused resources, and conflicting defaults. `AGENTS.md` always describes the present project and never records task history. Do not broaden authorization, auto-publish content, or install into user directories merely because a skill is being authored.

## Code and content conventions

Write instructions, code, identifiers, comments, commit messages, and documentation in English. Use hyphens for filenames unless a language or tool requires another form, such as Python imports, `SKILL.md`, `AGENTS.md`, or GitHub's template filenames. Keep one primary class, enum, component, view, or page per source file. Keep responsibilities visually separated with blank lines. Prefer readable concrete code, explicit errors, early returns, and named intermediate results. Avoid compatibility layers, generic fallbacks, dead code, speculative abstractions, and duplicated processes. Extract a context-specific helper class only when shared support logic warrants it.

Comments are rare, explain necessary intent, use complete English sentences, and end with a period. Do not join prose sentences with semicolons or add decorative section comments. Required syntax, shebangs, formatter directives, and declarative configuration headings are exceptions to prose rules. Python `__init__.py` files remain completely empty. Do not use `TYPE_CHECKING` imports. Use uv for dependencies and Ruff for Python formatting and linting.

Preserve the requested development preferences in the code-developer references. Distinguish them from universal language rules. Do not claim that a slug replaces authorization, a print PNG replaces a required press PDF, an Arial choice is mandated by ABNT, or one spine multiplier fits every paper and binding.

## Commands and verification

```bash
uv sync --locked
uv run --locked bash scripts/validate-skills.sh
uv run --locked python scripts/check-repository.py
uv run --locked python -m unittest discover -s tests -v
uv run --locked ruff check .
uv run --locked ruff format --check .
bash scripts/install-skills.sh codex code-review --destination /tmp/paulo-skills-preview
```

`pyproject.toml` and `uv.lock` pin the validation environment. The `skills-ref` upstream revision is immutable. Local validation and CI call the same `scripts/validate-skills.sh`, which invokes `skills-ref validate` for every immediate skill directory and stops on the first failure. CI must run on every push and pull request, with read-only repository permissions and no model calls or model credentials. Network is required to install tools, not to validate installed skills.

Run only checks warranted by the change. For utility changes, test actual output, invalid inputs, and protection against overwrites. Do not add tests that assert editorial wording or mirror the implementation. Do not claim that CI ran remotely when only local commands ran.

## Git, privacy, and delivery

Use the real configured author. Produce one commit per requested delivery. If a task identifier exists, preserve its exact case and prefix the branch and commit with it. Otherwise use a short lowercase conventional commit and a lowercase hyphenated branch. Do not add co-author trailers, generated-by footers, agent names, research source names, or third-party attribution to commit messages.

Stage only reviewed files. Check the staged diff, ignored files, temporary artifacts, logs, credentials, signing material, personal data, and package archives. Never commit `.venv`, caches, build output, runtime files, or secrets. Keep lockfiles, sanitized examples, source assets, and required wrapper tooling. A `.gitignore` cannot protect an already tracked secret. Never erase unrelated user changes, rewrite published history, push, tag, release, or publish without task authorization. Keep the final report factual about validation and any remaining external setup.
