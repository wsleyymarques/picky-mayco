---
name: picky-mayco-qa
description: "Plan and execute final verification for Picky Mayco implementations, including frontend, backend, build, and Cypress readiness. Use for every implementation and for any task that adds or changes a user flow."
---

# Picky Mayco QA

Turn task behavior and implementation risk into a test matrix, make changed frontend flows automatable, then run a final evidence-based gate.

When a frontend flow changes, read [Cypress selector conventions](references/cypress-selectors.md) before planning selectors or tests.

## Test matrix

Map each acceptance behavior and material failure mode to the highest useful test seam already supported by the repository. Cover both sides when applicable:

- Frontend: field constraints, state transitions, API errors, permissions, responsive behavior, and the complete user flow.
- Backend: request boundaries, domain invariants, authorization, persistence, conflicts, and stable response/error contracts.
- Shared contract: requiredness, nullability, limits, enum values, dates, pagination, and image constraints.
- Regression: neighboring behavior with credible break risk.

Prefer observable behavior over internal implementation details. Reuse repository fixtures, factories, seeds, helpers, and test patterns.

## Cypress readiness

- Add stable `data-cy` selectors to changed interaction points and critical state-dependent actions. Put each selector on the actual actionable element.
- Update the repository's selector catalog as the task evolves, not as a later memory exercise. If none exists, create `docs/qa/cypress-selectors.md` using the reference format. Use `$picky-mayco-docs` for the final reconciliation.
- When Cypress already exists, add or update coverage for the changed critical flow and its highest-risk failure path.
- When Cypress is absent, keep UI selector-ready and include the proposed E2E scenario in Verification. Ask before introducing Cypress or new test infrastructure.
- Keep test setup deterministic. Prefer API, task, fixture, or seed setup over unrelated UI navigation.
- Synchronize on observable requests and states with aliases/assertions. Avoid fixed-time waits.
- Keep tests isolated and clean up changed persistent state using repository-supported mechanisms.

## Final test gate

Inspect project instructions, CI, and package scripts to discover exact commands. Run supported checks relevant to changed scope:

1. Focused tests for changed modules and contracts.
2. Formatting or format check.
3. Lint and static analysis.
4. Type checking.
5. Frontend unit or component tests.
6. Backend unit or integration tests.
7. Cypress E2E for impacted flows when configured.
8. Production build.
9. Migration or schema validation when persistence changed.
10. Markdown links, Cypress catalog, and root `index.md` consistency when documentation changed.

Use `rtk` wrappers when they preserve needed evidence. Use native commands when filtered output hides decisive detail.

Do not claim a check passed without command evidence from the current implementation. For every failed or unrun check, report command, shortest decisive output or reason, and resulting risk. Completion requires every planned behavior mapped to passing evidence or an explicit unresolved item.
