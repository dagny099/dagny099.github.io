#!/usr/bin/env python3
"""Build a normalized Markdown corpus from selected public Jekyll sources."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml

PIPELINE_VERSION = "pageindex-normalizer-v1"
ROOT = Path(__file__).resolve().parents[3]
EXPERIMENT_DIR = ROOT / "experiments" / "pageindex"
DEFAULT_CONFIG = EXPERIMENT_DIR / "config" / "content-selection.yml"
DEFAULT_CORPUS = EXPERIMENT_DIR / "corpus" / "site-book-v1.md"
DEFAULT_MANIFEST = EXPERIMENT_DIR / "corpus" / "site-book-v1.manifest.json"
DEFAULT_REPORT = EXPERIMENT_DIR / "reports" / "NORMALIZATION_REPORT.md"

GROUP_HEADINGS = {
    "core_pages": "Core Positioning Pages",
    "projects": "Project Portfolio",
    "articles": "Articles",
    "resources": "Resources",
}
SELECTABLE_GROUPS = tuple(GROUP_HEADINGS)
LAYOUT_ONLY_INCLUDES = {
    "page__taxonomy.html",
    "resource/buttons.html",
    "social-share.html",
    "toc.html",
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{20,}\b"),
]


@dataclass
class TransformState:
    transformations: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    heading_transformations: list[dict[str, Any]] = field(default_factory=list)
    referenced_assets: list[str] = field(default_factory=list)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_git(args: list[str], default: str = "") -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return default


def display_path(path: Path) -> str:
    path = path.resolve()
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def serialize(value: Any) -> Any:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Path):
        return value.as_posix()
    if isinstance(value, dict):
        return {str(k): serialize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serialize(v) for v in value]
    return value


def read_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def split_front_matter(text: str, source_path: str = "<string>") -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"Front matter starts but does not close in {source_path}")
    raw = text[4:end]
    body = text[end + 4 :]
    if body.startswith("\n"):
        body = body[1:]
    try:
        parsed = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parse failed in {source_path}: {exc}") from exc
    if not isinstance(parsed, dict):
        raise ValueError(f"Front matter must parse to a mapping in {source_path}")
    return parsed, body


def infer_source_type(path: str) -> str:
    if path.startswith("_posts/"):
        return "post"
    if path.startswith("_projects/"):
        return "project"
    if path.startswith("_thinking/"):
        return "thinking"
    if path.startswith("_resources/"):
        return "resource"
    if path == "resources/index.md":
        return "resource_index"
    if path.startswith("data-stories/"):
        return "data_story"
    return "page"


def infer_canonical_url(path: str, front_matter: dict[str, Any], site_url: str = "") -> str | None:
    canonical = front_matter.get("canonical_url") or front_matter.get("permalink") or front_matter.get("url")
    if canonical:
        canonical = str(canonical)
        if site_url and canonical.startswith(site_url):
            canonical = canonical[len(site_url) :] or "/"
        return canonical
    if path.startswith("_posts/"):
        name = Path(path).stem
        match = re.match(r"\d{4}-\d{2}-\d{1,2}-(.+)$", name)
        if match:
            return f"/blog/{match.group(1)}/"
    return None


def normalize_title(path: str, front_matter: dict[str, Any], expected_title: str | None = None) -> str | None:
    title = front_matter.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    if expected_title:
        return expected_title
    if Path(path).name == "index.md":
        return "Index"
    return None


def normalize_metadata(
    path: str,
    source_type: str,
    front_matter: dict[str, Any],
    selection: dict[str, Any],
    site_url: str,
) -> dict[str, Any]:
    title = normalize_title(path, front_matter, selection.get("expected_title"))
    canonical = selection.get("canonical_url") or infer_canonical_url(path, front_matter, site_url)
    fields = {
        "title": title,
        "description": front_matter.get("description") or front_matter.get("excerpt"),
        "source_type": source_type,
        "canonical_url": canonical,
        "publication_date": front_matter.get("date"),
        "last_modified_at": front_matter.get("last_modified_at"),
        "tags": front_matter.get("tags"),
        "categories": front_matter.get("categories"),
        "status": front_matter.get("status"),
        "technologies": front_matter.get("stack") or front_matter.get("technologies"),
        "repository_url": front_matter.get("repo_url") or front_matter.get("repository_url"),
        "demo_url": front_matter.get("demo_url") or front_matter.get("url"),
        "docs_url": front_matter.get("docs_url"),
    }
    return {k: serialize(v) for k, v in fields.items() if v not in (None, "", [], {})}


class HtmlToMarkdown(HTMLParser):
    """Small deterministic HTML-to-Markdown converter for Jekyll page bodies."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.href_stack: list[str | None] = []
        self.skip_stack: list[str] = []
        self.list_depth = 0
        self.current_heading: int | None = None

    def add(self, text: str) -> None:
        if not self.skip_stack:
            self.parts.append(text)

    def newline(self, count: int = 1) -> None:
        self.add("\n" * count)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v for k, v in attrs}
        if tag in {"script", "style"}:
            self.skip_stack.append(tag)
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.current_heading = int(tag[1])
            self.newline(2)
            self.add("#" * self.current_heading + " ")
        elif tag in {"p", "section", "article", "div", "header", "footer", "blockquote"}:
            self.newline(2)
        elif tag == "br":
            self.newline()
        elif tag in {"ul", "ol"}:
            self.list_depth += 1
            self.newline()
        elif tag == "li":
            self.newline()
            self.add("  " * max(0, self.list_depth - 1) + "- ")
        elif tag == "a":
            self.href_stack.append(attrs_dict.get("href"))
            self.add("[")
        elif tag in {"strong", "b"}:
            self.add("**")
        elif tag in {"em", "i"}:
            self.add("*")
        elif tag == "code":
            self.add("`")
        elif tag == "img":
            src = attrs_dict.get("src") or ""
            alt = attrs_dict.get("alt") or ""
            self.add(f"![{alt}]({src})")

    def handle_endtag(self, tag: str) -> None:
        if self.skip_stack and self.skip_stack[-1] == tag:
            self.skip_stack.pop()
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.current_heading = None
            self.newline(2)
        elif tag in {"p", "section", "article", "div", "header", "footer", "blockquote"}:
            self.newline(2)
        elif tag in {"ul", "ol"}:
            self.list_depth = max(0, self.list_depth - 1)
            self.newline()
        elif tag == "li":
            self.newline()
        elif tag == "a":
            href = self.href_stack.pop() if self.href_stack else None
            self.add(f"]({href})" if href else "]")
        elif tag in {"strong", "b"}:
            self.add("**")
        elif tag in {"em", "i"}:
            self.add("*")
        elif tag == "code":
            self.add("`")

    def handle_data(self, data: str) -> None:
        if self.skip_stack:
            return
        data = re.sub(r"\s+", " ", data)
        if data.strip():
            self.add(data)

    def get_markdown(self) -> str:
        text = "".join(self.parts)
        lines = [line.strip() for line in text.splitlines()]
        cleaned: list[str] = []
        previous_blank = False
        for line in lines:
            blank = not line
            if blank and previous_blank:
                continue
            cleaned.append(line)
            previous_blank = blank
        return "\n".join(cleaned).strip() + "\n"


def html_to_markdown(text: str) -> str:
    parser = HtmlToMarkdown()
    parser.feed(text)
    return html.unescape(parser.get_markdown())


def is_html_heavy(body: str) -> bool:
    tags = len(re.findall(r"</?(?:div|section|article|h[1-6]|p|ul|li|a|span)\b", body, flags=re.I))
    md_headings = len(re.findall(r"^#{1,6}\s+", body, flags=re.M))
    return tags >= 8 and md_headings < 3


def post_url_replacement(match: re.Match[str]) -> str:
    slug = match.group(1).strip()
    slug = re.sub(r"^\d{4}-\d{2}-\d{1,2}-", "", slug)
    return f"/blog/{slug}/"


def load_public_resources(root: Path) -> list[dict[str, Any]]:
    resources: list[dict[str, Any]] = []
    for path in sorted((root / "_resources").rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if "/_archive/" in rel:
            continue
        text = path.read_text(encoding="utf-8")
        front_matter, _ = split_front_matter(text, rel)
        if front_matter.get("published") is False or front_matter.get("status") == "draft":
            continue
        resources.append(
            {
                "title": front_matter.get("title"),
                "permalink": infer_canonical_url(rel, front_matter),
                "excerpt": front_matter.get("excerpt"),
                "format": front_matter.get("format"),
                "level": front_matter.get("level"),
                "date": serialize(front_matter.get("date")),
                "tags": front_matter.get("tags"),
                "source_path": rel,
            }
        )
    resources.sort(key=lambda item: (item.get("date") or "", item.get("title") or ""), reverse=True)
    return resources


def render_resource_cards(root: Path) -> str:
    lines = ["## Resource Collection Entries", ""]
    for item in load_public_resources(root):
        lines.append(f"### {item.get('title') or item['source_path']}")
        if item.get("permalink"):
            lines.append(f"- URL: {item['permalink']}")
        if item.get("format"):
            lines.append(f"- Format: {item['format']}")
        if item.get("level"):
            lines.append(f"- Level: {item['level']}")
        if item.get("tags"):
            lines.append("- Tags: " + ", ".join(item["tags"]))
        if item.get("excerpt"):
            lines.append("")
            lines.append(str(item["excerpt"]))
        lines.append("")
    return "\n".join(lines)


def render_infographics(root: Path) -> str:
    path = root / "_data" / "infographics.yml"
    if not path.exists():
        return ""
    data = read_yaml(path)
    lines = ["## Infographics", ""]
    for item in data.get("items", []):
        title = item.get("title") or item.get("url") or "Untitled infographic"
        lines.append(f"### {title}")
        for key in ("url", "image", "alt", "date"):
            if item.get(key):
                label = key.replace("_", " ").title()
                lines.append(f"- {label}: {item[key]}")
        lines.append("")
    return "\n".join(lines)


def parse_include_args(raw: str) -> dict[str, str]:
    return {match.group(1): html.unescape(match.group(2)) for match in re.finditer(r"(\w+)\s*=\s*\"([^\"]*)\"", raw)}


def render_figure_include(args: dict[str, str]) -> str:
    image = args.get("image_path") or args.get("path") or args.get("image")
    if image and image.startswith("assets/"):
        image = "/" + image
    alt = args.get("alt", "")
    caption = args.get("caption")
    lines = []
    if image:
        lines.append(f"![{alt}]({image})")
    elif alt:
        lines.append(f"Image alt text: {alt}")
    if caption:
        lines.append(f"*Caption: {caption}*")
    return "\n\n" + "\n\n".join(lines) + "\n\n" if lines else ""


def render_named_callout(include_name: str, args: dict[str, str]) -> str:
    if include_name == "punchline.html" and args.get("text"):
        return f"\n\n> {args['text']}\n\n"
    if include_name == "download-callout.html":
        lines = ["#### Downloadable companion"]
        for key in ("title", "subtitle", "pdf", "video_label"):
            if args.get(key):
                lines.append(f"- {key.replace('_', ' ').title()}: {args[key]}")
        return "\n\n" + "\n".join(lines) + "\n\n"
    if include_name == "visual-companion.html":
        lines = ["#### Visual companion"]
        for key in ("title", "description", "mp4", "poster", "pdf"):
            if args.get(key):
                lines.append(f"- {key.replace('_', ' ').title()}: {args[key]}")
        return "\n\n" + "\n".join(lines) + "\n\n"
    return ""


def transform_liquid(body: str, root: Path, rel_path: str, state: TransformState) -> str:
    def relative_url(match: re.Match[str]) -> str:
        value = match.group(1) or match.group(2)
        state.transformations.append({"type": "liquid_variable", "action": "relative_url_resolved", "value": value})
        return value if value.startswith("/") else "/" + value

    body = re.sub(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", relative_url, body)
    body = re.sub(r'\{\{\s*"([^"]+)"\s*\|\s*relative_url\s*\}\}', relative_url, body)
    body = re.sub(r"\{%\s*post_url\s+([^%]+?)\s*%\}", post_url_replacement, body)

    include_pattern = re.compile(r"\{%\s*include\s+([^\s%]+)(.*?)%\}", flags=re.S)

    def include_replacement(match: re.Match[str]) -> str:
        include_name = match.group(1)
        include_args = parse_include_args(match.group(2))
        if include_name == "figure":
            state.transformations.append({"type": "include", "include": include_name, "action": "expanded_figure"})
            return render_figure_include(include_args)
        callout = render_named_callout(include_name, include_args)
        if callout:
            state.transformations.append({"type": "include", "include": include_name, "action": "expanded_callout"})
            return callout
        if include_name == "infographic-gallery.html":
            state.transformations.append({"type": "include", "include": include_name, "action": "expanded_from_data"})
            return "\n\n" + render_infographics(root) + "\n"
        if include_name == "cards_grid.html" and "variant=\"resource\"" in match.group(0):
            state.transformations.append({"type": "include", "include": include_name, "action": "expanded_resource_collection"})
            return "\n\n" + render_resource_cards(root) + "\n"
        if include_name in LAYOUT_ONLY_INCLUDES:
            state.transformations.append({"type": "include", "include": include_name, "action": "removed_layout_or_navigation"})
            return ""
        state.warnings.append(f"Unresolved include removed for review: {match.group(0)}")
        state.transformations.append({"type": "include", "include": include_name, "action": "removed_unresolved"})
        return ""

    body = include_pattern.sub(include_replacement, body)

    def control_replacement(match: re.Match[str]) -> str:
        tag = match.group(0)
        state.transformations.append({"type": "liquid_control", "action": "removed_layout_control", "tag": tag})
        return ""

    body = re.sub(r"\{%\s*(?:assign|if|endif|for|endfor|where_exp|capture|endcapture)[^%]*%\}", control_replacement, body)

    def unresolved_variable(match: re.Match[str]) -> str:
        state.warnings.append(f"Unresolved Liquid variable removed for review: {match.group(0)}")
        state.transformations.append({"type": "liquid_variable", "action": "removed_unresolved", "tag": match.group(0)})
        return ""

    body = re.sub(r"\{\{.*?\}\}", unresolved_variable, body, flags=re.S)
    return body


def collect_referenced_assets(text: str, front_matter: dict[str, Any]) -> list[str]:
    assets = set(re.findall(r"(?:!\[[^\]]*\]\(|src=[\"'])(/assets/[^)\"']+)", text))
    for key in ("header", "gallery", "gallery2", "gallery3", "feature_row"):
        value = front_matter.get(key)
        stack = [value]
        while stack:
            current = stack.pop()
            if isinstance(current, dict):
                stack.extend(current.values())
            elif isinstance(current, list):
                stack.extend(current)
            elif isinstance(current, str) and current.startswith("/assets/"):
                assets.add(current)
    return sorted(assets)


def remove_duplicate_title_heading(text: str, title: str, state: TransformState) -> str:
    title_key = re.sub(r"\s+", " ", title.strip().lower())
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", lines[i])
        if match:
            heading_text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", match.group(2)).strip().lower())
            if heading_text == title_key:
                state.heading_transformations.append(
                    {"type": "duplicate_title_heading_removed", "heading": lines[i].strip()}
                )
                del lines[i]
    return "\n".join(lines).strip() + "\n"


def demote_headings(text: str, state: TransformState, body_start_level: int = 4) -> str:
    lines = text.splitlines()
    in_fence = False
    headings: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))
    if not headings:
        return text.strip() + "\n"
    min_level = min(level for _, level, _ in headings)
    for index, level, heading in headings:
        new_level = level - min_level + body_start_level
        flattened = False
        if new_level > 6:
            new_level = 6
            flattened = True
        old = lines[index]
        lines[index] = "#" * new_level + " " + heading
        state.heading_transformations.append(
            {"type": "heading_demoted", "from": old, "to": lines[index], "flattened": flattened}
        )
        if flattened:
            state.warnings.append(f"Heading flattened to level 6: {heading}")
    return "\n".join(lines).strip() + "\n"


def normalize_body(body: str, root: Path, rel_path: str, front_matter: dict[str, Any], title: str, state: TransformState) -> str:
    body = transform_liquid(body, root, rel_path, state)
    body = re.sub(r"<script\b.*?</script>", "", body, flags=re.I | re.S)
    body = re.sub(r"<style\b.*?</style>", "", body, flags=re.I | re.S)
    if is_html_heavy(body):
        state.transformations.append({"type": "html", "action": "converted_to_markdown"})
        body = html_to_markdown(body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    state.referenced_assets = collect_referenced_assets(body, front_matter)
    body = remove_duplicate_title_heading(body, title, state)
    body = demote_headings(body, state)
    return body.strip() + "\n"


def metadata_block(metadata: dict[str, Any], source_path: str, commit: str) -> str:
    labels = [
        ("source_type", "Source type"),
        ("canonical_url", "Canonical URL"),
        ("publication_date", "Publication date"),
        ("last_modified_at", "Last modified"),
        ("status", "Status"),
        ("technologies", "Technologies"),
        ("tags", "Tags"),
        ("categories", "Categories"),
        ("repository_url", "Repository URL"),
        ("demo_url", "Demo URL"),
        ("docs_url", "Docs URL"),
    ]
    lines = [f"**Source path:** `{source_path}`"]
    for key, label in labels:
        if key not in metadata:
            continue
        value = metadata[key]
        if isinstance(value, list):
            value = ", ".join(str(item) for item in value)
        lines.append(f"**{label}:** {value}")
    lines.append(f"**Snapshot:** `{commit}`")
    description = metadata.get("description")
    if description:
        lines.extend(["", "#### Summary", "", str(description).strip()])
    return "\n".join(lines).strip() + "\n"


def iter_selected(config: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    selected: list[tuple[str, dict[str, Any]]] = []
    for group in SELECTABLE_GROUPS:
        entries = [entry for entry in config.get(group, []) if entry.get("include", True)]
        entries.sort(key=lambda entry: entry.get("order", 0))
        for entry in entries:
            selected.append((group, entry))
    return selected


def process_entry(
    root: Path,
    group: str,
    entry: dict[str, Any],
    site_url: str,
    commit: str,
    commit_timestamp: str,
) -> tuple[str, dict[str, Any]]:
    rel_path = entry["source_path"]
    path = root / rel_path
    if not path.exists():
        raise FileNotFoundError(rel_path)
    text = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(text, rel_path)
    source_type = entry.get("source_type") or infer_source_type(rel_path)
    title = normalize_title(rel_path, front_matter, entry.get("expected_title"))
    if not title:
        raise ValueError(f"Cannot determine title for {rel_path}")
    metadata = normalize_metadata(rel_path, source_type, front_matter, entry, site_url)
    if "canonical_url" not in metadata:
        raise ValueError(f"Cannot determine canonical URL for {rel_path}")
    state = TransformState()
    normalized_body = normalize_body(body, root, rel_path, front_matter, title, state)
    section_lines = [
        f"<!-- BEGIN SOURCE: {rel_path} -->",
        "",
        f"### {title}",
        "",
        metadata_block(metadata, rel_path, commit).strip(),
        "",
        normalized_body.strip(),
        "",
        f"<!-- END SOURCE: {rel_path} -->",
        "",
    ]
    section = "\n".join(section_lines)
    warnings = list(state.warnings)
    if "description" not in metadata:
        warnings.append("Missing description or excerpt.")
    if source_type in {"post", "thinking", "resource"} and "publication_date" not in metadata:
        warnings.append("Missing publication date.")
    if front_matter.get("published") is False or front_matter.get("private") is True or front_matter.get("status") == "draft":
        warnings.append("Selected source appears draft, private, or unpublished.")
    for asset in state.referenced_assets:
        if asset.startswith("/assets/") and not (root / asset.lstrip("/")).exists():
            warnings.append(f"Referenced local asset is missing: {asset}")
    manifest_entry = {
        "group": group,
        "source_path": rel_path,
        "source_type": source_type,
        "source_title": title,
        "canonical_url": metadata.get("canonical_url"),
        "selection_rationale": entry.get("selection_rationale"),
        "original_front_matter": serialize(front_matter),
        "normalized_metadata": metadata,
        "git_commit_sha": commit,
        "source_file_sha256": sha256_file(path),
        "output_content_sha256": sha256_text(section),
        "warnings": sorted(warnings),
        "liquid_include_transformations": state.transformations,
        "heading_transformations": state.heading_transformations,
        "referenced_assets": state.referenced_assets,
        "inclusion_timestamp": commit_timestamp,
        "pipeline_version": PIPELINE_VERSION,
    }
    return section, manifest_entry


def build(
    config_path: Path = DEFAULT_CONFIG,
    corpus_path: Path = DEFAULT_CORPUS,
    manifest_path: Path = DEFAULT_MANIFEST,
    report_path: Path | None = None,
) -> dict[str, Any]:
    config = read_yaml(config_path)
    site_config = read_yaml(ROOT / "_config.yml")
    site_url = str(site_config.get("url", "")).rstrip("/")
    commit = run_git(["rev-parse", "HEAD"], "unknown")
    commit_timestamp = run_git(["show", "-s", "--format=%cI", "HEAD"], "unknown")
    snapshot_date = commit_timestamp[:10] if re.match(r"\d{4}-\d{2}-\d{2}", commit_timestamp) else datetime.utcnow().date().isoformat()
    dirty = bool(run_git(["status", "--short"], ""))

    selected = iter_selected(config)
    sections: list[str] = []
    entries: list[dict[str, Any]] = []
    counts = {group: 0 for group in SELECTABLE_GROUPS}
    for group in SELECTABLE_GROUPS:
        group_entries = [(g, entry) for g, entry in selected if g == group]
        if not group_entries:
            continue
        sections.append(f"## {GROUP_HEADINGS[group]}\n")
        for _, entry in group_entries:
            section, manifest_entry = process_entry(ROOT, group, entry, site_url, commit, commit_timestamp)
            sections.append(section)
            entries.append(manifest_entry)
            counts[group] += 1

    preface = [
        f"# {config.get('corpus', {}).get('title', 'Barbara Hidalgo-Sotelo Website Corpus')}",
        "",
        "## Corpus Preface",
        "",
        f"Purpose: {config.get('corpus', {}).get('purpose')}",
        f"Snapshot date: {snapshot_date}",
        f"Git commit: `{commit}`",
        f"Source documents: {len(entries)}",
        "Content-type counts: "
        + ", ".join(f"{GROUP_HEADINGS[group]}={count}" for group, count in counts.items()),
        "This document is a derived experimental corpus for PageIndex-oriented navigation experiments.",
        "The original website source files remain authoritative.",
        "",
    ]
    corpus_text = "\n".join(preface + sections).rstrip() + "\n"

    line_lookup = {}
    lines = corpus_text.splitlines()
    for idx, line in enumerate(lines, start=1):
        begin = re.match(r"<!-- BEGIN SOURCE: (.+) -->", line)
        end = re.match(r"<!-- END SOURCE: (.+) -->", line)
        if begin:
            line_lookup.setdefault(begin.group(1), {})["start"] = idx
        if end:
            line_lookup.setdefault(end.group(1), {})["end"] = idx
    for entry in entries:
        lookup = line_lookup.get(entry["source_path"], {})
        entry["output_start_line"] = lookup.get("start")
        entry["output_end_line"] = lookup.get("end")

    corpus_path.parent.mkdir(parents=True, exist_ok=True)
    corpus_path.write_text(corpus_text, encoding="utf-8")
    corpus_sha = sha256_file(corpus_path)

    supporting_data = []
    for data_entry in config.get("supporting_data", []):
        data_path = ROOT / data_entry["source_path"]
        item = dict(data_entry)
        item["exists"] = data_path.exists()
        if data_path.exists():
            item["sha256"] = sha256_file(data_path)
        supporting_data.append(item)

    manifest = {
        "corpus": serialize(config.get("corpus", {})),
        "pipeline_version": PIPELINE_VERSION,
        "generated_at": commit_timestamp,
        "snapshot_date": snapshot_date,
        "git_commit_sha": commit,
        "worktree_dirty": dirty,
        "site_url": site_url,
        "config_path": config_path.relative_to(ROOT).as_posix(),
        "corpus_path": display_path(corpus_path),
        "corpus_sha256": corpus_sha,
        "expected_counts": config.get("expected_counts", {}),
        "counts": counts,
        "supporting_data": serialize(supporting_data),
        "documents": entries,
        "excluded_candidates": serialize(config.get("excluded_candidates", [])),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(serialize(manifest), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if report_path is not None:
        write_report(config, manifest, report_path)
    return manifest


def write_report(config: dict[str, Any], manifest: dict[str, Any], report_path: Path) -> None:
    warnings = [(doc["source_path"], warning) for doc in manifest["documents"] for warning in doc.get("warnings", [])]
    lines = [
        "# Normalization Report",
        "",
        "## Final Selected Content",
        "",
    ]
    for group in SELECTABLE_GROUPS:
        lines.append(f"### {GROUP_HEADINGS[group]}")
        for doc in [d for d in manifest["documents"] if d["group"] == group]:
            lines.append(f"- `{doc['source_path']}` — {doc['selection_rationale']}")
        lines.append("")
    lines.extend(["## Excluded Candidate Content", ""])
    for item in config.get("excluded_candidates", []):
        lines.append(f"- `{item['source_path']}` ({item.get('source_type', 'unknown')}): {item['reason']}")
    lines.extend(
        [
            "",
            "## Source Counts By Type",
            "",
            *[f"- {GROUP_HEADINGS[group]}: {count}" for group, count in manifest["counts"].items()],
            "",
            "## Front-Matter Schemas Encountered",
            "",
            "See `reports/NORMALIZATION_AUDIT.md` for the full schema audit. The builder preserves original front matter in the manifest and maps selected common fields into a normalized metadata model.",
            "",
            "## Field Mappings",
            "",
            "- `title` -> normalized title, falling back to the selection manifest expected title only when the source title is blank.",
            "- `description` or `excerpt` -> visible summary.",
            "- `permalink`, `canonical_url`, or Jekyll post slug -> canonical URL.",
            "- `date` -> publication date.",
            "- `last_modified_at` -> last modified date.",
            "- `tags`, `categories`, `status`, `stack`, `docs_url`, `url` -> visible item metadata when present.",
            "",
            "## Liquid/Include Transformations",
            "",
        ]
    )
    seen_transforms = []
    for doc in manifest["documents"]:
        for transform in doc.get("liquid_include_transformations", []):
            seen_transforms.append((doc["source_path"], transform))
    if seen_transforms:
        for source, transform in seen_transforms:
            lines.append(f"- `{source}`: `{transform.get('type')}` -> {transform.get('action')} ({transform.get('include') or transform.get('value') or transform.get('tag', '')})")
    else:
        lines.append("- No Liquid/include transformations were required.")
    lines.extend(["", "## Heading Transformations", ""])
    for doc in manifest["documents"]:
        count = len(doc.get("heading_transformations", []))
        lines.append(f"- `{doc['source_path']}`: {count} heading transformation(s).")
    lines.extend(["", "## Warnings And Unresolved Issues", ""])
    if warnings:
        for source, warning in warnings:
            lines.append(f"- `{source}`: {warning}")
    else:
        lines.append("- No warnings.")
    lines.extend(
        [
            "",
            "## Validation Results",
            "",
            "Run `python experiments/pageindex/scripts/validate_site_corpus.py`. The latest manual run should be recorded in task handoff notes.",
            "",
            "## Test Results",
            "",
            "Run `pytest experiments/pageindex/tests`. The latest manual run should be recorded in task handoff notes.",
            "",
            "## Reproduction Commands",
            "",
            "```bash",
            "python experiments/pageindex/scripts/build_site_corpus.py",
            "python experiments/pageindex/scripts/validate_site_corpus.py",
            "pytest experiments/pageindex/tests",
            "```",
            "",
            "## Known Limitations",
            "",
            "- HTML-to-Markdown conversion is deterministic but conservative; layout-only styling is removed and semantic text is retained.",
            "- Large HTML reference pages are deferred until Release 2 normalization rules can handle tables and filterable datasets more precisely.",
            "- External links are preserved but not fetched.",
            "",
            "## Recommendations Before Running PageIndex",
            "",
            "- Review `config/content-selection.yml` for editorial balance.",
            "- Review warnings in this report and in the manifest.",
            "- Decide whether the large Digital Twin reference pages should be normalized as a separate corpus.",
            "",
            "## Questions for Barbara",
            "",
            "- Should Release 1 include the large Digital Twin GraphRAG reference page despite its size and heavy HTML table structure?",
            "- Should data-story pages be promoted into the article group, or kept for a later project-evidence corpus?",
            "- Should `status: WIP` public project pages be labeled more explicitly in the corpus preface?",
            "",
        ]
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    manifest = build(args.config, args.corpus, args.manifest, DEFAULT_REPORT)
    print(f"Wrote {manifest['corpus_path']} ({manifest['counts']})")
    print(f"Wrote {display_path(args.manifest)}")
    print(f"Corpus SHA-256: {manifest['corpus_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
