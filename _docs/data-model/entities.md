# Shows, people, topics

Three YAML lists in `_data/`. Each is appended to by one `add_listen.py` subcommand
(see the [CLI reference](../reference/add-listen-cli.md)); comments at the top of each
file survive because the script appends rather than rewrites.

## `podcast_shows.yml`

```yaml
- id: superdatascience
  color_slot: 1
  name: SuperDataScience
  hosts:
  - jon_krohn
  itunes_id: 1163599059
  feed_url: https://feeds.megaphone.fm/SUPERDATASCIENCEPTYLTD9836501887
  apple_url: https://podcasts.apple.com/us/podcast/super-data-science-ml-ai-podcast-with-jon-krohn/id1163599059
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Slug; the value a listen's `show` field points at |
| `name` | yes | Display name, from Apple's `collectionName` unless overridden |
| `hosts` | yes, may be empty | Person ids; each becomes a `HOSTS` edge. Every id must exist in `podcast_people.yml` |
| `itunes_id` | yes | Apple `collectionId`; lets the script list episodes without touching the RSS host |
| `feed_url` | from lookup | The RSS feed, for episodes older than Apple's latest 200 |
| `apple_url` | from lookup | The show's Apple Podcasts page |
| `color_slot` | set on first listen | 1 to 6; pins the show's colour on the page. Absent means neutral ink |

A show with hosts and no listens is valid and renders as a hollow node. Nine shows are
on file as of November 2026, six of them with a colour slot.

## `podcast_people.yml`

```yaml
- id: sanjeev_mohan
  name: Sanjeev Mohan
  bio: Data & analytics industry analyst.
  source: Catalog & Cocktails 2025-11-12 description
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Slug of the name |
| `name` | yes | As written in the show notes |
| `bio` | yes | One line. If the description says nothing about who they are, the bio says what the description does say |
| `source` | yes | Where the bio came from: `itunes artistName`, `<show> <date> description`, `episode descriptions`, or a note such as `one feed mention; verify` |

Bios come from the episode description, not from general knowledge. The rule exists so
that a wrong guess never reaches a public page with a confident tone. A person can be
both a host of one show and a guest on another; that is a single entry.

## `podcast_topics.yml`

```yaml
- id: knowledge_graphs_semantics
  label: Knowledge graphs & semantics
  description: Ontologies, semantic layers, and graph-grounded AI.
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Slug |
| `label` | yes | Shown on the page and on episode pages |
| `description` | yes | One line, what belongs here |

The twelve topics as of November 2026:

| Id | Label |
|---|---|
| `ai_agents` | AI agents |
| `data_governance` | Data governance |
| `data_quality_trust` | Data quality & trust |
| `data_business_alignment` | Data & the business |
| `knowledge_graphs_semantics` | Knowledge graphs & semantics |
| `llm_internals` | How LLMs work |
| `ai_roi_adoption` | AI ROI & adoption |
| `human_taste_judgment` | Taste & judgment |
| `ai_era_careers` | AI-era careers |
| `managing_people_and_agents` | Managing people & agents |
| `teaching_ai` | Teaching AI |
| `evaluation_testing` | Evaluation & testing |

Topics are the cross-show connective tissue, so the vocabulary stays small: stretch an
existing topic before proposing a near-duplicate, and keep each episode to the one to
three topics that are central. More edges make the graph a hairball.
