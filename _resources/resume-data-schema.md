---
layout: single
title: "Resume Data Schema"
subtitle: "JSON-powered resume architecture for consistency across platforms"
permalink: /resources/resume-data-schema/
excerpt: "How I use a single JSON file as the source of truth for my resume, website experience page, and future automation—complete with schema diagrams and usage guide."
date: 2026-04-08
last_modified_at: 2026-04-08
tags: [data-architecture, json-schema, automation, systems-design]
categories: ["Technical Documentation"]
format: Documentation
level: Intermediate
header:
  teaser: /assets/diagrams/resume-data-flow.svg
cognitive_principle: "Information Architecture & Systems Design"
toc: true
toc_label: "Schema Guide"
toc_icon: "file-code"
---

## Overview

The `barbara_resume_golden.json` file serves as the **single source of truth** for my professional experience data. It powers the [Experience page](/experience/) with dynamic filtering, and is designed to support multiple output formats (web, PDF, TimelineJS, etc.).

## Visual Schema Map

<div style="text-align: center; margin: 2rem 0;">
  <img src="/assets/diagrams/resume-json-schema.svg" alt="Resume JSON Schema Diagram" style="max-width: 100%; height: auto; border: 1px solid #e5e7eb; border-radius: 8px; padding: 1rem; background: white;" />
</div>

## Data Flow Architecture

<div style="text-align: center; margin: 2rem 0; padding: 1.5rem; background: #f9fafb; border-radius: 8px;">
  <img src="/assets/diagrams/resume-data-flow.svg" alt="Resume Data Flow Diagram" style="max-width: 100%; height: auto;" />
</div>

## Why This Architecture?

**Problem:** Maintaining multiple resume versions (PDF, Word, web) leads to inconsistencies and manual sync work.

**Solution:** Store all professional data in one structured JSON file, then generate outputs programmatically.

### Benefits

- ✅ **Single source of truth** - Update once, reflect everywhere
- ✅ **Version controlled** - Track changes via Git
- ✅ **Queryable** - Filter and search programmatically
- ✅ **Portable** - Easy to transform into any format
- ✅ **AI-friendly** - Structured data for digital assistants

## Schema Structure

### Core Sections

| Section | Purpose | Used By |
|---------|---------|---------|
| `meta` | Version tracking, source files | Documentation |
| `profile` | Contact info, headline, summary | About page, contact forms |
| `education` | Academic degrees | About page, CV generation |
| `certifications` | Professional credentials | Resume, LinkedIn sync |
| `skills` | Technical capabilities (6 categories) | Resume, skills matrix |
| **`experience`** | **Work history with filtering** | **/experience/ page** |
| `projects` | Portfolio projects | Projects page |
| `publications` | Research papers | Publications page |
| `display` | UI configuration (colors, filters) | Experience page styling |

### Experience Section (Most Important)

The `experience` array is what powers the [/experience/](/experience/) page with dynamic filtering.

#### Required Fields

```json
{
  "title": "Job title",
  "employer": "Company name",
  "start_date": "YYYY-MM",
  "domains": ["category1", "category2"],
  "highlights": ["Achievement 1", "Achievement 2"],
  "tags": ["tag1", "tag2"]
}
```

#### Optional But Recommended

```json
{
  "employment_type": "Full-time | Contract | Consulting | Founder | Research",
  "end_date": "YYYY-MM or null for current",
  "location": "City, State or Remote",
  "outcomes": [
    {"metric": "cycle-time", "value": "↓ 25%"}
  ],
  "skills": ["Python", "SQL", "PowerBI"]
}
```

#### How Filtering Works

The experience page uses `domains` for the filter buttons:
- Each role can have multiple domains (e.g., "public sector", "data governance")
- Clicking a domain button shows only roles in that category
- Domain colors are configured in `display.style.domainColors`

**First 3 highlights** from each role are displayed on the card. Keep these concise and impactful.

## Usage Examples

### Adding a New Role

1. Open `_data/barbara_resume_golden.json`
2. Add new object to the `experience` array (at the top for most recent)
3. Follow the schema structure
4. Choose appropriate `domains` from existing filter list or add new ones
5. Rebuild the site: `bundle exec jekyll build`

### Updating Skills

The `skills` object has 6 predefined categories:
- `programming` - Languages and tools
- `ml` - Machine learning libraries
- `genai` - GenAI/LLM frameworks (new in 2024)
- `data_viz_bi` - Visualization and BI tools
- `cloud_data` - Cloud platforms and databases
- `governance_nlp` - Data governance and NLP
- `methods` - Methodologies and approaches

### Customizing Filter Buttons

Edit `display.filters.domains` to change which filter buttons appear on the experience page:

```json
"display": {
  "filters": {
    "domains": [
      "public sector",
      "healthcare",
      "AI engineering",
      "enterprise transformation"
    ]
  }
}
```

## Technical Details

### Date Format

All dates use `YYYY-MM` format:
- `start_date: "2024-01"` → January 2024
- `end_date: null` → Current role (displays as "Present")

### Multi-Domain Roles

Roles can belong to multiple domains for richer categorization:

```json
"domains": [
  "enterprise transformation",
  "analytics enablement",
  "web analytics"
]
```

Currently, filtering uses the **first domain** only. Future enhancement: support multi-domain filtering.

### Validation

Use the companion schema file for validation:

```bash
# Validate JSON structure
python3 -m json.tool _data/barbara_resume_golden.json > /dev/null && echo "✓ Valid JSON"

# Or use the JSON schema validator
# jsonschema -i _data/barbara_resume_golden.json _data/barbara_resume_golden_SCHEMA.json
```

## Files & Locations

| File | Purpose | Location |
|------|---------|----------|
| `barbara_resume_golden.json` | Main data file | `_data/` |
| `barbara_resume_golden_SCHEMA.json` | JSON Schema definition | `_data/` |
| `experience.md` | Template that renders the data | `_pages/` |
| `resume-json-schema.mmd` | Mermaid source for diagram | `assets/diagrams/` |
| `resume-json-schema.svg` | Visual schema diagram | `assets/diagrams/` |

## Maintenance Tips

### Keep It DRY
- The JSON is the source of truth
- Don't duplicate data in markdown files
- Generate outputs from JSON when possible

### Version Control Best Practices
- Commit JSON changes with descriptive messages
- Tag major versions (e.g., `resume-v2.0`)
- Keep old versions in git history

### Content Guidelines
- **Highlights:** Action verb + impact (quantify when possible)
- **Domains:** Keep list manageable (4-6 categories)
- **Tags:** Specific technologies/methodologies
- **Skills:** Group by category, avoid duplication

## Future Enhancements

Ideas for extending this system:

- [ ] Python script to generate PDF resume from JSON
- [ ] Automated sync to LinkedIn
- [ ] TimelineJS export for visual timeline
- [ ] Multi-domain filtering on experience page
- [ ] "Clear filters" button
- [ ] Schema validation in CI/CD pipeline
- [ ] API endpoint to serve resume data

## Questions?

This schema powers my [experience page](/experience/) and maintains consistency across my professional presence. If you're building something similar or have suggestions, [let's connect](/contact/)!

---

*Last updated: April 8, 2026 • [View raw JSON](https://github.com/dagny099/dagny099.github.io/blob/master/_data/barbara_resume_golden.json)*
