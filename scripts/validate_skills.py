#!/usr/bin/env python3
"""Validate skill metadata and layout."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, [f"{path}: missing YAML frontmatter"]

    fields: dict[str, str] = {}
    errors: list[str] = []

    for line_number, line in enumerate(match.group(1).splitlines(), start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        field_match = FIELD_RE.match(line)
        if not field_match:
            errors.append(f"{path}:{line_number}: unsupported frontmatter line")
            continue

        key, value = field_match.groups()
        fields[key] = value.strip().strip("'\"")

    return fields, errors


FENCE_RE = re.compile(r"^\s*```")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
TABLE_ROW_RE = re.compile(r"^\s*\|")
DASH_RE = re.compile(r"[\u2013\u2014]")

FLAGGED_WORDS = (
    "abyss actually basically certainly craft delve disruptive elucidate embark "
    "enlightening esteemed furthermore illuminate imagine intricate literally "
    "maybe moreover perhaps pivotal probably realm revolutionize skyrocket "
    "tapestry unveil utilize"
).split()
FLAGGED_PHRASES = [
    "game-changer",
    "best-in-class",
    "world-class",
    "move the needle",
    "circle back",
    "dive deep",
    "in a world where",
    "in closing",
    "in conclusion",
    "shed light",
    "worth noting",
    "not just",
    "not only",
    "not merely",
    "not simply",
]


def prose_lines(text: str):
    """Yield (line_number, line) for prose only.

    Skips frontmatter, fenced code, table rows, and inline code spans. The skill
    files name every flagged term as data inside tables and inline code, so those
    regions must not trip the lint.
    """
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                start = index + 1
                break

    in_fence = False
    for line_number, line in enumerate(lines[start:], start=start + 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence or TABLE_ROW_RE.match(line):
            continue
        yield line_number, INLINE_CODE_RE.sub("", line)


def lint_prose(path: Path) -> list[str]:
    findings: list[str] = []

    for line_number, line in prose_lines(path.read_text(encoding="utf-8")):
        if DASH_RE.search(line):
            findings.append(f"{path}:{line_number}: em or en dash in prose")

        lowered = line.lower()
        for word in FLAGGED_WORDS:
            if re.search(rf"\b{word}\w*\b", lowered):
                findings.append(f"{path}:{line_number}: flagged word '{word}' in prose")
        for phrase in FLAGGED_PHRASES:
            if phrase in lowered:
                findings.append(f"{path}:{line_number}: flagged phrase '{phrase}' in prose")

    return findings


def validate() -> int:
    errors: list[str] = []
    seen_names: dict[str, Path] = {}

    if not SKILLS_DIR.exists():
        print("No skills directory found.")
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("No skills found.")
        return 1

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue

        fields, frontmatter_errors = parse_frontmatter(skill_file)
        errors.extend(frontmatter_errors)

        name = fields.get("name", "")
        description = fields.get("description", "")

        if not name:
            errors.append(f"{skill_file}: missing required field 'name'")
        elif name != skill_dir.name:
            errors.append(
                f"{skill_file}: name '{name}' does not match directory '{skill_dir.name}'"
            )
        elif name in seen_names:
            errors.append(
                f"{skill_file}: duplicate skill name '{name}' also used by {seen_names[name]}"
            )
        else:
            seen_names[name] = skill_file

        if not description:
            errors.append(f"{skill_file}: missing required field 'description'")

        errors.extend(lint_prose(skill_file))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(validate())
