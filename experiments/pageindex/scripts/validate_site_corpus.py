#!/usr/bin/env python3
"""Validate the generated PageIndex experiment corpus and manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[3]
EXPERIMENT_DIR = ROOT / "experiments" / "pageindex"
DEFAULT_CONFIG = EXPERIMENT_DIR / "config" / "content-selection.yml"
DEFAULT_CORPUS = EXPERIMENT_DIR / "corpus" / "site-book-v1.md"
DEFAULT_MANIFEST = EXPERIMENT_DIR / "corpus" / "site-book-v1.manifest.json"

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
]
ALLOWED_LIQUID = []


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def split_front_matter(text: str, source_path: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"Front matter starts but does not close in {source_path}")
    raw = text[4:end]
    body = text[end + 4 :]
    parsed = yaml.safe_load(raw) or {}
    if not isinstance(parsed, dict):
        raise ValueError(f"Front matter must be a mapping in {source_path}")
    return parsed, body


def selected_entries(config: dict[str, Any]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for group in ("core_pages", "projects", "articles", "resources"):
        included = [entry for entry in config.get(group, []) if entry.get("include", True)]
        included.sort(key=lambda entry: entry.get("order", 0))
        for entry in included:
            item = dict(entry)
            item["group"] = group
            entries.append(item)
    return entries


def detect_secret_patterns(text: str) -> list[str]:
    hits = []
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            hits.append(pattern.pattern)
    return hits


def heading_violations(corpus: str) -> list[str]:
    violations = []
    in_fence = False
    for line_number, line in enumerate(corpus.splitlines(), start=1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,})\s+(.+)$", line)
        if not match:
            continue
        level = len(match.group(1))
        if level == 1 and line.strip() != "# Barbara Hidalgo-Sotelo Website Corpus":
            violations.append(f"Unexpected level-one heading at line {line_number}: {line}")
        if level > 6:
            violations.append(f"Heading deeper than level six at line {line_number}: {line}")
    return violations


def unresolved_liquid(corpus: str) -> list[str]:
    hits = sorted(set(re.findall(r"\{\{.*?\}\}|\{%.*?%\}", corpus, flags=re.S)))
    return [hit for hit in hits if hit not in ALLOWED_LIQUID]


def local_link_warnings(corpus: str) -> list[str]:
    warnings = []
    links = re.findall(r"\[[^\]]+\]\((/[^)#?]+)", corpus)
    links += re.findall(r"(?:Image|image):\s+(/assets/\S+)", corpus)
    for link in sorted(set(links)):
        if link.startswith("/assets/") and not (ROOT / link.lstrip("/")).exists():
            warnings.append(f"Missing referenced asset: {link}")
    return warnings


def validate(config_path: Path = DEFAULT_CONFIG, corpus_path: Path = DEFAULT_CORPUS, manifest_path: Path = DEFAULT_MANIFEST) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not corpus_path.exists():
        errors.append(f"Generated corpus does not exist: {corpus_path}")
        return errors, warnings
    if not manifest_path.exists():
        errors.append(f"Generated manifest does not exist: {manifest_path}")
        return errors, warnings

    config = load_yaml(config_path)
    corpus = corpus_path.read_text(encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    selected = selected_entries(config)
    documents = manifest.get("documents", [])

    if not corpus.strip():
        errors.append("Generated corpus is empty.")
    if not documents:
        errors.append("Manifest contains no documents.")

    selected_paths = [entry["source_path"] for entry in selected]
    manifest_paths = [doc["source_path"] for doc in documents]
    if selected_paths != manifest_paths:
        errors.append("Manifest document order differs from the selection manifest.")

    duplicate_sources = sorted({path for path in manifest_paths if manifest_paths.count(path) > 1})
    if duplicate_sources:
        errors.append(f"Selected item is duplicated: {duplicate_sources}")

    canonical_urls = [doc.get("canonical_url") for doc in documents]
    canonical_collisions = sorted({url for url in canonical_urls if url and canonical_urls.count(url) > 1})
    if canonical_collisions:
        errors.append(f"Canonical URLs collide: {canonical_collisions}")

    for entry in selected:
        source = ROOT / entry["source_path"]
        if not source.exists():
            errors.append(f"Selected source file does not exist: {entry['source_path']}")
            continue
        try:
            front_matter, _ = split_front_matter(source.read_text(encoding="utf-8"), entry["source_path"])
        except Exception as exc:
            errors.append(str(exc))
            continue
        if front_matter.get("published") is False or front_matter.get("private") is True or front_matter.get("status") == "draft":
            errors.append(f"Draft, private, or unpublished item selected unintentionally: {entry['source_path']}")
        doc = next((item for item in documents if item["source_path"] == entry["source_path"]), None)
        if doc:
            if doc.get("source_file_sha256") != sha256_file(source):
                errors.append(f"Source hash mismatch for {entry['source_path']}")
            if not doc.get("normalized_metadata", {}).get("title"):
                errors.append(f"Required normalized title missing for {entry['source_path']}")
            if not doc.get("normalized_metadata", {}).get("canonical_url"):
                errors.append(f"Required normalized canonical URL missing for {entry['source_path']}")

    if sha256_file(corpus_path) != manifest.get("corpus_sha256"):
        errors.append("Manifest corpus SHA-256 does not match generated corpus.")

    for doc in documents:
        source_path = doc["source_path"]
        begin = f"<!-- BEGIN SOURCE: {source_path} -->"
        end = f"<!-- END SOURCE: {source_path} -->"
        if corpus.count(begin) != 1 or corpus.count(end) != 1:
            errors.append(f"Source boundary is missing or duplicated for {source_path}")
        start = doc.get("output_start_line")
        finish = doc.get("output_end_line")
        if not isinstance(start, int) or not isinstance(finish, int) or start >= finish:
            errors.append(f"Invalid output line range for {source_path}: {start}-{finish}")
    ranges = [(doc.get("output_start_line"), doc.get("output_end_line"), doc["source_path"]) for doc in documents]
    ranges = [item for item in ranges if isinstance(item[0], int) and isinstance(item[1], int)]
    for previous, current in zip(ranges, ranges[1:]):
        if previous[1] >= current[0]:
            errors.append(f"Output line ranges overlap: {previous[2]} and {current[2]}")

    errors.extend(heading_violations(corpus))
    liquid = unresolved_liquid(corpus)
    if liquid:
        errors.append("Unresolved Liquid remains outside allowlist: " + "; ".join(liquid[:10]))

    secret_hits = detect_secret_patterns(corpus)
    if secret_hits:
        errors.append("Likely secret, credential, private key, or environment value appears in corpus.")

    for group, bounds in config.get("expected_counts", {}).items():
        count = manifest.get("counts", {}).get(group, 0)
        if count < bounds.get("min", 0) or count > bounds.get("max", 10**9):
            errors.append(f"Corpus source count for {group} is outside configured expectations: {count}")

    for doc in documents:
        for warning in doc.get("warnings", []):
            warnings.append(f"{doc['source_path']}: {warning}")
        body_lines = corpus.splitlines()[doc["output_start_line"] - 1 : doc["output_end_line"]]
        word_count = len(re.findall(r"\w+", "\n".join(body_lines)))
        if word_count < 120:
            warnings.append(f"{doc['source_path']}: suspiciously short normalized document ({word_count} words).")

    warnings.extend(local_link_warnings(corpus))
    return errors, sorted(set(warnings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    errors, warnings = validate(args.config, args.corpus, args.manifest)
    print("PAGEINDEX CORPUS VALIDATION")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
