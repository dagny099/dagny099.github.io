# Reference

| Page | Covers |
|---|---|
| [add_listen.py](add-listen-cli.md) | Every subcommand, its flags, and what it refuses |
| [Lookup helpers](lookups.md) | `itunes_lookup.py` and `works_lookup.py` |
| [Environment](environment.md) | Interpreters, locales, rate limits and other things that trip sessions up |

## Files map

| Path | What it is |
|---|---|
| `_listens/*.md` | One file per episode heard |
| `_data/podcast_shows.yml` | Shows and their hosts |
| `_data/podcast_people.yml` | Guests and hosts |
| `_data/podcast_topics.yml` | Topic vocabulary |
| `_data/podcast_works.yml` | Works and their mentions |
| `assets/data/listens-graph.json` | Liquid template; the page's data |
| `listening/index.html` | The graph page |
| `_layouts/listen.html` | The episode page layout |
| `_config.yml` | The `listens` collection, its permalink and layout default, and the `exclude` list that keeps `scripts/` out of the build |
| `scripts/listens/add_listen.py` | The mechanics |
| `scripts/listens/itunes_lookup.py` | Apple Podcasts lookups |
| `scripts/listens/works_lookup.py` | Open Library and Crossref lookups |
| `scripts/listens/validate.py` | The checks |
| `scripts/listens/test_moments.py` | Tests for moments |
| `.claude/skills/add-listen/SKILL.md` | The conversational workflow |
| `_planning/podcast-graph-pilot.md` | Pilot plan and as-built notes, October 2026 |
| `_planning/works-spike.md` | Works spike findings and decisions |
| `_planning/sparks-handoff.md` | Screenshot intake and moments handoff, November 2026 |
| `_planning/listening-docs-spec.md` | The spec for this documentation |
| `podcast-ingest-agent/screenshots/` (private) | `intake.py`, `test_intake.py`, `ledger.jsonl`, fixtures, README |
