# Cypress selector conventions

This standard generalizes the useful patterns from Urbe's selector catalog. Do not copy Urbe feature names into another project. Use the target project's canonical domain vocabulary.

## Selector grammar

Use colon-separated semantic segments:

```text
<feature>:<target>:<action>
<feature>:<entity>-<id>:<action>
```

- Use lowercase kebab-case for fixed segments.
- Name behavior and domain identity, not DOM structure, styling, visible copy, or screen position.
- Dynamic row selectors include the record's real stable ID: `users:user-${userId}:edit`.
- Dynamic options use the stable value emitted by the component, never its display label. Centralize normalization; default to lowercase kebab-case when no project convention exists.
- Preserve an established project convention when it is already stable and documented.

## Action vocabulary

Use one action consistently:

- `fill`: text-like input or textarea.
- `select`: select trigger, option, date choice, or tab.
- `toggle`: checkbox, switch, or visibility toggle.
- `open`: dialog, drawer, menu, creation flow, or details without route navigation.
- `navigate`: route-changing control.
- `submit`: form or operation submission.
- `cancel`: form or dialog cancellation.
- `confirm`: destructive or state-changing dialog confirmation.
- `clear`: clear filters or values.
- `view`, `edit`, `remove`, `activate`, `inactivate`, `export`: explicit record actions.

Add a new action only when none above describes the user behavior. Document it before reuse.

## Required patterns

Forms:

```text
users:full-name:fill
users:role:select
users:cancel:cancel
users:create:submit
users:update:submit
```

Create and edit forms reuse field selectors. Submit selectors distinguish operations when behavior differs.

Searchable selects expose all three automation points:

```text
projects:municipality:select
projects:municipality-search:fill
projects:municipality-${municipalityId}:select
```

Record rows and menus include identity:

```text
teams:team-${teamId}:open-actions
teams:team-${teamId}:edit
teams:team-${teamId}:remove
```

State-changing dialogs expose cancel and confirm separately:

```text
users:status-dialog:cancel
users:inactivate:confirm
users:activate:confirm
```

Use distinct `activate` and `inactivate` selectors when action changes with current state.

## Placement and scope

- Attach selector to input, button, link, option, tab, menu item, or dialog action Cypress will operate.
- Instrument changed flow entry points, fields, dynamic options, row actions, navigation, submit, cancel, and confirmation.
- Keep `data-cy` independent from React Hook Form `name`, DOM IDs, analytics IDs, and CSS classes.
- Use text and accessible roles for content assertions when stable. Add `data-cy` to non-interactive output only when it is a necessary stable assertion boundary.
- Avoid positional selectors, generated classes, DOM traversal, and translated visible text as interaction locators.

## Catalog

Maintain one selector catalog in the repository. Group selectors by feature and flow. Record dynamic placeholders such as `{userId}` and explain their source.

Use this table shape:

```markdown
| `data-cy` | Represents |
| --- | --- |
| `users:email:fill` | User email field. |
| `users:user-{userId}:edit` | Opens edit flow for the rendered user. |
```

Update catalog whenever selectors are added, renamed, or removed. A rename must update implementation, Cypress tests, and catalog in the same change.

## Cypress test behavior

- Exercise user-visible outcomes, not component internals.
- Cover happy path plus highest-risk validation, authorization, or server-failure path.
- For forms, assert required, invalid, boundary, successful submission, duplicate-submit prevention, and actionable server error where relevant.
- For responsive flows, run critical smoke coverage at one narrow and one wide viewport when layout or navigation differs.
- Use `cy.intercept()` aliases or observable UI states instead of arbitrary waits.
- Derive dynamic selector IDs from controlled fixtures, aliases, or API responses. Never depend on row order.
