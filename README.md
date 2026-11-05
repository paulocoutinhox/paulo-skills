<p align="center">
  <a href="https://github.com/paulocoutinhox/paulo-skills">
    <img width="560" src="extras/images/logo.svg" alt="Paulo Skills">
  </a>
</p>

<p align="center">
  <a href="https://github.com/paulocoutinhox/paulo-skills/actions/workflows/validate.yml"><img src="https://github.com/paulocoutinhox/paulo-skills/actions/workflows/validate.yml/badge.svg" alt="Validate"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-compatible-14b8a6" alt="Agent Skills compatible"></a>
  <img src="https://img.shields.io/badge/skills-12-2563eb" alt="12 skills">
</p>

<p align="center">
Researched, reusable workflows for building software, creating publications, and preparing social content.
</p>

<br>

## 🚀 Project

Paulo Skills is a collection of **12 independent skills in English** using the shared
[Agent Skills format](https://agentskills.io/specification). Each skill combines a focused `SKILL.md`
with the references, templates, or utilities its work needs. Copy one skill or install the collection
into Codex, Claude Code, or another compatible client.

The instructions distinguish official requirements, selected working defaults, and recommendations.
Platform limits and print specifications include verification notes and must be checked for the exact
job before publication. These skills prepare and validate work. External publication follows the
user's authorization.

## ✨ Skills

| Skill | What it does | Guide |
| --- | --- | --- |
| `skill-creator` | Research, author, update, and validate portable skills. | [Usage](docs/skill-creator.md) |
| `book-creator` | Typeset books and A4 workbooks, prepare white-page interiors and complete cover packages. | [Usage](docs/book-creator.md) |
| `code-developer` | Implement clear production code and documentation, including Rust, Lua, and Markdown profiles. | [Usage](docs/code-developer.md) |
| `git` | Prepare branches and one reviewed commit with task-aware naming. | [Usage](docs/git.md) |
| `npm-library` | Build and test npm libraries with automatic OIDC publication. | [Usage](docs/npm-library.md) |
| `pypi-library` | Build and test Python distributions with automatic trusted publication. | [Usage](docs/pypi-library.md) |
| `social-post` | Fill publishing fields for YouTube, Shorts, TikTok, Instagram, X, and LinkedIn. | [Usage](docs/social-post.md) |
| `social-thumbnail` | Generate readable thumbnail artwork and checked export derivatives. | [Usage](docs/social-thumbnail.md) |
| `editor-config` | Configure editing conventions for the repository's actual file types. | [Usage](docs/editor-config.md) |
| `git-ignore` | Exclude private and generated files while preserving source and lockfiles. | [Usage](docs/git-ignore.md) |
| `code-review` | Review changes and trace their impact across the system. | [Usage](docs/code-review.md) |
| `security-audit` | Assess web, API, mobile, desktop, authorization, and delivery risks. | [Usage](docs/security-audit.md) |

## 📦 Install

Clone the repository:

```bash
git clone https://github.com/paulocoutinhox/paulo-skills.git
cd paulo-skills
```

Install all skills for one client:

```bash
bash scripts/install-skills.sh codex
bash scripts/install-skills.sh claude
```

| Client | User installation | Project installation |
| --- | --- | --- |
| Codex | `~/.agents/skills/` | `.agents/skills/` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |

Install one skill or choose a project destination:

```bash
bash scripts/install-skills.sh codex code-review
bash scripts/install-skills.sh claude book-creator --destination /path/to/project/.claude/skills
```

The installer copies complete skill directories and refuses existing destinations. For an update,
review the new version, back up the installed directory, remove that exact old copy, and reinstall.
Existing same-name system skills can also affect selection. See [installation](docs/installation.md)
for manual copying, updates, naming conflicts, and verification.

## 💡 How to use

In Codex, mention a skill with `$skill-name`. In Claude Code, use `/skill-name`. Compatible clients can
also select skills when a request matches their descriptions. Client-specific invocation behavior is
documented in the [Codex guide](https://learn.chatgpt.com/docs/build-skills) and
[Claude Code guide](https://code.claude.com/docs/en/skills).

```text
$code-developer Implement account deletion in this repository and validate affected consumers.
$book-creator Create an A4 workbook for print and digital delivery from this manuscript.
$social-post Prepare YouTube, Instagram, X, and LinkedIn copy for this product demo.
$security-audit Review tenant isolation across the API, file downloads, exports, and background jobs.
```

Use `/code-developer`, `/book-creator`, or the corresponding slash name in Claude Code. Provide the
actual repository, manuscript, transcript, or brief. The skills ask for decisions that affect the result
and load only the references relevant to the chosen language, platform, or output.

## ✅ Validate locally and in CI

Install [uv](https://docs.astral.sh/uv/) and Python 3.11 or later, then run:

```bash
uv sync --locked
uv run --locked bash scripts/validate-skills.sh
```

The script uses the official **skills-ref** validator and the same command on every skill locally and
in GitHub Actions:

```bash
for skill in skills/*/; do
  skills-ref validate "$skill" || exit 1
done
```

The upstream revision and resolved tooling dependencies are pinned in `pyproject.toml` and `uv.lock`.
CI runs on every push and pull request. It also checks local links and resource packaging, Python lint
and formatting, shell/JavaScript syntax, and meaningful utility behavior. It uses no model or model API
credentials. Format validation checks the skill structure and metadata. It does not certify domain
accuracy or model behavior. Installed validation works offline. Initial dependency installation needs
network access.

Run all repository checks as described in [validation](docs/validation.md).

## 🧱 Organization

```text
skills/       Portable skill directories and their own resources
docs/         Installation, architecture, research policy, and per-skill usage
scripts/      Collection installer and validation commands
tests/        Utility behavior and boundary checks
extras/       Editable vector logo and project assets
.github/      CI, dependency updates, and contribution templates
AGENTS.md     Current authoring, architecture, and development contract
```

Resources are kept inside their skill so individual installation remains useful. A skill does not
need empty `references/`, `scripts/`, or `assets/` directories just to match a diagram.

## 📚 Documentation

- [Installation and updates](docs/installation.md)
- [Architecture and authoring](docs/architecture.md)
- [Validation and CI](docs/validation.md)
- [Research method, sources, and limitations](docs/research.md)
- Per-skill usage guides in the catalog above

## 🤝 Contributing

Read [AGENTS.md](AGENTS.md), research current primary documentation, keep the shared format portable,
and validate changed behavior. Add a usage guide and update the catalog when adding a skill. Keep
commits concise, use the real author, and omit generated attribution and co-author trailers.

## ☕ Buy me a coffee

Support the continuous development of this project.

<a href="https://ko-fi.com/A0A412XEV"><img height="36" src="https://storage.ko-fi.com/cdn/kofi2.png?v=6" alt="Buy Me a Coffee at ko-fi.com"></a>

## 📄 License

[MIT](LICENSE.md)

Copyright (c) 2026, Paulo Coutinho

---

Made with ❤️ by [Paulo Coutinho](https://github.com/paulocoutinhox)
