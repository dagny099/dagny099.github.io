# Decisions

A dated log of the choices that shaped the system, each with where it was made. The
planning documents in `_planning/` are the full record; this page is the index.

## Pilot (3 October 2026)

From the interview in `_planning/podcast-graph-pilot.md`, section 2.

| Question | Decision |
|---|---|
| Source of truth | Jekyll collection `_listens/`, one markdown file per episode |
| Date axis | Store `listened_on` and `published_on`; slider defaults to listened |
| Notes privacy | Public; notes render on episode pages and in the side panel |
| Node types | Show, Episode, Person (guests and hosts), Topic |
| Topics | Small controlled list; the skill proposes additions for approval |
| Enrichment | Session lookups only; no Neo4j |
| Visualisation | A fresh D3 page in the style of the project map |
| Add flow | A repo skill that writes on confirm and opens a PR |
| Out of scope | Organisation nodes, spark nodes, Wikidata ids, nav dropdowns, Neo4j, transcripts |

## As built (4 October 2026)

- **Six show colours, not eight.** Searching OKLCH candidates for the largest set where
  every pair clears the contrast and colour-vision gates with margin, with hues 45
  degrees apart, gives six. Seven only fits if cyan, blue and violet crowd together. A
  seventh show folds to neutral ink. A 7-slot alternative with bunched blues is kept on
  file.
- **Brand teal and coral are not show colours.** Teal fails the chroma floor; coral sits
  too close to the rose slot. Selection is an ink ring.
- **Design review** removed generated-UI tells and moved sparks into the tooltip.
- **`color_slot` is pinned** in `podcast_shows.yml` so adding a show never repaints
  another.
- **Apple only.** `itunes.apple.com` covers show search, feed URLs and the latest 200
  episodes, which was enough to unblock the cloud environment.

## Publishing (7 October 2026)

- **PRs build, pushes deploy.** The workflow had been deploying on pull requests; now a
  PR is a check only. The PR is the review gate.
- **Draft sparks never ship.** The graph JSON emits `null` and the episode layout shows
  "Nothing written yet" while `spark_draft` is true.

## Works

**Spike (8 October 2026)**, `_planning/works-spike.md`:

- Thirteen titled works in four of thirteen seed episodes, nine of them from one
  Lenny's episode. The layer is lopsided by construction.
- **Never list a person's works from an author record.** Catalogues merge namesakes.
  Anchor on a title, use the catalogue for metadata, check the author name.
- Open Library is reachable but flaky; OpenAlex needs a key; Crossref is the paper
  fallback.

**Decisions (25 October 2026)**, same file:

- **Recommendation segments count the same** as works the guest discussed. `kind` is one
  of `by_guest`, `discussed`, `recommended`; all equal; the data keeps the distinction so
  it can be shown, not ranked.
- **Both routes in.** A work enters because an episode mentions it or because I add it
  by hand. Automatic listing from author records stays out.
- **Facts, not influence scores.** Record who wrote what and who recommends what;
  patterns (two guests recommending the same book) can be pointed out, never scored.
- **The recommender is a person.** `RECOMMENDS` is person → work, alongside
  `MENTIONS` from the episode.
- **A show plugging its own content** is kept, marked `from_show`, drawn quieter.
- **My own reading starts small**: `my_status` of `want_to_read` or `read`, no Goodreads
  import, no ratings.

Built 25 October 2026 on branch `podcast-works`: the data file, the toggle, "Works
mentioned" on episode pages, `add-work`, `works_lookup.py`, validator checks, step 5b
of the skill.

## Screenshots and moments (16 November 2026)

From `_planning/sparks-handoff.md`:

- **Two moments.** The log must cost nothing new (a screenshot into one folder); the
  spark is asked for later, in a batch, by voice.
- **Log every show, colour only some.** A `featured` flag per show; not built.
- **Ledger location.** The private `podcast-ingest-agent/screenshots/`.
- **The `moments` field**: position and chapter only. Built, with validator checks and
  tests.
- **Work-adjacent sparks** stay off the public page.
- **Four dedupe checks**, in order: file bytes, burst, episode guid, other sources.
- **Matching rules**: published after the shot is impossible; fragments must fit
  respecting cut edges; duration breaks ties only.

First batch the same day: ten screenshots, six moments, five matched, four written in
one PR. Findings on the [screenshot intake](workflow/screenshot-intake.md#tests-and-findings)
page.

## Standing rules

Collected from all of the above and restated on the
[workflow overview](workflow/index.md#rules-every-session-keeps).
