---
name: picky-mayco-docs
description: "Maintain implementation documentation for every Picky Mayco task. Use in the final phase to synchronize Markdown, the project Cypress selector catalog, and the repository-root index.md folder map with the implemented code."
---

# Picky Mayco Docs

Make repository documentation describe the final code, not the original plan. Run this skill near the end of every implementation, before the final QA gate.

Read [repository index standard](references/repository-index.md) before creating or updating `index.md`.

## Markdown standard

- Inspect existing documentation and repository instructions before choosing a file or format. Update the established source of truth instead of creating a competing document.
- Use the repository's dominant documentation language. Keep headings descriptive, links relative, code fences language-tagged, and tables reserved for repeated fields or maps.
- Write current, verifiable behavior. Remove or revise stale statements introduced by the implementation.
- Keep secrets, credential values, populated environment variables, machine-specific absolute paths, generated output, and dependency internals out of documentation.
- Preserve human-written content. Make narrow edits unless a full rewrite was requested or the existing document is wholly generated.

## Cypress document

When frontend selectors change, reconcile code, Cypress tests, and the project selector catalog using the conventions from `$picky-mayco-qa`:

1. Search changed and neighboring flows for added, renamed, and removed `data-cy` values.
2. Update the existing Cypress catalog. If none exists, create `docs/qa/cypress-selectors.md`.
3. Group entries by feature and flow. Represent dynamic values with placeholders such as `{userId}` and explain their source.
4. Remove catalog entries only after confirming their selector no longer exists or was intentionally replaced.
5. Finish when every changed selector has one accurate catalog entry and every affected Cypress test uses the current value.

Tasks without frontend selector changes leave the Cypress catalog untouched.

## Repository index

At the end of every implementation, create or update lowercase `index.md` at each Git repository root changed by the task. The index is an agent navigation map, not a recursive inventory.

- Describe meaningful source, application, package, module, feature, test, migration, script, configuration, and documentation folders.
- Include what each folder owns and the main kinds of content inside it.
- Add, rename, or remove entries to match the final filesystem. Never document planned paths that do not exist.
- Exclude `.git`, dependencies, build output, caches, coverage, uploaded files, generated artifacts, and secret-bearing paths.
- In a monorepo, use one root index with clear app/package sections unless repository instructions require additional indexes.

## Completion

Inspect the final diff and filesystem after documentation updates. Finish when:

- Cypress catalog matches changed selectors and tests.
- Root `index.md` maps all meaningful folders affected by the task and contains no stale paths.
- Relative links resolve.
- Human-authored sections remain intact.
- Final handoff names every Markdown file created or updated.
