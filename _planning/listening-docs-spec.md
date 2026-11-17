# Spec: documentation site for the listening system

Status: drafted 2026-11-16; built 2026-11-17 in `_docs/` + `mkdocs.yml` (strict build clean). Not yet committed or hosted. Decision made the same day: MkDocs Material,
built in the site repo. Read this once, then read the sources in section 4 before writing.

## 1. What it is

A reference for the whole "listening" system: the `/listening/` graph page, the `_listens/`
collection and its data files, the `add_listen.py` toolchain and `add-listen` skill, the
screenshot intake in the private `podcast-ingest-agent` repo, validation and tests, and
publishing. It documents **what is built today**, with one clearly separate roadmap page
for what is designed but not built. The three planning files in `_planning/`
(`podcast-graph-pilot.md`, `works-spike.md`, `sparks-handoff.md`) stay as design history
and are linked from a decisions log, not rewritten into the docs.

## 2. Hard rules

- **Public/private line.** The site repo is public. The docs may describe the ledger's
  shape, the burst rules and the moments schema. They never include passage text from a
  screenshot, device names, the ledger itself, or any screenshot image.
- **No sweeping claims.** Scope every statement to this system as built.
- **Never hand-write `_listens/`** examples that could be mistaken for real files; label
  samples as samples.
- The Cirrus engagement is not mentioned anywhere.

## 3. Where it lives

- Source: `_docs/` (underscore folder, so Jekyll ignores it without a `_config.yml` change)
  with `docs_dir: _docs` in a root `mkdocs.yml`. Output `site_dir` goes to a gitignored
  folder (`_docs_site/`), never `_site/`, which Jekyll cleans.
- Hosting is a **separate, ask-first step**: one workflow step in
  `.github/workflows/pages.yml` running `mkdocs build -d _site/listening/docs` after the
  Jekyll build, so the docs land at `barbhs.com/listening/docs/`. Until approved, the docs
  build locally only.
- `mkdocs` is installed at `~/miniconda3/bin/mkdocs`; confirm `mkdocs-material` there.
  Conventions from the nine other MkDocs sites in `~/PROJECTS` (copy `mkdocs.yml` from
  `barbs-digital-twin`): theme material, plugins search / tags / glightbox /
  git-revision-date-localized / minify, pymdownx extensions, admonitions, tabbed blocks.

## 4. Sources to read before writing (all read once on 2026-11-16)

| Area | Files |
|---|---|
| Design history | `_planning/podcast-graph-pilot.md` (335 lines), `works-spike.md`, `sparks-handoff.md` |
| Workflow | `.claude/skills/add-listen/SKILL.md` |
| Scripts | `scripts/listens/add_listen.py`, `itunes_lookup.py`, `works_lookup.py`, `validate.py`, `test_moments.py` |
| Site | `_config.yml` (listens collection, defaults, exclude), `_layouts/listen.html`, `listening/index.html` (806 lines, D3), `assets/data/listens-graph.json` (Liquid-generated) |
| Data | `_data/podcast_shows.yml`, `podcast_people.yml`, `podcast_topics.yml`, `podcast_works.yml`, `_listens/*.md` |
| Private intake | `~/PROJECTS/podcast-ingest-agent/screenshots/README.md`, `intake.py`, `test_intake.py`, `CONTRACTS.md` (ids), `README.md` |

## 5. Nav outline

1. **Home**: what the page is (episodes as a graph, sparks in her words), the one-paragraph
   tour, links into each section.
2. **Concepts**: show, episode/listen, person (guest vs host), topic, work, spark vs
   spark draft, moment; the "guest who hosts another show" pattern; why color is reserved
   for shows (6 validated slots, 7th folds to ink).
3. **Data model**: one page per file with schema tables and a labelled sample; ids
   (snake-case slug of the normalized name); edges (HAS_EPISODE, HOSTS, GUEST_ON,
   COVERS, MENTIONS, WROTE, RECOMMENDS); the graph JSON shape; `listened_precision`;
   `provenance`; moments (`at`, `shot_on`, `chapter` only).
4. **Adding a listen**: the add-listen workflow step by step, with the real commands;
   dry-run vs `--write`; the Apple 200-episode limit and what to do past it; takeaway
   companions; works step 5b and the catalog rules (title lookups only, never author
   records).
5. **Screenshot intake** (private repo): flow from Drive inbox to ledger to bursts to
   `match_episode` to `add-moment`; the matching rules (published-after-shot impossible,
   fragments must fit respecting cut edges, duration breaks ties within 3 s); statuses
   matched / ambiguous / unresolved; what stays private.
6. **Validation and tests**: what `validate.py` checks, `test_moments.py`,
   `test_intake.py`, running them (pyenv python 3.10.12 for PyYAML).
7. **The page and episode pages**: controls, encodings, `?focus=`, list view, dark mode,
   what the episode layout renders and in what order.
8. **Publishing and review**: branch `listen/<slug>`, stage only listens and
   `podcast_*.yml`, commit format, PR as the review gate, PRs build but do not deploy.
9. **Roadmap**: RSS path in `add_listen.py` (needed for The AI Daily Brief), moments on
   the page, featured flag, spark call, logging from the phone, works tier 2,
   organizations, spark nodes, Neo4j export.
10. **Decisions log**: dated decisions pulled from the three planning files, each linking
    to its source.

## 6. Done means

- `mkdocs build --strict` passes from the repo root with zero warnings.
- Every page cross-links at least two others; no page is a dead end.
- `bundle exec jekyll build` still passes and `_site/` contains no `_docs` output.
- A PR on a branch `docs/listening-site` from `origin/master`, touching only
  `mkdocs.yml`, `_docs/`, `.gitignore`, and this file's status line. The workflow and
  any `_config.yml` change are proposed in the PR body, not made.
