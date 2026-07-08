from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[3]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


builder = load_module("build_site_corpus", "experiments/pageindex/scripts/build_site_corpus.py")
validator = load_module("validate_site_corpus", "experiments/pageindex/scripts/validate_site_corpus.py")


def test_valid_yaml_parsing_with_common_field_types():
    text = """---
title: Example
date: 2026-07-04
published: true
tags:
  - ai
  - evaluation
description: |
  Multiline
  description.
optional:
---
Body
"""
    front_matter, body = builder.split_front_matter(text, "fixture.md")
    assert front_matter["title"] == "Example"
    assert front_matter["tags"] == ["ai", "evaluation"]
    assert front_matter["published"] is True
    assert front_matter["optional"] is None
    assert "Body" in body


def test_files_without_front_matter_parse_as_body_only():
    front_matter, body = builder.split_front_matter("# Heading\nBody", "plain.md")
    assert front_matter == {}
    assert body.startswith("# Heading")


def test_malformed_front_matter_fails_clearly():
    text = "---\ntitle: [broken\n---\nBody\n"
    with pytest.raises(ValueError, match="YAML parse failed"):
        builder.split_front_matter(text, "bad.md")


def test_heading_demotion_preserves_fenced_code_headings():
    state = builder.TransformState()
    source = """## Real Heading

```python
# not a heading
```

### Child
"""
    output = builder.demote_headings(source, state)
    assert "#### Real Heading" in output
    assert "# not a heading" in output
    assert "##### Child" in output


def test_duplicate_title_heading_removed():
    state = builder.TransformState()
    output = builder.remove_duplicate_title_heading("# Same Title\n\nBody", "Same Title", state)
    assert output.strip() == "Body"
    assert state.heading_transformations[0]["type"] == "duplicate_title_heading_removed"


def test_liquid_relative_url_and_post_url_resolution(tmp_path):
    state = builder.TransformState()
    body = "See {{ '/assets/a.png' | relative_url }} and {% post_url 2026-03-18-example-post %}."
    output = builder.transform_liquid(body, tmp_path, "fixture.md", state)
    assert "/assets/a.png" in output
    assert "/blog/example-post/" in output
    assert "{{" not in output
    assert "{%" not in output


def test_layout_include_removed_and_resource_data_expanded(tmp_path):
    (tmp_path / "_resources").mkdir()
    (tmp_path / "_data").mkdir()
    (tmp_path / "_resources" / "one.md").write_text(
        "---\ntitle: One\npermalink: /resources/one/\ndate: 2026-01-01\nformat: Guide\nlevel: Intro\nexcerpt: Useful.\ntags: [ai]\n---\nBody\n",
        encoding="utf-8",
    )
    (tmp_path / "_data" / "infographics.yml").write_text(
        "items:\n  - title: Chart\n    url: /chart/\n    image: /assets/chart.png\n    alt: Chart alt\n",
        encoding="utf-8",
    )
    state = builder.TransformState()
    body = "{% include page__taxonomy.html %}\n{% include infographic-gallery.html %}\n{% include cards_grid.html variant=\"resource\" items=items %}"
    output = builder.transform_liquid(body, tmp_path, "resources/index.md", state)
    assert "Chart" in output
    assert "One" in output
    assert "page__taxonomy" not in output


def test_stable_ordering_from_selection_manifest():
    config = {
        "core_pages": [
            {"source_path": "b.md", "order": 2},
            {"source_path": "a.md", "order": 1},
        ]
    }
    assert [entry["source_path"] for _, entry in builder.iter_selected(config)] == ["a.md", "b.md"]


def test_stable_json_serialization():
    data = {"b": 1, "a": {"d": 4, "c": 3}}
    first = json.dumps(builder.serialize(data), indent=2, sort_keys=True)
    second = json.dumps(builder.serialize(data), indent=2, sort_keys=True)
    assert first == second
    assert first.splitlines()[1].strip().startswith('"a"')


def test_manifest_hashes_and_line_ranges_are_generated(tmp_path):
    corpus = tmp_path / "site-book-v1.md"
    manifest_path = tmp_path / "site-book-v1.manifest.json"
    manifest = builder.build(builder.DEFAULT_CONFIG, corpus, manifest_path)
    assert corpus.exists()
    assert manifest_path.exists()
    assert builder.sha256_file(corpus) == manifest["corpus_sha256"]
    for doc in manifest["documents"]:
        assert doc["output_start_line"] < doc["output_end_line"]
        assert doc["output_content_sha256"]


def test_secret_pattern_detection():
    hits = validator.detect_secret_patterns("api_key = 'abcdefghijklmnopqrstuvwxyz'")
    assert hits


def write_minimal_source(root: Path, name: str, title: str, permalink: str, body: str = "Body text with enough words to avoid short warnings. " * 8):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\ntitle: {title}\npermalink: {permalink}\n---\n{body}\n", encoding="utf-8")


def test_duplicate_canonical_urls_fail_validation(tmp_path, monkeypatch):
    monkeypatch.setattr(validator, "ROOT", tmp_path)
    write_minimal_source(tmp_path, "a.md", "A", "/same/")
    write_minimal_source(tmp_path, "b.md", "B", "/same/")
    config = tmp_path / "selection.yml"
    corpus = tmp_path / "corpus.md"
    manifest_path = tmp_path / "manifest.json"
    config.write_text(
        """
expected_counts:
  core_pages: {min: 2, max: 2}
core_pages:
  - source_path: a.md
    include: true
    order: 1
    canonical_url: /same/
  - source_path: b.md
    include: true
    order: 2
    canonical_url: /same/
""",
        encoding="utf-8",
    )
    corpus.write_text(
        "# Barbara Hidalgo-Sotelo Website Corpus\n\n<!-- BEGIN SOURCE: a.md -->\n### A\nBody\n<!-- END SOURCE: a.md -->\n<!-- BEGIN SOURCE: b.md -->\n### B\nBody\n<!-- END SOURCE: b.md -->\n",
        encoding="utf-8",
    )
    manifest = {
        "corpus_sha256": validator.sha256_file(corpus),
        "counts": {"core_pages": 2},
        "documents": [
            {
                "source_path": "a.md",
                "canonical_url": "/same/",
                "source_file_sha256": validator.sha256_file(tmp_path / "a.md"),
                "normalized_metadata": {"title": "A", "canonical_url": "/same/"},
                "output_start_line": 3,
                "output_end_line": 6,
            },
            {
                "source_path": "b.md",
                "canonical_url": "/same/",
                "source_file_sha256": validator.sha256_file(tmp_path / "b.md"),
                "normalized_metadata": {"title": "B", "canonical_url": "/same/"},
                "output_start_line": 7,
                "output_end_line": 10,
            },
        ],
    }
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    errors, _ = validator.validate(config, corpus, manifest_path)
    assert any("Canonical URLs collide" in error for error in errors)


def test_empty_generated_artifact_fails(tmp_path):
    config = tmp_path / "selection.yml"
    corpus = tmp_path / "empty.md"
    manifest_path = tmp_path / "manifest.json"
    config.write_text("core_pages: []\n", encoding="utf-8")
    corpus.write_text("", encoding="utf-8")
    manifest_path.write_text(json.dumps({"corpus_sha256": validator.sha256_file(corpus), "documents": [], "counts": {}}), encoding="utf-8")
    errors, _ = validator.validate(config, corpus, manifest_path)
    assert "Generated corpus is empty." in errors
    assert "Manifest contains no documents." in errors


def test_idempotent_regeneration(tmp_path):
    corpus = tmp_path / "site-book.md"
    manifest = tmp_path / "manifest.json"
    builder.build(builder.DEFAULT_CONFIG, corpus, manifest)
    first_corpus = corpus.read_text(encoding="utf-8")
    first_manifest = manifest.read_text(encoding="utf-8")
    builder.build(builder.DEFAULT_CONFIG, corpus, manifest)
    assert first_corpus == corpus.read_text(encoding="utf-8")
    assert first_manifest == manifest.read_text(encoding="utf-8")


def test_committed_selection_sources_exist():
    config = builder.read_yaml(builder.DEFAULT_CONFIG)
    missing = []
    for _, entry in builder.iter_selected(config):
        source_path = entry["source_path"]
        if not (ROOT / source_path).exists():
            missing.append(source_path)
    assert missing == []


def test_quote_include_with_data_id_expands(tmp_path):
    (tmp_path / "_data").mkdir()
    (tmp_path / "_data" / "quotes.yml").write_text(
        "field:\n  - id: hamming-insight\n    text: The purpose of computing is insight, not numbers.\n    author: Richard W. Hamming\n",
        encoding="utf-8",
    )
    state = builder.TransformState()
    output = builder.transform_liquid('{% include quote.html set="field" id="hamming-insight" variant="epigraph" %}', tmp_path, "fixture.md", state)
    assert "The purpose of computing is insight" in output
    assert "Richard W. Hamming" in output
    assert not state.warnings
