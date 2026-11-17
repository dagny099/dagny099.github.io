# Works

Books, articles, papers, newsletters and talks connected to episodes and people. They
live in `_data/podcast_works.yml`, appear on the page behind the "Works" toggle, and are
listed under "Works mentioned" on episode pages. The design came out of a spike in
October 2026; the decisions are in the [decisions log](../decisions.md#works).

## An entry

```yaml
- id: thinking_in_systems
  title: Thinking in Systems
  type: book
  authors_outside:
  - Donella H. Meadows
  year: 2008
  url: https://openlibrary.org/works/OL3737036W
  ids: {isbn: '9781136551390', openlibrary: OL3737036W}
  source: show_notes
  mentions:
  - {listen: 2026-07-19-lennys-podcast-why-netflix-is-betting-on-systems, kind: recommended, by: elizabeth_stone}
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Slug of the title |
| `title` | yes | |
| `type` | yes | `book`, `article`, `paper`, `newsletter` or `talk` |
| `authors` | one of the two | Person ids for authors who are on the graph (a guest's own book). Each becomes a `WROTE` edge |
| `authors_outside` | one of the two | Plain names for everyone else |
| `year`, `publisher`, `url` | optional | From the catalogue, or the notes for things no catalogue holds |
| `ids` | optional | `isbn`, `openlibrary`, `doi`; recorded separately from `source` |
| `source` | yes | `show_notes`, `transcript` or `manual` |
| `mentions` | optional | One per episode that mentions it; see below |
| `my_status` | optional | `want_to_read` or `read`. Mine to set, never set on my behalf |

A work with no mentions must be `source: manual` and must have at least one on-graph
author, or it cannot appear anywhere and the validator says so.

## Mentions

```yaml
mentions:
- {listen: <file name without .md>, kind: by_guest | discussed | recommended, by: <person id>, from_show: true}
```

| `kind` | Meaning | Extra |
|---|---|---|
| `by_guest` | The guest wrote it | |
| `discussed` | Came up in the episode or its notes | |
| `recommended` | A standing recommendation segment, such as Lenny's lightning round | `by` is required and names the recommender; it becomes a `RECOMMENDS` edge from that person |

All three kinds count the same. A show linking its own content (Lenny's newsletter
posts) carries `from_show: true`: kept, drawn quieter, and excluded from any
"most recommended" count.

## Catalogue rules

Bibliographic facts come from a catalogue, never from a model's memory, and the lookup
always **starts from a title** someone chose. The spike tried author-record search on
three test people and found Open Library merging a machine-learning author with a
lignin chemist and Portuguese novelists, and the Selenium author with the psychiatrist
of the same name. So:

1. Take the title from the show notes (or from me).
2. Look it up by title with `works_lookup.py`, passing the author's surname to check.
3. Use a result only if `author_match` is true and the author is the one the notes name.
4. Articles and newsletters have no catalogue: title and URL from the notes, URL
   verified to load.

Untitled pointers ("her TED talk", "the paper he co-authored") are not stored until a
title is confirmed. Products, companies, frameworks named in passing, films and TV are
skipped.

## On the page

Works are a layer. With the toggle off, the layout and every edge are exactly what they
were before works existed. With it on, works hang off the episodes that mention them and
the people who wrote or recommended them; people reached only through works appear too.
`?works=1` in the URL turns the layer on at load. A small marker shows `my_status`.
