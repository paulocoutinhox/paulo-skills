#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo 'Usage: bash scripts/install-skills.sh <codex|claude> [skill-name|all] [--destination directory]'
}

if [ "$#" -eq 0 ]; then
  usage >&2
  exit 2
fi

client="$1"
shift

case "$client" in
  codex) destination="$HOME/.agents/skills" ;;
  claude) destination="$HOME/.claude/skills" ;;
  --help|-h) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

selection=all

if [ "$#" -gt 0 ] && [ "$1" != '--destination' ]; then
  selection="$1"
  shift
fi

if [ "$#" -gt 0 ]; then
  if [ "$#" -ne 2 ] || [ "$1" != '--destination' ] || [ -z "$2" ]; then
    usage >&2
    exit 2
  fi

  destination="$2"
fi

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
sources=()

if [ "$selection" = all ]; then
  shopt -s nullglob
  sources=("$repository_root"/skills/*/)
else
  if [[ ! "$selection" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo 'Invalid skill name.' >&2
    exit 2
  fi

  sources=("$repository_root/skills/$selection")
fi

if [ "${#sources[@]}" -eq 0 ]; then
  echo 'No skills were found.' >&2
  exit 1
fi

for source in "${sources[@]}"; do
  name="$(basename "$source")"

  if [ ! -f "$source/SKILL.md" ] || [ -L "${source%/}" ]; then
    echo "Not a regular skill directory: $name" >&2
    exit 1
  fi

  if [ -e "$destination/$name" ] || [ -L "$destination/$name" ]; then
    echo "Destination already exists: $destination/$name. Back it up and remove it before reinstalling." >&2
    exit 1
  fi
done

mkdir -p "$destination"

for source in "${sources[@]}"; do
  name="$(basename "$source")"
  cp -R "${source%/}" "$destination/$name"
  echo "Installed $name into $destination/$name"
done
