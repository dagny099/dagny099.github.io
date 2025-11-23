# Scripts Directory

Automation scripts for maintaining the Jekyll site.

## Sitemap Generator

**File:** `generate_sitemap.py`

Automatically generates an interactive Mermaid diagram sitemap by scanning the site's content structure.

### Quick Start

```bash
# Install dependencies (one time)
pip install -r scripts/requirements.txt

# Run the generator
python scripts/generate_sitemap.py
```

### What It Does

1. **Scans** all Jekyll content directories:
   - `_posts/` — Blog posts
   - `_projects/` — Project showcase items
   - `_thinking/` — Essay collection
   - `_resources/` — Templates and guides
   - `data-stories/` — Technical narratives
   - `_pages/` — Static pages

2. **Parses** YAML front matter from each markdown file to extract:
   - Title
   - Permalink/URL
   - Tags and categories
   - Status indicators

3. **Auto-detects** content status:
   - 🚧 **WIP** — Work in progress items
   - 📌 **Pinned** — Featured/foundational content
   - ✅ **Active** — Live/production projects

4. **Generates** Mermaid diagram with:
   - Hierarchical structure (Home → Collections → Items)
   - Clickable nodes (links to live site)
   - Color-coded content types
   - Status indicators

5. **Updates** two files:
   - `SITEMAP.md` (repository documentation)
   - `_pages/site-architecture.md` (live site page)

### Configuration

Edit these constants at the top of `generate_sitemap.py`:

```python
# Base URL for your live site
SITE_URL = "https://barbhs.com"

# Directories to scan
CONTENT_DIRS = {
    "posts": "_posts",
    "projects": "_projects",
    # ...
}

# Status detection keywords
STATUS_KEYWORDS = {
    "wip": ["wip", "work in progress", "draft"],
    "pinned": ["pinned", "featured"],
    "active": ["active", "live"]
}
```

### Front Matter Examples

The script looks for these fields in your markdown front matter:

**Explicit status:**
```yaml
---
title: "My Project"
permalink: /projects/my-project/
status: wip  # Auto-detected as 🚧 WIP
---
```

**Keyword detection in title/excerpt:**
```yaml
---
title: "My Project (WIP)"  # Auto-detected as 🚧 WIP
permalink: /projects/my-project/
---
```

**Pinned content:**
```yaml
---
title: "Important Post"
status: pinned  # Auto-detected as 📌 Pinned
---
```

### Output Example

```mermaid
graph TB
    Home[🏠 Home Page]
    Home --> Projects[📊 Projects]
    Projects --> PROJ1[My Project<br/>🚧 WIP]

    click Home "https://barbhs.com" "Visit Home"
    click Projects "https://barbhs.com/projects/" "View Projects"
    click PROJ1 "https://barbhs.com/projects/my-project/" "My Project"

    classDef wip fill:#f8d7da,stroke:#842029
    class PROJ1 wip
```

### When to Run

Run the script whenever you:
- Add new blog posts
- Create new projects/essays/resources
- Change content structure
- Update content status (WIP → Active, etc.)

### Troubleshooting

**Error: "No module named 'frontmatter'"**
- Run: `pip install -r scripts/requirements.txt`

**Warning: "Could not parse [file]"**
- Check that the file has valid YAML front matter
- Ensure front matter is at the top of the file
- Verify YAML syntax (proper indentation, quotes)

**Sitemap not updating on site**
- The script updates markdown files only
- Jekyll needs to rebuild the site
- If using GitHub Pages, push changes to trigger rebuild
- If local, run `bundle exec jekyll serve`

### Future Enhancements

Ideas for extending the script:
- [ ] Group blog posts by series
- [ ] Add year/month nodes for blog archive
- [ ] Generate topic-based alternate views
- [ ] Include post counts in collection nodes
- [ ] Add interactive filtering options
- [ ] Generate multiple diagram layouts

### Contributing

When modifying the script:
1. Maintain detailed comments (blog article-ready)
2. Add examples for new features
3. Update this README
4. Test with your actual content
5. Verify both SITEMAP.md and site-architecture.md update correctly

---

*Part of the dagny099.github.io repository*
*Maintained by Barbara Hidalgo-Sotelo*
