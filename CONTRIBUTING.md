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
name: skill-name
description: What the skill does. Use when the user asks to do X, mentions Y, or works on Z.
---
```

The description should explain when the skill should be used. Write it as trigger guidance, not marketing copy. Name the situations that should invoke it, since this text is what an agent matches against a request.

## Structure

Write skills as numbered rule guides. An agent reads a skill while working, so a rule buried in a paragraph gets skipped. `skills/refine-text/SKILL.md` is the reference implementation.

1. **Number top-level sections and order them by priority.** The first section a reader hits should be the one that settles arguments.
2. **Open with a precedence table.** Rank the competing concerns, give each rank a short identifier such as `P1`, and state the resolution for every conflict a reader will hit. A rule guide without a precedence order is a list of suggestions.
3. **State each shared exception once.** Give it its own section, then reference it. Repeating "unless the user asks otherwise" on twenty rules is how a two-page skill becomes six.
4. **Use tables for lookups.** One row per rule: the trigger, an example, and the repair. Reserve prose for the reasoning a table cannot carry.
5. **Give rules stable identifiers.** Sections cite `rule 8` or `P3`. Never write "see the rule below", which breaks the moment a section moves.
6. **Close with one examples table.** Cover the cases most often applied wrong, especially where a rule correctly does nothing.

Keep a skill short enough to scan. When it outgrows roughly 250 lines, move reference material such as long word lists into a separate file and link it, rather than diluting the rules.

## Authoring Guidelines

- Define the scope clearly.
- State expected inputs and outputs.
- Preserve technical literals such as code, identifiers, file paths, CLI flags, config keys, and quoted source text unless the user explicitly asks to change them.
- Prefer concrete steps over broad advice.
- Add examples only when they clarify behavior.
- Avoid overlapping another skill unless the difference is clear.
- Keep instructions current with the capabilities of the target agent runtime.
- A skill must obey the rules it teaches. The validator lints skill prose for the terms and punctuation the skill itself flags. Name a flagged term inside backticks or a table cell so the lint reads it as data.

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

When you change an existing skill, also check for conflicts the validator cannot see:

- **No contradictions.** Two rules must not demand different outcomes for the same text. Where they legitimately compete, the precedence table names the winner.
- **No duplication.** One rule, one home. If a rule is restated in a second section, cut it and cite the first.
- **Cross-references resolve.** Every `rule N` and rank identifier points at a section that still exists with that number.
- **Numbering is gapless.** Deleting a rule from a numbered list renumbers the rest.
- **Examples match current rules.** An example written against an older rule becomes a counterexample. Verify each one still demonstrates what it claims.
- **New exceptions do not undercut a rule.** An exemption needed for a term's most common usage means the rule is miscalibrated, so narrow the rule instead.
- **The description still matches.** It is the trigger surface, and the README quotes it. Changing one requires changing the other.

## License

By contributing, you agree that your contribution is licensed under the Apache License 2.0.
