# Information Architecture (IA) Recommendations

**Date**: 2025-11-21
**Site**: barbhs.com (dagny099.github.io)
**Current State**: 5-item main navigation, multiple content types, some content hidden from primary navigation

---

## Executive Summary

Your site has excellent content organization but faces **discoverability challenges**. High-quality content (Data Stories, Blog posts, Research) is hidden from primary navigation, while your content taxonomy has evolved beyond your navigation structure. These recommendations focus on improving content discoverability, clarifying mental models, and aligning navigation with your current content strategy.

---

## Critical Issues & Recommendations

### 🔴 CRITICAL ISSUE #1: Data Stories is Orphaned

**Problem:**
Data Stories has 3 high-quality technical narratives but is **not in main navigation**. Users must know the URL `/data-stories/` directly or stumble upon it.

**Impact:**
- Hidden showcase content that demonstrates your technical storytelling
- Missed opportunity to differentiate from dry portfolio pieces
- Content exists but provides no value if undiscoverable

**Recommendation: Add Data Stories to Main Navigation**

**Option A (Recommended): Add as 6th Nav Item**
```yaml
# _data/navigation.yml
- title: "Data Stories"
  short: "Stories"
  url: /data-stories/
  color: "#5a189a"
  background-color: "#f4f0fb"
  subtitle: "Technical narratives with interactive visualizations."
  description: "Case studies told through data, from problem to insight."
```

**Option B: Merge with Projects**
Combine Projects and Data Stories under a single "Work" or "Case Studies" section with subcategories.

**Rationale:**
- Data Stories represents your unique voice (technical + narrative)
- It's distinct from Projects (which focus on systems/products) and Thinking (which is more abstract)
- Showcases your ability to communicate technical work to non-technical audiences
- 3 items is enough to warrant dedicated navigation

---

### 🟡 ISSUE #2: Blog Content is Hidden

**Problem:**
You have **16 blog posts** organized into coherent series (Website Building, Sensor Fleet), but:
- Blog is NOT in main navigation (removed in recent redesign)
- Users can't discover this tutorial content
- Posts demonstrate learning in public and teaching ability

**Impact:**
- SEO value lost (blog posts drive organic traffic)
- Teaching/tutorial content goes unseen
- Missed community building opportunity

**Recommendation: Restore Blog to Navigation (Footer or Utility Nav)**

**Option A: Add to Footer Navigation**
Create a "Learn" or "Archive" section in footer with:
- Blog
- Tags
- Categories
- Archives by date

**Option B: Add Dropdown to Main Nav**
Add a "More" dropdown with:
- Blog
- Research
- Experience
- Gallery

**Option C: Merge with Thinking**
Rename "Thinking" to "Writing" and include both essays and tutorials.

**Rationale:**
- Blog content has value (tutorials are evergreen)
- Series structure (4-part + 7-part) shows depth
- Differentiates you from portfolio-only sites
- Community-focused content builds trust

---

### 🟡 ISSUE #3: Inconsistent Content Taxonomy

**Problem:**
Content types overlap conceptually:
- **Projects** = Systems/products you've built
- **Data Stories** = Technical narratives about specific problems
- **Portfolio** = Legacy version of Projects
- **Thinking** = Essays and conceptual pieces
- **Blog** = Tutorials and technical how-tos

Users don't have clear mental models for "Where do I find X?"

**Recommendation: Clarify Content Types with Descriptive Subtitles**

**Update Navigation Descriptions:**

| Section | Current Subtitle | Recommended Subtitle |
|---------|-----------------|---------------------|
| Projects | "Case studies with a 30-sec summary → 2-min overview → deep dive." | **"Systems and products I've built"** |
| Data Stories | *(not in nav)* | **"Technical narratives with interactive visualizations"** |
| Thinking | "Foundational posts are pinned; everything else is living research." | **"Essays on cognition, data systems, and AI governance"** |
| Blog | *(not in nav)* | **"Tutorials, series, and learning in public"** |
| Resources | "Plug-and-play PDFs and checklists for faster collaboration." | ✓ *Good as-is* |

**Content Type Matrix:**

| If User Wants... | They Should Visit... |
|-----------------|---------------------|
| See what you've shipped | **Projects** |
| Understand your technical storytelling | **Data Stories** |
| Explore your thinking/philosophy | **Thinking** |
| Learn how to do something | **Blog** |
| Grab a template/checklist | **Resources** |

**Rationale:**
- Clear mental models reduce cognitive load
- Users can self-navigate without guessing
- Reduces overlap confusion

---

### 🟠 ISSUE #4: URL Pattern Inconsistency

**Problem:**
Blog posts have 3 different URL patterns:
- Website series: `/posts/{title}/`
- Sensor Fleet series: `/temp-sensor-{n}/`
- Individual posts: `/{category}/{title}/`

**Impact:**
- Confusing for users trying to remember URLs
- Harder to implement site-wide changes
- SEO dilution across multiple patterns

**Recommendation: Standardize to Single Pattern**

**Option A (Recommended): Use Category-Based URLs**
```yaml
# _config.yml
permalink: /blog/:title/
```
All posts become: `/blog/{title}/`

**Option B: Keep Category Structure**
```yaml
permalink: /:categories/:title/
```
But ensure ALL posts have a category defined.

**Migration Plan:**
1. Add Jekyll redirects for old URLs
2. Update internal links
3. Submit old URLs to Google Search Console for remapping

**Rationale:**
- Consistency improves UX and SEO
- `/blog/{title}` is conventional and expected
- Easier to maintain long-term

---

### 🟢 ISSUE #5: Portfolio vs Projects Confusion

**Problem:**
You have both `/portfolio/` (legacy, 6 items) and `/projects/` (modern, 4 items).

**Current Strategy:** Migrating Portfolio → Projects (noted in sitemap)

**Recommendation: Complete the Migration**

**Steps:**
1. ✓ Keep Projects in main nav (already done)
2. Add redirects from `/portfolio/{item}` → `/projects/{item}` for migrated content
3. Create a `/portfolio/` redirect to `/projects/` after migration complete
4. Remove Portfolio from sitemap once empty
5. Keep 2-3 best portfolio pieces as "Archive" subsection on Projects page

**Rationale:**
- Eliminates confusion
- Consolidates showcase content
- "Projects" is more modern terminology than "Portfolio"
- Cleaner mental model for visitors

---

## Secondary Recommendations

### 🔵 #6: Elevate Research Page

**Problem:**
Research page (4 papers, 8 posters) is only accessible via footer/utility navigation, but your PhD background is a key differentiator.

**Recommendation:**
Add Research to main navigation OR create a "Background" dropdown with:
- Research
- Experience
- My Journey

**Rationale:**
- Establishes credibility for enterprise clients
- Differentiates you from bootcamp grads
- Academic work is impressive and should be featured

---

### 🔵 #7: Add Breadcrumb Navigation

**Problem:**
Deep content (individual blog posts, data stories) doesn't show hierarchy.

**Recommendation:**
Ensure breadcrumbs are enabled site-wide:
```yaml
# _config.yml (already set)
breadcrumbs: true
```

Verify they appear on:
- Blog posts: Home > Blog > {Title}
- Data stories: Home > Data Stories > {Title}
- Resources: Home > Resources > {Title}

**Rationale:**
- Improves wayfinding
- Reduces bounce rate
- Shows content hierarchy visually

---

### 🔵 #8: Create Topic Taxonomy

**Problem:**
Content spans multiple themes but isn't grouped by topic/expertise area.

**Recommendation:**
Add a "Topics" page that cross-references content by theme:

**Example Topics:**
- **Computer Vision** → Research papers + Hive Photo Tracker
- **Knowledge Graphs** → Projects + Thinking essays + Citation Networks
- **AI Governance** → Thinking essays + RAG post
- **Data Visualization** → Exercise Dashboard + Vision & Perception resources
- **DevOps/Infrastructure** → Sensor Fleet series + GitHub Actions posts

**Implementation:**
Use Jekyll tags/categories to auto-generate topic pages.

**Rationale:**
- Users often search by topic, not content type
- Shows expertise breadth and depth
- Improves SEO for topical searches
- Helps recruiters/clients find relevant work

---

### 🔵 #9: Add "Start Here" or "New Visitor" Landing

**Problem:**
No obvious entry point for first-time visitors.

**Recommendation:**
Create a "Start Here" page or section on homepage with:
- **For Recruiters** → Experience + Projects + Research
- **For Data Scientists** → Thinking + Resources + Blog
- **For Teams** → Projects + Data Stories + Contact
- **For Career Changers** → My Journey + Blog + Resources

**Rationale:**
- Reduces choice paralysis
- Segments audiences
- Increases engagement time
- Personalized pathways improve conversion

---

### 🔵 #10: Implement Search Facets

**Problem:**
Search is enabled but doesn't offer filtering by content type.

**Current:** Lunr.js site-wide search
**Recommendation:** Add filter checkboxes:
- [ ] Projects
- [ ] Data Stories
- [ ] Thinking
- [ ] Blog
- [ ] Resources
- [ ] Research

**Rationale:**
- Improves search precision
- Users can narrow results by intent
- Makes large content libraries navigable

---

## Proposed Information Architecture (Option A)

### Primary Navigation (Main Masthead)
1. **Projects** - Systems and products I've built
2. **Data Stories** - Technical narratives with visualizations *(NEW)*
3. **Thinking** - Essays on cognition, data, and AI
4. **Resources** - Templates, guides, and starter kits
5. **My Journey** - Career timeline and pivots
6. **Contact** - Let's collaborate

### Secondary Navigation (Footer)
**Explore**
- Blog (Tutorials & Series)
- Research (Papers & Posters)
- Experience (Professional Roles)
- Gallery (Creative Work)

**Archives**
- Topics A-Z
- Tags
- Categories
- All Posts

**About**
- About Me
- Resume (PDF)
- Site Architecture *(NEW - link to SITEMAP.md)*

---

## Proposed Information Architecture (Option B - More Consolidated)

### Primary Navigation (Main Masthead)
1. **Work** *(dropdown)*
   - Projects (Systems/Products)
   - Data Stories (Narratives)
   - Portfolio Archive
2. **Writing** *(dropdown)*
   - Thinking (Essays)
   - Blog (Tutorials)
   - Research Papers
3. **Resources** - Templates & Guides
4. **About** *(dropdown)*
   - My Journey
   - Experience
   - Research
   - Contact

**Pros:**
- Cleaner, fewer top-level items
- Groups related content
- Modern mega-menu pattern

**Cons:**
- Hides content behind clicks
- May reduce discoverability for browsing users

---

## Implementation Priority

### 🔥 Phase 1 (High Impact, Low Effort)
1. ✅ **Add Data Stories to main navigation** *(5 min)*
2. ✅ **Add Blog to footer navigation** *(5 min)*
3. ✅ **Update navigation subtitles for clarity** *(10 min)*
4. ✅ **Add sitemap link to footer** *(2 min)*

**Estimated Time:** 30 minutes
**Impact:** Immediate content discoverability improvement

### 🟡 Phase 2 (Medium Impact, Medium Effort)
5. Standardize blog URL patterns with redirects *(2-3 hours)*
6. Create Topics taxonomy page *(1-2 hours)*
7. Complete Portfolio → Projects migration *(1-2 hours)*
8. Add "Start Here" section to homepage *(1 hour)*

**Estimated Time:** 5-8 hours
**Impact:** Improved UX and content organization

### 🔵 Phase 3 (High Impact, High Effort)
9. Implement search facets/filters *(3-4 hours)*
10. Add Research to main navigation or create Background dropdown *(1 hour)*
11. Audit all internal links for consistency *(2-3 hours)*
12. Create visual topic map (interactive Mermaid diagram by topic) *(2 hours)*

**Estimated Time:** 8-10 hours
**Impact:** Professional polish and scalability

---

## Success Metrics

Track these metrics before/after IA changes:

1. **Discoverability**
   - % of users who visit Data Stories page
   - % of users who visit Blog from homepage
   - Pages per session (should increase)

2. **Engagement**
   - Average session duration
   - Bounce rate (should decrease)
   - Internal link click rate

3. **Navigation Clarity**
   - Search query patterns (should shift from navigation queries like "blog" to content queries)
   - Exit pages (should shift away from dead-ends)

4. **Content Performance**
   - Time on page for Data Stories
   - Scroll depth on long-form content
   - Social shares of previously hidden content

---

## Conclusion

Your content is high-quality but suffering from **discoverability issues**. The recommendations above prioritize:

1. **Surfacing hidden content** (Data Stories, Blog)
2. **Clarifying content types** (Projects vs Thinking vs Data Stories)
3. **Improving wayfinding** (breadcrumbs, topics, search filters)
4. **Completing migrations** (Portfolio → Projects)

**Quick Win:** Implement Phase 1 recommendations (30 minutes) to immediately improve content accessibility.

**Long-term:** Consider Option A architecture for maximum content exposure, or Option B for cleaner minimalist navigation.

---

*Generated: 2025-11-21*
*For: dagny099.github.io (barbhs.com)*
*Based on: Site analysis, navigation review, content audit*
