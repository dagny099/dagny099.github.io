# PageIndex Corpus Experiment

This directory contains a reproducible Jekyll-to-Markdown normalization pipeline for a Release 1 PageIndex corpus experiment.

The goal is to create one deliberately structured "site book" from selected public website content so a later PageIndex run can test hierarchical navigation over Barbara Hidalgo-Sotelo's public body of work. PageIndex execution, embeddings, PDF conversion, and chat interfaces are outside this task.

## Release 1 Boundaries

The pipeline reads public Jekyll source files and selected public data files. It does not rewrite the website, layouts, styles, routes, or published behavior.

Release 1 includes:

- 4 core positioning/orientation pages.
- 6 flagship project pages.
- 10 representative articles/thinking pieces.
- The Resources page and selected public resources that support knowledge legibility, RAG, evaluation, and AI-readiness themes.
- Public supporting data from `_data/infographics.yml` and `_data/portfolio.json`.

Draft, private, unpublished, archive, or superseded candidates are excluded in `config/content-selection.yml`.

## How Selection Works

`config/content-selection.yml` is the authoritative editable selection manifest. Each selected item records:

- source path;
- source type;
- inclusion flag;
- order;
- selection rationale;
- expected title;
- canonical URL.

To change the corpus, edit that file first, then regenerate and validate.

## How Normalization Works

`scripts/build_site_corpus.py` performs deterministic transformations:

- parses YAML front matter with PyYAML;
- maps source metadata into a normalized model;
- preserves original front matter in the JSON manifest;
- converts selected HTML-heavy pages to Markdown;
- demotes source body headings so the composite document has one level-one heading, group level-two headings, document level-three headings, and source-body headings from level four onward;
- removes duplicate source title headings;
- resolves deterministic Liquid such as `relative_url` and `post_url`;
- expands selected content-bearing includes such as resource cards, infographics, figures, punchlines, and visual companions;
- removes layout-only includes and records the transformation;
- records source hashes, output hashes, line ranges, warnings, referenced assets, and provenance.

The output is source-derived. The builder does not add interpretive claims to the corpus.

## Regenerate And Validate

From the repository root:

```bash
python experiments/pageindex/scripts/build_site_corpus.py
python experiments/pageindex/scripts/validate_site_corpus.py
pytest experiments/pageindex/tests
```

The builder is idempotent: repeated runs over the same sources and selection manifest produce stable corpus and manifest artifacts.

## Artifacts

- `config/content-selection.yml` — editable selection manifest.
- `corpus/site-book-v1.md` — normalized composite Markdown corpus.
- `corpus/site-book-v1.manifest.json` — provenance manifest.
- `reports/NORMALIZATION_AUDIT.md` — repository audit and normalization risks.
- `reports/NORMALIZATION_REPORT.md` — selection, transformation, validation, and handoff report.
- `workspace/` — scratch area for local experiment work; do not commit temporary files from it.

## What To Commit

Commit the experiment code, configuration, reports, tests, corpus, and manifest when they are intentionally regenerated.

Do not commit caches, virtual environments, downloaded external assets, PageIndex outputs, embeddings, PDFs, or ad hoc scratch files.

## Why Markdown First

PageIndex builds navigable hierarchy from Markdown headings. A normalized Markdown site book makes the first experiment reviewable by both humans and tools before adding embeddings or UI layers.

## Why PDF Conversion Is Deferred

PDFs are useful for visual review and distribution, but they are not the source representation for this experiment. Converting to PDF before validating headings, boundaries, provenance, and Liquid handling would make the pipeline harder to inspect.
