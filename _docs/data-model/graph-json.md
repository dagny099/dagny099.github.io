# Graph JSON

`assets/data/listens-graph.json` is what the page fetches. It is a Liquid template with
`layout: null` that Jekyll renders at build time from the data files and the listens
collection, so it is **never edited by hand** and never out of step with the files.

## Shape

```json
{
  "generated": "2026-11-16T...",
  "shows":  [ ...podcast_shows.yml as JSON... ],
  "people": [ ...podcast_people.yml... ],
  "topics": [ ...podcast_topics.yml... ],
  "works":  [ ...podcast_works.yml... ],
  "listens": [
    {
      "id": "/listening/2025-12-18-catalog-cocktails-fall-2025-data-analytics-trends-with/",
      "url": "/listening/2025-12-18-catalog-cocktails-fall-2025-data-analytics-trends-with/",
      "title": "Fall 2025 Data & Analytics trends with Sanjeev Mohan",
      "show": "catalog_cocktails",
      "episode_number": null,
      "published_on": "2025-11-12",
      "listened_on": "2025-12-18",
      "listened_precision": "day",
      "guests": ["sanjeev_mohan"],
      "topics": ["knowledge_graphs_semantics", "ai_agents"],
      "duration_min": 59,
      "episode_url": "https://podcasts.apple.com/...",
      "summary": "Tim and Juan chat with ...",
      "spark": null,
      "spark_draft": false,
      "related_links": null,
      "notes_html": ""
    }
  ]
}
```

Listens are sorted by `listened_on`, newest first. The four data files pass through
`jsonify` unchanged, so anything added to them reaches the client. The listen objects
are an explicit allow-list of fields: `moments`, `audio_url`, `guid` and
`itunes_track_id` are **not** emitted.

## The draft-spark rule, in the template

```liquid
"spark": {% if l.spark_draft %}null{% else %}{{ l.spark | jsonify }}{% endif %},
```

A drafted spark is replaced by `null` before it leaves the build. The episode layout
applies the same test. Removing `spark_draft` from the file is what publishes a spark.

## Node ids on the client

The page builds nodes from this JSON. Episode nodes are keyed `ep:` plus the listen's
URL, which is what the episode page's "See it on the graph" link passes as
`?focus=ep:/listening/<name>/`. Shows, people, topics and works are keyed by their ids.
People and topics referenced by nothing are dropped before layout.

## Shape compatibility

The `nodes` / `links` / `type` / `provenance` vocabulary follows the Graph Garnish
convention used in other projects of mine, so that tooling can move between them. The
edge types are listed on the [data model overview](index.md#edges).
