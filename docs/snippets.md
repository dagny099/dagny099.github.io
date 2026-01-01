---
layout: single
title: Tackboard Snippets Guide
permalink: /docs/snippets/
---

This guide explains how to add and maintain Tackboard snippets.

## Add a snippet
1. Duplicate `_snippets/TEMPLATE.md` and rename it with a descriptive slug (for example, `_snippets/2025-02-15-designing-feedback-loops.md`).
2. Fill in the front matter fields:
   - `status`: `inbox` or `garden`.
   - `source_*` fields: capture the origin (book, podcast, article, etc.).
   - `highlight` and `takeaway`: the quote + your synthesis.
   - `tags` and `topics`: short, reusable labels.
   - `impact`: 1–5 for how useful the idea feels.
3. Add any extra context in the Markdown body.

## Inbox → Garden workflow
Snippets stay in `inbox` until you manually change `status` to `garden`.
The board at `/snippets/` always lists Garden first, then Inbox, both sorted newest-first.

## Customize the layout
- Card markup lives in `_includes/snippet-card.html` (chips, metadata, preview text).
- Snippet page layout lives in `_layouts/snippet.html` (chips, source line, highlight).
- Board styling and column counts live in `_sass/_snippets.scss`.
  Adjust the CSS variables at the top to change radius, padding, and shadows.

## GitHub Issue Form workflow
Use `.github/ISSUE_TEMPLATE/new-snippet.yml` to capture a snippet via GitHub:
1. Create a new issue and select **New Snippet**.
2. Fill in the form fields to match the snippet schema.
3. When you’re ready, copy the issue content into a new file under `_snippets/`.

## Future filtering
The snippet cards already include `data-*` attributes for `status`, `type`, `tags`, and `topics`.
You can add a lightweight filter bar later with client-side JS that toggles card visibility,
without changing the markup.
