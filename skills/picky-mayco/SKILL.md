---
name: picky-mayco
description: "Run Mayco's strict task-analysis and implementation workflow."
disable-model-invocation: true
---

# Picky Mayco

Turn a task description into a complete implementation strategy before code changes. Prevent small validation, responsive-layout, API-contract, and operational details from being forgotten.

Keep chat updates and handoff concise. Use `$caveman` in full mode when it is available. Keep persisted code, comments, and documentation in normal prose.

Prefer the `rtk` proxy when it is available for supported file inspection, search, Git, test, build, lint, and other noisy shell commands. Fall back to native commands when `rtk` is unavailable, exact unfiltered output is required, or its result is insufficient.

## Workflow

1. Read the task and inspect every attached visual reference plus the relevant repository paths, project instructions, neighboring implementations, scripts, schemas, and tests. Treat screenshots and Figma exports as frontend evidence and route their detailed analysis to `$picky-mayco-frontend`. Finish when every affected surface has evidence.
2. Classify scope as **Frontend**, **Backend**, and **Shared contract**. Always report Frontend and Backend; write `No change` with the reason when one side is unaffected.
3. Use `$consume` in recall mode. Read only global lessons relevant to the classified scope and lessons for the current repository. Map applicable lessons into the strategy.
4. Load only applicable specialist guidance:
   - Use `$picky-mayco-frontend` for UI, forms, client state, browser behavior, or frontend code.
   - Use `$picky-mayco-backend` for APIs, domain logic, persistence, jobs, or backend code.
   - Also use `$picky-mayco-images` whenever images are selected, uploaded, transformed, stored, returned, cached, or displayed.
   - Use `$picky-mayco-qa` for every implementation. It owns the final test gate and Cypress readiness. Read its Cypress selector reference whenever a frontend flow changes.
   - Use `$picky-mayco-docs` in the final phase of every implementation. It owns Markdown consistency, the project Cypress catalog, and the root `index.md` repository map.
5. List concrete omissions and risks found on each side. Tie each item to task behavior or repository evidence.
6. Ask concise questions when an answer changes behavior, contract, data model, authorization, UX, or implementation scope. Ask before choosing a strategy. Continue without questions when repository evidence resolves the choice.
7. Produce one strategy with explicit **Frontend**, **Backend**, **Shared contract**, and **Verification** sections. Verification must split frontend, backend, Cypress/QA, and final project checks. Include relevant edge cases, validation ownership, states, tests, and rollout or migration needs.
8. Wait for strategy approval before implementation unless the user explicitly requested immediate implementation. Resolve blocking questions first in either case.
9. During implementation, apply every loaded specialist rule and run focused checks while changing code.
10. Before the final gate, use `$picky-mayco-docs` to reconcile changed Markdown, the Cypress selector catalog, and the repository-root `index.md` against the final code structure.
11. Finish through the `$picky-mayco-qa` test gate. Report each command and result; report every unrun or failed check with its reason.
12. Use `$consume` in consume mode. Capture any durable lesson from user corrections, root causes, failed checks, review findings, or non-obvious implementation behavior. If the lesson exposes a current gap, reopen implementation and repeat documentation and QA before handoff.

## Global invariants

- Repository instructions and established architecture outrank personal preferences unless they create a correctness or security problem; surface conflicts.
- Keep client and server contracts aligned: field names, requiredness, limits, enum values, nullability, error shapes, and image constraints.
- Keep secrets outside code and version control. Never create or commit a populated `.env` file or real credential. Update an example env file with placeholders only when repository convention requires it.
- Treat frontend validation as fast feedback and backend validation as authoritative enforcement.
- Design changed frontend flows for stable Cypress automation. Keep selectors and selector documentation aligned with the UI.
- Keep one current `index.md` at each Git repository root. It maps meaningful folders to their responsibilities and contents for future agents.
- Report final result under Frontend, Backend, Shared contract, Verification, and Learning, even when a section says `No change` or `No durable lesson`.
