---
name: picky-mayco-frontend
description: "Review or implement frontend tasks with strict field validation, responsive behavior, state coverage, and repository-aligned module boundaries. Use for UI, forms, client state, browser behavior, and frontend code reached through Picky Mayco."
---

# Picky Mayco Frontend

Inspect the framework, design system, form library, validation library, styling approach, breakpoints, and neighboring features before choosing patterns. Reuse established components and schemas where they meet the task.

When a task adds or changes a form, field, filter, search, inline edit, dynamic collection, or upload, read [common validation modes](references/validation-catalog.md). Apply only relevant modes, but account for every changed field and cross-field rule.

## Visual reference

When the user provides screenshots, Figma exports, or other screen references, inspect each one before strategy. Extract the visible screen structure, component hierarchy, spacing, alignment, typography, colors, content behavior, control states, and source viewport. Map those findings to repository components and design tokens.

Keep three categories explicit: **observed** visual requirements, **inferred** responsive or interactive behavior, and **unknown** states. Written task requirements define behavior; visual references define visible intent. Ask before strategy when they conflict or when an unknown changes UX, scope, or contract. A single viewport is evidence only for that viewport, so derive other breakpoints from repository patterns and flag material ambiguity.

When the application can run, verify the result against the reference at a matching viewport. Record intentional differences and their reason instead of silently drifting from the supplied design.

## Learning loop

Before analysis, invoke `$consume` in recall mode for the `frontend` domain and current repository. Apply every relevant active lesson to the field matrix, implementation, and verification; explicitly discard lessons that do not match the task.

Before completion, invoke `$consume` in consume mode when the work produced a user correction, confirmed root cause, failed check or review, avoidable rework, repository gotcha, or reusable non-obvious insight. If the resulting lesson exposes a gap in the current change, reopen the implementation, fix it, and rerun affected QA and documentation checks. Report the learning outcome even when there is no durable lesson.

## Field contract

For every changed input, derive constraints from domain rules, API contract, and persistence limits. Build a field matrix covering value semantics, normalization, boundaries, dependencies, lifecycle states, API failure, responsive behavior, and test evidence.

Use native input attributes for affordance and schema or handler validation for enforcement. Show accessible, field-specific errors. Preserve actionable server errors. Prevent duplicate submission while pending and define retry behavior.

## Responsive behavior

- Verify smallest supported viewport, intermediate width, and wide layout.
- Keep controls inside their containers. Use flexible width and `min-width: 0` where flex/grid children could overflow.
- Make long labels, values, validation messages, filenames, URLs, and unbroken user content wrap or truncate deliberately. Keep full content accessible when truncating.
- Keep touch targets usable and avoid layouts that depend on hover.
- Check keyboard navigation, visible focus, label association, and error announcement.

## States and boundaries

Cover relevant initial, loading, empty, success, error, disabled, unauthorized, and stale-data states. Keep server data, form state, and transient UI state in their established layers.

Follow repository feature boundaries. Use `index` files as explicit module APIs only when that convention exists; avoid broad barrels that hide ownership or introduce cycles.

## Completion

For every changed user flow, use `$picky-mayco-qa` as the source of truth for Cypress-ready selectors, selector documentation, and final tests.

Before declaring frontend complete, account for every changed field, cross-field rule, interactive state, supported viewport, supplied visual reference, API error path, Cypress interaction point, and relevant test/check. Report any intentional visual difference or unsupported case.
