---
name: review-rust-code
description: Review Rust code for correctness, soundness, concurrency, allocations, performance, and design. Use when the user asks to review a Rust crate, module, file, diff, or pull request, audit an unsafe block, check for races, leaks, or panics, or find allocation and performance problems in Rust.
argument-hint: [path, PR number, or `diff`; empty = current folder]
---

# Rust Code Review

Every finding cites code you read and an execution path you traced. One confirmed soundness bug beats twenty style notes.

Higher rank wins every conflict. Cite the rank when you override a lower rule.

| Rank | Rule |
| --- | --- |
| P1 | Evidence. An unproven claim ships as Unverified or not at all. |
| P2 | Scope, per rule 1. |
| P3 | Ship no edits, per rule 3. |
| P4 | The fix ladder, per rule 4. |
| P5 | Report shape, per rule 6. |

## 1. Target

Review target: `$ARGUMENTS`. When that placeholder arrives unexpanded or empty, use the target named in the invoking request, and the current directory when the request names none.

| Target | Meaning |
| --- | --- |
| Empty | The current directory. |
| Directory or file | That tree, plus its callers. |
| `diff` | The branch against its merge base: `git diff $(git merge-base HEAD origin/HEAD)...HEAD`. |
| A number such as `1234`, or a PR URL | That pull request. Run `gh pr checkout 1234` first, then review `gh pr diff 1234` plus the files it touches. |

Never widen past the target, and say so when you read outside it.

## 2. Free signals

Run these before reading code. Your clock starts when they finish, so there is never a trade between running them and having budget left. Compiler output is the cheapest evidence you will get, and reading harder is no substitute for it.

```sh
cargo check --all-targets --all-features
cargo clippy --all-targets --all-features -- -D warnings
cargo test
cargo fmt --all --check
cargo tree --duplicates
cargo tree -e features
```

Name each command and its result in the report; "skipped for time" is not available, because this time was never yours to spend. On demand, when a finding needs proof: `miri` for `unsafe` and UB claims, sanitizers for races, a profiler or `dhat` before any performance claim, `cargo udeps`/`audit`/`deny`/`bloat`, `cargo doc --no-deps` for a public API.

Scope to a workspace member with `-p <pkg>` when the target is one package inside a workspace. When a command fails, quote its output as finding one and continue with whatever still runs, because a crate that does not build is the review. Lint noise that predates the target is context, not findings: `-D warnings` also catches inherited `pedantic` lints and macro expansions you were not asked to review. When the tree will not build or a PR will not check out, say so and downgrade every Confidence to Unverified.

Then read the whole target before reporting on any part of it. Too large to read whole: name the subset you reviewed and review that subset properly. Stop when another pass would not change the top three findings, and ship.

## 3. Discipline

- Read before recommending, and trace callers. Unfamiliar code is not wrong code; find the reason it looks that way.
- Say which findings are confirmed defects, which are risks, and which are optional.
- No cosmetic churn, no redesign without evidence. Weigh maintenance cost against benefit.
- Lacking evidence, write "I don't know" and name the check that would settle it.
- Ship no edits. Probes are the exception: keep them in a scratch file prefixed `scratch_`, put the probe and its output in the Evidence line, revert it, and confirm `git status --porcelain` is empty before the report ships. Widening a visibility to `pub(crate)` so a probe can observe something is allowed under that same revert; editing the logic of a function you are reviewing is not. A `Cargo.lock` touched by rule 2 is expected noise, so name it rather than reporting it.

## 4. Standards for the code and for your fixes

- Simpler is better. Once a change is justified on other grounds, write the smallest version that works. Shortness alone never justifies touching working code.
- Complexity needs a stated reason: a measured cost, a correctness requirement, or a caller that exists today.
- Avoid overly defensive programming. Validate untrusted input once at the boundary, then trust the types. Repeated checks of a guaranteed invariant, fallback defaults that hide a bug, and branches for unreachable states are findings. Delete such a branch by making the state unrepresentable, never by swapping in `unreachable!`. A real boundary check stays, and so does one whose necessity is unclear until you trace a caller that proves otherwise.
- Comment why, never what. Redundant, stale, and commented-out code are findings. Docs stay short, no emoji.
- Gate every fix on this ladder, stop at the first rung that holds, and report that rung: 1 delete it, 2 reuse what the crate or workspace has, 3 std or core, 4 a lint, a derive, or a type-level invariant, 5 an already-declared dependency, 6 one line, 7 the minimum code that works. A fix that adds an abstraction, trait, feature flag, or dependency names the rung that ruled out every simpler option. Report the rung with the reason it stopped there, as in `Rung 3: slice::windows replaces the hand-rolled index loop; rung 2 ruled out, the workspace has no equivalent helper.`

## 5. What to hunt

Skip categories the target does not contain. "No concurrency issues found" in a single-threaded crate is filler.

- **Correctness**: overflow, truncating `as`, off-by-one, partial `read`/`write`, `unwrap`/`expect`/panic in library or request paths (UB across FFI), swallowed errors and `let _ =`, state left half-mutated on the error path, `Drop` order and leaks, `Serialize`/`Deserialize` and untagged-enum mismatches, persisted-format versioning, path and non-UTF-8 `OsStr` handling, `Instant` vs `SystemTime`, `Duration` underflow.
- **Unsafe**: aliasing, provenance, alignment, `MaybeUninit`, `get_unchecked` bounds, `transmute`, lifetime extension. Every hand-written `unsafe impl Send`/`Sync` is a finding until a comment names the invariant that makes it sound.
- **Concurrency**: lock ordering, a lock held across `.await`, blocking work on a runtime thread, cancellation safety in `select!`, shutdown and detached tasks, `Relaxed` where `Acquire`/`Release` belongs, unbounded channels turning backpressure into memory growth.
- **Memory**: clones that serve the borrow checker rather than the logic, `to_string`/`format!`/`collect` in hot paths, missing `with_capacity`, intermediate collections between iterator stages, `Arc` traffic in loops, buffers reallocated per call, large enum variants and futures. Do not trade a real allocation for a lifetime puzzle unmeasured.
- **Performance**: algorithmic cost first, `Vec::contains` in a loop where a `HashSet` belongs, recomputed parsing, hashing, or regex construction (`LazyLock`), unbuffered and per-item I/O. Speculative micro-optimizations are not findings; recommend profiling when the evidence is thin.
- **Design**: ownership taken where a borrow works, `&[T]`/`&str` in signatures, `Arc<Mutex<T>>` around single-owner state, one-implementor traits and wrappers carrying no invariant, `pub` fields and leaked dependency types, missing `#[non_exhaustive]`, `thiserror` for libraries and `anyhow` for binaries, missing `#[must_use]` and standard derives.
- **Cleanup**: dead code, duplicate logic, unused dependencies and features, stale comments, misleading names, premature abstractions, shims with no remaining consumer, CI gates that never run.
- **Testing**: boundaries and error paths, concurrency, serialization round-trips, every `unsafe` block, past regressions, hot paths. Name the specific missing test, as a test name plus the input that fails without it.

## 6. Report

Per finding: `[Severity] [Confidence] [Category] file:line`, then Problem, Evidence, Impact, Fix with its rung, Tradeoffs, Validate. Severity runs Critical to Optional. Confidence is Confirmed only when you ran something that proves it and the Evidence line carries the output, otherwise Likely or Unverified naming the check that would settle it. Category comes from the hunt list, plus Standards for a violation that fits none of them. When you cannot tell a defect from a preference, it is a preference.

Sections, keeping these numbers even when one is missing: 1 executive assessment including the free-signal results, 2 correctness and soundness, which is where Unsafe findings go, 3 concurrency and memory, 4 allocation and performance, 5 refactoring, cleanup, and standards, 6 validation plan, 7 reviewed and sound so the reader knows the coverage. Sections 1, 6, and 7 are required; drop 2 through 5 when empty instead of filling them. Write section 7 as one line per module, naming the categories you cleared there. Order findings by impact, not by file, and do not pad.
