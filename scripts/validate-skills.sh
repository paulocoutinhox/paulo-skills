#!/usr/bin/env bash
set -euo pipefail

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repository_root"

if ! command -v skills-ref >/dev/null 2>&1; then
  echo 'skills-ref is missing. Run uv sync --locked and use uv run --locked.' >&2
  exit 1
fi

shopt -s nullglob
skill_directories=(skills/*/)

if [ "${#skill_directories[@]}" -eq 0 ]; then
  echo 'No skill directories were found.' >&2
  exit 1
fi

for skill in "${skill_directories[@]}"; do
  skills-ref validate "$skill" || exit 1
done
