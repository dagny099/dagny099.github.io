#!/usr/bin/env python3
"""
Jekyll Site Sitemap Generator
=============================

Automatically generates an interactive Mermaid diagram sitemap by scanning
a Jekyll site's content structure. The sitemap includes clickable nodes with
auto-detected status indicators and color-coded content types.

Author: Barbara Hidalgo-Sotelo
Created: 2025-11-22
License: MIT

Usage:
    python scripts/generate_sitemap.py

Features:
    - Scans Jekyll collections (_posts, _projects, _thinking, _resources, data-stories)
    - Parses YAML front matter to extract metadata
    - Auto-detects status (WIP, Active, Pinned) from front matter
    - Auto-assigns colors based on content type
    - Generates Mermaid diagram with clickable links
    - Updates both SITEMAP.md and _pages/site-architecture.md

Requirements:
    pip install python-frontmatter pyyaml
"""

import frontmatter
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import re
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

# Base URL for your live site (used for clickable links)
SITE_URL = "https://barbhs.com"

# Directory paths to scan (relative to repo root)
CONTENT_DIRS = {
    "posts": "_posts",
    "projects": "_projects",
    "thinking": "_thinking",
    "resources": "_resources",
    "data_stories": "data-stories",
    "pages": "_pages"
}

# Color definitions for different content types (Mermaid CSS classes)
COLORS = {
    "collection": {"fill": "#e1f5ff", "stroke": "#0077b6"},
    "data_story": {"fill": "#e7d4ff", "stroke": "#5a189a"},
    "legacy": {"fill": "#fff3cd", "stroke": "#856404"},
    "pinned": {"fill": "#d1e7dd", "stroke": "#0a3622"},
    "wip": {"fill": "#f8d7da", "stroke": "#842029"},
    "blog_post": {"fill": "#fff4e6", "stroke": "#d97706"}
}

# Status detection keywords in front matter
STATUS_KEYWORDS = {
    "wip": ["wip", "work in progress", "in progress", "draft"],
    "pinned": ["pinned", "pin", "featured"],
    "active": ["active", "live", "production"]
}

# ============================================================================
# CONTENT SCANNING FUNCTIONS
# ============================================================================

def parse_markdown_file(filepath: Path) -> Optional[Dict]:
    """
    Parse a markdown file and extract front matter metadata.

    Args:
        filepath: Path to the markdown file

    Returns:
        Dictionary containing front matter data, or None if parsing fails

    Example front matter:
        ---
        title: "My Post Title"
        permalink: /blog/my-post/
        tags: [python, automation]
        status: wip
        ---
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # Extract relevant metadata
        metadata = {
            "title": post.get("title", filepath.stem),
            "permalink": post.get("permalink", ""),
            "tags": post.get("tags", []),
            "categories": post.get("categories", []),
            "status": post.get("status", ""),
            "excerpt": post.get("excerpt", ""),
            "layout": post.get("layout", ""),
            "filepath": str(filepath)
        }

        return metadata

    except Exception as e:
        print(f"Warning: Could not parse {filepath}: {e}")
        return None


def detect_status(metadata: Dict) -> str:
    """
    Auto-detect content status from front matter and title.

    Checks for:
    1. Explicit 'status' field in front matter
    2. Keywords in title or excerpt
    3. Default to empty string if no status found

    Args:
        metadata: Dictionary of front matter data

    Returns:
        Status string: "wip", "pinned", "active", or ""
    """
    # Check explicit status field
    if metadata.get("status"):
        status_lower = metadata["status"].lower()
        if any(keyword in status_lower for keyword in STATUS_KEYWORDS["wip"]):
            return "wip"
        if any(keyword in status_lower for keyword in STATUS_KEYWORDS["pinned"]):
            return "pinned"
        if any(keyword in status_lower for keyword in STATUS_KEYWORDS["active"]):
            return "active"

    # Check title and excerpt for keywords
    searchable_text = f"{metadata.get('title', '')} {metadata.get('excerpt', '')}".lower()

    if any(keyword in searchable_text for keyword in STATUS_KEYWORDS["wip"]):
        return "wip"
    if any(keyword in searchable_text for keyword in STATUS_KEYWORDS["pinned"]):
        return "pinned"
    if any(keyword in searchable_text for keyword in STATUS_KEYWORDS["active"]):
        return "active"

    return ""


def get_content_type(filepath: Path) -> str:
    """
    Determine content type from file path.

    Args:
        filepath: Path to the content file

    Returns:
        String identifier: "post", "project", "thinking", "resource",
        "data_story", or "page"
    """
    path_str = str(filepath)

    if "_posts" in path_str:
        return "post"
    elif "_projects" in path_str:
        return "project"
    elif "_thinking" in path_str:
        return "thinking"
    elif "_resources" in path_str:
        return "resource"
    elif "data-stories" in path_str:
        return "data_story"
    elif "_pages" in path_str:
        return "page"
    else:
        return "other"


def scan_content_directory(repo_root: Path) -> Dict[str, List[Dict]]:
    """
    Scan all content directories and extract metadata from markdown files.

    Args:
        repo_root: Path to the repository root directory

    Returns:
        Dictionary mapping content types to lists of metadata dictionaries

    Example return:
        {
            "posts": [{title: "Post 1", permalink: "/blog/post-1", ...}, ...],
            "projects": [{title: "Project 1", ...}, ...],
            ...
        }
    """
    content_inventory = {
        "posts": [],
        "projects": [],
        "thinking": [],
        "resources": [],
        "data_stories": [],
        "pages": []
    }

    print("Scanning content directories...")

    for content_type, dir_path in CONTENT_DIRS.items():
        full_path = repo_root / dir_path

        if not full_path.exists():
            print(f"  Warning: {dir_path} not found, skipping")
            continue

        # Find all markdown files
        md_files = list(full_path.glob("*.md"))
        print(f"  Found {len(md_files)} files in {dir_path}")

        for md_file in md_files:
            # Skip certain files
            if md_file.name.startswith(("README", "CONTRIBUTING", ".")):
                continue

            metadata = parse_markdown_file(md_file)
            if metadata:
                # Add detected status and content type
                metadata["detected_status"] = detect_status(metadata)
                metadata["content_type"] = get_content_type(md_file)

                # Add to appropriate category
                content_inventory[content_type].append(metadata)

    return content_inventory


# ============================================================================
# MERMAID DIAGRAM GENERATION
# ============================================================================

def generate_node_id(title: str, index: int) -> str:
    """
    Generate a unique, valid Mermaid node ID from a title.

    Mermaid node IDs must be alphanumeric (no spaces or special chars).

    Args:
        title: Content title
        index: Numeric index for uniqueness

    Returns:
        Valid node ID string (e.g., "POST1", "PROJ2")
    """
    # Remove non-alphanumeric characters and limit length
    clean_title = re.sub(r'[^a-zA-Z0-9]', '', title)[:10]
    return f"{clean_title}{index}".upper()


def format_node_label(title: str, status: str = "") -> str:
    """
    Format a node label with optional status indicator.

    Args:
        title: Content title
        status: Status string ("wip", "pinned", "active", or "")

    Returns:
        Formatted label with emoji if status present

    Examples:
        format_node_label("My Project", "wip") -> "My Project<br/>🚧 WIP"
        format_node_label("My Post", "") -> "My Post"
    """
    # Status emoji mapping
    status_emoji = {
        "wip": "🚧 WIP",
        "pinned": "📌 Pinned",
        "active": "✅ Active"
    }

    if status and status in status_emoji:
        return f"{title}<br/>{status_emoji[status]}"
    return title


def generate_mermaid_diagram(content_inventory: Dict[str, List[Dict]]) -> str:
    """
    Generate complete Mermaid diagram code from content inventory.

    Creates a hierarchical graph showing:
    - Home page at the root
    - Collection index pages as main branches
    - Individual content items as leaves
    - Clickable links on all nodes
    - Color-coded by content type
    - Status indicators where applicable

    Args:
        content_inventory: Dictionary of content metadata by type

    Returns:
        String containing complete Mermaid diagram code
    """
    lines = []

    # Start diagram
    lines.append("```mermaid")
    lines.append("graph TB")
    lines.append("    %% Root")
    lines.append("    Home[🏠 Home Page<br/>barbhs.com]")
    lines.append("")

    # Main navigation connections
    lines.append("    %% Main Navigation")
    lines.append("    Home --> Projects[📊 Projects]")
    lines.append("    Home --> DataStories[📖 Data Stories]")
    lines.append("    Home --> Thinking[💭 Thinking]")
    lines.append("    Home --> Resources[📚 Resources]")
    lines.append("    Home --> Blog[📝 Blog Archive]")
    lines.append("")

    # Generate nodes for each content type
    node_mapping = {}  # Track node IDs for click directives

    # Projects
    if content_inventory["projects"]:
        lines.append("    %% Projects Collection")
        for idx, item in enumerate(content_inventory["projects"], 1):
            node_id = generate_node_id("PROJ", idx)
            label = format_node_label(item["title"], item["detected_status"])
            lines.append(f"    Projects --> {node_id}[{label}]")
            node_mapping[node_id] = item["permalink"]
        lines.append("")

    # Data Stories
    if content_inventory["data_stories"]:
        lines.append("    %% Data Stories")
        for idx, item in enumerate(content_inventory["data_stories"], 1):
            node_id = generate_node_id("DS", idx)
            label = format_node_label(item["title"], item["detected_status"])
            lines.append(f"    DataStories --> {node_id}[{label}]")
            node_mapping[node_id] = item["permalink"]
        lines.append("")

    # Thinking
    if content_inventory["thinking"]:
        lines.append("    %% Thinking Collection")
        for idx, item in enumerate(content_inventory["thinking"], 1):
            node_id = generate_node_id("THINK", idx)
            label = format_node_label(item["title"], item["detected_status"])
            lines.append(f"    Thinking --> {node_id}[{label}]")
            node_mapping[node_id] = item["permalink"]
        lines.append("")

    # Resources
    if content_inventory["resources"]:
        lines.append("    %% Resources Collection")
        for idx, item in enumerate(content_inventory["resources"], 1):
            node_id = generate_node_id("RES", idx)
            label = format_node_label(item["title"], item["detected_status"])
            lines.append(f"    Resources --> {node_id}[{label}]")
            node_mapping[node_id] = item["permalink"]
        lines.append("")

    # Blog Posts (organized by series if detected)
    if content_inventory["posts"]:
        lines.append("    %% Blog Posts")
        # For simplicity, show count rather than all individual posts
        post_count = len(content_inventory["posts"])
        lines.append(f"    Blog --> BlogPosts[{post_count} Blog Posts]")
        lines.append("")

    # Add clickable links
    lines.append("    %% Clickable Links")
    lines.append(f'    click Home "{SITE_URL}" "Visit Home Page"')
    lines.append(f'    click Projects "{SITE_URL}/projects/" "View Projects"')
    lines.append(f'    click DataStories "{SITE_URL}/data-stories/" "Explore Data Stories"')
    lines.append(f'    click Thinking "{SITE_URL}/thinking/" "Read Essays"')
    lines.append(f'    click Resources "{SITE_URL}/resources/" "Browse Resources"')
    lines.append(f'    click Blog "{SITE_URL}/blog/" "Read Blog"')
    lines.append("")

    for node_id, permalink in node_mapping.items():
        if permalink:
            url = f"{SITE_URL}{permalink}" if not permalink.startswith("http") else permalink
            title = node_id.replace("_", " ").title()
            lines.append(f'    click {node_id} "{url}" "{title}"')
    lines.append("")

    # Add styling classes
    lines.append("    %% Styling")
    lines.append("    classDef collection fill:#e1f5ff,stroke:#0077b6,stroke-width:2px")
    lines.append("    classDef dataStory fill:#e7d4ff,stroke:#5a189a,stroke-width:2px")
    lines.append("    classDef pinned fill:#d1e7dd,stroke:#0a3622,stroke-width:2px")
    lines.append("    classDef wip fill:#f8d7da,stroke:#842029,stroke-width:2px")
    lines.append("    classDef blogPost fill:#fff4e6,stroke:#d97706,stroke-width:2px")
    lines.append("")

    lines.append("    class Projects,Thinking,Resources collection")
    lines.append("    class DataStories dataStory")
    lines.append("    class BlogPosts blogPost")
    lines.append("```")

    return "\n".join(lines)


# ============================================================================
# FILE UPDATING FUNCTIONS
# ============================================================================

def update_sitemap_file(filepath: Path, new_diagram: str) -> bool:
    """
    Update a sitemap file with new Mermaid diagram while preserving
    front matter and surrounding content.

    Strategy:
    1. Read existing file
    2. Find the Mermaid code block (```mermaid ... ```)
    3. Replace it with new diagram
    4. Write back to file

    Args:
        filepath: Path to sitemap markdown file
        new_diagram: New Mermaid diagram code (includes ```mermaid markers)

    Returns:
        True if successful, False otherwise
    """
    try:
        # Read existing content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find and replace Mermaid block
        # Pattern: ```mermaid ... ``` (non-greedy, multiline)
        pattern = r'```mermaid.*?```'

        if re.search(pattern, content, re.DOTALL):
            # Replace existing diagram
            new_content = re.sub(pattern, new_diagram, content, flags=re.DOTALL)
            print(f"  Updated existing diagram in {filepath.name}")
        else:
            # No existing diagram found - append after front matter
            print(f"  Warning: No existing Mermaid diagram found in {filepath.name}")
            print(f"  Appending new diagram to end of file")
            new_content = content + "\n\n" + new_diagram

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    except Exception as e:
        print(f"  Error updating {filepath}: {e}")
        return False


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function.

    Workflow:
    1. Determine repository root
    2. Scan all content directories
    3. Generate Mermaid diagram
    4. Update sitemap files
    5. Print summary
    """
    print("=" * 70)
    print("Jekyll Sitemap Generator")
    print("=" * 70)
    print()

    # Find repository root (assumes script is in scripts/ directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    print(f"Repository root: {repo_root}")
    print()

    # Step 1: Scan content
    content_inventory = scan_content_directory(repo_root)

    # Print summary
    print()
    print("Content Summary:")
    print("-" * 70)
    for content_type, items in content_inventory.items():
        count = len(items)
        print(f"  {content_type.replace('_', ' ').title()}: {count} items")
    print()

    # Step 2: Generate diagram
    print("Generating Mermaid diagram...")
    mermaid_diagram = generate_mermaid_diagram(content_inventory)
    print(f"  Generated diagram with {len(mermaid_diagram.splitlines())} lines")
    print()

    # Step 3: Update files
    print("Updating sitemap files...")

    files_to_update = [
        repo_root / "SITEMAP.md",
        repo_root / "_pages" / "site-architecture.md"
    ]

    success_count = 0
    for filepath in files_to_update:
        if filepath.exists():
            if update_sitemap_file(filepath, mermaid_diagram):
                success_count += 1
        else:
            print(f"  Warning: {filepath} not found, skipping")

    print()
    print("=" * 70)
    print(f"Complete! Updated {success_count}/{len(files_to_update)} files")
    print()
    print("Next steps:")
    print("  1. Review the updated sitemap files")
    print("  2. Commit the changes: git add SITEMAP.md _pages/site-architecture.md")
    print("  3. Push to your branch")
    print("=" * 70)


if __name__ == "__main__":
    main()
