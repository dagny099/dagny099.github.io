# Normalization Audit

## Scope

This audit covers the Jekyll source repository for the PageIndex Release 1 corpus pipeline. It inspects repository guidance, Jekyll configuration, collections, pages, posts, resources, data files, includes, layouts, and existing scripts relevant to deriving a normalized Markdown corpus.

## Repository Instructions

- `CLAUDE.md` describes the site as a Jekyll/Minimal Mistakes personal website hosted on GitHub Pages.
- No `AGENTS.md` file was found.
- The public site must remain authoritative; this experiment is isolated under `experiments/pageindex/`.

## Jekyll Configuration

Source: `_config.yml`

- Remote theme: `mmistakes/minimal-mistakes@4.27.1`
- Site URL: `https://barbhs.com`
- Default post permalink: `/blog/:title/`
- Included nonstandard pages path: `_pages`
- Collections:
  - `projects`, output true, permalink `/projects/:name/`
  - `resources`, output true, permalink `/resources/:name/`
  - `snippets`, output true, permalink `/snippets/:name/`
  - `thinking`, output true, permalink `/thinking/:name/`
- `data-stories` exists as a directory but is not currently enabled as a collection in `_config.yml`.
- Excluded from build: repository docs, scripts, agent context, Gem files.

## Discovered Content Types

| Type | Source directory | Count inspected | Notes |
| --- | --- | ---: | --- |
| Static pages | `_pages/`, root pages, `about/`, `contact/`, `projects/`, `resources/`, `thinking/` | 24 | Mix of Markdown and HTML-heavy pages. Some pages have blank `title` and rely on visible HTML headings. |
| Posts | `_posts/` | 25 | Standard dated Jekyll posts. Some older posts are short series stubs. |
| Projects | `_projects/` | 8 | Current public project collection with architecture, stack, status, docs links, and implementation notes. |
| Resources | `_resources/` | 19 | Public resources plus `_archive` and draft/schema resources. |
| Thinking | `_thinking/` | 4 | Short essay collection focused on RAG, perception, graphs, and chunking. |
| Snippets | `_snippets/` | 8 | Garden/inbox style notes; not selected for Release 1. |
| Data stories | `data-stories/` | 5 | Public narrative pages plus one unpublished draft. Not configured as a collection. |
| Legacy portfolio | `_portfolio/` | 6 | Older portfolio collection noted in repo docs but not configured in current `_config.yml`. |
| Data files | `_data/` | 8 | Includes public infographics, navigation, UI text, quotes, portfolio JSON, and resume data. |

## Front-Matter Schemas

### Pages

Common fields: `layout`, `title`, `description`, `excerpt`, `permalink`, `classes`, `author_profile`, `breadcrumbs`, `toc`, `header`, `gallery`, `tags`, `categories`, `canonical_url`, `published`, `noindex`, `sitemap`.

Meaningful differences:

- Several HTML-heavy pages use blank titles in front matter and render visible titles in HTML.
- Some pages act as navigational indexes rather than substantive source documents.
- Some pages, such as the Digital Twin reference pages, contain large HTML structures and filterable data tables.

### Posts

Common fields: `title`, `date`, `permalink`, `canonical_url`, `description`, `excerpt`, `subtitle`, `tags`, `categories`, `stack`, `header`, `last_modified_at`, `published`, `redirect_from`, `sitemap`.

Meaningful differences:

- Most current posts have explicit permalinks; posts without explicit permalinks follow `_config.yml` default `/blog/:title/`.
- Older series entries can be short and primarily navigational.
- One post is explicitly unpublished.

### Projects

Common fields: `title`, `permalink`, `excerpt`, `description`, `tags`, `stack`, `status`, `header`, `gallery`, `docs_url`, `docs_label`, `url`, `order`, `toc`, `last_modified_at`.

Meaningful differences:

- Project pages are the strongest implementation evidence: architecture, data models, evaluation, screenshots/artifacts, and links.
- Several public projects are marked `WIP`; this is public source metadata and is preserved.
- Project image paths in front matter reference some missing local assets.

### Resources

Common fields: `title`, `subtitle`, `permalink`, `excerpt`, `date`, `tags`, `categories`, `format`, `level`, `download_url`, `cognitive_principle`, `header`, `toc`, `published`, `status`, `sitemap`, `last_modified_at`.

Meaningful differences:

- `_resources/_archive/` contains plausible but archived/superseded items.
- Two schema.org resources are draft/unpublished and excluded.
- The Resources index is partly data-driven from `site.resources` and `_data/infographics.yml`.

### Thinking

Common fields: `title`, `subtitle`, `date`, `permalink`, `excerpt`, `tags`, `categories`, `stack`, `header`, `teaser`, `teaser_alt`, `pin`, `read_time`, `toc`.

Meaningful differences:

- Short, concept-dense essays rather than implementation writeups.
- Useful for PageIndex cross-theme navigation because headings are already semantic.

### Data Stories

Common fields: `layout`, `title`, `description`, `excerpt`, `permalink`, `date`, `tags`, `stack`, `status`, `published`, `redirect_from`, `header`, `section`.

Meaningful differences:

- Three public long narratives overlap selected project themes.
- One ChronoScope data story is draft/unpublished and excluded.

## Liquid Tags And Includes Found

Selected content contains or references:

- Variables: `relative_url`, loop variables such as `{{ f }}`, and post URL helpers.
- Includes: `page__taxonomy.html`, `resource/buttons.html`, `infographic-gallery.html`, `cards_grid.html`, `figure`, `punchline.html`, `download-callout.html`, `visual-companion.html`, `quote.html`, `feature_row_dual`, `section_tiles.html`.
- Control flow: `assign`, `if`, `for`, `endif`, `endfor`.

Normalization handling:

- Deterministic URLs are resolved.
- Resource cards and infographic gallery are expanded from local data/source files.
- Figures, punchlines, download callouts, and visual companion blocks are converted to Markdown.
- Layout-only includes and filter controls are removed and recorded.
- Unresolved quote/homepage tile includes are removed with warnings, not silently discarded.

## Data-Driven Content

- `resources/index.md` renders the infographic band through `_data/infographics.yml`.
- `resources/index.md` renders resource cards from `site.resources`.
- `projects/index.html` and `_data/portfolio.json` describe a broader public project set than `_projects/`, including Digital Twin, Concept Cartographer, TranscriptWorkbench, and Naruto Network Graph.
- `_data/barbara_resume_golden.json` and its schema back the Experience/resume architecture, but they were not selected as source corpus documents for Release 1 to avoid over-expanding the scope.

## Duplicate, Deprecated, Redirected, Draft, Or Ambiguous Content

- `_resources/_archive/` contains archived resources that are plausible but short or superseded.
- `_resources/resource-schema-org-cheatsheet-builders.md` and `_resources/resource-schema-org-cheatsheet-humans.md` are draft/unpublished.
- `data-stories/converting-textual-to-visual-timeline.md` is draft/unpublished.
- `_posts/2022-09-16-diy-stock-ticker-to-learn-python-frameworks.md` is unpublished.
- `_pages/about-prev.md` is explicitly unpublished.
- Legacy `_portfolio/` pages overlap newer `_projects/` and `_data/portfolio.json`.
- Digital Twin reference pages are public and substantive but very large and HTML/table-heavy; they are deferred.

## Risks To Normalization

- HTML-heavy pages need deterministic Markdown conversion and can lose some layout nuance.
- Deep HTML heading structures can exceed Markdown level six after demotion; the pipeline flattens and reports these.
- Missing local image paths in source front matter/body should be reviewed before treating assets as evidence.
- Public WIP statuses must be preserved without implying shipped state.
- Data-driven cards must be rendered from local source data, not live website output.
- Liquid includes can be content-bearing; unresolved constructs must be warnings, not silent drops.
- Current repository worktree was dirty before this task; generated manifest records source hashes to preserve provenance.

## Recommended Provisional Corpus Selection

Core pages:

- `index.md`
- `_pages/start_here.md`
- `_pages/work-with-me.md`
- `_pages/my-journey.html`

Projects:

- `_projects/poolula-platform-rag-chatbot.md`
- `_projects/fitness-dashboard-ml-pipeline.md`
- `_projects/beehive-knowledge-builder.md`
- `_projects/chronoscope-timeline-builder.md`
- `_projects/digital-memory-chest-app.md`
- `_projects/convoscope-llm-chat-compare.md`

Articles/thinking:

- `_posts/2026-05-12-twin-evaluate-models.md`
- `_posts/2026-05-16-twin-graphrag-migration.md`
- `_posts/2026-06-26-ai-literacy-judgment.md`
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`
- `_posts/2026-07-04-scoring-ai-instruction-files.md`
- `_posts/2026-03-12-three-readers-of-your-web-page.md`
- `_posts/2025-11-7-metadata-matters.md`
- `_thinking/2025-09-11-rag-without-the-theater.md`
- `_thinking/2025-09-11-bees-graphs-governance.md`
- `_thinking/2024-09-26-chunking-is-all-you-need.md`

Resources:

- `resources/index.md`
- `_resources/knowledge-legibility-diagnostic.md`
- `_resources/what-is-a-harness-in-ai.md`
- `_resources/memory-is-more-than-storage.md`
- `_resources/resume-data-schema.md`
- `_resources/ai-instructions-evaluation-worksheet.md`

Supporting data:

- `_data/infographics.yml`
- `_data/portfolio.json`

## Assumptions For The Pipeline

- Public content means source files not explicitly marked `published: false`, `private: true`, or `status: draft`.
- `_resources/_archive/` is treated as archived and excluded from Release 1 resource-card expansion.
- Expected titles in the selection manifest may be used only when front matter has a blank title.
- Jekyll's default post URL can be derived from `_config.yml` permalink and the filename slug when a post lacks an explicit permalink.
- HTML-rendered layout wrappers, filters, global navigation, repeated card chrome, and JavaScript are not semantic corpus content.
- Source Markdown remains more authoritative than rendered `_site` HTML for Release 1.
