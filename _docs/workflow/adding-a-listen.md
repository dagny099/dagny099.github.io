# Adding a listen

The `add-listen` skill (`.claude/skills/add-listen/SKILL.md`) turns "I just listened to
X" into one reviewed file in `_listens/`, any new show, person, topic or work entries,
and a pull request. This page is the same workflow with the reasoning next to each
step. Every command runs from the repository root and is a dry run unless given
`--write`.

!!! note "Python"
    The scripts need PyYAML. On this machine the system `python3` does not have it; use
    the pyenv interpreter. See [Environment](../reference/environment.md).

## 1. Parse the request

Per episode: the show, any identifier (episode number, title words, guest name, "the
latest", "recent-ish"), when I listened, and anything I already said about it, which is
spark material in my own wording.

| I said | `--listened-on` | `--precision` |
|---|---|---|
| nothing | today | `day` |
| "last week" | best guess | `approximate` |
| "back in May" | `YYYY-05-01` | `month` |
| a batch back-fill with no dates | the publish date | `approximate` |

## 2. Resolve the show

```bash
python3 scripts/listens/add_listen.py shows "practical ai"
```

`known` means use its `id`. Only `apple_candidates` means the show is new: pick the one
that is clearly it (exact name, sensible episode count; ask if two are plausible), then
add it with its hosts. Hosts come from the episode descriptions or Apple's
`artistName`, and each host is added as a person before validation.

```bash
python3 scripts/listens/add_listen.py add-show --itunes-id 1406537385 --id practical_ai \
  --hosts daniel_whitenack,chris_benson --write
```

The show's colour is assigned automatically on its first logged episode. Six slots
exist; when they are all taken the script says so and the show renders in neutral ink.

## 3. Find the episode

```bash
python3 scripts/listens/add_listen.py episodes superdatascience --number 1029
python3 scripts/listens/add_listen.py episodes catalog_cocktails --match "Doerr|governance"
python3 scripts/listens/add_listen.py episodes linear_digressions --limit 5
```

`--match` is a regex over title **and** description, so a guest's name works when the
title does not carry it. Each row carries `trackId`, date, minutes, title, episode
number, the first 600 characters of the description, and `already_logged` when the guid
is already in `_listens/`.

- One clear hit: continue.
- Several: show the top two or three (date, title) and ask.
- `already_logged`: say so and offer to update that file instead.
- Nothing: Apple returns only a show's **latest 200 episodes**. A local session can
  read the RSS feed (`feed_url` on the show entry) to find an older one, but the
  `listen` subcommand itself only accepts a `trackId` from those 200, so an older
  episode cannot yet be written by the script. This is the first item on the
  [roadmap](../roadmap.md).
- `TAKEAWAY - …` companion episodes are skipped; the script links the companion from
  the full episode on its own.

## 4. Guests

Read the description. For each guest (not host):

```bash
python3 scripts/listens/add_listen.py person "Katie Malone"
```

`exists: true` reuses the id. A non-empty `similar` list is almost always the same
person spelled differently, so reuse the existing id. Otherwise:

```bash
python3 scripts/listens/add_listen.py add-person --id ben_jaffe --name "Ben Jaffe" \
  --bio "Co-host of Linear Digressions." --source "Linear Digressions 2026-09-28 description" --write
```

Watch for a guest who hosts another show. That show gets added with the guest as host
and appears as a hollow node reached through them, before any episode of it is logged.
A hosts-only episode is fine: leave `--guests` empty.

## 5. Topics

```bash
python3 scripts/listens/add_listen.py topics
```

One to three topics that are central. If nothing fits, propose one new topic (id,
label, one-line description) and ask before `add-topic --write`.

## 5b. Works mentioned

From the full description, list every **titled** work with its kind (`by_guest`,
`recommended` with `--by`, or `discussed`; `--from-show` when the show links its own
content). Show the list as one table and ask which to keep; all three kinds count the
same, so nothing is pre-filtered. For each kept work:

```bash
python3 scripts/listens/add_listen.py works "thinking in systems"
python3 scripts/listens/works_lookup.py book "Thinking in Systems" --author Meadows
python3 scripts/listens/add_listen.py add-work --title "Thinking in Systems" --type book \
  --authors-outside "Donella H. Meadows" --year 2008 --url https://openlibrary.org/works/OL3737036W \
  --isbn 9781136551390 --openlibrary OL3737036W \
  --listen 2026-07-19-lennys-podcast-why-netflix-is-betting-on-systems --kind recommended --by elizabeth_stone
```

`--listen` is the listen's file name without `.md`, so a new listen is written before
its works. The catalogue rules are on the [works](../data-model/works.md#catalogue-rules)
page.

## 6. Spark and notes

Ask what the episode sparked, unless I already said it. Options: type it now, leave it
blank, or have a draft written for me to rewrite (then `--spark-draft`). Longer notes go
in a file passed with `--notes-file` and render publicly.

## 7. Draft, confirm, write

```bash
python3 scripts/listens/add_listen.py listen --show superdatascience --track-id 1000791095249 \
  --listened-on 2026-10-03 --guests katie_malone --topics ai_agents,teaching_ai \
  --spark "Her words here"
```

The dry run prints the file name, the colour note and the full front matter. On
confirmation the same commands run again with `--write`, people and topics first, then
listens. The script refuses to write when the episode is already logged (by guid), when
a guest hosts the show, or when a guest or topic id does not exist yet.

## 8. Validate

```bash
python3 scripts/listens/validate.py
```

Must print `OK`. See [Validation and tests](validation.md).

## 9. Branch, commit, PR

Covered on [Publishing and review](publishing.md). The PR is my review gate; the merge
rebuilds the graph.

## Marking a moment

For an episode already logged (log it first otherwise):

```bash
python3 scripts/listens/add_listen.py add-moment \
  --listen 2026-09-25-catalog-cocktails-ai-inherits-the-business-choices-you \
  --at 25:53 --shot-on 2026-09-27 --chapter "Chapter title as shown" --write
```

Several screenshots of one passage are one moment at the earliest position. Position
and chapter only; the [moments](../data-model/moments.md) page says why.

## Updating a listen

Edit the file directly. A rewritten spark: replace `spark`, delete `spark_draft`, set
`provenance.spark: mine`. A corrected date: change `listened_on` and
`listened_precision`, keep the file name. Then validate, commit and open a PR as usual.
To mark a work read or wanted:

```bash
python3 scripts/listens/add_listen.py add-work --id thinking_in_systems --my-status want_to_read --write
```
