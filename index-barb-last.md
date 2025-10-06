---
layout: splash
classes: home
title: "Barbara Hidalgo-Sotelo"
author_profile: false
excerpt: >
  From AI to analytics, I build tools that bridge the gap between data, decisions, and people.

  <p class="hero-ctas hero-ctas--pinned">
  <a class="btn hero-btn hero-btn--primary" href="/projects/">View Projects</a>
  <a class="btn hero-btn hero-btn--ghost" href="/contact/">Contact</a>
  </p>

header:
  overlay_filter: 0.7;
  overlay_color: "#1e3a5f"
  caption:  Austin, TX · Data Scientist & System-Builder · Human-Centered AI · Explainable Systems
# Keep the same data structure you already had so it's a safe drop‑in.
# We will render this via the new cards component below.
feature_row:
  - image_path: /assets/images/teasers/proj-fitness-v1-1024x768.jpg
    alt: "Fitness Dashboard"
    title: "Self-Hosted Workout Intelligence"
    excerpt: When my running data collided with daily dog walks, every workout got mislabeled as a "run"—even the 30 minute sniff walks. I built a full pipeline (auto csv export → <i class="fab fa-aws"></i> λ → <i class="fas fa-database"></i> → <i class="fas fa-chart-line"></i>) that classifies runs vs. walks using ML, with built-in model retraining for transparency. It's not about perfect analytics—it's about creating an explainable loop where messy real-world data becomes actionable insights, and the system evolves alongside my habits.
    url: /projects/fitness-dashboard/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/fitness-dashboard/
    docs_label: "Docs"
  - image_path: /assets/images/teasers/proj-convo-v1-1024x768.jpg
    alt: "Convoscope"
    title: "Conversational AI Management"
    excerpt: "Hopping between AI providers while losing track of what worked where felt increasingly inefficient. Convoscope is my solution: one interface, <i class='fas fa-robot'></i> multiple models (OpenAI, Anthropic, Google), <i class='fas fa-save'></i> persistent conversation history, and automatic topic extraction. It's a flexible workspace for comparing outputs side-by-side, experimenting with APIs, and capturing the conversations worth keeping—all without losing context when you switch providers or close tabs."
    url: /projects/convoscope/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/convoscope/
    docs_label: "Docs"
  - image_path: /assets/images/teasers/proj-beehive-v1-1024x768.jpg
    alt: "Beehive Tracker"
    title: "Beehive Analytics Platform"
    excerpt: "Four years of unlabeled bee photos became a living knowledge base by combining <i class='fas fa-camera'></i>  + EXIF metadata, Google Cloud Vision, and <i class='fas fa-cloud-sun'></i> weather APIs. The result: a KG with a query UI that surfaces patterns—when swarms happened, which seasons were productive, what weather preceded problems. Beyond bees, it demonstrates how to structure chaotic domain knowledge into a system that makes expertise explicit and searchable." 
    url: /projects/beehive-tracker/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/beehive-tracker/
    docs_label: "Docs"
---
<div class="home-section">

I’m Barbara Hidalgo-Sotelo, a data scientist with a PhD in cognitive science. I build systems that make complex data work for real people—across healthcare, federal consulting, and the cloud. My focus: turning technical capability into tools teams actually use.  <br><br>

<!-- =======================
     Featured Work (cards)
     ======================= -->
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