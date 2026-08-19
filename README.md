# smart-agents

A curated collection of AI agent skills.

## Skills

| Skill | Description |
| --- | --- |
| `refine-text` | Refines, rewrites, proofreads, and edits prose for clarity, accuracy, and directness. |

`refine-text` overlaps the `humanizer` skill where both remove AI markers. Use `refine-text` to edit prose for accuracy, structure, and tone, including work you are drafting. Use `humanizer` when the only goal is stripping AI tells from finished text.

Each skill lives in `skills/<skill-name>/SKILL.md` and starts with YAML frontmatter:

```yaml
---
name: skill-name
description: Short trigger-oriented description.
---
```

## Structure

Skills are written as numbered rule guides, not as essays. An agent scans a skill mid-task, so each rule must be findable and quotable on its own.

- Number the top-level sections, and order them by priority.
- Open with a precedence table that ranks the rules and names the winner of every foreseeable conflict.
- State each shared exception once, then reference it. Repeating a hedge on every rule is the main source of bloat.
- Put lookups in tables: one row per rule, with the repair beside it.
- Give rules stable identifiers so other sections cite `rule 8` or `P3` instead of "see below".
- Close with a single examples table covering the cases most often applied wrong.

`skills/refine-text/SKILL.md` is the reference implementation.

## Use

Copy a skill directory into the target agent or Codex skills directory supported by your runtime. Keep the directory name aligned with the `name` field in `SKILL.md`.

## Validate

Run the local validator before committing skill changes:

```bash
python3 scripts/validate_skills.py
```

The validator checks layout and metadata:

- a `SKILL.md` file
- YAML frontmatter
- `name` and `description` fields
- a directory name that matches the skill name
- no duplicate skill names

It also lints the skill's own prose, since a writing skill that breaks its own rules teaches the wrong pattern. Flagged in prose: em and en dashes, the flagged words and phrases listed in `scripts/validate_skills.py`, and the `not just X` construction.

The lint skips frontmatter, fenced code, table rows, and inline code spans, so a skill can still name a flagged term as data. Write flagged terms inside backticks or a table cell, never in running prose.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for skill authoring and review guidelines.
