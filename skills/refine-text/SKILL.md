---
name: refine-text
description: Refine, rewrite, proofread, or edit prose for clarity, accuracy, tone, and directness. Use when the user asks to improve wording, rewrite text, tighten prose, polish comments, edit documents, refine commit messages, remove AI-sounding language, apply edits to file paths or globs, or refine the previous assistant prose when no argument is provided.
---

# Refine Text

Rewrite prose for clarity, accuracy, and directness while preserving meaning.

## 1. Precedence

Higher rank wins every conflict. Cite the rank when you override a lower rule.

| Rank | Rule |
| --- | --- |
| P1 | Factual accuracy |
| P2 | The user's explicit request |
| P3 | Verbatim text, preserved exactly |
| P4 | Grammatical correctness |
| P5 | User-requested tone or voice |
| P6 | Style rules 5 through 9 below |

Two resolutions follow from this order:

- P1 over P2: when the request would introduce a factual error, do the rest of the work, state the problem in one sentence, and let the user decide.
- P2 over P4: when the user restricts the edit, respect the restriction and report the grammar error in one sentence instead of fixing it silently.

## 2. The Exception Rule

Every rule below yields when meaning requires it. Keep the flagged form, without asking, when it carries: factual accuracy, legal or contractual force, a domain term of art, product or brand wording, direct quotation, or a voice the user asked for.

This is stated once and applies throughout. Precision outranks every ban.

**Verbatim, never edited (P3):** identifiers, API names, CLI flags, config keys, file paths, error text, code blocks, inline code, quoted source material, third-party product names. Leave errors inside them as found.

## 3. Inputs

| Input | Action |
| --- | --- |
| File paths or globs | Resolve targets, read each file fully, overwrite changed files, report which changed. |
| Static text | Return only the replacement text. |
| No argument | Refine the previous assistant message. Return text only, never write files. If none exists, say so. |
| Paths inside a sentence to rewrite | Treat as static text, not as targets. |

- Skip binary, generated, unreadable, and non-text files. Report skips briefly.
- Ask before overwriting on broad globs, large match sets, or ambiguous intent.
- If a glob matches nothing or a file fails to read, say so. Never fabricate output.

## 4. Edit Depth

- Repair at sentence and paragraph level by default.
- Merge sentences that carry one idea. Split a sentence that carries three.
- Give each paragraph one job, and lead with the sentence that states it, unless the source builds to it deliberately.
- Do not reorder sections, retitle headings, merge across a heading boundary, or delete a paragraph whole unless asked. When order blocks comprehension, refine in place and say so in one sentence.
- In file mode, preserve heading levels, list nesting, table columns, link targets, anchors, and front matter.
- Leave a sentence unchanged when it is already accurate, clear, and marker-free. Prefer the smallest edit that fixes the defect.

## 5. Grammar (P4)

Fix in any sentence you edit, including one you would otherwise leave alone.

| Check | Repair |
| --- | --- |
| Pronoun reference | Every `it`, `this`, `that`, `they` needs one obvious antecedent. Two candidates, name the noun. The most common real ambiguity in technical prose. |
| Subject-verb agreement | Watch a plural noun between subject and verb: `The list of accounts are stale` becomes `is stale`. |
| Dangling modifier | An opening participle must attach to the subject: `After deploying, the tests failed` becomes `After we deployed, the tests failed`. |
| Misplaced `only` | Put it next to what it limits. |
| Tense consistency | Hold one tense within a passage. |
| Parallel form | Coordinated items, list entries, and sibling headings match in grammatical shape and verb mood. |
| Correlatives | Put `both/and`, `either/or`, `not/but` next to the elements they join. |
| Sentence boundaries | Fix comma splices, run-ons, and fragments. Keep a fragment that is established voice. |

Dialect and regional standard forms are not errors.

## 6. Sentence Construction

| Rule | Repair |
| --- | --- |
| Given to new | Start with what the reader knows, end with what is new. The highest-leverage fix for prose that parses but does not land. |
| Active voice | Name the actor, unless the actor is unknown or irrelevant. |
| Nominalizations | `perform an analysis of` becomes `analyze`. `provide a recommendation` becomes `recommend`. |
| One idea per sentence | Carry one idea when practical. |
| Varied length | A run of uniform-length sentences reads as machine output even when every sentence is correct. |

## 7. AI Markers

Remove. These identify machine prose more reliably than any single word.

| Marker | Example | Repair |
| --- | --- | --- |
| Negative parallelism | `It is not a tool, it is a platform.` | State the positive claim once. |
| `not just X, but also Y` | Includes `not only`, `not merely`, `not simply`. | One claim per sentence. |
| Padded triple | `fast, reliable, and scalable`, where the third item adds nothing. | Cut the padding. Three real items are fine, so count content, not items. |
| Trailing participial | `The release shipped Friday, highlighting the value of automation.` | Cut it, or make it a sentence with a stated subject. |
| Expletive opener | `There are three reasons that the build fails.` | `The build fails for three reasons.` |
| Overbalanced pair | Consecutive sentences of near-identical length and shape. | Vary length and structure. Merge or split. |
| Formulaic transition | `That said,` `At the end of the day,` `When it comes to X,` | Delete, or name the actual relation. |
| Inflated phrasing | `a comprehensive suite of capabilities` | `four features`, or name them. |
| Generic summary | `In summary, this approach has benefits and drawbacks.` | State the benefit and the drawback. |
| Vague claim | `This significantly improves performance.` | Give the number, or drop the claim. |

Also cut: metaphors, cliches, broad generalizations, and unsolicited commentary.

## 8. Words

Inflections and derived forms count. Rule 2 governs every row.

| Category | Words | Repair |
| --- | --- | --- |
| Intensifiers | `very`, `really`, `just`, `basically`, `actually`, `literally` | Delete. Meaning rarely changes. |
| Reflexive hedges | `probably`, `maybe`, `certainly`, `perhaps` | State the fact, or name the deciding condition. Keep when the uncertainty is real: `The regression probably came from the cache change` is honest, and cutting `probably` asserts a cause nobody verified. |
| Register mismatch | `utilize`, `delve`, `elucidate`, `embark`, `illuminate`, `unveil`, `unlock` | Plain synonym: `use`, `examine`, `explain`, `start`, `show`, `reveal`, `open`. |
| Marketing terms | `abyss`, `realm`, `tapestry`, `game-changer`, `disruptive`, `revolutionize`, `skyrocket`, `enlightening`, `esteemed`, `pivotal`, `intricate`, `imagine` | Cut the claim, or name the specific: `important`, `detailed`. |
| Corporate filler | `synergy`, `leverage`, `circle back`, `move the needle`, `best-in-class`, `world-class`, `mission-critical`, `strategic` | Cut, or state the concrete action. |
| Connective tics | `however`, `furthermore`, `hence`, `moreover` | Restructure. See rule 9. |
| Phrases | `dive deep`, `in a world where`, `in closing`, `in conclusion`, `not alone`, `shed light`, `worth noting` | Cut. |

`craft` and `discover` are plain English, not markers. Flag them only when inflating: `craft a solution` becomes `build a solution`, `discover the root cause` becomes `find the root cause`.

## 9. Connectives

Do not open a sentence with `However,` or `Furthermore,` as a transition tic. Restructure instead of deleting the logic, and match the repair to the real relation.

| Relation | Repair |
| --- | --- |
| Concession | `but`, or subordinate with `although` or `while`. |
| Addition | Start the new sentence with its own subject, or join with `and`. |
| Consequence | `so`, or state cause and effect in one sentence. |

`so` is causal, so it never substitutes for a concessive. Keep the connective when restructuring would lose a genuine relation.

## 10. Modality (P1)

`can`, `may`, `could`, `must`, `should` carry different meanings. Never swap one for another, and never delete one as filler.

| Modal | Rule |
| --- | --- |
| `can` | Ability. Cut only when padding a capability: `The API can support webhooks` becomes `supports`. Keep when the ability is the point, or when conditional. |
| `may` | Permission or possibility. Keep. `You may cancel within 30 days` becomes an obligation if cut. |
| `could` | Conditional or possibility. Keep unless it hedges a known fact, then rule 8 applies. |
| `must`, `should` | Obligation strength. Never adjust. In policy, legal, and API contracts the difference is the requirement. |

## 11. Tone and Voice

- Plain, natural language. Adjectives and adverbs only when they add information.
- Use `you` where the genre takes direct address: documentation, instructions, customer-facing copy. Narrative, legal, and academic prose usually do not.
- Preserve intentional voice (P5). Never flatten expressive, casual, technical, legal, academic, or brand prose into generic business prose. When brand voice and business register conflict, brand voice wins.
- Business contexts take plain business English: precise verbs (`recommend`, `approve`, `reduce`, `resolve`, `deliver`, `decide`), and state the action, owner, deadline, decision, risk, or impact. `We recommend X because Y.` `This reduces cost by 12%.` `Owner: Finance. Due: August 30.`
- Support claims with data and examples where they improve accuracy.
- Group related alternatives, and number them when the genre uses lists. Leave running prose as prose.
- Logical quoting: punctuation outside the closing quote unless the source includes it.
- No em or en dashes in rewritten prose. Use a comma, colon, period, or parentheses.

## 12. Output

Return only the requested output. Add one sentence only for a material risk, a failure, a skipped target, or a P1/P2 conflict.

## Examples

| Case | Before | After | Why |
| --- | --- | --- | --- |
| Words and hedges | `We can probably utilize the new process to really improve approvals.` | `The new process will likely speed up approvals, though we have not measured it yet.` | `utilize` and `really` go, `can` is padding. `probably` marks real uncertainty, so it survives as a stated limit. |
| Load-bearing modal | `Reviewers may reject a submission after the deadline.` | unchanged | `may` grants permission. Cutting it makes rejection sound automatic. |
| Given to new | `A cache invalidation bug that the team found last week causes the stale reads.` | `The stale reads come from a cache invalidation bug the team found last week.` | Known information first, new information last. |
| Negative parallelism, vague claim | `This is not merely a refactor, it is a rethinking of the pipeline. It significantly improves throughput.` | `This refactor restructures the pipeline. Throughput rose from 4k to 11k events per second.` | One positive claim, and the number replaces `significantly`. Drop the claim when no number exists. |
| Trailing participial | `The team shipped the migration in March, demonstrating the value of incremental rollout.` | `The team shipped the migration in March. The incremental rollout kept each step reversible.` | The participle asserted a lesson with no subject. |
| Connective | `The cache reduced latency. However, it introduced stale reads.` | `The cache reduced latency, but it introduced stale reads.` | Concessive relation, so `but` carries it. Never `so`. |
| Grammar over style | `Updating the config, the service failed to restart.` | `When we updated the config, the service failed to restart.` | The modifier dangled. Fix even when asked only to shorten. |
| Paragraph merge | `The API supports webhooks. Webhooks are supported for events. You register a URL and we post to it.` | `The API supports webhooks: register a URL and we post events to it.` | Three sentences, one idea. Position in the document is unchanged. |
| Path as text | `Rewrite this sentence: Save it to docs/release-notes.md when ready.` | `Save it to docs/release-notes.md when it is ready.` | Path sits inside the sentence, so it is static text and stays verbatim. |
| File target | `Refine docs/release-notes.md.` | Read fully, preserve literals, overwrite prose, report `Changed docs/release-notes.md.` | File mode writes and reports. |
