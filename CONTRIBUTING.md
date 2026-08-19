# Contributing

This repository stores reusable AI agent skills. A good skill is narrow, explicit about when it applies, and careful about preserving user intent.

## Skill Layout

Add each skill under:

```text
skills/<skill-name>/SKILL.md
```

The directory name must match the `name` field in the skill frontmatter.

Use lowercase kebab-case names, for example:

```text
skills/refine-text/SKILL.md
```

## Required Frontmatter

Every `SKILL.md` must start with YAML frontmatter:

```yaml
---
name: refine-text
description: Refine, rewrite, proofread, or edit prose for clarity and accuracy.
---
```

The description should explain when the skill should be used. Write it as trigger guidance, not marketing copy.

## Authoring Guidelines

- Define the scope clearly.
- State expected inputs and outputs.
- Preserve technical literals such as code, identifiers, file paths, CLI flags, config keys, and quoted source text unless the user explicitly asks to change them.
- Prefer concrete steps over broad advice.
- Add examples only when they clarify behavior.
- Avoid overlapping another skill unless the difference is clear.
- Keep instructions current with the capabilities of the target agent runtime.

## Review Checklist

Before opening a pull request or committing changes:

```bash
python3 scripts/validate_skills.py
```

Then check:

- The skill name matches its directory.
- The description accurately describes when to use the skill.
- The instructions are specific enough for an agent to follow.
- The skill does not require unavailable tools or hidden context.
- The skill preserves user-provided technical content by default.

## License

By contributing, you agree that your contribution is licensed under the Apache License 2.0.
