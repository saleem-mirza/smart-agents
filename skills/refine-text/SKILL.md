---
name: refine-text
description: Refine, rewrite, proofread, or edit prose so it is grammatically correct, precise, plain, active, clear, and free of common AI markers. Use when the user asks to improve wording, rewrite text, tighten prose, polish comments, edit documents, refine commit messages, remove AI-sounding language, apply edits to file paths or globs, or refine the previous assistant prose when no argument is provided.
---

# Refine Text

Rewrite prose for clarity, accuracy, and directness while preserving meaning.

## Scope

Apply these rules to user-provided text and requested drafting or editing work, including documents, code comments, commit messages, and chat messages.

Preserve verbatim: identifiers, API names, CLI flags, config keys, file paths, error text, code blocks, inline code, quoted source material, and third-party product names.

## Inputs

If the user provides one or more file references or glob patterns, resolve the targets before editing. Refine only readable text files, overwrite each changed file with the replacement text, and report which files changed.

Skip binary files, generated files, unsupported file types, unreadable files, and targets that cannot be safely rewritten as text. Report skipped files briefly.

For broad globs or unexpectedly large match sets, ask before overwriting files.

If the user provides static text instead of a file reference or glob, refine that text and return only the replacement text.

If the user invokes the skill without a file reference, glob, or static text argument, refine the previous assistant prose in the current conversation and return only the replacement text. Do not overwrite files in this mode. If there is no previous assistant prose, report that briefly.

When paths and static text are both present, treat paths or globs as file targets only when the user clearly asks to edit, refine, or apply the skill to those files. Treat path-like strings inside a sentence as static text when the user asks to rewrite the sentence itself. If intent is ambiguous, ask before overwriting files.

Before overwriting files, preserve non-prose and technical literals under the scope rule. Do not rewrite code blocks, identifiers, config keys, file paths, quoted source material, or error messages unless the user explicitly asks for that exact change.

If a glob matches no files or a referenced file cannot be read, report the issue briefly and do not fabricate output for that target.

## Precedence

Apply rules in this order:

1. Accuracy.
2. The user's explicit request.
3. Preservation of verbatim text.
4. These style rules.

## Method

1. Read the full text before rewriting or rephrasing. In file or glob mode, read the full target file before overwriting it, or preserve all untouched sections exactly when editing only part of a file. For static text or conversational rewrites where full context is unavailable, read enough surrounding context, usually one or two paragraphs, to understand the local meaning.
2. Identify the source meaning, audience, context, and purpose.
3. Keep correct content unchanged.
4. Fix grammar, ambiguity, and imprecision.
5. Rewrite with correct grammar.
6. Make the text concise when clarity or accuracy improves.
7. Prefer active voice unless the actor is unknown or irrelevant.
8. Remove AI markers, filler, cliches, unsupported claims, repeated ideas, and setup phrases.
9. Use one idea per sentence when practical.
10. Keep terminology, formatting, and references consistent.
11. Return only the requested output, unless a material risk, failure, or skipped scope needs one sentence.

## Style

Use clear, simple, natural language.

Use "you" and "your" when direct address fits.

Use data and examples when they improve accuracy.

Use adjectives and adverbs only when they add information.

Group related alternatives together. Number them when there is more than one.

Use logical quoting. Put punctuation outside the closing quote unless the source includes it.

## Professional Tone

Use plain business English when the context is workplace, executive, sales, legal, finance, operations, product, or customer-facing.

Prefer precise verbs: `recommend`, `approve`, `confirm`, `reduce`, `increase`, `resolve`, `prioritize`, `align`, `deliver`, `measure`, `decide`, `assign`.

State the action, owner, deadline, decision, risk, tradeoff, or business impact when relevant.

Prefer concrete phrasing:

- `We recommend X because Y.`
- `This reduces cost by 12%.`
- `The main risk is delayed approval.`
- `Next step: Legal approves the draft by Friday.`
- `Owner: Finance. Due: August 30.`

Avoid corporate filler: `synergy`, `leverage`, `circle back`, `move the needle`, `best-in-class`, `world-class`, `mission-critical`, and `strategic`, unless the term has a precise meaning in context.

## Avoid

Remove common AI markers: em dashes, en dashes, formulaic transitions, inflated phrasing, generic summaries, overbalanced sentence pairs, and vague claims.

Do not use em dashes or en dashes in rewritten prose. Replace each one with a comma, colon, period, or parentheses. Keep em dashes and en dashes only when they are part of code, CLI flags, technical terminology, or quoted material.

Do not use "not just X, but also Y", including "not only", "not merely", and "not simply". Split into one claim per sentence.

Avoid metaphors, cliches, broad generalizations, unsolicited commentary, and vague sentences that do not add useful information.

Avoid these words unless needed for accuracy, legal meaning, product wording, direct quotation, or preserved text: `abyss`, `actually`, `basically`, `can`, `certainly`, `could`, `craft`, `delve`, `discover`, `disruptive`, `elucidate`, `embark`, `enlightening`, `esteemed`, `furthermore`, `game-changer`, `hence`, `however`, `illuminate`, `imagine`, `intricate`, `just`, `literally`, `may`, `maybe`, `pivotal`, `probably`, `really`, `realm`, `revolutionize`, `skyrocket`, `tapestry`, `unlock`, `unveil`, `utilize`, `very`.

Avoid these phrases unless needed for accuracy, legal meaning, product wording, direct quotation, or preserved text: `dive deep`, `in a world where`, `in closing`, `in conclusion`, `not alone`, `shed light`, `worth noting`.

Inflections and derived forms count.

## Replacements

| Flagged | Use |
| --- | --- |
| can, could, may | present tense, or `supports` / `works with`, when replacement preserves meaning |
| utilize | use |
| however, furthermore, hence | new sentence, or `so` |
| just, very, really, actually, basically, literally | delete |
| probably, certainly, maybe | state the fact, or name the condition |
| craft | write, build |
| discover, unlock, illuminate, unveil | show, find, explain |
| pivotal, intricate | important, detailed |
| em dash, en dash | comma, colon, or period |
| "not just X, but also Y" | one claim per sentence |
