# Repository index

Picky Mayco packages a full-stack implementation workflow as a portable collection of Agent Skills.

<!-- picky-mayco:index:start -->
## Repository map

| Path | Responsibility | Main contents |
| --- | --- | --- |
| [`skills/`](skills/) | Agent workflows distributed by the plugin. | Router, frontend, backend, image, QA, documentation, and learning skills. |
| [`skills/picky-mayco/`](skills/picky-mayco/) | Coordinates task analysis, specialist selection, implementation, and handoff. | Router `SKILL.md` and Codex interface metadata. |
| [`skills/picky-mayco-frontend/`](skills/picky-mayco-frontend/) | Owns browser-facing implementation guidance. | Visual-reference analysis, validation catalog, responsive rules, and UI state coverage. |
| [`skills/picky-mayco-backend/`](skills/picky-mayco-backend/) | Owns server-facing implementation guidance. | Boundary validation, domain invariants, authorization, persistence, and API contracts. |
| [`skills/picky-mayco-images/`](skills/picky-mayco-images/) | Owns image workflows across client and server. | Upload, validation, transformation, storage, delivery, and display rules. |
| [`skills/picky-mayco-qa/`](skills/picky-mayco-qa/) | Owns final verification and test automation readiness. | Test matrix, Cypress conventions, and final test gate. |
| [`skills/picky-mayco-docs/`](skills/picky-mayco-docs/) | Owns implementation documentation consistency. | Markdown rules, Cypress catalog maintenance, and repository index standard. |
| [`skills/consume/`](skills/consume/) | Owns durable implementation learning. | Recall, ingestion, deduplication, sanitization, and promotion rules. |
| [`scripts/`](scripts/) | Provides deterministic package operations. | Dependency-free validation and local installation commands. |
| [`tests/`](tests/) | Verifies package structure and installer behavior. | Standard-library integration tests. |
| [`.github/workflows/`](.github/workflows/) | Runs repository quality gates. | Validation and test workflow for pushes and pull requests. |

<!-- picky-mayco:index:end -->
