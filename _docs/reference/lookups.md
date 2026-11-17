# Lookup helpers

Two standard-library scripts in `scripts/listens/`, both usable on their own and both
imported by `add_listen.py`.

## `itunes_lookup.py`

Apple's iTunes Search API is the one source for shows and episodes. One domain covers
show search, feed URLs and the latest 200 episodes per show, which is why the toolchain
does not need to reach any RSS host and works from a cloud session whose egress proxy
allows only `itunes.apple.com`.

```bash
python3 scripts/listens/itunes_lookup.py show "superdatascience"
python3 scripts/listens/itunes_lookup.py episodes 1163599059 --match "Katie Malone"
```

| Call | Endpoint | Returns |
|---|---|---|
| `search_shows(term, limit=5)` | `search?media=podcast&entity=podcast` | `collectionId`, `collectionName`, `artistName`, `feedUrl`, `trackCount`, `releaseDate` |
| `list_episodes(collection_id, match=None, limit=200)` | `lookup?entity=podcastEpisode&limit=200` | `trackName`, `releaseDate` (date only), `minutes`, `guid`, `trackId`, `url` (tracking parameter stripped), `audio_url`, `description` |

Known limits:

- **200 episodes.** Older episodes need the RSS feed. A local session can read it, but
  `add_listen.py listen` does not take RSS records yet.
- **No episode-number field.** Numbers are parsed from titles where the show puts them
  there.
- **About 20 calls a minute.** The client retries three times with a growing wait.

## `works_lookup.py`

Catalogue metadata for a work, always starting from a title.

```bash
python3 scripts/listens/works_lookup.py book "Thinking in Systems" --author Meadows
python3 scripts/listens/works_lookup.py paper "Ironies of Automation" --author Bainbridge
```

| Kind | Source | Fields |
|---|---|---|
| `book` | Open Library title search, no key | `title`, `authors`, `year`, `openlibrary` work id, a 13-digit `isbn` when there is one, `url`, `author_match` |
| `paper` | Crossref bibliographic search, no key | `title`, `authors`, `year`, `venue`, `doi`, `url`, `author_match` |

`--author` is a surname; `author_match` is true when it appears in the record's author
names. Open Library drops roughly one request in three, so the client retries five
times. The request carries a user agent naming the listening graph, as both services
ask.

Newsletters, articles and talks have no catalogue. Their record is the title and URL
from the show notes.

## What was tried and set aside

From the works spike: OpenAlex now needs an API key (keyless calls share a daily budget
per IP, exhausted on a shared cloud address); Google Books hits the same shared-quota
wall; Wikidata and show websites were unreachable from the cloud session. Crossref,
keyless, became the fallback for papers. A free OpenAlex key stored as a secret is a
noted option, not done.
