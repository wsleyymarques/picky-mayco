---
name: consume
description: "Recall and ingest durable implementation lessons. Use at the start of Picky Mayco tasks to load relevant prior lessons and at the end when a correction, root cause, failed check, review finding, or reusable insight should prevent recurrence."
---

# Consume

Maintain a small evidence-backed memory loop for implementation work. Store rules that change future decisions, not task diaries.

Resolve a persistent memory root outside the installed skill package. Use `PICKY_MAYCO_HOME` when configured; otherwise use `$XDG_DATA_HOME/picky-mayco`, `~/.local/share/picky-mayco`, or `%LOCALAPPDATA%\picky-mayco` according to the host platform. Ask for a writable location when none is available. Lessons live under `<memory-root>/lessons/global/` or `<memory-root>/lessons/projects/`. Create domain files only when a real lesson exists.

## Choose mode

- **Recall:** task is starting or strategy is being prepared.
- **Consume:** implementation produced a correction, root cause, surprising failure, review finding, recurring omission, or reusable non-obvious insight.
- When invoked without an explicit mode, infer it from task phase. Ask only when phase is genuinely ambiguous.

## Recall

1. Classify task into `general`, `frontend`, `backend`, `images`, `qa`, or `docs`.
2. Read only matching files under `<memory-root>/lessons/global/` plus matching files for the current repository under `<memory-root>/lessons/projects/<repository-key>/`.
3. Derive `<repository-key>` from normalized Git remote owner and repository name when available; otherwise use normalized repository-root basename. Never store the remote URL.
4. Apply active lessons to analysis, questions, strategy, implementation, and verification. Surface conflicts with current repository instructions instead of silently overriding them.

Recall completes when every relevant active lesson is mapped to a task decision or explicitly marked not applicable.

## Consume

Accept evidence from:

- User correction or rejected behavior.
- Confirmed bug root cause.
- Failed test, build, lint, typecheck, Cypress run, or review finding.
- Non-obvious repository behavior that caused rework.
- Repeated omission caught before delivery.

Do not store speculation, generic advice, raw logs, temporary environment failures, task summaries, secrets, personal data, credentials, absolute machine paths, or rules already owned by another skill.

For each candidate:

1. Verify cause and successful correction with current evidence.
2. Decide scope:
   - **Global:** likely applies across independent repositories using similar technology or behavior.
   - **Project:** depends on this repository's architecture, domain, infrastructure, or conventions.
3. If rule reveals a current implementation gap, fix that gap and rerun affected documentation and QA before recording completion.
4. Search existing lessons and specialist skills. Merge with the closest rule instead of adding a synonym or duplicate.
5. Write or update only the matching domain file:
   - Global: `<memory-root>/lessons/global/<domain>.md`
   - Project: `<memory-root>/lessons/projects/<repository-key>/<domain>.md`
6. Increment `Occurrences` only for an independent recurrence with fresh evidence.
7. Promote a lesson into the relevant Picky Mayco specialist skill when it has two independent occurrences or one high-severity, broadly applicable failure. Use skill-authoring guidance such as `$skill-creator` and `$writing-for-agents` when available. Keep only a concise promotion pointer in the lesson store so the rule has one source of truth.

## Lesson format

```markdown
## Stable lesson title

- Applies when: Observable trigger.
- Failure: What went wrong or was repeatedly omitted.
- Rule: Concrete future behavior.
- Verify: Check proving the rule was applied.
- Occurrences: 1
- Status: Active
```

Use `Status: Promoted to $skill-name` after promotion and remove the duplicated detailed rule from the lesson entry.

## Completion

Report one of:

- `No durable lesson`: no qualifying evidence.
- `Lesson added`: name, scope, and destination.
- `Lesson updated`: name and new evidence count.
- `Lesson promoted`: destination skill and verification performed.

Finish only when stored content is deduplicated, sanitized, actionable, and connected to a repeatable verification step.
