---
name: picky-mayco-images
description: "Review or implement image selection, upload, validation, transformation, storage, delivery, and display. Use whenever a Picky Mayco task handles images in frontend or backend."
---

# Picky Mayco Images

Trace the complete image lifecycle: select, preview, upload, validate, decode, transform, store, reference, deliver, replace, and delete. State which layer owns each constraint.

## Frontend

- Declare accepted formats, count, and size before selection; validate again after selection and show precise recovery guidance.
- Revoke preview object URLs and avoid base64 payloads in JSON unless an existing contract requires them.
- Preserve responsive layout for extreme aspect ratios and long filenames. Reserve display space to avoid layout shift.
- Upload with progress, cancellation when supported, duplicate-submit protection, retry behavior, and accessible errors.
- Use responsive image variants and lazy loading where display context benefits; set dimensions or aspect ratio.

Client compression is an optimization, never the authoritative safety boundary. Avoid quality loss when the source is already suitable or fidelity is required.

## Backend

- Enforce byte size, count, decoded dimensions, pixel count, and supported format. Verify decoded content or signature instead of trusting extension or client MIME type.
- Generate storage keys server-side. Treat original filenames as display metadata, not paths.
- Decode with bounded resources. Normalize orientation and strip unnecessary metadata when privacy and product requirements allow.
- Resize once into explicit variants. Preserve aspect ratio, avoid unintended upscaling, and choose format and quality from delivery needs and repository capabilities.
- Prefer object storage and direct or signed upload flows when payload size and infrastructure justify them. Keep access scope, expiry, and ownership explicit.
- Make database reference and object lifecycle consistent. Handle abandoned, replaced, deleted, and failed uploads without orphan leaks.

## Delivery and verification

Set content type, cache policy, access control, and content disposition intentionally. Use CDN delivery where available and appropriate.

Verify malformed files, spoofed MIME, oversized input, extreme dimensions, corrupt decode, interrupted upload, unauthorized access, replacement, deletion, and display across supported viewports. Apply only cases relevant to the task and state exclusions.
