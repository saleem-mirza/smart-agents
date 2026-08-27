# smart-agents

## 1. Core principles

- Be simple. Do not overengineer. Do not program defensively.
- Work incrementally, in small steps. Validate each increment before moving on.
- Use the latest library APIs as of now.

## 2. Code style

- Favor short modules, short methods and functions. Name things clearly.
- Favor clear, concise docstring comments.
- Never use emojis in code, logging, or any text.
- Keep README.md concise.

## 3. Debugging and fixing

- Identify root cause before fixing. Prove the problem with evidence, don't guess.
- Reproduce the problem consistently.
- Try one test at a time. Be methodical.
- Don't jump to conclusions. Don't apply workarounds.

## 4. This repository

smart-agents is a collection of agent skills under `skills/<skill-name>/SKILL.md`.

- Write skills as numbered rule guides, not essays: precedence table first, tables over prose, stable rule IDs (`P1`, `rule 8`), one examples table at the end. See `skills/refine-text/SKILL.md` as the reference implementation.
- Run `python3 scripts/validate_skills.py` before committing any skill change.
- Directory name must match the `name` field in frontmatter. `description` is trigger guidance, not marketing copy.
- Skills are distributed by symlinking the directory into each runtime (`~/.claude/skills/`, `~/.codex/skills/`), never copied.
- Full authoring rules live in `CONTRIBUTING.md`.
