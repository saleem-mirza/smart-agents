---
name: categorize-docs
description: Read, rename, and file loose documents into the correct folders. Use when the user asks to organize, sort, file, categorize, or clean up a folder of documents, downloads, scans, receipts, or PDFs, or asks where a document belongs.
argument-hint: [folder to organize; empty = current folder]
---

# Categorize Documents

Target: $ARGUMENTS. Empty means the current directory.

Read every loose document in the target folder, then propose a filing plan and, once approved, rename and file each document into the correct folder. Follow these rules exactly.

## What counts as a loose document

In scope: regular files sitting in the target folder's root.

Never touched:
- Dotfiles and OS metadata (`.DS_Store`, `Thumbs.db`, `.gitignore`).
- Symlinks.
- Repo furniture: `README*`, `LICENSE*`, `Makefile`, `CHANGELOG*`, and similar.
- Anything already inside a subfolder.
- The `_duplicates/` folder.

Recurse into subfolders only when the user asks.

## Phase 1: Survey (read-only)

Change nothing in this phase.

- List the current folders and their contents.
- Open and read each in-scope file. For PDFs, extract text with the first tool that works: `pdftotext` (poppler), then `python3 -c "import pypdf"`, then the Read tool's `pages` parameter. If none work, ask the user how to proceed. Never install packages into system Python. For images, read them visually.
- Take the date, category, and any other classifying detail from the document content, not the filename. When the filename date and the content date disagree, file by the content date and flag the mismatch.
- Infer the folder taxonomy and the file-naming convention from the documents already filed. Match them exactly: terminology, capitalization, and date format. If filed documents use no separators (e.g. `MMDDYYYY`), match that.
- Treat the deepest existing folder that fits a document as its destination.

**Cold start.** When the folder is empty, or has too few filed documents to establish a pattern, do not guess silently. Propose `YYYY-MM-DD-descriptor.ext` as the default scheme, omitting the date for undated documents, as part of the Phase 2 proposal, and let the user amend it.

## Phase 2: Propose, then stop

Print the plan and wait for approval. Make no moves, renames, deletions, or folder creations before the user approves.

1. **Filing table**, one row per document: current name → destination path and new name → reason. Mark rows that require a new folder.
2. **Suspected duplicates table**, each candidate mapped to the file it matches. Compare by extracted text, not by byte hash: re-exports differ in bytes but not content. This comparison is a heuristic that OCR noise and two genuinely similar records both defeat, so every candidate needs the user's eye before anything moves.
3. **Cannot place**, files that could not be read or match no category.

If a cold-start default scheme is in play, state it above the tables.

## Phase 3: Execute

Apply the approved plan.

- Use `git mv` inside a git repo, `mv` otherwise.
- Never overwrite an existing destination file. On a name collision, stop that one move, report it, and let the user decide.
- Suspected duplicates move to `_duplicates/` under their original name. Delete nothing.
- Leave unreadable, corrupt, or encrypted files where they are. Never guess a destination for a file you could not read.
- When a document already has a sidecar of the same base name (e.g. `statement.pdf` and `statement.md`), move and rename both together so the base names stay matched. This skill does not create sidecars.

## Report back

- Confirm whether the root has loose files left.
- Every file moved, with its old and new name and destination.
- Duplicates moved to `_duplicates/`, each mapped to the existing file it matched.
- Files left unfiled, each with the reason.
- Name collisions encountered.
- Date mismatches, ambiguous placements, and new folders created.
