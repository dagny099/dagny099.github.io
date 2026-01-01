---
layout: single
title: Tackboard Snippets
permalink: /docs/snippets/
sitemap: false
---

# Tackboard Snippets

The Tackboard is a lightweight snippets system for capturing ideas, quotes, and research notes. Each snippet lives in `_snippets/` and renders both on the `/snippets/` board and as its own page.

## Add a new snippet

1. Duplicate `_snippets/_TEMPLATE.md`.
2. Rename the file (e.g., `ai-notes-on-annotation.md`).
3. Fill in the frontmatter fields and write the body content.
4. Save the file in `_snippets/`.

### Frontmatter fields

The template already includes the full schema:

- `title`, `date`, `last_modified_at`
- `status`: `inbox` or `garden`
- `source_type`, `source_title`, `source_creator`, `source_url`, `source_locator`
- `highlight`, `takeaway`
- `tags`, `topics`, `impact`
- Optional: `header.teaser`, `related`

## Inbox → Garden workflow

Snippets start in the Inbox and move to the Garden when you’ve refined the idea. This is entirely manual — just change the `status` field to `garden`. The board always shows Garden first, then Inbox.

## Customize the layout

- **Board + cards**: `_includes/snippet-card.html`
- **Snippet page**: `_layouts/snippet.html`
- **Styles**: `_sass/_snippets.scss` (tweak the CSS variables at the top)
- **Board sections**: `snippets/index.md`

## Future filtering (tags/topics)

Cards already include data attributes for `status`, `source_type`, `tags`, and `topics`. You can add lightweight client-side filtering later without changing the HTML structure.

## GitHub Issue Template workflow

Use `.github/ISSUE_TEMPLATE/new-snippet.yml` to capture new snippets as GitHub Issues:

1. Open **New Issue** in the repo.
2. Choose **New Snippet**.
3. Fill in the form (it mirrors the snippet frontmatter fields).
4. Copy the generated details into a new `_snippets/` file using the template.

Tip: keep issues labeled `snippet` or `inbox` so you can triage them before moving to the Garden.
