# Listens

One markdown file per episode heard, in `_listens/`. The front matter is produced by
`add_listen.py listen` from the Apple lookup plus the choices made in conversation; the
body, if any, is my longer notes and renders publicly on the episode page.

## A real file

```yaml
---
title: Fall 2025 Data & Analytics trends with Sanjeev Mohan
show: catalog_cocktails
published_on: '2025-11-12'
listened_on: '2025-12-18'
listened_precision: day
guests:
- sanjeev_mohan
topics:
- knowledge_graphs_semantics
- ai_agents
duration_min: 59
episode_url: https://podcasts.apple.com/us/podcast/fall-2025-data-analytics-trends-with-sanjeev-mohan/id1524652737?i=1000743978257
audio_url: https://traffic.omny.fm/d/clips/.../audio.mp3
guid: 780518b8-8ffd-4721-b863-b39201789b51
itunes_track_id: 1000743978257
summary: Tim and Juan chat with the honest no-bs analyst Sanjeev Mohan to discuss the latest trends in the data & analytics space. ...
spark:
spark_draft: false
moments:
- at: '24:25'
  shot_on: '2025-12-18'
  chapter: Exploring AI as the New UI and Agent Experie
provenance:
  metadata: itunes
  guests: confirmed in conversation
  spark: not yet written
---
```

That is `_listens/2025-12-18-catalog-cocktails-fall-2025-data-analytics-trends-with.md`,
logged from a screenshot. The chapter title is stored as the player showed it, cut off.

## Fields

| Field | Set by | Meaning |
|---|---|---|
| `title` | lookup | Episode title as published, zero-width characters stripped |
| `show` | conversation | Show id |
| `episode_number` | lookup, optional | Parsed from the title (`1029:`, `Episode 12`, `Ep. 12`, `#12`); overridable |
| `published_on` | lookup | `YYYY-MM-DD` |
| `listened_on` | conversation | `YYYY-MM-DD`; default today |
| `listened_precision` | conversation | `day`, `month`, `year` or `approximate`. Back-filled seeds use the publish date with `approximate` |
| `guests` | conversation | Person ids; empty for host-only episodes. Hosts of this show are refused here |
| `topics` | conversation | One to three topic ids |
| `duration_min` | lookup | Rounded minutes |
| `episode_url` | lookup | Apple episode page, tracking parameter removed |
| `audio_url` | lookup | Direct audio |
| `guid` | lookup | The feed guid; the **dedupe key** |
| `itunes_track_id` | lookup | Apple's episode id |
| `summary` | lookup | First two sentences of the show notes, cut before sponsor and boilerplate blocks |
| `spark` | me | One sentence in my words, or empty |
| `spark_draft` | flag | `true` only when a model drafted the spark; such sparks are never published |
| `related_links` | lookup, optional | For example a `Takeaway - <title>` companion episode the script found in the same feed |
| `moments` | `add-moment`, optional | See [Moments](moments.md) |
| `provenance` | script | `metadata`: itunes, rss or manual. `guests`: confirmed in conversation. `spark`: mine, drafted by Claude, or not yet written |

`provenance` is always the last key; `add-moment` keeps it there.

## File name

```
<listened_on>-<show id with _ replaced by ->-<first six words of the title>.md
```

The name is the episode's URL (`/listening/<name>/`) and the key that works and the
graph use to point at it, so it is **never renamed**. A corrected listen date changes
`listened_on` in the front matter and leaves the file name alone.

## Dates

Two dates, two meanings. `published_on` is the episode's; `listened_on` is mine. The page
has a slider that filters on either, defaulting to listened. `listened_precision` says
how much to trust `listened_on`: the episode page prefixes "About" when it is
`approximate`.

## The spark and the draft flag

The Liquid template that generates the graph JSON emits `spark: null` whenever
`spark_draft` is true, and the episode layout shows "Nothing written yet" in the same
case. So a drafted spark can sit in the file, in the public repository, as a starting
point, without ever appearing on the site. Rewriting it means: replace `spark`, delete
`spark_draft`, set `provenance.spark: mine`.

## What a listen may not contain

Transcript text from a screenshot, or any key under `moments` other than `at`,
`shot_on` and `chapter`. The validator rejects both. The reasoning is on the
[moments](moments.md) page.
