# Tackboard Snippets Guide

## Add a snippet
1. Duplicate `_snippets/_TEMPLATE.md` and rename the file (use a short slug, e.g. `_snippets/ambient-information-radiators.md`).
2. Fill in the front matter fields:
   - **Required:** `title`, `date`, `status`, `source_type`.
   - **Recommended:** `source_title`, `source_creator`, `source_url`, `highlight`, `takeaway`, `tags`, `topics`.
3. Write any extra context in the Markdown body.
4. Commit the new file and run `bundle exec jekyll build` to verify the build.

## Inbox → Garden workflow
- The board reads the `status` field.
- `status: inbox` shows in the Inbox section.
- `status: garden` shows in the Garden section (listed first on `/snippets/`).
- Promote a snippet by changing the status to `garden` when it’s refined.

## Customize the board
- **Layout & card fields:** `_includes/snippet-card.html`
- **Page layout (single snippet):** `_layouts/snippet.html`
- **Masonry columns & visual styling:** `_sass/_snippets.scss`
- **Board sections:** `snippets/index.md`

Look for inline comments in each file for quick customization points.

## Filtering (future enhancement)
Cards already include `data-*` attributes for `status`, `type`, `tags`, and `topics`. You can add a lightweight filter bar later by reading those attributes with a tiny JS enhancement while keeping the board functional without JS.

## GitHub Issue Template workflow
Use `.github/ISSUE_TEMPLATE/new-snippet.yml` when you want to capture a snippet as an Issue:
1. Open a new GitHub issue and select **New Snippet**.
2. Fill in the form fields (they match the snippet front matter schema).
3. When ready, copy the generated info into a new `_snippets/` file or into `_snippets/_TEMPLATE.md`.

## Tips
- Keep highlights short; the card preview truncates long quotes.
- Use `header.teaser` in front matter if you want a custom teaser image on the snippet page.
