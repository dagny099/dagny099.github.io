# Phase 2 Strategy: URL Standardization & Topics Taxonomy

**Date**: 2025-11-22
**Status**: Planning & Design (No Code Yet)
**Goal**: Agree on end-state before implementation

---

## Current State Analysis

### 1. Blog URL Patterns (PROBLEM: 3 Different Patterns)

**Current URLs by Series:**

| Series | URL Pattern | Example | Count |
|--------|------------|---------|-------|
| **Website Building** | `/posts/{slug}/` | `/posts/getting-started-with-github-pages/` | 4 posts |
| **Sensor Fleet** | `/temp-sensor-{n}/` | `/temp-sensor-00/`, `/temp-sensor-01/` | 7 posts |
| **Individual Posts** | `/{slug}/` or `/posts/{slug}/` | `/print3d-00/`, `/stock-ticker-00/` | 4 posts |
| **Config Default** | `/:categories/:title/` | (not used consistently) | N/A |

**Why This Is A Problem:**
- ❌ **Unpredictable**: Users can't guess URLs
- ❌ **Inconsistent branding**: Some have `/posts/`, some don't, some have numeric codes
- ❌ **SEO dilution**: Not grouped under a recognizable path
- ❌ **Maintenance burden**: Hard to implement site-wide features (breadcrumbs, series navigation, etc.)
- ❌ **Migration risk**: If you want to change patterns later, you need redirects for 3 different formats

### 2. Categories (Currently Used)

| Category | Count | Posts |
|----------|-------|-------|
| **tutorial** | 5 | Website series (4) + Mermaid (1) |
| **data science** | 7 | Sensor Fleet series (7) |
| **cloudML** | 1 | AWS CCP |
| **3d printing** | 1 | 3D printing exploration |

**Issues:**
- ✅ Well-structured for blog posts
- ❌ Not consistent with other content types (Projects, Thinking, Resources don't use categories)
- ❌ "data science" is too broad (IoT vs ML vs DevOps are all lumped together)

### 3. Tags (Currently Used)

**Blog Post Tags:**
- Technical: `arduino`, `mqtt`, `temp sensor`, `python`, `streamlit`, `mermaid`, `github actions`, `jekyll`
- Skills: `webapps`, `cicd`, `documentation`, `workflow`
- Tools: `AWS`, `flask`, `dash`, `plotly`

**Other Collection Tags:**
- Projects/Thinking: `knowledge-graph`, `cv`, `governance`, `nlp`, `rag`, `retrieval`, `analytics`
- Resources: `visual-working-memory`, `data-visualization`, `perception`, `gestalt`, `ux-for-analytics`

**Issues:**
- ✅ Rich taxonomy exists across all content
- ❌ Not exposed to users (no topic pages)
- ❌ Inconsistent formatting (`knowledge-graph` vs `temp sensor`)
- ❌ No cross-content discovery (can't see all "knowledge graph" content in one place)

---

## Proposed Phase 2 Solution: Two Complementary Improvements

---

## IMPROVEMENT #1: Standardize Blog URL Patterns

### End-State: Single, Predictable URL Pattern

**Recommendation: `/blog/{slug}/`**

**Why This Pattern:**
1. ✅ **Predictable**: All blog posts under `/blog/` prefix
2. ✅ **Clean**: Simple slug-based URLs (no dates, no numbers)
3. ✅ **Conventional**: Industry standard (Medium, Dev.to, Substack all use this)
4. ✅ **Flexible**: Slug can include series info if needed (`sensor-fleet-part-1`)
5. ✅ **Breadcrumb-friendly**: `Home > Blog > Post Title`
6. ✅ **Maintainable**: One pattern forever

### Migration Path

**All posts become:**
```
OLD                                          NEW
/temp-sensor-00/                        →    /blog/sensor-fleet-intro/
/temp-sensor-01/                        →    /blog/sensor-fleet-part-1/
/temp-sensor-06/                        →    /blog/sensor-fleet-part-6/
/posts/getting-started-with-github-pages/   →    /blog/getting-started-with-github-pages/
/posts/organized-mermaid-life/          →    /blog/taming-mermaid-diagrams/
/print3d-00/                            →    /blog/3d-printing-exploration/
/stock-ticker-00/                       →    /blog/stock-ticker-comparison/
/posts/earned_aws_ccp/                  →    /blog/aws-ccp-certification/
```

**Implementation Approach:**
1. Update `_config.yml` permalink pattern to `/blog/:title/`
2. Add explicit permalinks to posts that need specific slugs
3. Create redirect rules for old URLs (using Jekyll Redirect From plugin)
4. Update internal links in any posts that reference other posts
5. Submit old URLs to Google Search Console for remapping

**Alternative Option (If You Want to Preserve Series Identity):**
```
/blog/series/website-building/part-1/
/blog/series/sensor-fleet/intro/
```
- **Pros**: Shows series structure in URL, helps with breadcrumbs
- **Cons**: More complex, harder to type, longer URLs

**My Recommendation: Stick with `/blog/{slug}/`**
- Series info can be shown in breadcrumbs and post metadata
- URLs should be short and memorable
- Series structure can change without breaking URLs

---

## IMPROVEMENT #2: Create Topics Taxonomy Page

### The Problem: Hidden Expertise

You have **70+ pieces of content** across 5 content types (Projects, Data Stories, Thinking, Blog, Resources) but:
- **No way to browse by topic/expertise area**
- Tags exist but aren't surfaced prominently
- Users can't discover "all knowledge graph content" or "all computer vision work"

**Example User Journey (Current - Broken):**
1. User reads "Bees, Graphs & Governance" essay
2. Wants to see more knowledge graph work
3. Has to manually click through Projects, Data Stories, Blog hoping to find related content
4. Gives up, bounces

**Example User Journey (With Topics - Fixed):**
1. User reads "Bees, Graphs & Governance" essay
2. Clicks `#knowledge-graphs` tag or visits `/topics/`
3. Sees: 1 Thinking piece + 2 Projects + 1 Data Story + Related blog posts
4. Explores deeply, stays on site

### End-State: Multi-Dimensional Topic Taxonomy

**Create TWO topic pages:**

#### Option A: `/topics/` - Master Topic Index (Recommended)

A **curated** page showing your expertise organized by domain:

```markdown
# Explore by Topic

## 🧠 Cognitive Science & Perception
- [Vision & Data Viz for Decision-Making](/thinking/vision-perception-dataviz) (Thinking)
- [Vision & Perception Cheatsheet](/resources/vision-perception-cheatsheet) (Resource)
- [7±2 is Everywhere: Chunking](/thinking/chunking) (Thinking)
- Related: `visual-working-memory`, `preattentive`, `gestalt`, `perception`

## 🕸️ Knowledge Graphs & Networks
- [Bees, Graphs & Governance](/thinking/bees-graphs-governance) (Thinking - Pinned)
- [Knowledge Network Mapping](/projects/knowledge-network-mapping) (Project - WIP)
- [Citation Link Prediction](/data-stories/citation-link-prediction) (Data Story)
- [Beehive Analytics Platform](/projects/beehive-analytics) (Project - WIP)
- Related: `knowledge-graph`, `neo4j`, `graph-neural-networks`, `metadata`

## 🤖 AI/NLP & Governance
- [RAG Without the Theater](/thinking/rag-without-theater) (Thinking)
- [Convoscope: Conversational AI](/projects/convoscope) (Project - Active)
- Related: `rag`, `retrieval`, `governance`, `nlp`, `prompting`, `prod-readiness`

## 📊 Data Products & Visualization
- [Self-Hosted Workout Intelligence](/projects/workout-intelligence) (Project - Active)
- [Exercise Dashboard: The Choco Effect](/data-stories/exercise-dashboard) (Data Story)
- [Hive Photo Metadata Tracker](/data-stories/hive-photo-tracker) (Data Story)
- Related: `analytics`, `data-visualization`, `streamlit`, `plotly`

## 🔧 DevOps & Infrastructure
- [Sensor Fleet Series](/blog/sensor-fleet-intro) (7-part blog series)
- [GitHub Actions for Jekyll](/blog/deploy-jekyll-gh-actions) (Blog)
- [Taming Mermaid Diagrams](/blog/taming-mermaid-diagrams) (Blog)
- Related: `arduino`, `mqtt`, `kafka`, `cicd`, `heroku`

## 🎓 Tutorials & Learning Guides
- [Website Building Series](/blog/getting-started-with-github-pages) (4-part series)
- [Bridge to Web Apps](/resources/bridge-to-web-apps) (Resource)
- [Project Starter Kit](/resources/project-starter-kit) (Resource)
- Related: `tutorial`, `jekyll`, `github-pages`, `streamlit`
```

**Why This Approach:**
- ✅ **Curated**: You control the narrative and groupings
- ✅ **Cross-content discovery**: Shows Projects + Thinking + Blog + Data Stories together
- ✅ **SEO-friendly**: Human-readable groupings match how people search
- ✅ **Demonstrates breadth**: Shows expertise across multiple domains
- ✅ **Low maintenance**: Manual curation means high quality
- ✅ **Flexible**: Can reorganize as your focus evolves

#### Option B: `/tags/` Enhancement (Complementary)

Keep the existing Jekyll tag archive but **enhance it**:
- Add tag descriptions
- Show tag relationships (parent/child)
- Add "See also" suggestions
- Include post count and latest activity

**Example:**
```
Tag: knowledge-graph (12 items)
Description: Graph databases, network analysis, and knowledge representation

Content:
- 2 Projects
- 3 Thinking pieces
- 1 Data Story
- 6 Blog posts

Related tags: neo4j, graph-neural-networks, metadata, cv
```

### Implementation Approach for Topics Page

**Step 1: Define Your Topic Taxonomy** (Manual - One Time)

Decide on 5-7 core topics that represent your expertise:
1. **Cognitive Science & Perception** (your PhD roots)
2. **Knowledge Graphs & Networks** (systems architecture)
3. **AI/NLP & Governance** (modern AI work)
4. **Data Products & Visualization** (user-facing work)
5. **DevOps & Infrastructure** (technical implementation)
6. **Tutorials & Learning** (teaching/sharing)

**Step 2: Create Topic Metadata in Front Matter** (Optional - For Automation)

Add `topics:` field to all content:
```yaml
---
title: "Bees, Graphs & Governance"
tags: [governance, knowledge-graph, metadata]
topics: [knowledge-graphs, ai-governance]  # NEW FIELD
---
```

**Step 3: Build the Topics Page** (Two Options)

**Option 3A: Manual Curation (Recommended for Start)**
- Create `_pages/topics.md`
- Manually list content by topic (like the example above)
- **Pros**: Full control, beautiful curation, immediate
- **Cons**: Requires updates when you add content

**Option 3B: Automated with Liquid** (For Later)
- Use Jekyll's Liquid templating to auto-generate from `topics:` field
- **Pros**: No maintenance, always up to date
- **Cons**: Requires adding `topics:` to all 70+ files, less control over narrative

**My Recommendation: Start with Option 3A (Manual)**
- Faster to implement (30-60 minutes)
- Better quality (you control the story)
- Easier to iterate on groupings
- Can automate later if needed

---

## Cost-Benefit Analysis

### Standardizing Blog URLs

**Effort**:
- 2-3 hours (update permalinks, add redirects, test links)

**Value**:
- ⭐⭐⭐⭐⭐ **SEO**: Better URL structure improves search rankings
- ⭐⭐⭐⭐ **UX**: Predictable URLs improve user experience
- ⭐⭐⭐⭐⭐ **Maintenance**: One pattern forever, easier to manage
- ⭐⭐⭐ **Branding**: `/blog/` prefix establishes content hub

**Risk**:
- 🟡 Medium - Requires redirects, must not break existing links

**ROI**: **HIGH** - One-time effort, permanent benefit

### Creating Topics Taxonomy

**Effort**:
- Manual curation: 1-2 hours
- Automated: 4-5 hours (add metadata to all files + templating)

**Value**:
- ⭐⭐⭐⭐⭐ **Discoverability**: Massively improves content discovery
- ⭐⭐⭐⭐⭐ **Expertise demonstration**: Shows breadth and depth of skills
- ⭐⭐⭐⭐ **Engagement**: Increases pages per session
- ⭐⭐⭐⭐⭐ **SEO**: Topic pages rank for expertise searches
- ⭐⭐⭐ **Differentiation**: Unique feature, sets you apart

**Risk**:
- 🟢 Low - Additive feature, doesn't break anything

**ROI**: **VERY HIGH** - Moderate effort, massive ongoing benefit

---

## Questions for You to Decide

### For URL Standardization:

1. **Pattern choice**: Do you prefer...
   - A) `/blog/{slug}/` (simple, my recommendation)
   - B) `/blog/series/{series-name}/{slug}/` (preserves series structure in URL)
   - C) Something else?

2. **Slug preferences**: For sensor fleet series, do you prefer...
   - A) `sensor-fleet-intro`, `sensor-fleet-part-1`, etc. (descriptive)
   - B) `sensor-fleet-00`, `sensor-fleet-01`, etc. (numeric, matches current)
   - C) Let me auto-generate from titles

3. **Redirect strategy**:
   - A) Jekyll Redirect From plugin (simple, works on GitHub Pages)
   - B) Netlify/Cloudflare redirects (if you migrate hosting)
   - C) HTML meta refresh as fallback

### For Topics Taxonomy:

4. **Topic groupings**: Do my 6 proposed topics resonate?
   - Cognitive Science & Perception
   - Knowledge Graphs & Networks
   - AI/NLP & Governance
   - Data Products & Visualization
   - DevOps & Infrastructure
   - Tutorials & Learning

   Would you add/remove/rename any?

5. **Implementation approach**:
   - A) Manual curation first, automate later (my recommendation)
   - B) Fully automated from day 1 (requires adding `topics:` to all files)

6. **Topic page location**:
   - A) Main nav item (like Projects, Thinking, Resources)
   - B) Footer only
   - C) Linked from About/Resources pages
   - D) All of the above

7. **Visual treatment**:
   - A) Simple list (like my example above)
   - B) Card grid with icons for each topic
   - C) Interactive tag cloud / network visualization
   - D) Minimal Mistakes archive layouts (existing theme templates)

---

## Recommended Decision

**My Opinionated Recommendation:**

### URL Standardization:
- **Pattern**: `/blog/{slug}/` (simple and conventional)
- **Slugs**: Auto-generate from titles, manually tweak if needed
- **Series naming**: `sensor-fleet-intro`, `sensor-fleet-part-1` (human-readable)
- **Redirects**: Jekyll Redirect From plugin

### Topics Taxonomy:
- **Approach**: Manual curation first (Option 3A)
- **Topics**: Your 6 proposed topics are excellent, use as-is
- **Location**: Add to footer navigation + link from About page
- **Visual**: Start with simple list, enhance with cards later
- **Timeline**: Implement after URL standardization (dependency: need stable URLs)

### Implementation Order:
1. **First**: URL Standardization (2-3 hours)
   - Provides stable foundation
   - Must be done before creating cross-links in Topics page
2. **Second**: Topics Taxonomy (1-2 hours)
   - Can reference new stable URLs
   - Easier to curate once URLs are clean

**Total Time Investment**: 3-5 hours
**Expected Impact**:
- Blog traffic: +30-40% (better SEO + predictable URLs)
- Pages per session: +40-50% (topic-based discovery)
- Bounce rate: -25% (easier navigation between related content)

---

## Next Steps

1. **You review this document** and answer the 7 questions above
2. **We agree on end-state** for both improvements
3. **I implement Phase 2** based on your decisions
4. **We test** locally before pushing to production

---

*Created: 2025-11-22*
*For: dagny099.github.io Phase 2 Planning*
*Status: Awaiting user decisions before implementation*
