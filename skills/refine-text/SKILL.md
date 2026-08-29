---
name: refine-text
description: Refine, rewrite, proofread, or edit prose for clarity, accuracy, tone, directness, and genre-appropriate style. Use when the user asks to improve wording, tighten prose, remove AI-sounding language, edit text or files, or adapt supplied prose to a judicial, journalistic, public-service, developer-documentation, product, UI, or general register.
---

# Refine Text

Rewrite prose for clarity, accuracy, and directness while preserving its facts, meaning, and intended voice.

## 1. Precedence

Higher rank wins every conflict. Cite the rank only when a conflict affects the output.

| Rank | Rule |
| --- | --- |
| P1 | Factual accuracy and source fidelity |
| P2 | The user's explicit request |
| P3 | Protected verbatim text |
| P4 | Grammatical correctness |
| P5 | Supplied binding house style or required format |
| P6 | Selected genre profile and requested voice |
| P7 | Default editorial guidance |

- P1 over P2: never introduce an unsupported factual claim. Complete the rest of the work, state the problem in one sentence, and let the user decide.
- P2 over P3: edit inside user-authored dialogue or quoted copy only when the user explicitly asks. Otherwise preserve quoted source material.
- P2 over P4: when the user restricts the edit, respect the restriction and report a remaining grammar error in one sentence instead of fixing it silently.
- P5 over P6: a supplied court, newsroom, agency, publication, or organizational guide outranks a general genre profile.

## 2. Fidelity and Protected Text

Never invent facts, figures, quotations, examples, anecdotes, experiences, citations, measurements, or supporting evidence. Use only information supplied by the user or source. Do not turn an attributed claim into the writer's assertion.

Every default style rule yields when meaning requires it. Preserve a flagged form when it carries factual accuracy, legal or contractual force, a term of art, product or brand wording, direct quotation, deliberate emphasis, or a voice the user requested. Precision outranks every style preference.

**Protected verbatim text (P3):** identifiers, API names, CLI flags, config keys, file paths, error text, code blocks, inline code, quoted source material, and third-party product names. Leave errors inside them as found. Preserve the punctuation and placement of existing quotations. Factual accuracy does not authorize altering a quotation; it requires preserving the quotation and its attribution.

## 3. Inputs

| Input | Action |
| --- | --- |
| File paths or globs | Resolve targets, read each file fully, overwrite changed files, and report which changed. |
| Static text | Return only the replacement text. |
| No argument | Refine the previous assistant message. Return text only and never write files. If none exists, say so. |
| Paths inside a sentence to rewrite | Treat as static text, not as targets. |

- Skip binary, generated, unreadable, and non-text files. Report skips briefly.
- Ask before overwriting on broad globs, large match sets, or ambiguous intent.
- If a glob matches nothing or a file fails to read, say so. Never fabricate output.

## Style Profiles

Choose one primary profile. Read only the references required for the current text.

| Text or request | Reference |
| --- | --- |
| Grammar, syntax, collocation, modality, dialect, or disputed usage needs attention | Read [grammar-and-syntax.md](references/grammar-and-syntax.md). This foundation may accompany any profile. |
| Judicial opinion or order | Read [judicial.md](references/judicial.md). Do not use it for briefs, contracts, statutes, or regulations unless the user explicitly requests judicial-opinion style. |
| News report, news release, or journalistic copy | Read [journalism.md](references/journalism.md). |
| U.S. federal notice, instruction, benefit or service information, form text, or other public-facing agency copy | Read [public-service.md](references/public-service.md). Do not apply it automatically to statutes, regulations, contracts, or adjudicative text. |
| Google-style developer documentation, API guide, tutorial, or technical reference | Read [google-developer-docs.md](references/google-developer-docs.md). |
| Microsoft-style product documentation, UI text, help content, procedure, or error message | Read [microsoft-writing.md](references/microsoft-writing.md). |
| General prose or no clear profile | Use this file without a genre reference. Read the grammar reference only when needed. |

Resolve style in this order: the user's explicit request, a supplied binding or house guide, a clearly established document type, consistent document-wide conventions, then genre defaults. Do not mistake an isolated inconsistency for house style.

When profiles overlap, choose the profile that matches the document's primary function and borrow only necessary constraints from another. For example, a court's public notice may use the public-service profile while preserving judicial terminology. If the choice would materially change the result and the intended function is unclear, ask; otherwise use general refinement.

Do not infer Google or Microsoft house style merely because a document discusses one company's product. When neither profile is explicitly requested, prefer Google for clearly developer-facing documentation, Microsoft for clearly product- or UI-facing help, and general refinement when the distinction is unclear.

A profile governs style and organization only. It never authorizes new facts, legal analysis, reporting, citations, holdings, policy, or substantive requirements.

## 4. Context and Edit Depth

Before editing, identify the text's purpose, audience, genre, point of view, formality, emotional register, terminology, voice, and structural conventions. Resolve context in this order: the user's explicit request, consistent document-wide conventions, then genre defaults. Do not mistake an isolated inconsistency for intentional voice. When the context does not establish a special register, use plain natural language. Do not manufacture personality, opinions, emotion, or personal experience.

Preserve source-supplied first-person observations, anecdotes, concrete nouns, dates, locations, sensory details, and distinctive phrasing when they contribute meaning or voice. Never manufacture them.

- Repair at sentence and paragraph level by default.
- Merge sentences that carry one idea. Split a sentence that carries three.
- Give each paragraph one job, and lead with the sentence that states it unless the source deliberately builds to it.
- Do not reorder sections, retitle headings, or merge across a heading boundary unless asked. When order blocks comprehension, refine in place and say so in one sentence.
- When adjacent paragraphs make one point, merge them without removing unique information.
- In file mode, preserve heading levels, list nesting, table columns, link targets, anchors, and front matter.
- Leave a sentence unchanged when it is already accurate, clear, natural, and not redundant. Prefer the smallest edit that fixes the defect.

## 5. Grammar and Terminology (P4)

Fix grammatical errors throughout the requested scope, including sentences that need no stylistic edit. Dialect and regional standard forms are not errors.

| Check | Repair |
| --- | --- |
| Pronoun reference | Give every `it`, `this`, `that`, and `they` one obvious antecedent. When two nouns compete, name the intended noun. |
| Subject-verb agreement | Ignore intervening nouns when matching the subject and verb: `The list of accounts are stale` becomes `is stale`. |
| Dangling modifier | Attach an opening modifier to the grammatical subject: `After deploying, the tests failed` becomes `After we deployed, the tests failed`. |
| Misplaced `only` | Put `only` next to what it limits. |
| Tense consistency | Hold one tense within a passage unless the timeline requires a change. |
| Parallel form | Give coordinated items, list entries, and sibling headings matching grammatical forms and verb moods. |
| Correlatives | Put `both/and`, `either/or`, and `not/but` next to the elements they join. |
| Sentence boundaries | Fix comma splices, run-ons, and unintended fragments. Preserve a fragment that belongs to the established voice. |
| Terminology | Use the same term for the same concept. Do not alternate among near-synonyms merely for variety. Preserve domain distinctions, capitalization, and terms of art. Do not merge terms that may differ without evidence from the source. |

## 6. Sentence Construction

| Rule | Repair |
| --- | --- |
| Given to new | Start with what the reader knows and end with what is new. |
| Active voice | Name the actor unless the actor is unknown or irrelevant. |
| Nominalizations | `perform an analysis of` becomes `analyze`; `provide a recommendation` becomes `recommend`. |
| One idea per sentence | Carry one main idea when practical. |
| Natural rhythm | Break runs of uniform sentence length, repeated openings, identical clause patterns, and overbalanced pairs. Vary structure only when it improves clarity, rhythm, or emphasis. |

## 7. Concision

Cut only what loses no fact, function, caveat, emphasis, or intentional voice. Keep numbers and qualifiers that change meaning. Preserve attribution and evidentiary hedges such as `it said`, `according to`, `alleged`, `reportedly`, `described as`, `billing themselves as`, `sought to`, and `deemed`. Cutting one can turn a reported claim into the writer's assertion.

Never add a characterizing word to an attribution: `said` does not become `conceded` or `admitted`. The added word asserts something the source did not.

| Pattern | Example | Repair |
| --- | --- | --- |
| Restatement | `The job runs nightly. It is scheduled to execute once every 24 hours.` | Keep the clearer sentence. |
| Throat-clearing | `It is important to note that`, `It should be mentioned that`, `One thing to consider is` | Delete the frame and keep the claim. |
| Empty qualifier | `in order to`, `at this point in time`, `due to the fact that`, `has the ability to` | Use `to`, `now`, `because`, or `can`, subject to the modality rules. |
| Preview and recap | `The next section covers rollback.` `To recap, we covered rollback.` | Delete when the heading and body already make the point. |
| Redundant pair | `each and every`, `first and foremost`, `plan ahead`, `end result` | Keep the word that carries the meaning. |
| Deducible clause | `The build failed, which means it did not succeed.` | Delete the clause that the main clause already implies. |
| Audience-obvious explanation | Background the intended audience can reasonably be expected to know | Remove only when it does not support the argument or prevent ambiguity. |

A successful edit may remain close to the original length. Stop when further cutting would remove meaning, useful emphasis, or voice. Never cut into meaning to hit a length target.

## 8. AI Markers

AI markers are contextual patterns, not proof of authorship or forbidden words. Judge them across the sentence, paragraph, and document. Remove a marker when it makes the prose generic, repetitive, mechanical, inflated, or poorly adapted to its context. Preserve it when it carries meaning, factual uncertainty, attribution, required disclosure, or intentional voice.

| Marker | Detect | Repair |
| --- | --- | --- |
| Generic or overly formal tone | Bland neutrality, impersonal phrasing, or a register that does not suit the document | Match the user's requested voice. When none is specified, infer an appropriate register from the document's purpose, audience, genre, and strongest natural passages. Do not add opinions, emotion, or enthusiasm absent from the source. |
| Repetition | Repeated words, claims, examples, sentence openings, grammatical structures, or paragraph conclusions | Consolidate only what adds no information, emphasis, qualification, or rhythm. |
| Unnecessary explanation | Background, previews, recaps, or deductions the audience does not need | Keep the claim and remove the scaffolding. Preserve context needed for comprehension. |
| Generic abstraction | Vague language where the source already supplies concrete detail | Use the supplied detail. Never invent anecdotes, experiences, measurements, quotations, or examples. |
| Predictable syntax | Uniform sentence length, repeated `X is Y because` forms, matched paragraph shapes, or formulaic introductions and conclusions | Vary openings and structure where it improves the reading flow. |
| Terminology drift | Different words used for the same concept without a reason, or technical terms used imprecisely | Apply the terminology rule in section 5. |
| Negative parallelism | `It is not a tool, it is a platform` or `not just X, but also Y` used as a stock contrast | State the positive claim directly. Preserve a contrast that carries real meaning or voice. |
| Padded list | A trio such as `fast, reliable, and scalable` in which an item adds no information | Keep every substantive item and cut padding. Count content, not items. |
| Trailing participial | A sentence ends with an `-ing` clause that adds a vague lesson or claim | Cut the clause, or make it a sentence with a stated subject using only source-supported information. |
| Expletive opener | `There are three reasons that the build fails` | Name the subject: `The build fails for three reasons`. |
| Forced transition | `Additionally`, `Moreover`, `That said`, or another transition merely announces movement | Remove it, or state the actual relation: addition, contrast, cause, consequence, or sequence. Check paragraph-to-paragraph flow. |
| Generic summary | `In summary, this approach has benefits and drawbacks` | State the actual benefit and drawback when the source provides them; otherwise remove the empty summary. |
| Vague claim | `This significantly improves performance` without supporting detail | Use a measurement only when the source provides one. Otherwise preserve the claim, refine it with supplied information, or flag it for verification. Never invent evidence. |
| Empty hedge | `It is important to note that` or `In general` delays a claim without expressing uncertainty | Remove the frame. Preserve hedges that mark probability, attribution, legal qualification, evidentiary limits, or confidence. |
| AI self-reference | Irrelevant boilerplate such as `As an AI language model` | Remove it when it does not belong in the requested document. Preserve AI references when AI is the subject, the wording is quoted, or disclosure is required. |
| Context mismatch | The text defaults to a generic template instead of the document's genre, audience, intent, or voice | Apply the context pass in section 4. Do not turn specialized or expressive prose into generic business language. |

Cut clichés, empty metaphors, unsupported generalizations, promotional judgments, and unsolicited commentary. Preserve figurative language that carries meaning or belongs to the requested voice.

## 9. Words in Context

Never treat an isolated word as proof of AI writing. Inflections and derived forms count only when the use has the same defect.

| Category | Common examples | Repair |
| --- | --- | --- |
| Empty intensifiers | `very`, `really`, `just`, `basically`, `actually`, `literally` | Delete only when the degree, restriction, correction, or emphasis does not change meaning. |
| Reflexive hedges | `probably`, `maybe`, `certainly`, `perhaps` | Remove only when they do not express real uncertainty. `The regression probably came from the cache change` must remain uncertain unless the cause is verified. |
| Register mismatch | `utilize`, `delve`, `elucidate`, `embark`, `illuminate`, `unveil`, `unlock` | Prefer a plain synonym when the formal word adds no precision. |
| Inflated or promotional usage | `game-changer`, `best-in-class`, `world-class`, `revolutionize`, `skyrocket`, `pivotal`, `strategic` | Cut the judgment or state the concrete source-supported action, result, or importance. Preserve an ordinary or domain-specific use. |
| Corporate filler | `synergy`, `leverage`, `circle back`, `move the needle`, `mission-critical` | State the concrete action when the phrase obscures it. |
| Formulaic phrases | `dive deep`, `in a world where`, `in closing`, `in conclusion`, `shed light`, `worth noting` | Remove the frame or state the point directly. |

`craft`, `discover`, `imagine`, `realm`, `intricate`, and similar words are ordinary English. Replace them only when their particular use inflates or obscures the meaning.

## 10. Connectives and Flow

Do not delete a connective when doing so loses a genuine relation. Match the repair to the logic.

| Relation | Repair |
| --- | --- |
| Concession | Use `but`, or subordinate with `although` or `while`. |
| Addition | Start the sentence with its subject, or join related clauses with `and`. |
| Cause or consequence | Use `because` or `so`, or state cause and effect in one sentence. |
| Sequence | State the event or step that follows instead of announcing that another point is coming. |

`so` is causal and never substitutes for a concession.

## 11. Modality (P1)

`can`, `may`, `could`, `must`, and `should` carry different meanings. Never swap one for another, and never delete one as filler.

| Modal | Rule |
| --- | --- |
| `can` | Ability. Cut only when padding a capability: `The API can support webhooks` becomes `supports`. Keep when ability or a condition is the point. |
| `may` | Permission or possibility. Keep. `You may cancel within 30 days` becomes an obligation if cut. |
| `could` | Conditional or possibility. Keep unless it hedges a verified fact. |
| `must`, `should` | Obligation strength. Never adjust. In policy, legal, and API contracts the difference is the requirement. |

## 12. Tone and Voice

- Use plain, natural language unless the genre or requested voice calls for another register.
- Use `you` where the genre takes direct address, including documentation, instructions, and customer-facing copy. Narrative, legal, and academic prose usually do not.
- Preserve expressive, casual, technical, legal, academic, journalistic, and brand voices. Never flatten them into generic business prose.
- In business prose, state the action, owner, deadline, decision, risk, or impact when the source supplies it.
- Support claims only with facts, data, examples, or citations supplied by the user or source.
- Group related alternatives, and number them when the genre uses lists. Leave running prose as prose.
- For quote marks you introduce, follow the source document's punctuation convention. Never restyle punctuation in quoted source material or move a mark across an existing closing quote.
- Remove excessive or mannered dashes. Preserve a dash when it is the clearest punctuation, part of a title or range, or consistent with the requested voice.

## 13. Mandatory Final Proofread

After applying the shared rules and every selected style profile, proofread each final text or document once from beginning to end before returning it or reporting completion. This pass is mandatory even when the main edit made few or no changes.

During this verification pass:

- Confirm that facts, meaning, attribution, uncertainty, modality, quotations, and protected text still match the source.
- Correct any remaining or newly introduced grammar, spelling, punctuation, sentence-boundary, agreement, reference, or typographical error.
- Check terminology, names, numbers, dates, dialect, voice, house style, and the selected profile for consistency.
- Check sentence and paragraph flow, repetition, unnecessary explanation, and unresolved AI markers in context.
- In file mode, confirm that headings, lists, tables, links, anchors, code, and front matter remain structurally intact.

Make only corrections supported by the source and the applicable rules. Do not turn the proofread into another open-ended rewrite, expand the requested scope, or add new information. In file mode, proofread the final draft before overwriting the target, then verify that the saved file is readable and structurally intact.

## 14. Output

Return only the requested output. Add one sentence only for a material risk, failure, skipped target, or P1/P2 conflict.

## Examples

| Case | Before | After | Why |
| --- | --- | --- | --- |
| Words and uncertainty | `We can probably utilize the new process to really improve approvals.` | `We can probably use the new process to improve approvals.` | `utilize` and `really` add no meaning. `can` and `probably` preserve ability and uncertainty. |
| Load-bearing modal | `Reviewers may reject a submission after the deadline.` | unchanged | `may` grants permission or marks possibility. Cutting it changes the claim. |
| Given to new | `A cache invalidation bug that the team found last week causes the stale reads.` | `The stale reads come from a cache invalidation bug the team found last week.` | Known information comes first and no fact changes. |
| Negative parallelism | `This is not merely a refactor, it is a rethinking of the pipeline. It significantly improves throughput.` | `This refactor rethinks the pipeline and significantly improves throughput.` | The positive claim replaces the stock contrast. No measurement is added. |
| Trailing participial | `The team shipped the migration in March, demonstrating the value of incremental rollout.` | `The team's March migration demonstrated the value of an incremental rollout.` | The revision gives `demonstrated` a stated subject and adds no claim. |
| Connective | `The cache reduced latency. However, it introduced stale reads.` | `The cache reduced latency, but it introduced stale reads.` | `but` carries the concession. |
| Grammar over style | `Updating the config, the service failed to restart.` | `When we updated the config, the service failed to restart.` | The revision repairs the dangling modifier. |
| Paragraph merge | `The API supports webhooks. Webhooks are supported for events. You register a URL and we post to it.` | `The API supports webhooks: register a URL and we post events to it.` | The revision keeps the unique information and removes repetition. |
| Path as text | `Rewrite this sentence: Save it to docs/release-notes.md when ready.` | `Save it to docs/release-notes.md when it is ready.` | The path appears inside prose to rewrite, so it stays verbatim. |
| Quote punctuation | `"...reserved for qualified Americans in need," a spokesperson said.` | unchanged | Existing quoted source material stays verbatim. |
| Attribution hedge | `The department plans to revoke the visas of people who, it said, came billing themselves as visitors.` | unchanged | `it said` and `billing themselves as` attribute the characterization. Cutting them would assert it as fact. |
| Concision floor | `The job retries three times. Each retry waits twice as long as the last, so the third wait is four seconds.` | unchanged | The second sentence carries the backoff rule and a number. |
| AI self-reference | `As an AI language model, I can explain the configuration.` | `I can explain the configuration.` | The disclosure is irrelevant to the requested prose. Preserve it when disclosure is required or AI is the subject. |
| File target | `Refine docs/release-notes.md.` | Read fully, preserve protected text and structure, overwrite changed prose, and report `Changed docs/release-notes.md.` | File mode writes and reports. |
