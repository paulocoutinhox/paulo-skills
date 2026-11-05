#!/usr/bin/env python3
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


class RepositoryCheckHelper:
    ROOT = Path(__file__).resolve().parents[1]
    LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)|(?:src|href)=[\"']([^\"']+)[\"']")
    RESOURCE_PATTERN = re.compile(r"(?:references|assets|scripts)/[a-zA-Z0-9][a-zA-Z0-9./_-]*")
    FENCE_PATTERN = re.compile(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$")

    @classmethod
    def run(cls) -> None:
        failures = []
        skills = sorted(path for path in (cls.ROOT / "skills").iterdir() if path.is_dir())

        if not skills:
            failures.append("No skills were found.")

        for skill in skills:
            entrypoint = skill / "SKILL.md"

            if not entrypoint.is_file():
                failures.append(f"Missing entrypoint: {skill.name}")
                continue

            if len(entrypoint.read_text().splitlines()) >= 500:
                failures.append(f"Entrypoint exceeds the project limit: {skill.name}")

            if not (cls.ROOT / "docs" / f"{skill.name}.md").is_file():
                failures.append(f"Missing usage guide: {skill.name}")

            resources = []

            for path in skill.rglob("*"):
                if path.is_symlink():
                    failures.append(f"Nonportable symlink: {path.relative_to(cls.ROOT)}")

                if path.is_dir() and not any(path.iterdir()):
                    failures.append(f"Empty resource directory: {path.relative_to(cls.ROOT)}")

                if path.is_file() and path.parts[-2] in {"references", "assets", "scripts"}:
                    resources.append(path)

            reachable = set()
            pending = [entrypoint]

            while pending:
                current = pending.pop()

                if current in reachable:
                    continue

                reachable.add(current)

                if current.suffix != ".md":
                    continue

                for match in cls.RESOURCE_PATTERN.finditer(current.read_text()):
                    target = (skill / match.group(0).rstrip("./")).resolve()

                    if target.is_file() and target.is_relative_to(skill.resolve()):
                        pending.append(target)

            for resource in resources:
                if resource.resolve() not in reachable:
                    failures.append(f"Unrouted skill resource: {resource.relative_to(cls.ROOT)}")

        markdown_files = [cls.ROOT / "README.md", cls.ROOT / "AGENTS.md", cls.ROOT / "LICENSE.md"]

        for directory in ["skills", "docs", ".github"]:
            markdown_files.extend((cls.ROOT / directory).rglob("*.md"))

        for document in markdown_files:
            content = document.read_text(encoding="utf-8")

            if "\r" in content or not content.endswith("\n"):
                failures.append(f"Invalid text newline policy: {document.relative_to(cls.ROOT)}")

            link_content = cls.FENCE_PATTERN.sub("", content)

            for match in cls.LINK_PATTERN.finditer(link_content):
                raw = (match.group(1) or match.group(2)).strip().strip("<>")
                parsed = urlsplit(raw)

                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue

                target = (document.parent / unquote(parsed.path)).resolve()

                if not target.is_relative_to(cls.ROOT) or not target.exists():
                    failures.append(f"Broken local link: {document.relative_to(cls.ROOT)} -> {raw}")

                relative_document = document.relative_to(cls.ROOT)

                if relative_document.parts[0] == "skills":
                    skill_root = cls.ROOT / "skills" / relative_document.parts[1]

                    if not target.is_relative_to(skill_root.resolve()):
                        failures.append(f"Skill link escapes its package: {relative_document} -> {raw}")

        if failures:
            raise SystemExit("\n".join(failures))

        print(f"Checked {len(skills)} portable skill packages and {len(markdown_files)} Markdown files.")


if __name__ == "__main__":
    RepositoryCheckHelper.run()
