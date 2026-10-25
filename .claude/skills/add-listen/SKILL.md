---
name: add-listen
description: Add podcast episodes Barbara has listened to into the "My podcast loves, as a graph" page (/listening/) on barbhs.com. Resolves the show and episode through Apple Podcasts, links guests, hosts, topics and the works (books, articles, papers) the episode mentions, captures her spark in her own words, writes the _listens/ file, validates it, and opens a PR. Use this whenever she mentions listening to a podcast episode and wanting it logged, added, saved or graphed, e.g. "I just listened to the SuperDataScience episode with the Linear Digressions creator, add it", "log these episodes", "put this on my podcast graph / I-<3-Podcasts graph", or pastes a list of episodes. Also use it to fix or enrich an existing listen (rewrite a spark, correct a listen date, add notes).
---

# add-listen

Turns "I just listened to X" into one reviewed file in `_listens/` (plus any new
show, person or topic entries) and a PR. The graph at `/listening/` rebuilds from
those files when the PR merges.

The division of labor matters. **`scripts/listens/add_listen.py` does everything
mechanical**: Apple lookups, id slugs, duplicate checks, color slots and the exact
front matter. Don't hand-write `_listens/` files or re-derive ids, because small
drift there (a second `katie_malone` spelled `katy_malone`, a hand-typed date)
quietly splits nodes in the graph. **Your job is the judgment**: which episode she
means, who the guests are, which topics are central, and getting her spark in her
own words.

Run every command from the repo root. All subcommands are dry runs unless given `--write`.

## Ground rules

- **Metadata comes from Apple, never from memory.** Title, dates, duration, URLs
  and guid come from the lookup. If you can't find the episode, say so; don't
  reconstruct it.
- **Guests and bios come from the episode description.** A bio is one line,
  sourced (`source: "<show> <ep> description"`). If the description doesn't say
  who someone is, write what it does say and mark the source; don't fill gaps
  from general knowledge.
- **The spark is hers.** It's the point of the page: what the episode made *her*
  think. Ask for it. Draft one only if she asks, and then it carries
  `--spark-draft`. Draft sparks stay in the file for her to rewrite but are never
  published: the site shows "Nothing written yet" until `spark_draft` is removed.
- **Hosts are not guests.** Hosts link to the show (`hosts:` in
  `_data/podcast_shows.yml`); the script refuses a host in `--guests`.
- **Ask with AskUserQuestion when a choice is genuinely hers** (which of 3
  candidate episodes, a new topic, the spark). Don't ask about things the lookup settles.

## Workflow

### 1. Parse the request

Pull out, per episode: show name, any identifier (episode number, title words,
guest name, "the latest", "recent-ish"), when she listened, and any reaction she
already expressed (that's spark material; keep her wording).

Listen date: default today with `--precision day`. "Last week" → best-guess date,
`approximate`. "Back in May" → `YYYY-05-01`, `month`. Batch back-fill with no
dates → publish date, `approximate` (that's what the seed batch used).

### 2. Resolve the show

```bash
python3 scripts/listens/add_listen.py shows "superdatascience"
```

- `known` → use its `id`.
- Only `apple_candidates` → pick the one that's clearly the show (exact name,
  sensible episode count); ask if two are plausible. Then add it:
  ```bash
  python3 scripts/listens/add_listen.py add-show --itunes-id 1406537385 --id practical_ai --hosts daniel_whitenack,chris_benson --write
  ```
  Hosts come from the episode descriptions or Apple's `artistName`; add each host
  as a person (step 4) *before* validating. A show's color is assigned
  automatically on its first logged episode. Only six colors exist; if they're all
  taken the script says so, and you tell her the show will render in neutral ink.

### 3. Find the episode

```bash
python3 scripts/listens/add_listen.py episodes superdatascience --number 1029
python3 scripts/listens/add_listen.py episodes catalog_cocktails --match "Doerr|governance"
python3 scripts/listens/add_listen.py episodes linear_digressions --limit 5
```

`--match` is a regex over title *and* description, so a guest's name works even
when the title doesn't carry it.

- One clear hit → continue.
- Several → show her the top 2–3 (date, title) and ask.
- `already_logged` set → tell her it's in already and offer to update that file instead (see "Updating a listen").
- Nothing → Apple only returns a show's latest 200 episodes. Tell her that. A
  local session can read the RSS feed (`feed_url` in the show entry); otherwise
  ask whether to log it by hand from the episode page, marked
  `provenance.metadata: manual`.
- Skip `TAKEAWAY - …` companion episodes unless she means one; the script links
  the companion from the full episode automatically.

### 4. Guests

Read the episode description. For each guest (not host):

```bash
python3 scripts/listens/add_listen.py person "Katie Malone"
```

- `exists: true` → reuse the id.
- `similar` non-empty → almost always the same person spelled differently; reuse
  the existing id.
- New → add them:
  ```bash
  python3 scripts/listens/add_listen.py add-person --id ben_jaffe --name "Ben Jaffe" --bio "Co-host of Linear Digressions." --source "Linear Digressions 2026-09-28 description" --write
  ```

**Watch for guests who host another show** ("Katie Malone, host of Linear
Digressions"). Those are the links that make this a graph and not a list. Offer to
add that show with the guest as host. It appears as a hollow node reached through
them, even before she logs an episode of it.

No identifiable guest (a hosts-only episode) is fine: leave `--guests` empty.

### 5. Topics

```bash
python3 scripts/listens/add_listen.py topics
```

Pick the 1–3 topics that are central to the episode, not every one it touches.
More edges make the graph a hairball, and the topics are what connect
episodes across shows. If nothing fits, propose one new topic (id, label, one-line
description) and ask before adding it with `add-topic --write`. Keep the vocabulary
small; prefer stretching an existing topic over a near-duplicate.

### 5b. Works mentioned

Books, articles, papers, newsletters and talks named in the show notes go in
`_data/podcast_works.yml` and appear on the graph behind the "Works" toggle. Design
and Barbara's decisions: `_planning/works-spike.md` (read "Decisions" and "Barbara's
thoughts" once per session).

1. Read the full description and list every **titled** work, each with its kind:
   - `by_guest`: the guest wrote it (their book, their Substack).
   - `recommended`: a recommendation segment, such as Lenny's "Recommended books".
     Name who recommended it with `--by`. On Lenny's that's the guest (the lightning round).
   - `discussed`: anything else the episode or its notes point to.
   - Add `--from-show` when the show is linking its own content (Lenny's newsletter posts).
     These are kept but drawn quieter.
   Skip products, companies, frameworks named in passing, films and TV, and
   untitled pointers ("her TED talk"). Ask Barbara for the title before recording one.
2. Show her the list as one table (title, type, kind, by) and ask which to keep. All
   three kinds count the same, so don't pre-filter recommendations.
3. For each work she keeps, check whether it already exists, then get metadata from a
   catalog. Never fill in year, author or ISBN from memory.
   ```bash
   python3 scripts/listens/add_listen.py works "thinking in systems"
   python3 scripts/listens/works_lookup.py book "Thinking in Systems" --author Meadows
   python3 scripts/listens/works_lookup.py paper "Ironies of Automation" --author Bainbridge
   ```
   Look up by **title**, never by an author's record (catalogs merge namesakes). Use a
   result only if `author_match` is true and the author is the one the notes name.
   Articles and newsletters have no catalog: use the title and URL from the notes, and
   verify the URL loads.
4. Write it. An existing id gets the new mention added instead.
   ```bash
   python3 scripts/listens/add_listen.py add-work --title "Thinking in Systems" --type book \
     --authors-outside "Donella H. Meadows" --year 2008 --url https://openlibrary.org/works/OL3737036W \
     --isbn 9781136551390 --openlibrary OL3737036W \
     --listen 2026-07-19-lennys-podcast-why-netflix-is-betting-on-systems --kind recommended --by elizabeth_stone
   ```
   `--authors` takes person ids for people on the graph (a guest's own book);
   everyone else goes in `--authors-outside "Name; Name"`. `--listen` is the
   `_listens/` file name without `.md`. If the listen file is new in this run,
   write it first.

Barbara can also add a work by hand that no episode mentions (`--source manual`, no
`--listen`), for example another book by a guest. It needs at least one on-graph
author or it won't appear. She can mark any work `--my-status want_to_read` or
`read`; that's hers to say, so never set it on her behalf.

### 6. Spark and notes

Ask what the episode sparked for her, unless she already said it. Offer:
type it now / leave it blank for later / draft one for her to rewrite. Use her words
verbatim (light punctuation fixes only). Longer notes go in a temp file passed with
`--notes-file`; they render publicly on the episode page.

### 7. Draft, confirm, write

Dry-run first:

```bash
python3 scripts/listens/add_listen.py listen --show superdatascience --track-id 1000791095249 \
  --listened-on 2026-10-03 --guests katie_malone --topics ai_agents,teaching_ai \
  --spark "Her words here"
```

Show her a compact card: show, title, listened/published dates, guests, topics,
spark, and the color note. For a batch, one table for all episodes. When she
confirms, rerun the same commands with `--write` (people and topics first, then
listens).

### 8. Validate

```bash
python3 scripts/listens/validate.py
```

It must say OK. It checks every show, guest, host and topic id resolves, dates
parse and no episode is logged twice. It also checks works: every mention points
at a real listen, every `recommended` mention names who, and every person id resolves. A full Jekyll build is optional; in a cloud
session it needs the workarounds in `_planning/podcast-graph-pilot.md` ("Building
locally in a cloud session").

### 9. Branch, commit, PR

- If the session assigned a branch, use it. Otherwise branch from the default:
  `git fetch origin master && git checkout -b listen/<first-file-slug> origin/master`.
  Never push to `master` directly; the PR is her review gate.
- Stage only what changed: the new `_listens/` files and any `_data/podcast_*.yml` edits
  (including `podcast_works.yml`).
- Commit message: `Add listen: <Show> — <episode title>` (batch: `Add N listens: <shows>`),
  plus whatever attribution lines the environment requires.
- Push and open a PR (GitHub MCP tool or `gh pr create`). Body: one line per
  episode (show, title, listened date), then new shows/people/topics, then any
  draft sparks she still needs to rewrite.
- Give her the PR link and the episode's future URL: `/listening/<file name without .md>/`.

## Updating a listen

Edit the file in `_listens/` directly. For a spark she rewrote: replace `spark`,
delete `spark_draft`, set `provenance.spark: mine`. For a corrected date: change
`listened_on` and `listened_precision`; leave the filename alone, since renaming
breaks the episode's URL. Then validate, commit and open a PR as above.

To mark a work she wants to read or has read:
`python3 scripts/listens/add_listen.py add-work --id thinking_in_systems --my-status want_to_read --write`.

## Example

> "I just listened to a recent-ish episode from the SuperDataScience podcast and
> the guest was the creator of the Linear Digressions podcast, add it"

1. `shows superdatascience` → known.
2. `episodes superdatascience --match "Linear Digressions"` → 1029, Katie Malone.
3. `person "Katie Malone"` → new: add with a bio from the description. The
   description says she hosts Linear Digressions, so offer `add-show` for it with
   `--hosts katie_malone`.
4. Topics: `ai_agents`, `managing_people_and_agents`, `teaching_ai`.
5. Ask for her spark; she listened today → `--listened-on <today>`.
6. Dry-run card → she confirms → `--write` → validate → branch, commit, PR.
