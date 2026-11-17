# add_listen.py

`scripts/listens/add_listen.py` does everything that must be identical every time. All
subcommands print JSON or the drafted file; **nothing is written without `--write`**.
It needs PyYAML and reaches only `itunes.apple.com` (catalogue lookups live in
[`works_lookup.py`](lookups.md)).

```bash
python3 scripts/listens/add_listen.py <subcommand> [options]
```

## Reading

### `shows "<name or id>"`

Known show, or Apple candidates.

Output: `{"known": [...]}` when the term matches an id, an Apple id, a name, or a close
name (difflib, cutoff 0.55); otherwise `{"known": [], "apple_candidates": [...]}` with
up to five Apple results (`collectionId`, `collectionName`, `artistName`, `feedUrl`,
`trackCount`, `releaseDate`).

### `episodes <show_id|collectionId> [--match REGEX] [--number N] [--limit K]`

The show's latest 200 episodes from Apple, filtered. `--match` is a case-insensitive
regex over title and description. `--number` keeps episodes whose parsed number equals
N. `--limit` defaults to 8. Each row: `trackId`, `date`, `minutes`, `title`,
`episode_number`, `already_logged` (the `_listens/` file name if the guid is logged),
and the first 600 characters of the description. A `note` reminds that Apple returns
only the latest 200 when nothing comes back.

### `person "<Full Name>"`

`suggested_id` (the slug), `exists` (that id is on file), and `similar` (people whose
names are close, cutoff 0.7, with a different id).

### `topics`

The vocabulary, as JSON.

### `works ["<title words>"]`

Without a term: every work with its id, title, type and mention count. With a term:
`suggested_id` and `matches` (substring matches on the title, else close matches).

## Writing entities

### `add-show --itunes-id N --id SLUG [--name NAME] --hosts a,b [--write]`

Appends a show. Refuses an id or Apple id already on file. Name, feed URL and Apple URL
come from the Apple search result whose `collectionId` matches. No colour slot is set
here; that happens on the first listen.

### `add-person --id SLUG --name NAME --bio TEXT --source TEXT [--write]`

Appends a person. Refuses an existing id. All four flags are required.

### `add-topic --id SLUG --label TEXT --description TEXT [--write]`

Appends a topic. Refuses an existing id.

## Writing a listen

### `listen`

```
listen --show ID --track-id N [--listened-on YYYY-MM-DD]
       [--precision day|month|year|approximate] --guests a,b --topics x,y
       [--spark TEXT] [--spark-draft] [--notes-file F] [--episode-number N] [--write]
```

Builds the file from the Apple record for `--track-id`. Refuses when:

- the show is unknown (add it first);
- the `trackId` is not among the show's latest 200 on Apple;
- the episode's guid is already logged (`already logged as _listens/...`);
- a guest is a host of this show (`hosts connect through the show, list only guests`);
- a guest or topic id does not exist yet (`add these first: ...`).

Then it: parses the episode number from the title unless given; takes the first two
sentences of the description as `summary`, cut before sponsor and boilerplate blocks;
looks for a `Takeaway - <title>` companion in the same feed and links it under
`related_links`; sets `provenance`; assigns a colour slot to the show if it has none
and one is free (with `--write`, a one-line insert in `podcast_shows.yml`); and writes
`_listens/<listened_on>-<show-id>-<six title words>.md`. Output: the file name, whether
it was written, the colour note, then the whole file.

### `add-moment --listen FILE-SLUG --at MM:SS --shot-on YYYY-MM-DD [--chapter TEXT] [--write]`

Adds a moment to a logged listen. `--listen` is the file name without `.md`. Refuses a
missing file, a malformed `--at`, a position past the episode's end (two minutes of
slack), or a `--shot-on` before `published_on`. A second mark within 60 seconds on the
same day is reported as `already marked` and changes nothing. Moments are sorted and
`provenance` stays the last key. The body of the file is preserved.

## Writing works

### `add-work`

```
add-work --title T --type book|article|paper|newsletter|talk [--id SLUG]
         [--authors a,b] [--authors-outside "Name; Name"] [--year N] [--publisher P] [--url U]
         [--isbn N] [--openlibrary OL…W] [--doi D] [--source show_notes|transcript|manual]
         [--listen FILE-SLUG --kind by_guest|discussed|recommended [--by PERSON] [--from-show]]
         [--my-status want_to_read|read] [--write]
```

A new id creates the work; an existing id adds the mention and/or sets `my_status`,
and refuses to do nothing. `--authors` must be person ids; outside authors are
semicolon-separated names. A mention needs `--listen` (an existing file) and `--kind`;
`recommended` needs `--by` (an existing person). A `manual` work with no mention and no
on-graph author is written with a warning that it cannot appear. **This subcommand
rewrites `podcast_works.yml` whole**, keeping its header comment and putting each
mention on one line.

## Exit codes and output

Refusals print `ERROR: <reason>` to stderr and exit 1. Successful dry runs and writes
print JSON to stdout, followed by the YAML block that was or would be appended.
