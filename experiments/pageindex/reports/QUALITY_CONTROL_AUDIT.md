# Quality Control Audit — PageIndex Corpus Normalization

## 1. Executive assessment

Final status after remediation: **conditionally ready for PageIndex experimentation**. The corpus now regenerates from committed files, validates with zero errors, and is byte-for-byte deterministic across two consecutive builder runs from the same revision. The corpus should still be treated as an experimental Release 1 site book, not a semantically complete Jekyll render.

The audit found one blocking reproducibility defect and one source-fidelity defect that were remediated:

- **High, resolved:** the selection manifest referenced `_resources/knowledge-legibility-diagnostic.md`, which is not present in the repository, so the builder failed before producing a corpus.
- **Medium, resolved:** the selected My Journey page uses `_includes/quote.html` with a pinned data-backed quote; the original normalizer removed it as unresolved Liquid instead of expanding the public quote text from `_data/quotes.yml`.

Remaining non-blocking concerns are warnings and editorial limitations: missing referenced image assets already present as warnings, flattened deep HTML headings in My Journey, unresolved homepage presentation includes, and resource filter Liquid controls that are intentionally presentation logic rather than corpus content.

## 2. Reproduction results

Commands run during audit and remediation:

```bash
find / -name AGENTS.md -print 2>/dev/null | head -20
rg --files experiments/pageindex | sort
python experiments/pageindex/scripts/build_site_corpus.py
python experiments/pageindex/scripts/build_site_corpus.py && cp experiments/pageindex/corpus/site-book-v1.md /tmp/c1.md && cp experiments/pageindex/corpus/site-book-v1.manifest.json /tmp/m1.json && python experiments/pageindex/scripts/build_site_corpus.py && cmp -s /tmp/c1.md experiments/pageindex/corpus/site-book-v1.md; echo corpus_cmp:$?; cmp -s /tmp/m1.json experiments/pageindex/corpus/site-book-v1.manifest.json; echo manifest_cmp:$?; python experiments/pageindex/scripts/validate_site_corpus.py
pytest -q experiments/pageindex/tests
bundle exec jekyll build
bundle install
```

Initial clean-state reproduction failed with:

```text
FileNotFoundError: _resources/knowledge-legibility-diagnostic.md
```

After remediation:

- `python experiments/pageindex/scripts/build_site_corpus.py` succeeded.
- Two consecutive builds produced `corpus_cmp:0` and `manifest_cmp:0`.
- `python experiments/pageindex/scripts/validate_site_corpus.py` reported `Errors: 0` and `Warnings: 34`.
- `pytest -q experiments/pageindex/tests` reported `16 passed`.
- `bundle exec jekyll build` could not run because `jekyll` is not installed in this environment.
- `bundle install` attempted dependency installation but failed with a Rubygems `403 "Forbidden"`; no Jekyll build result is available from this environment.

No public website source files were modified during remediation.

## 3. Pass/fail matrix

| Area | Status | Evidence |
| --- | --- | --- |
| Repository instructions reviewed | Pass | No `AGENTS.md` found under `/workspace`; task-specific developer instructions applied. |
| Public-site behavior unchanged | Pass | Changes are limited to `experiments/pageindex/`. |
| Build reproducibility | Pass after remediation | Builder succeeds and emits deterministic corpus/manifest on repeated runs. |
| YAML parser usage | Pass | Scripts use `yaml.safe_load`. |
| Selection manifest paths | Pass after remediation | Added regression test for all selected source paths. |
| Source provenance | Pass | Manifest records source path, front matter, normalized metadata, source hash, corpus hash, commit, line ranges, warnings, transformations, assets, and pipeline version. |
| Heading validity | Pass with warnings | Validator reports no heading errors; My Journey has multiple level-six flattening warnings. |
| Liquid/data-driven handling | Pass with caveats | Resource cards and infographics expand; quote include now expands; some presentation-only filters/includes remain warnings. |
| Security/privacy | Pass within simple-pattern limits | Validator secret scan reports no errors; detection remains pattern-based and not exhaustive. |
| Documentation claims | Pass with caveats | README/report document reproduction and limitations; audit notes should be read with generated warnings. |
| Jekyll build | Not verified | Environment lacks installed Jekyll and dependency install was blocked by Rubygems 403. |

## 4. Findings by severity

### High — Resolved: selected source did not exist

- **Evidence:** `python experiments/pageindex/scripts/build_site_corpus.py` raised `FileNotFoundError: _resources/knowledge-legibility-diagnostic.md`.
- **Affected files:** `experiments/pageindex/config/content-selection.yml`; generated corpus and manifest were stale relative to the broken configuration.
- **Reproduction steps:** run `python experiments/pageindex/scripts/build_site_corpus.py` on the original branch state.
- **Why it matters:** the corpus was not reproducible from committed files, directly violating the Release 1 requirement.
- **Recommended resolution:** remove or replace the nonexistent selected resource and add a regression test that every selected source exists.
- **Blocks PageIndex experimentation:** yes, before remediation; no, after remediation.
- **Resolution:** removed the missing resource selection, kept resource count within configured bounds, regenerated corpus/manifest/report, and added `test_committed_selection_sources_exist`.

### Medium — Resolved: pinned public quote include was silently dropped

- **Evidence:** `_pages/my-journey.html` includes `{% include quote.html set="field" id="hamming-insight" variant="epigraph" %}`. The original validator warning showed this include was removed as unresolved, even though `_data/quotes.yml` contains the pinned public quote.
- **Affected files:** `experiments/pageindex/scripts/build_site_corpus.py`, `experiments/pageindex/tests/test_normalization.py`, generated corpus/manifest/report.
- **Reproduction steps:** run the builder/validator before remediation and inspect warnings for `_pages/my-journey.html`.
- **Why it matters:** content-bearing data-backed Liquid was lost from a selected source.
- **Recommended resolution:** implement deterministic expansion for `quote.html` includes when text is explicit or when `set`/`id` or numeric `pick` can resolve to `_data/quotes.yml`; avoid nondeterministic random selection.
- **Blocks PageIndex experimentation:** no after remediation.
- **Resolution:** added deterministic quote expansion and a regression test for data-backed quote includes.

### Medium — Remaining: resource filter Liquid variables are removed with warnings

- **Evidence:** validator reports unresolved variable removal warnings for `{{ f | slugify }}` and `{{ f }}` from `resources/index.md`.
- **Affected files:** `resources/index.md`, generated `resources/index.md` corpus section.
- **Reproduction steps:** run `python experiments/pageindex/scripts/validate_site_corpus.py`.
- **Why it matters:** these variables are part of interactive filter controls, not primary prose; warnings are appropriate, but the pipeline does not render the exact filter buttons.
- **Recommended resolution:** optional: render a deterministic list of available resource formats from public `_resources` front matter or explicitly document that filter UI controls are presentation-only.
- **Blocks PageIndex experimentation:** no.

### Medium — Remaining: missing referenced image assets

- **Evidence:** validator reports missing local assets including `/assets/images/llm-comparison-metrics.png`, `/assets/images/hero.jpg`, project hero/card images, and bee/RAG hero images.
- **Affected files:** selected project/article/thinking pages and generated manifest warnings.
- **Reproduction steps:** run `python experiments/pageindex/scripts/validate_site_corpus.py`.
- **Why it matters:** image alt text/captions can be included, but missing physical assets may indicate stale front matter or image paths in the public site.
- **Recommended resolution:** editorial/site-maintenance review outside this task; do not fabricate assets in the corpus pipeline.
- **Blocks PageIndex experimentation:** no, because warnings are explicit and text corpus remains valid.

### Low — Remaining: homepage presentation includes are removed with warnings

- **Evidence:** validator reports `index.md` unresolved includes for `feature_row_dual` and a commented-out `section_tiles.html` include.
- **Affected files:** `index.md`, generated homepage section.
- **Reproduction steps:** run validation.
- **Why it matters:** the warning is noisy; the commented include is not active public content. `feature_row_dual` may carry presentation cards, but core homepage prose is retained.
- **Recommended resolution:** optionally classify commented Liquid as inactive before transformation and either expand or explicitly document `feature_row_dual` handling.
- **Blocks PageIndex experimentation:** no.

### Low — Remaining: My Journey deep HTML headings are flattened to level six

- **Evidence:** validator reports multiple `Heading flattened to level 6` warnings for My Journey.
- **Affected files:** `_pages/my-journey.html`, generated corpus hierarchy.
- **Reproduction steps:** run validation.
- **Why it matters:** flattened headings are syntactically valid but less semantically precise for navigation.
- **Recommended resolution:** optional page-specific hierarchy mapping for the highly structured HTML journey page.
- **Blocks PageIndex experimentation:** no.

## 5. Content-selection findings

- The selected core pages, project pages, articles, and remaining resources exist after remediation.
- Counts after remediation are `core_pages=4`, `projects=6`, `articles=10`, `resources=5`, all within configured bounds.
- The removed `_resources/knowledge-legibility-diagnostic.md` selection was a definite implementation error because the file is absent from the repository.
- The selected articles are weighted toward AI evaluation, GraphRAG/RAG, metadata, judgment, and knowledge-system themes. This is credible for Release 1, though including data stories remains an editorial question.
- Excluded large HTML Digital Twin reference pages are credible deferrals given the stated table-normalization limitation.

## 6. Source-fidelity findings

- Titles, source paths, canonical URLs, dates, tags/categories, descriptions/excerpts, status/technologies/repo/demo fields are derived from front matter plus explicit selection data.
- Markdown body prose is retained for selected Markdown documents, with heading demotion and duplicate title heading removal.
- HTML-heavy pages are converted conservatively to Markdown. This is deterministic but not full Jekyll rendering parity.
- The My Journey pinned quote is now present in the normalized corpus rather than dropped.
- Presentation-only includes are removed with manifest warnings rather than silently ignored.

## 7. Hierarchy findings

- The generated corpus has exactly one top-level heading.
- Group headings use level two; selected source documents use level three; source body headings are demoted to start below each source heading.
- Headings inside backtick and tilde fences are protected by tests.
- Some My Journey headings are flattened to level six; this is reported and deterministic.
- Manifest line ranges validate and do not overlap after regeneration.

## 8. Liquid and data-driven-content findings

- `relative_url` and `post_url` are resolved deterministically.
- `infographic-gallery.html` is expanded from `_data/infographics.yml`.
- `cards_grid.html variant="resource"` is expanded from public `_resources` entries.
- `quote.html` is now expanded when deterministic (`text`, `set` + `id`, or numeric `pick`). Random quote selection falls back deterministically to the first quote rather than sampling.
- Generic Liquid loops/conditionals are removed as layout controls; unresolved variables are warned.
- The implementation does not execute arbitrary template code, which is appropriate for this audit scope.

## 9. Provenance and manifest findings

- Manifest entries include repository-relative source paths, source types, titles, canonical URLs, selection rationales, original front matter, normalized metadata, source hashes, content hashes, commit SHA, output line ranges, warnings, transformations, referenced assets, and pipeline version.
- Corpus and source hashes validate after regeneration.
- Manifest serialization uses sorted JSON keys.
- Paths are repository-relative; no absolute home-directory paths were found in generated corpus/manifest.
- `generated_at` and per-document `inclusion_timestamp` use the commit timestamp, so they are stable for a fixed commit rather than wall-clock time.

## 10. Security and privacy findings

- Pattern-based secret detection found no blocking errors in the generated corpus.
- The selected content is public website content and public data files.
- No API keys, private keys, passwords, or home-directory paths were identified in selected generated artifacts during this audit.
- Secret detection is not comprehensive; realistic-looking fixtures should continue to avoid live secret formats.

## 11. Test-coverage findings

Existing tests covered YAML parsing, malformed YAML, missing front matter, heading demotion around code fences, duplicate title headings, selected ordering, JSON serialization, line ranges, duplicate canonical URLs, empty artifacts, idempotent regeneration, and basic secret detection.

Added tests:

- `test_committed_selection_sources_exist` protects against missing selected files.
- `test_quote_include_with_data_id_expands` protects data-backed `quote.html` include expansion.

Remaining test opportunities:

- HTML headings and tables from deferred large reference pages.
- Missing data keys for data-backed includes.
- Local link verification beyond assets.
- Explicit stale-artifact detection when source files change without regeneration.

## 12. Documentation findings

- The generated normalization report is updated by the builder and now reflects the reduced resource count and quote expansion transformation.
- The README and report do not claim PageIndex has been run.
- Documentation correctly presents the corpus as experimental and the original site source as authoritative.
- The setup path for Jekyll is not fully verifiable in this environment due missing installed gems and Rubygems 403 during `bundle install`.

## 13. Questions requiring editorial judgment

- Should a replacement for the removed knowledge-legibility diagnostic be selected, or should the Resources release intentionally contain five entries?
- Should data-story pages be promoted into the article group in a future corpus?
- Should the large Digital Twin GraphRAG/model-comparison HTML pages be normalized in Release 2 with table-specific handling?
- Should missing image assets be restored in the public site or treated as stale metadata?
- Should WIP public projects receive a more prominent corpus label?

## 14. Recommended fixes in priority order

1. **Completed:** remove the nonexistent selected resource and add a selected-source existence test.
2. **Completed:** expand deterministic `quote.html` includes from `_data/quotes.yml`.
3. Review missing local image assets as public-site maintenance.
4. Optionally render resource filter labels deterministically from `_resources` formats or document them as presentation-only.
5. Optionally add page-specific hierarchy normalization for My Journey to reduce heading flattening.
6. Optionally ignore Liquid inside HTML comments before transformation to reduce warnings.

## Final pass/fail status

- **Final audit status:** Pass with non-blocking warnings.
- **Ready for PageIndex experiment:** Yes, for a first experimental corpus, provided users accept the documented warnings and limitations.
- **Do not use as:** a full Jekyll-rendered semantic archive, a complete security scan, or a substitute for the authoritative website source.
