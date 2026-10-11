# Common frontend validation modes

Use this catalog to expose frequent omissions before implementation. Apply only sections relevant to the changed flow. Backend enforcement remains authoritative.

## Field matrix

Create a compact matrix before coding forms or filters:

| Field or action | Value semantics | Normalization | Boundaries | Dependencies | Failure states | Evidence |
| --- | --- | --- | --- | --- | --- | --- |

Every changed field or action needs either an applicable rule or an explicit `Not applicable` reason.

## Text and identity values

- Distinguish `undefined`, `null`, empty string, and whitespace-only input.
- Decide whether trimming happens before required and length validation. Keep displayed, submitted, and stored behavior aligned.
- Test minimum and maximum length at `limit - 1`, `limit`, and `limit + 1` where boundaries matter.
- Account for pasted content, multiline input, repeated spaces, line endings, accents, emoji, combining Unicode characters, and invisible characters when the domain permits free text.
- Keep masks separate from raw submitted values. Verify paste, autofill, deletion, and partially completed masks.
- For identifiers, define case sensitivity, leading zeros, allowed separators, and whether formatting characters are stored.
- Constrain URLs to allowed schemes and normalize only when product behavior is explicit.

## Numbers, currency, percentage, and measurement

- Treat empty value separately from zero. Avoid truthiness checks for numeric fields.
- Define minimum, maximum, sign, decimal precision, rounding, step, and whether scientific notation is accepted.
- Parse locale separators deliberately. Never silently reinterpret ambiguous currency or decimal input.
- Reject `NaN`, infinities, unsafe integers, and values beyond backend or database capacity.
- Keep displayed formatting separate from canonical submitted value.
- Test keyboard entry, paste, increment controls, and mobile numeric keyboard behavior.

## Dates and time

- Define date-only versus instant semantics and local versus UTC conversion.
- Validate impossible dates, leap days, daylight-saving boundaries, and timezone shifts where relevant.
- Define past/future allowance and inclusive or exclusive boundaries.
- Validate cross-field order such as start before end and recalculate when either side changes.
- Prevent date-only values from shifting a calendar day during serialization or hydration.

## Selects, autocomplete, and dependent fields

- Cover loading, empty results, search failure, disabled options, stale selections, and options removed after initial load.
- Use stable underlying IDs or enum values, not labels, for submission and Cypress selectors.
- Reset or revalidate dependent fields when a parent selection changes.
- Prevent late async responses from replacing newer search results. Cancel or ignore stale requests.
- Define duplicate-option behavior and permission-filtered options.
- For edit forms, verify stored values still render when absent from the first options page.

## Conditional and cross-field rules

- Keep UI visibility, schema requiredness, submission, and backend rules synchronized.
- Clear or intentionally preserve hidden values; never submit stale hidden data accidentally.
- Account for disabled controls that browsers omit from native form submission.
- Cover mutual exclusion, at-least-one, exact-count, matching fields, range pairs, and role-dependent rules.
- Revalidate dependent fields immediately when the controlling value changes.

## Dynamic collections

- Define minimum and maximum item count, duplicate detection, ordering, and empty-row behavior.
- Use stable keys so editing or removing one row does not move errors or values to another.
- Map nested server errors to the correct item after reorder or removal.
- Define partial completion, bulk removal, retry, and per-item failure behavior.

## Files and images

- Validate count, extension, reported MIME, actual size, filename length, replacement, removal, and interrupted upload behavior.
- Treat client validation as feedback only. Backend must revalidate content.
- For image fields, use `$picky-mayco-images` for decoded format, dimensions, pixel limits, metadata, variants, storage, and delivery.

## Form lifecycle

- Verify create defaults, edit hydration, reset, cancel, reopen, and server-refetched values.
- Define dirty and touched behavior, unsaved-change warnings, and what happens after successful submission.
- Prevent double submission from click, Enter, slow network, and repeated retry.
- Keep values after actionable server errors. Clear sensitive values only when security requires it.
- Handle async validation races, component unmount, route change, and session expiry.
- Define whether Enter submits, inserts a newline, or selects an autocomplete option for each relevant control.

## Server and network failures

- Map field errors, form errors, conflict errors, authorization failures, rate limits, timeouts, offline state, and unexpected errors separately when user recovery differs.
- Keep server error codes as stable mapping keys; do not depend on translated message text.
- Define retry safety and optimistic rollback. Avoid replaying non-idempotent actions accidentally.
- Prevent stale responses from overwriting newer state after filters, pagination, or route parameters change.

## Rendering and security

- Render user content as text unless sanitized rich content is an explicit feature.
- Validate redirect and external URL schemes before navigation.
- Avoid placing secrets, tokens, credentials, or sensitive personal data in client storage, URLs, logs, analytics, or error messages.
- Treat hidden and disabled UI as presentation, never authorization.

## Accessibility, responsive behavior, and localization

- Associate labels, hints, counters, and errors with the field. Move focus to the first invalid field or an error summary when submission fails.
- Preserve visible focus, keyboard operation, screen-reader announcements, and usable touch targets.
- Test long translated labels, validation messages, filenames, and unbroken values at narrow and wide viewports.
- Define locale behavior for dates, currency, decimals, phone numbers, casing, accents, and right-to-left layout when supported.
- Verify mobile keyboard, browser autofill, password managers, zoom, and controls hidden by the virtual keyboard where relevant.

## Evidence

For each material rule, prefer a focused unit or component test for boundary behavior and a Cypress flow for user-visible integration. Include happy path, invalid input, exact boundaries, backend rejection, duplicate-submit prevention, and recovery where applicable.
