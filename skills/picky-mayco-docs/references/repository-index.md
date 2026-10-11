# Repository index standard

Create `index.md` in the Git repository root. Use it as a fast map for agents entering an unfamiliar codebase.

## Managed region

When creating the file, wrap the maintained map in markers:

```markdown
# Repository index

Short factual description of the repository.

<!-- picky-mayco:index:start -->
## Repository map

| Path | Responsibility | Main contents |
| --- | --- | --- |
| [`src/features/users/`](src/features/users/) | User management. | Forms, API adapters, schemas, and feature tests. |

<!-- picky-mayco:index:end -->
```

When `index.md` exists:

- Update content between matching markers.
- Preserve everything outside the managed region.
- If markers are absent, inspect the existing purpose and structure. Merge a managed region without overwriting human content.
- If malformed or unmatched markers exist, stop and ask before replacing content.

## What to map

Start with folders that help an agent decide where work belongs:

- Applications and packages.
- Source roots and architectural layers.
- Domain modules and independently owned features.
- Tests, fixtures, Cypress support, and test data.
- Database schemas, migrations, and seeds.
- Scripts, configuration, public assets, and maintained documentation.

Use enough depth to expose ownership boundaries. Collapse purely mechanical nesting into the nearest meaningful parent. Do not list every file or mirror the whole tree.

## Entry rules

- `Path`: repository-relative Markdown link ending in `/` for directories.
- `Responsibility`: one sentence stating what the folder owns.
- `Main contents`: concise content types, important entrypoints, or interfaces found there.
- Base every entry on inspected files. Avoid inferred or aspirational descriptions.
- Keep rows in stable architectural order: apps/packages, source/domain, persistence, tests, scripts/config, docs/assets.
- Update renamed or deleted paths in the same implementation that changes them.

Do not add timestamps, change logs, task summaries, local absolute paths, generated directories, dependency trees, or secret values. Those create churn or risk without improving navigation.
