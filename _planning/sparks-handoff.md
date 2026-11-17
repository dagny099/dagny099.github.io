# Handoff: screenshot intake and sparks on /listening/

Written 2026-11-14, revised 2026-11-16, from a chat session.
Read `podcast-graph-pilot.md` first; this file assumes it.

## The idea

Barbara already screenshots the podcast player when a passage catches her. That habit is
the intake. A screenshot becomes a logged episode with the moment marked, and later she
says in a sentence why it mattered. That sentence is the spark.

Two separate moments, on purpose:

- **The log** costs nothing new: she screenshots, then drops the file in one folder.
- **The spark** is asked for later, in a batch, by voice.

The earlier flow asked for both at a desk in one sitting. All 13 seed episodes still carry
Claude-drafted sparks, none in her words, and no episode was added between the 2026-10-04
seed and 2026-11-16. The friction is at intake.

## What a screenshot carries

Test on 2026-11-16: 10 Spotify screenshots she supplied, taken June to December 2025,
read by eye in a chat session. Small sample, one app, one reader.

| Field | Readable in | Notes |
|---|---|---|
| Show name | 10 of 10 | |
| Exact playback position | 9 of 10 | The tenth was an episode page showing "25 min left". |
| Total duration | 9 of 10 | Right-hand time is total, checked against one "min left" value. |
| Episode title | 3 full, 6 cut off, 1 illegible | The title scrolls. Shots from one burst show different fragments that join into the whole title. |
| Passage text | 6 of 10 | Spotify's transcript view. Contains recognition errors ("A to a agent identity" for A2A). |
| Chapter title | 6 of 10 | Auto-generated; usable as a topic hint. |
| A note from her | 0 of 10 | The shot says "this mattered", never why. |
| Date and time taken | 10 of 10 | File name: `Screenshot_YYYYMMDD-HHMMSS.png`. |

Ten screenshots were six moments in six episodes. Four were taken within three and a half
minutes on one passage. **The unit is a burst, not a file.**

Not tested: whether the episodes resolve. The Apple lookup was blocked from that session.
Expect two problems. Apple returns a show's latest 200 episodes, so an old episode of a
daily show needs the RSS feed. A shot with no legible title has to match on show, total
duration and chapter name.

## Where things live

| Thing | Place | Why |
|---|---|---|
| Screenshot files | Google Drive folder "Podcast screenshots inbox" (My Drive, created 2026-11-16) | Private. Reachable from her phone's share sheet and from a session with the Drive connector. |
| Extraction ledger | Private. Recommended: `podcast-ingest-agent/screenshots/ledger.jsonl` | Holds passage text copied from a third party's transcript. Must not be in this public repo. |
| Episode, moment position, her spark | This repo, `_listens/`, through `add_listen.py` | Public-safe. |

Never commit screenshots here. They show device names, notifications and other people's
transcript text.

## No duplicates: four checks, in order

A screenshot can arrive twice, a burst is several files, and the Spotify history export
will later cover the same episodes. Re-running the whole inbox must change nothing.

1. **File.** Key each ledger row on the SHA-256 of the image bytes. Same bytes, skip.
   Keep the original file name as a second key for re-saved copies.
2. **Burst.** Same show, same total duration, positions within 5 minutes, taken within
   15 minutes: one moment. Keep the earliest position and every fragment of title and passage.
3. **Episode.** `add_listen.py` already refuses a second file for the same `guid`
   (`already_logged`). A new moment on a logged episode updates that file.
4. **Other sources.** The Spotify export and the share-sheet path resolve to the same
   `guid`. They add plays or moments to an existing listen and never create a second one.

Files stay in the inbox after processing. The ledger records what was done; nothing is
moved or deleted, so a failed run can be repeated.

## Schema change (approved 2026-11-16)

An optional list on a `_listens/` file:

```yaml
moments:
  - at: "25:53"            # playback position
    shot_on: 2025-12-18    # from the file name
    chapter: "Exploring AI as the New UI and Agent Experience"
```

No passage text in the public file. If a quote is ever shown, it is short, checked against
the audio, and links to the episode.

## Decisions (made 2026-11-16)

1. **Log every show, color only some.** Yes. A `featured` flag per show; not built yet.
2. **Ledger location.** `podcast-ingest-agent/screenshots/` (private).
3. **The `moments` field.** Yes, position and chapter only. Built: `add_listen.py add-moment`,
   checks in `validate.py`, tests in `scripts/listens/test_moments.py`.
4. **Work-adjacent sparks** stay off the public page.

## Built so far

- `podcast-ingest-agent/screenshots/intake.py`: ledger, burst merging, title-fragment
  joining, episode matching. Tested on the 10 screenshots and a 390-episode Catalog &
  Cocktails catalog. Network-free.
- This repo: `add-moment` and its validator checks (above).

Not built: live episode lookup for a burst (needs Apple or RSS, so a local session),
the `featured` flag, any display of moments on the page, the spark call.

## Build order

1. **Extract.** Read every file in the inbox into ledger rows: show, title fragments,
   position, total, chapter, passage as shown, date taken, file hash. Burst-merge.
   Dry run first; report rows and bursts.
2. **Match.** Resolve each burst to an episode: `podcast_shows.yml`, then Apple, then RSS.
   Report matched, ambiguous and unresolved. Never guess; list candidates.
3. **Write.** For matched bursts, call `add_listen.py` (new show, new listen, or added
   moment). One PR for the backlog batch. Sparks stay empty.
4. **Spark call.** List moments without a spark, read her the passage, take her sentence
   verbatim. Skips are fine.
5. **Later:** Spark nodes derived from sparks that share a topic; the Spotify export as a
   second source; a scheduled run over the inbox.

Stop after step 2 and show her the report before writing anything.

## Rules the session must keep

- The spark is hers. Never write one unless asked, and then mark it `spark_draft`.
- Record her words verbatim.
- Episode metadata comes from the lookup, never from memory or from the screenshot alone.
- `add_listen.py` does the mechanical work. Do not hand-write `_listens/` files.
- On-screen transcript text is "as shown", never a verified quote.
- One session writes to this repo at a time. `add_listen.py` rewrites the data files whole.
- The October design review removed generated-UI tells from this page. Keep them out.

## Open checks

- The plan says `validate.py` runs in a GitHub Action. Only `pages.yml` is in
  `.github/workflows/`. Confirm whether validation runs inside it.
- Backlog size: she estimates about 50, under 100. Count once they are in the inbox.
- Seven of the ten test shots had a different status-bar style from the first three.
  Check the file-name pattern holds for all of them.

## Kickoff prompt

> Read `_planning/podcast-graph-pilot.md` and `_planning/sparks-handoff.md`. Do build
> steps 1 and 2 only, as dry runs, over the Drive folder "Podcast screenshots inbox".
> Show me the extraction table and the match report, with every ambiguous or unresolved
> burst listed. Write nothing to `_listens/` until I approve.
