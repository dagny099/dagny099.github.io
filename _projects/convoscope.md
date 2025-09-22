---
layout: single
title: "Conversational AI Management"
permalink: /projects/convoscope/
classes: [project, hero, wide]    
author_profile: false
read_time: false
# Optional: right rail ToC for the deep dive (auto-generates from headings)
toc: true
toc_sticky: true
order: 30

# taxonomy
tags: [governance, nlp, python, retrieval, summarization, ui-ux]
categories: ["AI Systems & MLOps (Pragmatic)", "Data Products & Interfaces"]

# Make the header a true hero
header:
  # card image used on /projects/ (and any archive grids)
  teaser: /assets/images/projects/convoscope/card.jpg

 # banner image for the big hero at the top of the page
  overlay_image: /assets/images/projects/convoscope/hero.jpg   # swap in a real banner
  overlay_filter: 0.25
  caption: "Configure your LLM to taste"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/convoscope
      class: "btn--primary"
    - label: "Read Docs"
      url: https://docs.barbhs.com/convoscope/
      class: "btn--light-outline"

# Convoscope image gallery displayed on screen
gallery:
  - url: /assets/images/projects/convoscope/s1.jpg
    image_path: /assets/images/projects/convoscope/s1.jpg
    alt: "Brief view"
    title: "Brief"
  - url: /assets/images/projects/convoscope/s2.jpg
    image_path: /assets/images/projects/convoscope/s2.jpg
    alt: "Evidence links"
    title: "Evidence"

# For cards/site previews
excerpt: "Building data science projects means constantly iterating on ideas, and I found myself having the same types of conversations with AI tools repeatedly without any way to track patterns or build on previous insights. Instead of being locked into one provider's approach, I wanted the flexibility to switch between OpenAI, Anthropic, and Google models based on the task. More importantly, I wanted to analyze these conversations—tracking how my questioning evolves and building a personal knowledge base from AI interactions that reveals patterns in human-AI dialogue."
last_modified_at: 
# CTAs
url: /projects/convoscope/
btn_label: "Project"
docs_url: https://docs.barbhs.com/convoscope/
docs_label: "Docs"
---

<!-- Project meta grid (fast facts) -->
<div class="project-meta">
  <div><span class="k">Role</span><span>DS/PM, IC builder</span></div>
  <div><span class="k">When</span><span>2024–2025</span></div>
  <div><span class="k">Stack</span><span>Python · FastAPI · pgvector · Postgres · OpenAI · Docker</span></div>
  <div><span class="k">Links</span>
    <a class="btn btn--sm btn--primary" href="https://github.com/dagny099/convoscope">GitHub</a>
    <a class="btn btn--sm" href="https://docs.barbhs.com/convoscope/">Docs</a>
  </div>
</div>

<!-- 30-second lead -->
<p class="lead">
<strong>30-second summary.</strong> Convoscope turns messy, multi-channel conversations into crisp briefs and next-step checklists—evidence-linked, explainable, and ready for action.
</p>

{% include page__taxonomy.html %}

<!-- 2-minute overview -->
<details class="toggle-block">
  <summary>Read the 2-minute overview</summary>
  <div class="toggle-content">
    <p><strong>Problem.</strong> Information overload across channels makes status, accountability, and decision prep slow.</p>
    <p><strong>Approach.</strong> Lightweight ingestion → segment/label → summarize with guardrails → surface citations. Retrieval patterns with prompt+version control; simple UI for brews/briefs.</p>
    <p><strong>Impact.</strong> Shorter “Where are we?” meetings; clearer “what/why/next” briefs; traceable claims.</p>
    <p><strong>Governance.</strong> Dataset cards, prompt/version control, environment lockfiles, reproducible runs.</p>
  </div>
</details>

{% include gallery id="convoscope-gallery" caption="Screens & flows" %}

<!-- Impact stats (visual bite) -->
<div class="stat-cards">
  <div><div class="n">−40%</div><div class="c">time in status meetings</div></div>
  <div><div class="n">3×</div><div class="c">faster brief prep</div></div>
  <div><div class="n">0</div><div class="c">silent prompt changes</div></div>
</div>

## Deep dive

### Problem
Information scattered across Slack/notes/Docs increases the cost of “what changed?” and “what’s next?”

### Approach
- **Ingest** light; keep original sources and link back.  
- **Segment & label** turns long threads into units; **retrieve** with task-specific indices.  
- **Summarize with rails:** claims + citations, no “vibes.”  
- **UI for work:** brief → next steps → owners.

### Impact
- Reduced status time; teams arrive aligned.  
- Brevity with traceability → leaders sign off faster.

### Governance
- Dataset cards for each source; environment pinning; prompt/version diffing; automatic provenance on every claim.

---

## Links
- <a class="btn btn--primary" href="https://github.com/dagny099/convoscope">GitHub</a>
- <a class="btn" href="https://docs.barbhs.com/convoscope/">Docs</a>
