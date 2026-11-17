# Concepts

The vocabulary the rest of these docs use. Each term maps to a node type, a field, or a
rule in the [data model](data-model/index.md).

## Show

A podcast. A show is a node on the graph, coloured, and the only thing that is coloured.
It lives in `_data/podcast_shows.yml` with its hosts and its Apple catalogue id. A show
can be on the graph with **no listens at all**: it appears as a hollow node reached
through a person who hosts it. That is how a guest's own podcast shows up before I have
listened to it (the Linear Digressions pattern, see [people](#person) below).

## Listen (episode)

One episode I heard, as one markdown file in `_listens/`. The file carries the
episode's published metadata, when I listened, who was on it, which topics it covers, my
spark, and any moments I marked. Its file name is its URL: `/listening/<file name>/`.
The word *listen* is used for the file and the node; *episode* for the thing itself.

An episode is logged at most once. The dedupe key is the feed `guid`.

## Person

A guest or a host. Both live in `_data/podcast_people.yml` with a one-line bio and the
source of that bio. The difference is in the edges:

- A **host** connects to the show (`HOSTS`), never to individual episodes.
- A **guest** connects to the episode (`GUEST_ON`).

The script refuses a host listed as a guest of their own show. When a guest hosts
*another* show, that show is added with the guest as host, and the graph gains a path
from one show to another through a person. Those paths are the point of a graph rather
than a list.

## Topic

A small controlled vocabulary in `_data/podcast_topics.yml`, twelve entries as of
November 2026. An episode gets one to three topics, the ones that are central. Topics
are what connect episodes across shows, so the vocabulary is kept small on purpose: a
new topic is proposed and approved, never free-tagged.

## Work

A book, article, paper, newsletter or talk that an episode mentions, or that a person on
the graph wrote. Works live in `_data/podcast_works.yml` and are shown behind a "Works"
toggle on the page, off by default. Bibliographic facts come from catalogues (Open
Library, Crossref), looked up **by title**, never by listing an author's record, because
catalogues merge namesakes. The full rules are on the [works](data-model/works.md) page.

## Spark

One sentence, in my words, on what the episode made me think. It is the reason the page
exists. A spark is never written by a model unless I ask, and then it carries
`spark_draft: true` and is **not published**: the page shows "Nothing written yet" and
the node gets a paper centre until I rewrite it and drop the flag.

## Moment

A playback position I marked, usually with a screenshot of the player. A moment is
`at` (position), `shot_on` (date from the screenshot's file name) and optionally
`chapter` (the player's chapter title). Nothing else: the transcript text visible in a
screenshot stays in a private ledger. Several screenshots of one passage are one moment.
A moment is not a spark; the spark is asked for separately.

## Provenance

Every listen records where its facts came from: `metadata` (itunes, rss, manual),
`guests` (confirmed in conversation) and `spark` (mine, drafted by Claude, or not yet
written). Every person records the `source` of their bio. Every work records its
`source` (show notes, transcript, manual) and catalogue identifiers separately.

## Colour slots

The page has six validated show colours (hues at least 45 degrees apart, checked
all-pairs for colour-vision deficiency and for contrast on both light and dark paper).
A show takes the first free slot the first time an episode of it is logged, and keeps
it. The seventh and later shows render in neutral ink. The slots are pinned in
`podcast_shows.yml` as `color_slot` so that adding a show never repaints another.

| Slot | Light | Dark | Held by |
|---|---|---|---|
| 1 <span class="swatch s1"></span> | `#139bbe` | `#0fa3bf` | SuperDataScience |
| 2 <span class="swatch s2"></span> | `#9b541c` | `#9e5c1a` | Catalog & Cocktails |
| 3 <span class="swatch s3"></span> | `#006cec` | `#3364db` | Lenny's Podcast |
| 4 <span class="swatch s4"></span> | `#9354b5` | `#8f52a1` | The Stack Overflow Podcast |
| 5 <span class="swatch s5"></span> | `#93174f` | `#de4675` | Knowledge Graph Insights |
| 6 <span class="swatch s6"></span> | `#939133` | `#9b981b` | The Best Job I've Ever Had |
| none <span class="swatch s0"></span> | `#8A867C` | `#8A867C` | Practical AI, GraphGeeks, Linear Digressions |

A `featured` flag that would decide which shows get colour is on the
[roadmap](roadmap.md).

## Two kinds of work, one script

The division of labour runs through everything here. **Mechanics** (Apple lookups, id
slugs, duplicate checks, colour slots, the exact front matter) belong to
`add_listen.py` and are identical every time. **Judgment** (which episode I mean, who
the guests are, which topics are central, my spark) belongs to the conversation. No one
hand-writes a `_listens/` file, because a second `katie_malone` spelled `katy_malone`
quietly splits a node in the graph.
