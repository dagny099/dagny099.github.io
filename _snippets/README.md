# Tackboard Snippets

This directory powers the Tackboard snippets system. Each markdown file here becomes a snippet page and appears on `/snippets/`.

## Add a snippet
1. Duplicate `_snippets/TEMPLATE.md`.
2. Rename it (the filename becomes the URL slug).
3. Fill in the front matter fields (title, date, status, source, highlight, etc.).
4. Optional: add a short note in the body.

### Inbox → Garden workflow
Snippets start as `status: inbox`. When you’ve synthesized the idea, update the status to `garden` and it will move to the Garden section automatically.

## Customize the board
- **Cards + board layout**: edit `_includes/snippet-card.html` and `snippets/index.md`.
- **Snippet page layout**: edit `_layouts/snippet.html`.
- **Styling + columns**: edit `_sass/_snippets.scss` (look for the CSS variables at the top).

## GitHub Issue Form (capture quickly)
Use the **New Snippet** Issue Form at `.github/ISSUE_TEMPLATE/new-snippet.yml` to capture ideas on the go. The form fields map directly to the snippet front matter, so you can copy the content into a new `_snippets/*.md` file later.

## Future filtering (optional)
Snippet cards include `data-` attributes for status, type, tags, and topics. You can add a lightweight JS filter later that reads those attributes without changing the HTML structure.
