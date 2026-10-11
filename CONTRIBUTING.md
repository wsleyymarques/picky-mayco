# Contributing

Keep each change focused on observable agent behavior. Update the smallest skill that owns the rule and avoid copying the same instruction into multiple skills.

## Workflow

1. Create a branch from `main`.
2. Change the owning `SKILL.md`, reference, script, or test.
3. Update `README.md` and `index.md` only when package behavior or structure changed.
4. Run:

   ```bash
   python3 scripts/validate.py
   python3 -m unittest discover -s tests -v
   ```

5. Open a pull request explaining the observed problem, the behavioral rule, and verification evidence.

## Skill rules

- Keep `name` aligned with the skill directory.
- Make `description` state capability and activation conditions.
- Put branch-specific detail in `references/` and link it from `SKILL.md`.
- Keep repository-specific lessons out of the package.
- Never add credentials, populated environment files, personal data, raw logs, or absolute machine paths.
- Preserve explicit user instructions over skill preferences.

## Changes to learning behavior

Learning rules require evidence from a confirmed correction, root cause, failed check, review finding, or repeatable repository behavior. Generic advice and task summaries do not belong in the lesson store.
