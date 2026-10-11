---
name: picky-mayco-backend
description: "Review or implement backend tasks with strict boundary validation, domain invariants, authorization, persistence safety, and API-contract coverage. Use for APIs, services, jobs, databases, and backend code reached through Picky Mayco."
---

# Picky Mayco Backend

Inspect the framework, module boundaries, schema, migrations, authorization model, error conventions, tests, and neighboring features before choosing patterns.

## Learning loop

Before analysis, invoke `$consume` in recall mode for the `backend` domain and current repository. Apply every relevant active lesson to the request contract, domain invariants, implementation, and verification; explicitly discard lessons that do not match the task.

Before completion, invoke `$consume` in consume mode when the work produced a user correction, confirmed root cause, failed check or review, avoidable rework, repository gotcha, or reusable non-obvious insight. If the resulting lesson exposes a gap in the current change, reopen the implementation, fix it, and rerun affected QA and documentation checks. Report the learning outcome even when there is no durable lesson.

## Request and domain contract

For every changed operation, account for each applicable item:

- Validate request shape, types, requiredness, nullability, ranges, lengths, formats, enums, collections, and unknown fields at the transport boundary.
- Enforce business invariants in the domain or service layer, independent of frontend checks.
- Normalize only where semantics are explicit; keep stored and returned values consistent.
- Verify authentication, authorization, tenant or owner scope, and information disclosure for success and failure paths.
- Keep response shape, status codes, error codes, pagination, sorting, filtering, and null behavior stable or explicitly migrate consumers.

## Persistence and operations

- Back important invariants with database constraints when practical.
- Use transactions where partial writes would leave invalid state. Define concurrency, duplicate request, retry, and idempotency behavior when relevant.
- Plan migrations for existing data, deployment order, rollback compatibility, defaults, and indexes.
- Bound queries and batch work. Check pagination and avoid accidental unbounded reads or N+1 access.
- Log operational context without secrets, credentials, tokens, or unnecessary personal data.
- Keep real environment values outside code and version control. Use validated configuration and placeholder-only example env files when established by the repository.

## Failure and verification

Map expected domain failures to stable API errors. Preserve unexpected failures for observability without exposing internals.

Before declaring backend complete, account for validation failures, authorization failures, missing records, conflicts, persistence failure, relevant edge values, contract tests, migration checks, and project checks. Report any intentionally unsupported case.
