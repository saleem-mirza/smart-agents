# smart-agents

A curated collection of AI agent skills.

## Skills

| Skill | Description |
| --- | --- |
| `refine-text` | Refines, rewrites, proofreads, and edits prose for clarity, accuracy, and directness. |

Each skill lives in `skills/<skill-name>/SKILL.md` and starts with YAML frontmatter:

```yaml
---
name: skill-name
description: Short trigger-oriented description.
---
```

## Use

Copy a skill directory into the target agent or Codex skills directory supported by your runtime. Keep the directory name aligned with the `name` field in `SKILL.md`.

## Validate

Run the local validator before committing skill changes:

```bash
python3 scripts/validate_skills.py
```

The validator checks that each skill has:

- a `SKILL.md` file
- YAML frontmatter
- `name` and `description` fields
- a directory name that matches the skill name
- no duplicate skill names

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for skill authoring and review guidelines.
