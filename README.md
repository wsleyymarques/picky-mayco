# Picky Mayco

Picky Mayco is an opinionated Agent Skills suite for planning, implementing, verifying, and documenting full-stack changes. It keeps frontend and backend analysis explicit, treats supplied designs as evidence, adds Cypress-ready interaction points, and records durable lessons without turning task history into prompt baggage.

## Included skills

| Skill | Responsibility |
| --- | --- |
| `picky-mayco` | Explicitly invoked router for task analysis and implementation. |
| `picky-mayco-frontend` | Field validation, visual references, responsive behavior, accessibility, and client state. |
| `picky-mayco-backend` | Request validation, domain invariants, authorization, persistence, and API contracts. |
| `picky-mayco-images` | Image selection, upload, transformation, storage, delivery, and display. |
| `picky-mayco-qa` | Test matrix, Cypress readiness, and the final verification gate. |
| `picky-mayco-docs` | Markdown reconciliation, Cypress selector catalog, and repository `index.md`. |
| `consume` | Persistent recall and ingestion of evidence-backed implementation lessons. |

The repository is also a portable skills-only plugin. `plugin.json` is the package manifest and every skill lives under `skills/<name>/SKILL.md`.

## Install in Codex

Clone the repository, then run:

```bash
python3 scripts/install.py
```

The installer validates the package and copies every skill into `${CODEX_HOME}/skills` when `CODEX_HOME` is set, otherwise `~/.codex/skills`. It refuses to overwrite an existing skill.

To install directly from a public GitHub repository with Codex's built-in installer, ask Codex:

```text
$skill-installer install every skill under the skills directory from this GitHub repository.
```

Or use its helper with the repository owner and name:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo wsleyymarques/picky-mayco \
  --path \
    skills/picky-mayco \
    skills/picky-mayco-frontend \
    skills/picky-mayco-backend \
    skills/picky-mayco-images \
    skills/picky-mayco-qa \
    skills/picky-mayco-docs \
    skills/consume
```

Installed skills become available on the next agent turn. Other Agent Skills-compatible hosts can load the individual directories under `skills/` or install the repository as a plugin when they support the Agent Plugins manifest.

## Use

Start a task explicitly with:

```text
$picky-mayco analyze and implement this task: ...
```

Attach task screenshots or Figma exports when available. The frontend specialist separates observed design requirements from inferred responsive behavior and unknown states before strategy.

The router asks only behavior-changing questions, produces separate frontend and backend strategy sections, waits for approval unless immediate implementation was requested, and finishes with QA, documentation, and learning gates.

## Optional tools

- `caveman`: used when available for concise chat updates; normal concise communication is the fallback.
- `rtk`: preferred when available for compact command output; native commands are the fallback.

Neither optional tool is required to install or run the suite.

## Durable lessons

`consume` stores lessons outside the installed package so plugin upgrades do not erase them. Storage priority:

1. `PICKY_MAYCO_HOME`, when configured.
2. `$XDG_DATA_HOME/picky-mayco` on Unix-like systems.
3. `~/.local/share/picky-mayco` on Unix-like systems.
4. `%LOCALAPPDATA%\picky-mayco` on Windows.

The skill asks for a writable location when none is available. Lesson files exclude credentials, personal data, raw logs, and machine-specific repository paths.

## Validate

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Validation uses only the Python standard library.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security-sensitive findings belong in a private report as described in [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
