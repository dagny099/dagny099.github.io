---
layout: splash
classes: home
title: "Barbara Hidalgo-Sotelo"
excerpt: >
  Data scientist with a governance mindset who turns fuzzy
  business priorities into <strong>shippable, explainable</strong> AI. I sit with
  doers and execs, translate priorities into plans, and iterate
  with clear checkpoints.
header:
  overlay_color: "#000000"
  overlay_filter: 0.78
  caption: "Austin, TX · Data Science · Knowledge Graphs · Human‑Centered AI"

# Keep the same data structure you already had so it's a safe drop‑in.
# We will render this via the new cards component below.
feature_row:
  - image_path: /assets/images/teasers/fitness.jpg
    alt: "Fitness Dashboard"
    title: "Fitness Dashboard → Decisions, not dashboards"
    excerpt: "From CSV sprawl to weekly, explainable training insights—consistency metrics, deltas, and trend‑break detection."
    url: /projects/fitness-dashboard/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/fitness-dashboard/
    docs_label: "Docs"
  - image_path: /assets/images/teasers/convoscope.jpg
    alt: "Convoscope"
    title: "Convoscope → AI that briefs you"
    excerpt: "Structures messy conversations into crisp briefs and next‑step checklists; retrieval without hallucination theater."
    url: /projects/convoscope/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/convoscope/
    docs_label: "Docs"
  - image_path: /assets/images/teasers/beehive.jpg
    alt: "Beehive Tracker"
    title: "Beehive Tracker → A living knowledge base"
    excerpt: "EXIF + weather + CV → structured apiculture insights; a friendly UI over a knowledge graph."
    url: /projects/beehive-tracker/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/beehive-tracker/
    docs_label: "Docs"
---

<!-- =======================
     Featured Work (cards)
     ======================= -->
<div class="home-section">
<details class="home-accordion" data-section="projects" markdown="1" open>
<summary><h2>Featured Projects</h2></summary>

{% include feature_row_dual %}

</details>
</div>

<!-- =======================
     Resources & Guides (keep minis for now)
     ======================= -->
<div class="home-section">
  <details class="home-accordion" data-section="resources" markdown="1" open>
  <summary><h2>Resources &amp; Guides</h2></summary>
  <div class="feature__wrapper">

  <div class="resource-minis">
    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-file-alt" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/executive-brief/">Executive brief template</a></h3>
        <p>Turn fuzzy threads into crisp, action‑ready briefs with surface links to evidence.</p>
      </div>
    </article>

    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-project-diagram" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/dataset-cards/">Dataset &amp; prompt cards</a></h3>
        <p>Lightweight governance you can actually keep—structure, versions, and reproducible envs.</p>
      </div>
    </article>

    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-laptop-code" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/streamlit-bridge/">Streamlit: DS to app, without drama</a></h3>
        <p>From notebook to interactive app in hours. Pragmatic guide, patterns, and gotchas.</p>
      </div>
    </article>
  </div>

    <p style="margin:.5rem 0 0 0.5rem;">
      <a class="browse-all" href="/resources/">Browse all resources</a>
    </p>
  </div>
  </details>
</div>

<!-- =======================
     Explore (brand chips)
     =======================
<div class="home-section">
  <h2 class="sr-only">Explore the site</h2>
  <nav class="explore-chips" aria-label="Primary sections">
    <a class="chip chip--projects" href="/projects/">
      <span class="chip__title">Projects</span>
      <span class="chip__desc">Case studies &amp; systems</span>
    </a>
    <a class="chip chip--thinking" href="/thinking/">
      <span class="chip__title">Thinking</span>
      <span class="chip__desc">Essays &amp; working notes</span>
    </a>
    <a class="chip chip--resources" href="/resources/">
      <span class="chip__title">Resources</span>
      <span class="chip__desc">Guides &amp; templates</span>
    </a>
    <a class="chip chip--journey" href="/my-journey/">
      <span class="chip__title">My Journey</span>
      <span class="chip__desc">Timeline &amp; pivots</span>
    </a>
  </nav>
</div> -->

{% include section_tiles.html exclude="/contact/" %}
<!-- {% include section_tiles.html  %} -->