# Normalization Report

## Final Selected Content

### Core Positioning Pages
- `index.md` — Primary professional positioning and public homepage framing for applied AI, data systems, and knowledge systems.
- `_pages/start_here.md` — Orientation page that makes the site navigable by audience and intent.
- `_pages/work-with-me.md` — Service and offer framing for knowledge legibility audits, verified AI systems, and workshops.
- `_pages/my-journey.html` — Professional narrative connecting cognitive science, data systems, and human-centered AI work.

### Project Portfolio
- `_projects/poolula-platform-rag-chatbot.md` — Flagship RAG business-intelligence system with structured data, unstructured documents, evaluation harnesses, and provenance.
- `_projects/fitness-dashboard-ml-pipeline.md` — Concrete ETL, ML classification, evaluation, and transparent analytics project with implementation evidence.
- `_projects/beehive-knowledge-builder.md` — Multimodal knowledge-system project combining photos, metadata, APIs, weather context, and graph-oriented reasoning.
- `_projects/chronoscope-timeline-builder.md` — Document-to-timeline extraction system with validation concerns and structured temporal knowledge.
- `_projects/digital-memory-chest-app.md` — Knowledge graph and AI narrative system for memory, provenance, transcription, and multimodal organization.
- `_projects/convoscope-llm-chat-compare.md` — Multi-provider LLM orchestration and model-comparison project that supports evaluation and resilience themes.

### Articles
- `_posts/2026-05-12-twin-evaluate-models.md` — AI-system evaluation article based on a controlled Digital Twin model comparison.
- `_posts/2026-05-16-twin-graphrag-migration.md` — GraphRAG migration article comparing vector retrieval and graph-backed retrieval systems.
- `_posts/2026-06-26-ai-literacy-judgment.md` — Thought-leadership piece connecting AI literacy, judgment, evaluation, and human-led decision boundaries.
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md` — Organizational AI adoption article focused on operating infrastructure, quality bars, and value realization.
- `_posts/2026-07-04-scoring-ai-instruction-files.md` — Evaluation-harness thinking applied to AI instruction files and agent configuration.
- `_posts/2026-03-12-three-readers-of-your-web-page.md` — Knowledge legibility article explaining audiences for metadata, structured data, and public web representation.
- `_posts/2025-11-7-metadata-matters.md` — Metadata and schema article that supports the corpus theme of making public work machine-legible.
- `_thinking/2025-09-11-rag-without-the-theater.md` — Compact RAG design guidance focused on evidence-linked retrieval, guardrails, and evaluation.
- `_thinking/2025-09-11-bees-graphs-governance.md` — Knowledge graph and governance essay that bridges a personal data project to enterprise evidence practices.
- `_thinking/2024-09-26-chunking-is-all-you-need.md` — Cognitive-science framing for chunking, interface design, and sensemaking systems.

### Resources
- `resources/index.md` — Required Resources page; combines public resource records, infographics, guide links, and project artifacts.
- `_resources/what-is-a-harness-in-ai.md` — Evaluation terminology resource that clarifies multiple meanings of harness in AI systems.
- `_resources/memory-is-more-than-storage.md` — Public proof asset connecting human memory, AI agent memory, and knowledge-system architecture.
- `_resources/resume-data-schema.md` — Structured resume metadata reference relevant to Resume Graph Explorer and machine-legible professional history.
- `_resources/ai-instructions-evaluation-worksheet.md` — Companion evaluation worksheet that operationalizes the AI instruction-file scoring article.

## Excluded Candidate Content

- `_pages/digital-twin-graphrag-reference.html` (page): substantive but extremely large and heavily HTML/data-table driven; better candidate for Release 2 once table normalization is designed.
- `_pages/digital-twin_compare_llms.html` (page): substantive but overlaps the selected Digital Twin evaluation article and is highly HTML-specific.
- `_pages/ai-pulse-q2-2026-companion.html` (page): strong article but outside the first release's tighter emphasis on Barbara's own systems and reusable evaluation patterns.
- `_projects/job-application-assistant.md` (project): public project, but superseded by stronger current AI-system examples for Release 1.
- `_projects/midjourney-tracker-browser-extension.md` (project): public project, but less central to RAG, knowledge graphs, evaluation, or knowledge legibility.
- `data-stories/citation-link-prediction.md` (data_story): strong graph/ML story; deferred to keep article count within target and avoid over-weighting project-style narratives.
- `data-stories/hive-photo-metadata-tracker.md` (data_story): substantially overlaps selected Beehive project page and Bees/Graphs/Governance essay.
- `data-stories/converting-textual-to-visual-timeline.md` (data_story): unpublished/draft.
- `_posts/2022-09-16-diy-stock-ticker-to-learn-python-frameworks.md` (post): unpublished.
- `_resources/resource-schema-org-cheatsheet-builders.md` (resource): draft/unpublished.
- `_resources/resource-schema-org-cheatsheet-humans.md` (resource): draft/unpublished.
- `_resources/_archive/` (resources_archive): archived resources are plausible but mostly short, superseded, or outside Release 1 focus.

## Source Counts By Type

- Core Positioning Pages: 4
- Project Portfolio: 6
- Articles: 10
- Resources: 5

## Front-Matter Schemas Encountered

See `reports/NORMALIZATION_AUDIT.md` for the full schema audit. The builder preserves original front matter in the manifest and maps selected common fields into a normalized metadata model.

## Field Mappings

- `title` -> normalized title, falling back to the selection manifest expected title only when the source title is blank.
- `description` or `excerpt` -> visible summary.
- `permalink`, `canonical_url`, or Jekyll post slug -> canonical URL.
- `date` -> publication date.
- `last_modified_at` -> last modified date.
- `tags`, `categories`, `status`, `stack`, `docs_url`, `url` -> visible item metadata when present.

## Liquid/Include Transformations

- `index.md`: `include` -> removed_unresolved (feature_row_dual)
- `index.md`: `include` -> removed_unresolved (section_tiles.html)
- `index.md`: `html` -> converted_to_markdown ()
- `_pages/start_here.md`: `html` -> converted_to_markdown ()
- `_pages/work-with-me.md`: `html` -> converted_to_markdown ()
- `_pages/my-journey.html`: `include` -> expanded_quote (quote.html)
- `_pages/my-journey.html`: `html` -> converted_to_markdown ()
- `_projects/poolula-platform-rag-chatbot.md`: `include` -> removed_layout_or_navigation (page__taxonomy.html)
- `_projects/fitness-dashboard-ml-pipeline.md`: `include` -> removed_layout_or_navigation (page__taxonomy.html)
- `_projects/beehive-knowledge-builder.md`: `include` -> removed_layout_or_navigation (page__taxonomy.html)
- `_projects/chronoscope-timeline-builder.md`: `include` -> removed_layout_or_navigation (page__taxonomy.html)
- `_projects/digital-memory-chest-app.md`: `include` -> removed_layout_or_navigation (page__taxonomy.html)
- `_projects/convoscope-llm-chat-compare.md`: `include` -> removed_layout_or_navigation (page__taxonomy.html)
- `_posts/2026-05-12-twin-evaluate-models.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-26-ai-literacy-judgment.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-26-ai-literacy-judgment.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_callout (punchline.html)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_callout (punchline.html)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_callout (punchline.html)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_callout (punchline.html)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_figure (figure)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_callout (download-callout.html)
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: `include` -> expanded_callout (visual-companion.html)
- `_posts/2026-03-12-three-readers-of-your-web-page.md`: `liquid_variable` -> relative_url_resolved (/assets/diagrams/head-architecture-v2.svg)
- `resources/index.md`: `liquid_variable` -> relative_url_resolved (/assets/downloads/missing-layer-two-reports.pdf)
- `resources/index.md`: `include` -> expanded_from_data (infographic-gallery.html)
- `resources/index.md`: `include` -> expanded_resource_collection (cards_grid.html)
- `resources/index.md`: `liquid_control` -> removed_layout_control ({% assign items = site.resources | sort: 'date' | reverse %})
- `resources/index.md`: `liquid_control` -> removed_layout_control ({% assign formats = items | map: 'format' | compact | uniq | sort %})
- `resources/index.md`: `liquid_control` -> removed_layout_control ({% if formats.size > 1 %})
- `resources/index.md`: `liquid_control` -> removed_layout_control ({% for f in formats %})
- `resources/index.md`: `liquid_control` -> removed_layout_control ({% endfor %})
- `resources/index.md`: `liquid_control` -> removed_layout_control ({% endif %})
- `resources/index.md`: `liquid_variable` -> removed_unresolved ({{ f | slugify }})
- `resources/index.md`: `liquid_variable` -> removed_unresolved ({{ f }})
- `_resources/what-is-a-harness-in-ai.md`: `liquid_variable` -> relative_url_resolved (/assets/images/resources/ai-harness-meaning-llm-agents-evals.png)
- `_resources/what-is-a-harness-in-ai.md`: `liquid_variable` -> relative_url_resolved (/blog/twin-evaluate-models/)
- `_resources/what-is-a-harness-in-ai.md`: `liquid_variable` -> relative_url_resolved (/compare-models/)
- `_resources/what-is-a-harness-in-ai.md`: `liquid_variable` -> relative_url_resolved (/blog/twin-graphrag-migration/)
- `_resources/what-is-a-harness-in-ai.md`: `liquid_variable` -> relative_url_resolved (/graphrag-reference/)
- `_resources/what-is-a-harness-in-ai.md`: `liquid_variable` -> relative_url_resolved (/work-with-me/)
- `_resources/what-is-a-harness-in-ai.md`: `include` -> removed_layout_or_navigation (resource/buttons.html)
- `_resources/memory-is-more-than-storage.md`: `liquid_variable` -> relative_url_resolved (/assets/images/resources/memory-is-more-than-storage.png)
- `_resources/memory-is-more-than-storage.md`: `include` -> removed_layout_or_navigation (resource/buttons.html)
- `_resources/ai-instructions-evaluation-worksheet.md`: `include` -> removed_layout_or_navigation (resource/buttons.html)

## Heading Transformations

- `index.md`: 13 heading transformation(s).
- `_pages/start_here.md`: 9 heading transformation(s).
- `_pages/work-with-me.md`: 13 heading transformation(s).
- `_pages/my-journey.html`: 28 heading transformation(s).
- `_projects/poolula-platform-rag-chatbot.md`: 16 heading transformation(s).
- `_projects/fitness-dashboard-ml-pipeline.md`: 23 heading transformation(s).
- `_projects/beehive-knowledge-builder.md`: 14 heading transformation(s).
- `_projects/chronoscope-timeline-builder.md`: 15 heading transformation(s).
- `_projects/digital-memory-chest-app.md`: 16 heading transformation(s).
- `_projects/convoscope-llm-chat-compare.md`: 13 heading transformation(s).
- `_posts/2026-05-12-twin-evaluate-models.md`: 7 heading transformation(s).
- `_posts/2026-05-16-twin-graphrag-migration.md`: 8 heading transformation(s).
- `_posts/2026-06-26-ai-literacy-judgment.md`: 5 heading transformation(s).
- `_posts/2026-06-30-missing-layer-ai-adoption-value.md`: 10 heading transformation(s).
- `_posts/2026-07-04-scoring-ai-instruction-files.md`: 7 heading transformation(s).
- `_posts/2026-03-12-three-readers-of-your-web-page.md`: 7 heading transformation(s).
- `_posts/2025-11-7-metadata-matters.md`: 11 heading transformation(s).
- `_thinking/2025-09-11-rag-without-the-theater.md`: 11 heading transformation(s).
- `_thinking/2025-09-11-bees-graphs-governance.md`: 8 heading transformation(s).
- `_thinking/2024-09-26-chunking-is-all-you-need.md`: 17 heading transformation(s).
- `resources/index.md`: 21 heading transformation(s).
- `_resources/what-is-a-harness-in-ai.md`: 1 heading transformation(s).
- `_resources/memory-is-more-than-storage.md`: 1 heading transformation(s).
- `_resources/resume-data-schema.md`: 26 heading transformation(s).
- `_resources/ai-instructions-evaluation-worksheet.md`: 0 heading transformation(s).

## Warnings And Unresolved Issues

- `index.md`: Unresolved include removed for review: {% include feature_row_dual %}
- `index.md`: Unresolved include removed for review: {% include section_tiles.html exclude="/contact/" %}
- `_projects/fitness-dashboard-ml-pipeline.md`: Referenced local asset is missing: /assets/images/projects/fitness-dashboard/card.jpg
- `_projects/fitness-dashboard-ml-pipeline.md`: Referenced local asset is missing: /assets/images/projects/fitness-dashboard/hero.jpg
- `_projects/beehive-knowledge-builder.md`: Referenced local asset is missing: /assets/images/projects/hivetracker/card.jpg
- `_projects/beehive-knowledge-builder.md`: Referenced local asset is missing: /assets/images/projects/hivetracker/hero.jpg
- `_projects/convoscope-llm-chat-compare.md`: Referenced local asset is missing: /assets/images/projects/convoscope/card.jpg
- `_projects/convoscope-llm-chat-compare.md`: Referenced local asset is missing: /assets/images/projects/convoscope/hero.jpg
- `_projects/convoscope-llm-chat-compare.md`: Referenced local asset is missing: /assets/images/projects/convoscope/s1.jpg
- `_projects/convoscope-llm-chat-compare.md`: Referenced local asset is missing: /assets/images/projects/convoscope/s2.jpg
- `_posts/2026-05-12-twin-evaluate-models.md`: Referenced local asset is missing: /assets/images/llm-comparison-metrics.png
- `_thinking/2025-09-11-rag-without-the-theater.md`: Referenced local asset is missing: /assets/images/rag-hero.jpg
- `_thinking/2025-09-11-bees-graphs-governance.md`: Referenced local asset is missing: /assets/images/bees-hero.jpg
- `_thinking/2024-09-26-chunking-is-all-you-need.md`: Referenced local asset is missing: /assets/images/bees-hero.jpg
- `resources/index.md`: Unresolved Liquid variable removed for review: {{ f | slugify }}
- `resources/index.md`: Unresolved Liquid variable removed for review: {{ f }}

## Validation Results

Run `python experiments/pageindex/scripts/validate_site_corpus.py`. The latest manual run should be recorded in task handoff notes.

## Test Results

Run `pytest experiments/pageindex/tests`. The latest manual run should be recorded in task handoff notes.

## Reproduction Commands

```bash
python experiments/pageindex/scripts/build_site_corpus.py
python experiments/pageindex/scripts/validate_site_corpus.py
pytest experiments/pageindex/tests
```

## Known Limitations

- HTML-to-Markdown conversion is deterministic but conservative; layout-only styling is removed and semantic text is retained.
- Large HTML reference pages are deferred until Release 2 normalization rules can handle tables and filterable datasets more precisely.
- External links are preserved but not fetched.

## Recommendations Before Running PageIndex

- Review `config/content-selection.yml` for editorial balance.
- Review warnings in this report and in the manifest.
- Decide whether the large Digital Twin reference pages should be normalized as a separate corpus.

## Questions for Barbara

- Should Release 1 include the large Digital Twin GraphRAG reference page despite its size and heavy HTML table structure?
- Should data-story pages be promoted into the article group, or kept for a later project-evidence corpus?
- Should `status: WIP` public project pages be labeled more explicitly in the corpus preface?
