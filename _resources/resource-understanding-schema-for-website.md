---
layout: single
title: "Understanding Your Schema.org Implementation"
subtitle: "This document explains how Schema.org structured data works on your site and how to verify it's working correctly."
date: 2025-12-01
last_modified_at: 2025-12-23
sitemap:
    priority: 0.5
permalink: /resources/explainer-schema-org-website/
excerpt: "Understand how Schema.org is implmented on a website like this one :)"
tags: [connected-data, schema.org, seo]
categories: [""]
format: Explainer
level: Beginner
# header:
#   teaser: /assets/resources/vision/teaser.jpg
#download_url: /assets/resources/checklist_color_contrast.pdf
#cognitive_principle: "Perception & Visual Processing"
---

## What is Schema.org?

**Simple definition:** Schema.org is a vocabulary of tags (or structured data) that you can add to your HTML to help search engines understand your content better.

**How it appears:** As invisible JSON-LD code embedded in your page's `<head>` section. Humans don't see it, but search engines read it.

**What it does:**
- Tells search engines the **type** of content (Article, Tutorial, Software Project)
- Provides structured information (author, dates, keywords, technologies used)
- Makes you **eligible** for rich snippets in search results (enhanced listings with images/dates)
- Does NOT guarantee better rankings—it's about structure, not magic

## How Your Site Implements It

### The Include File
Your site automatically generates Schema.org markup via `_includes/schema.html`, which is included in `_includes/head.html` on every page.

### Three Schema Types

1. **Article Schema** - Regular blog posts
2. **HowTo Schema** - Tutorial posts (auto-detected when `categories` or `tags` include "tutorial")
3. **SoftwareSourceCode Schema** - Projects in your `_projects` collection

### The Mapping

When you write this in your YAML front matter:
```yaml
title: "Getting Started with GitHub Pages"
subtitle: "Launch a free website in minutes"
excerpt: "A beginner-friendly guide..."
tags: [github-pages, tutorial, web-development]
date: 2024-07-28
```

Your site automatically generates this Schema.org markup:
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "headline": "Getting Started with GitHub Pages",
  "alternativeHeadline": "Launch a free website in minutes",
  "description": "A beginner-friendly guide...",
  "datePublished": "2024-07-28T00:00:00-06:00",
  "keywords": "github-pages, tutorial, web-development"
}
```

## How to Verify It's Working

### Method 1: View Page Source
1. Visit any blog post on your site (e.g., https://barbhs.com/blog/metadata-matters/)
2. Right-click → "View Page Source"
3. Press Cmd+F (Mac) or Ctrl+F (Windows)
4. Search for: `"@type": "HowTo"` or `"@type": "Article"`
5. You should see the JSON-LD structured data block

### Method 2: Google Rich Results Test
1. Go to: https://search.google.com/test/rich-results
2. Enter your page URL: `https://barbhs.com/blog/metadata-matters/`
3. Click "Test URL"
4. Google will show you what structured data it detected

### Method 3: Schema.org Validator
1. Go to: https://validator.schema.org/
2. Enter your page URL
3. See validation results and any warnings

### Method 4: Interactive Visualization
Open the interactive visualization at:
`/assets/visualizations/schema-examples.html`

This shows side-by-side comparisons of:
- Your YAML front matter (what you write)
- Generated Schema.org JSON-LD (what search engines read)
- Field mapping (which YAML fields map to which schema properties)

## What to Look For

**Good signs:**
- ✅ JSON-LD is present in page source
- ✅ Google Rich Results Test validates successfully
- ✅ All key fields are populated (headline, description, date, author)

**Warning signs:**
- ❌ No JSON-LD found in page source (check that schema.html is included)
- ❌ Google test shows errors or warnings
- ❌ Missing key fields (usually means YAML front matter is incomplete)

## Understanding the Visualization

The interactive visualization (`/assets/visualizations/schema-examples.html`) has three tabs:

### Tab 1: Article Schema
- Shows regular blog post example
- Demonstrates basic Article schema
- Maps YAML → Schema.org fields

### Tab 2: HowTo Schema
- Shows tutorial post example
- Demonstrates HowTo schema with "about" field (from `stack` array)
- Explains auto-detection logic

### Tab 3: Software Schema
- Shows project page example
- Demonstrates SoftwareSourceCode schema
- Shows how `stack` becomes `programmingLanguage`

## Common Questions

**Q: Does Schema.org improve my search rankings?**
A: Not directly. It makes your content more understandable to search engines and eligible for rich snippets, but it doesn't guarantee ranking improvements.

**Q: How do I know if it's working?**
A: Use the verification methods above. If Google's Rich Results Test validates successfully, it's working.

**Q: Do I need to do anything to maintain it?**
A: No. As long as you include proper YAML front matter (title, excerpt, date, tags), the schema is generated automatically.

**Q: What if I want to add more fields?**
A: Edit `_includes/schema.html` to add additional schema properties. Refer to https://schema.org for valid properties.

## Files Involved

- `_includes/schema.html` - Template that generates JSON-LD
- `_includes/head.html` - Includes schema.html on every page (line 4)
- `assets/visualizations/schema-examples.html` - Interactive visualization
- Individual content files (YAML front matter provides the data)

## Resources

- [Schema.org documentation](https://schema.org/docs/gs.html)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Google Search Central - Structured Data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [JSON-LD specification](https://json-ld.org/)

IN PROGRESS: A one-pager to help me remember how Schema.org impacts my site. 
---

*Last updated: December 23, 2025*
