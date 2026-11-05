# Validation and CI

Use Python 3.11+ and uv. CI currently selects Python 3.13 and pins uv 0.12.19. The locked environment contains `skills-ref`, Ruff, and the small dependencies used to test export and configuration behavior.

```bash
uv sync --locked
uv run --locked bash scripts/validate-skills.sh
uv run --locked python scripts/check-repository.py
uv run --locked python -m unittest discover -s tests -v
uv run --locked ruff check .
uv run --locked ruff format --check .
bash -n scripts/install-skills.sh
bash -n scripts/validate-skills.sh
node --check skills/social-post/scripts/count-x.cjs
```

GitHub Actions runs these checks on every push and pull request. The validator installation is reproducible through `uv.lock` and an immutable upstream Git revision. Dependency installation needs network access. Once dependencies are installed, the validation loop itself does not make network or model calls.

## Reference validator

The canonical invocation is `skills-ref validate <skill-directory>`. The collection wrapper enumerates every immediate directory under `skills/`, errors if there are none, and stops at the first validation failure. The same wrapper is used locally and in CI. It does not substitute a custom frontmatter checker for the reference validator.

For an independent upstream installation:

```bash
git clone https://github.com/agentskills/agentskills.git /tmp/agentskills
cd /tmp/agentskills/skills-ref
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
skills-ref validate /absolute/path/to/paulo-skills/skills/book-creator
```

For exact parity with this repository, check out the revision declared in `pyproject.toml` before installing. The upstream tool is a reference implementation, not a guarantee that a skill's domain instructions are correct or that an agent will follow them.

## Behavioral checks

Tests cover installation collision protection, independent copies, path validation, text counting across encodings, cover geometry, invalid numeric inputs, JPEG dimensions and proportions, byte-limit failures, source preservation, and relevant EditorConfig and Git ignore behavior. They use temporary fixtures and do not publish packages or social content.

The JavaScript syntax check does not execute X weighting. That optional helper requires `twitter-text`, as documented in its skill. Production renderer checks, platform account limits, registry trust, and real model behavior require task-specific verification beyond repository CI.
