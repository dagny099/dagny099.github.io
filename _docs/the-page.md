# The page

Two templates render the listening data: the graph at `/listening/` and an episode page
at `/listening/<name>/` for every listen.

## `/listening/`

`listening/index.html` is a standalone page (`layout: null`), a D3 force layout in the
same visual language as the project map at `/projects/graph.html`: EB Garamond and IBM
Plex Sans, paper, teal and coral tokens, and a dark mode that follows the system or a
`data-theme` attribute. It fetches `assets/data/listens-graph.json` and builds
everything client-side.

### Encoding

- **Colour is for shows only.** Episodes take their show's colour. People are ink;
  topics are small, sand-outlined, and sit on an outer ring with faint edges that
  strengthen on hover. Show nodes scale with the number of logged episodes.
- **Selection is an ink ring**, which reads against every show colour. The brand teal
  stays in the UI chrome; it fails the chroma floor for a show colour, and coral sits too
  close to the rose slot.
- **A paper centre** marks an episode whose spark is not in my words yet.
- The six show colours and the fold to neutral ink are described under
  [colour slots](concepts.md#colour-slots).

### Controls

| Control | What it does |
|---|---|
| Listened / Published | Which date the slider filters on. Listened is the default |
| Date range | Two handles; a rug under the track shows where episodes fall |
| Search | Matches guests, topics and episode titles |
| Graph / List | The list view is the table twin of the graph, same filters |
| Works | Adds the works layer (hidden until there is at least one work) |
| Show legend | Click a show to hide or show its episodes |

### Interaction

- Hover an episode: a tooltip with the spark.
- Click an episode: a side panel with show, guests, both dates, topics, spark, notes,
  works mentioned, and links to the episode page and the audio. On phones the panel is a
  bottom sheet and the layout goes portrait with counter-scaled labels.
- Click a person or a topic: its neighbourhood is highlighted.
- The layout settles before first paint, then fits the space under the header.

### URL parameters

| Parameter | Effect |
|---|---|
| `?focus=ep:/listening/<name>/` | Preselects that episode; the episode page's "See it on the graph" link uses it |
| `?works=1` | Turns the works layer on at load |

## Episode pages

`_layouts/listen.html` extends the theme's `single` layout. Every listen renders with
it because `_config.yml` sets `layout: listen` as the default for the collection, with
`classes: wide` and the author profile, sharing and comments turned off.

The page shows, in order:

1. A kicker with the show's colour key, its name and the episode number.
2. Listened and published dates ("About" prefixes an approximate listen date) and the
   length.
3. **What it sparked**: the spark in large serif, or "Nothing written yet" when it is
   empty or a draft.
4. **My notes**: the markdown body, if any.
5. **From the show notes**: the two-sentence summary.
6. **Guests**, as chips with their one-line bios.
7. **Topics**, as chips.
8. **Works mentioned**, grouped by the guest's own, recommended (with who recommended
   it), then discussed; the show's own posts drawn quieter; my read / want-to-read
   marker if set.
9. **Connected on the graph**: up to six other episodes, those sharing a guest first,
   then those sharing a topic, each with the show name and the reason.
10. Links: "See it on the graph" (with `?focus=`), "Listen", and any related links such
    as a takeaway episode.

Moments are not rendered yet; see the [roadmap](roadmap.md).

## Design review, October 2026

A review of the first build removed what it called generated-UI tells: an italic
coloured title clause, mono uppercase micro-labels, a quote rail on the spark, and
chains of middots. Sparks moved into the hover tooltip; ticks appeared under the date
slider. The rule that came out of it, kept by every session since, is simply that those
tells stay out.

## How it is linked

`/listening/` is not in the site navigation. `/projects/` carries a text link under the
project-map link, labelled as a pilot. A second navigation level is on the parking lot
until there are two or three lab-style pages to group.
