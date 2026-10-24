#!/usr/bin/env bash
set -euo pipefail

replace=false
if [[ $# -gt 1 ]]; then
  printf 'Usage: %s [--replace]\n' "$0" >&2
  exit 2
fi
if [[ ${1:-} == '--replace' ]]; then
  replace=true
elif [[ $# -eq 1 ]]; then
  printf 'Usage: %s [--replace]\n' "$0" >&2
  exit 2
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_source="$repo_root/.agents/skills/florence-notify"
codex_home="${CODEX_HOME:-$HOME/.codex}"
skills_dir="$codex_home/skills"
destination="$skills_dir/florence-notify"

if [[ ! -f "$skill_source/SKILL.md" ]]; then
  printf 'Skill source not found: %s\n' "$skill_source" >&2
  exit 1
fi

if [[ -e "$destination" || -L "$destination" ]]; then
  if [[ -d "$destination" ]] && diff -qr "$skill_source" "$destination" >/dev/null 2>&1; then
    printf 'Already installed and up to date: %s\n' "$destination"
    exit 0
  fi
  if [[ "$replace" != true ]]; then
    printf 'An existing skill differs at %s\n' "$destination" >&2
    printf 'Review it first, then rerun with --replace to overwrite it.\n' >&2
    exit 1
  fi
  rm -rf "$destination"
fi

mkdir -p "$skills_dir"
cp -R "$skill_source" "$destination"
printf 'Installed florence-notify for Codex: %s\n' "$destination"
