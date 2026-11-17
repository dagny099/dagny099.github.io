# Roadmap

Designed for, decided, or noticed, and not built. Each item says what it would take.
Nothing here is on the page today; the rest of these docs describe what is.

## Next

**RSS path for older episodes.** `add_listen.py listen` only accepts a `trackId` from
Apple's latest 200. One matched screenshot burst (an episode of The AI Daily Brief from
October 2025) is waiting on this. The fix: let `listen` take a record from the show's
`feed_url`, with `provenance.metadata: rss`, keeping the same guid dedupe.

**Moments on the page.** Moments are stored and validated but not rendered. Add them to
the graph JSON allow-list and to the episode layout as a short list of positions with
chapter titles, each linking to the audio where the player supports a timestamp.

**The spark call.** A batch session that lists moments without a spark, reads me the
passage from the private ledger, and records my sentence verbatim. Skips allowed. This
is the second of the two moments the system was built around.

**Validator in CI.** `validate.py` runs locally only. A job in `pages.yml`, or its own
workflow, on PRs touching `_listens/` or `_data/podcast_*.yml`.

**The screenshot backlog.** About fifty screenshots in the Drive inbox, after the ten
test shots. One extraction pass, one match report, one or two PRs.

**Confirm The Moth.** The one ambiguous burst: no legible title, 99 candidates by date.
A feed-description search suggested one episode; the screen's total duration did not
match the feed's. Mine to confirm or drop.

## Decided, not built

**`featured` flag per show.** Log every show, colour only some. The flag would replace
first-come colour slots with a choice. Decided 16 November 2026.

**Works tier 2.** Up to three works *by* a guest or host, confirmed one at a time, on top
of the works mentioned in episodes. Depends on the title-first catalogue rule holding.

**Logging from the phone.** The phone is Android, so no iOS Shortcuts. Options on the
table: the Claude mobile app opening a cloud session, an Android share-target app that
opens a GitHub issue, or a GitHub issue form. Open question: which podcast app, since
Apple links carry an episode id and others need a different resolver. The screenshot
inbox is the current answer for the "while listening" half.

**Swappable models for the judgment step.** Everything except guest, topic and bio
judgment is deterministic. Isolate that step behind one function with fixed input and
output and route it through LiteLLM with a stage-to-model map. The thirteen seed
episodes are a ready evaluation set.

## Designed for, later

- **Organizations** (`AFFILIATED_WITH`), once a guest list justifies it.
- **Spark nodes**: ideas shared across episodes, promoted from sparks that share a topic.
- **Neo4j export**: Cypher `MERGE`s from the same files.
- **Guest deep-dive** through the biographical pipeline in another repository.
- **Transcript layer**, for episodes worth going deep on. Transcripts would change the
  works picture: mentions in conversation are far richer than show notes.
- **Spotify export** as a second source of plays, resolving to the same guids.
- **A scheduled run** over the inbox.
- **Second navigation level**, once there are two or three lab-style pages to group.
- **My own reading** on the graph (a Goodreads export), making works the bridge between
  what I listen to and what I read.

## Hosting these docs

Build the MkDocs site in the Pages workflow and serve it under `/listening/docs/`, or
publish it to `docs.barbhs.com/listening/` next to the other project docs. Either way
it is a deploy change, so it is a separate, approved step.
