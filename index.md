---
title: "Barbara Hidalgo-Sotelo, PhD — Cognitive Scientist & Data Scientist" #"Barbara Hidalgo-Sotelo, PhD"
description: >
  Cognitive scientist and data scientist exploring messy data, intelligent systems,
  and how people make meaning. Projects, data stories, and resources on human-centered AI,
  visualization, and knowledge systems.
layout: splash
classes: home
author_profile: false
excerpt: >
  Making meaning out of messy data. I apply cognitive science to build AI and data systems that work the way humans think.

  <p class="hero-ctas hero-ctas--centered">
  <a class="btn hero-btn hero-btn--ghost" href="/contact/"> Let's Connect &nbsp;<i class="fas fa-paper-plane"></i></a>
  </p>

header:
  overlay_filter: 0.7;
  overlay_color: "#4a3a5f"
  caption: Applied AI Engineer & Cognitive Scientist · Knowledge Graphs, RAG & Evaluation · PhD Cognitive Science, MIT
  profile_image: /assets/images/biopic/bhs-new-headshot-v1.png

# Updated project descriptions with cognitive angles
feature_row:
  - image_path: /assets/images/teasers/proj-fitness-v1-1024x768.jpg
    alt: "Fitness Dashboard"
    title: "Self-Hosted Workout Intelligence"
    excerpt: >
      <strong>Attention patterns reveal signal in 14 years of messy data.</strong><br><br>
      When my running data collided with daily dog walks, every workout got mislabeled as a "run"—even the 30 minute sniff walks. 
      I built a full pipeline (auto csv export → <i class="fab fa-aws"></i> λ → <i class="fas fa-database"></i> → <i class="fas fa-chart-line"></i>) 
      that classifies runs vs. walks using ML, with built-in model retraining for transparency. 
      <br><br>
      <em>Cognitive insight: Humans recognize patterns through contrast and repetition—this system leverages both to surface the real story in behavioral data.</em>
    url: /projects/fitness-dashboard/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/fitness-dashboard/
    docs_label: "Docs"
    
  - image_path: /assets/images/teasers/proj-convo-v1-1024x768.jpg
    alt: "Convoscope"
    title: "Conversational AI Management"
    excerpt: >
      <strong>Multi-modal comparison designed for cognitive load management.</strong><br><br>
      Hopping between AI providers while losing track of what worked where felt increasingly inefficient. Convoscope is my solution: 
      one interface, <i class='fas fa-robot'></i> multiple models (OpenAI, Anthropic, Google), <i class='fas fa-save'></i> persistent 
      conversation history, and automatic topic extraction. It's a flexible workspace for comparing outputs side-by-side.
      <br><br>
      <em>Cognitive insight: Working memory can only hold 7±2 items—by offloading comparison to visual space, we free cognitive resources for actual thinking.</em>
    url: /projects/convoscope/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/convoscope/
    docs_label: "Docs"
    
  - image_path: /assets/images/teasers/proj-beehive-v1-1024x768.jpg
    alt: "Beehive Tracker"
    title: "Beehive Analytics Platform"
    excerpt: >
      <strong>Computer vision meets human memory to structure 4 years of visual documentation.</strong><br><br>
      Four years of unlabeled bee photos became a living knowledge base by combining <i class='fas fa-camera'></i> EXIF metadata, 
      Google Cloud Vision, and <i class='fas fa-cloud-sun'></i> weather APIs. The result: a knowledge graph with a query UI that 
      surfaces patterns—when swarms happened, which seasons were productive, what weather preceded problems.
      <br><br>
      <em>Cognitive insight: Human memory is associative, not chronological—this system mirrors how beekeepers actually recall and connect observations.</em>
    url: /projects/beehive-tracker/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/beehive-tracker/
    docs_label: "Docs"
---
<!--
<div class="home-section">
<b>I'm Barbara Hidalgo-Sotelo, a data scientist with a PhD in cognitive science from MIT.</b> My research on visual attention—how humans find meaning in complex visual scenes—has been 
<a href="https://scholar.google.com/citations?user=nQG25vkAAAAJ" target="_blank">cited 430+ times</a> and continues to shape how I approach every data problem.

Here's what that looks like in practice: When I build metadata tools, I don't just make them technically correct—I design them to match how people actually recall information, through association and context rather than alphabetical lists. When I develop dashboards, I think about where eyes naturally land first and what questions people are actually trying to answer under cognitive load.

<b>I solve data problems through a cognitive lens</b>—across healthcare, federal consulting, and cloud platforms. Not just technically capable, but designing for how attention works, how memory organizes, and how understanding happens in layers.
</div>
      Every interface I design, every model I train, every visualization I create is informed by 
      <strong>years of tracking eye movements</strong> and studying how humans process information.

-->
<!-- =======================
     Currently
     ======================= -->
<div class="home-section home-section--currently">
  <div class="current-feature current-feature--slim">
    <div class="current-feature__content">

      <h2 class="current-feature__title">Teaching Semantic Web in public</h2>
      <p class="current-feature__body">
        A 12-week curriculum on RDF, OWL, SPARQL, and modern knowledge graphs — built around real projects, readable explanations, and honest tradeoffs.
      </p>

      <p class="current-feature__actions">
        <a class="btn btn--primary" href="https://curriculum.barbhs.com" target="_blank" rel="noopener">Explore the curriculum ↗</a>
        <a class="current-feature__secondary" href="https://curriculum.barbhs.com/modules/1/" target="_blank" rel="noopener">See Module 1 →</a>
      </p>

      <p class="current-feature__status">Currently on Module 1 of 4:</p>
      <!-- p class="current-feature__status">Module 1 of 4 · Week 1 of 12 · Foundations</p -->
      <nav class="module-arc" aria-label="Course structure">
        <span class="module-arc__item module-arc__item--active" aria-current="true">1) Foundations</span>
        <span class="module-arc__sep" aria-hidden="true">·</span>
        <span class="module-arc__item">2) Modeling</span>
        <span class="module-arc__sep" aria-hidden="true">·</span>
        <span class="module-arc__item">3) Reasoning</span>
        <span class="module-arc__sep" aria-hidden="true">·</span>
        <span class="module-arc__item">4) Shipping</span>
      </nav>

    </div>

    <aside class="current-feature__thesis" aria-label="Thesis behind this series">
      <p class="current-feature__thesis-body">Some AI problems need probability. Some need structure. The useful systems know the difference.</p>
      <p class="current-feature__thesis-aside">
        <!-- TODO: replace placeholder with real Buttondown subscribe URL once configured -->
        <a href="https://buttondown.email/barbarahs" target="_blank" rel="noopener">Follow along by email →</a>
      </p>
    </aside>
  </div>
</div>

<!-- =======================
     My Approach + Digital Twin (merged row) — placed right after Currently so the two visually distinct "who I am" sections cluster, then the credibility sections (Projects / Writing / Principles) flow as a unit
     ======================= -->
<div class="home-section home-section--duo">
  <div class="duo-row">
    <div class="duo-row__card duo-row__card--approach">
      <p class="duo-row__eyebrow">How I think about data</p>
      <h3 class="duo-row__title">I build for how humans think</h3>
      <p class="duo-row__body">
        Every system I build starts with a cognitive question — where attention goes, what gets remembered, and what decision the data is really being asked to support.
      </p>
      <p class="duo-row__actions">
        <a class="duo-row__link" href="/my-journey/#cognitive-foundation">Read about my approach →</a>
      </p>
    </div>

    <div class="duo-row__card duo-row__card--twin">
      <p class="duo-row__eyebrow">Interactive</p>
      <h3 class="duo-row__title">Ask my Digital Twin</h3>
      <p class="duo-row__body">
        Curious how I think through messy problems? I built an AI grounded in my work, writing, and frameworks. Ask it anything — explore projects, brainstorm ideas, or test my reasoning.
      </p>
      <p class="duo-row__actions">
        <a class="btn btn--primary duo-row__btn" href="https://twin.barbhs.com" target="_blank" rel="noopener">Open Digital Twin ↗</a>
      </p>
    </div>
  </div>
</div>

<!-- =======================
     Featured Projects — mirrors Featured Writing layout (centered title + subheading + browse-all), without the tinted background
     ======================= -->
<div class="home-section home-section--projects">
  <h2 class="home-section__heading">Featured Projects</h2>
  <p class="home-section__subheading">
    Self-hosted data products, AI systems, and knowledge graphs—built end-to-end to learn what actually works in production.
  </p>

  {% include feature_row_dual %}

  <p class="featured-projects__cta">
    <a class="browse-all" href="/projects/">Browse all projects</a>
  </p>
</div>

<!-- =======================
     Featured Writing
     ======================= -->
<div class="home-section home-section--writing">
  <h2 class="home-section__heading">Featured Writing</h2>
  <p class="home-section__subheading">
    A mix of notes &amp; experiments, data narratives, and essays &amp; perspectives—built to show how I approach messy problems.
  </p>

  <div class="featured-writing">
    <article class="featured-writing__card">
      <p class="featured-writing__badge">Data Narrative</p>
      <h3><a href="/data-stories/hive-photo-metadata-tracker/">The Beekeeper’s Time Machine</a></h3>
      <p>
      Explore how extracting timestamps and visual features from years of my own hive photos lets me travel through inspection history, revealing rhythms, surprises, and insights that would otherwise remain hidden. 
      </p>
      <a class="featured-writing__link" href="/data-stories/hive-photo-metadata-tracker/">Read the story →</a>
    </article>

    <article class="featured-writing__card">
      <p class="featured-writing__badge featured-writing__badge--tutorial">Tutorials &amp; Guides</p>
      <h3><a href="/series/website-building/">Building a Sustainable Digital Home</a></h3>
      <p>
      A supportive, skills-forward series that helps you launch a personal website, automate publishing, document your process, and build a platform you’ll actually want to keep using over time.
      </p>
      <a class="featured-writing__link" href="/series/website-building/">Open the guide →</a>
    </article>

    <article class="featured-writing__card">
      <p class="featured-writing__badge featured-writing__badge--thinking">Applied Thinking</p>
      <h3><a href="/blog/taming-mermaid-diagrams/">Making Mermaid Diagrams Work for You</a></h3>
      <p>
      Cut through the chaos of tangled graph drawings with practical tips and structured approaches that bring confidence to crafting Mermaid diagrams that actually convey what you mean.
      </p>
      <a class="featured-writing__link" href="/blog/taming-mermaid-diagrams/">Read the post →</a>
    </article>
  </div>

  <p class="featured-writing__cta" style="text-align:center; margin: 1rem 0 0 0;" >
    <a class="browse-all" href="/writing/">Browse all writing</a>
  </p>
</div>

<!-- =======================
     Cognitive Principles (NEW)
     ======================= -->
<div class="home-section home-section--principles">
  <h2 class="home-section__heading">Cognitive Principles in Practice</h2>

  <div class="principles-grid">
    <div class="principle-card principle-card--vision">
      <div class="principle-card__icon" aria-hidden="true">👁️</div>
      <h3>Metadata Matters</h3>
      <p>
        Just as our brains rely on associations to retrieve memories, the web relies on metadata to surface meaning from the void.
      </p>
      <a href="/blog/metadata-matters/">More on metadata, the digital equivalent of cognitive context →</a>
    </div>

    <div class="principle-card principle-card--attention">
      <div class="principle-card__icon" aria-hidden="true">🧠</div>
      <h3>Cognitive Offloading</h3>
      <p>
        Leverage preattentive attributes—like position and luminance—to design dashboards that respect the brain's  processing limits.
      </p>
      <a href="/thinking/vision-perception-data-viz-decisions/">Designing for How People Actually See →</a>
    </div>

    <div class="principle-card principle-card--patterns">
      <div class="principle-card__icon" aria-hidden="true">🏃🏽‍♀️</div>
      <h3>Grow from Messiness</h3>
      <p>
        Life rarely fits into neat database schemas. I used ML on my real-world exercise data, granting me trust in my own metrics again.
      </p>
      <a href="data-stories/exercise-dashboard/">Why perfect data is not a prereq for a healthy system →</a>
    </div>
  </div>
</div>

<!-- =======================
     Resources & Guides #TODO ASAP - Combine the Archive stuff linked below with the newer stuff on Resources page
     ======================= 
<div class="home-section">
  <details class="home-accordion" data-section="resources" markdown="1" open>
  <summary><h2>Resources & Guides</h2></summary>
   
  <div class="feature__wrapper">

  <div class="resource-minis">
    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-eye" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/visual-decision-making/">Vision & Perception Cheatsheet</a></h3>
        <p>One-pager turning perception science into practical defaults for dashboards and briefs.</p>
      </div>
    </article>

    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-file-alt" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/executive-brief/">Executive Brief Template</a></h3>
        <p>Turn fuzzy threads into crisp, action-ready briefs with evidence links—designed for executive attention spans.</p>
      </div>
    </article>

    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-project-diagram" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/dataset-cards/">Dataset & Prompt Cards</a></h3>
        <p>Lightweight governance you can actually keep—structure, versions, and reproducible envs.</p>
      </div>
    </article>

    <article class="resource-mini">
      <div class="resource-mini__icon"><i class="fas fa-laptop-code" aria-hidden="true"></i></div>
      <div class="resource-mini__body">
        <h3><a href="/resources/streamlit-bridge/">Streamlit: DS to App, Without Drama</a></h3>
        <p>From notebook to interactive app in hours. Pragmatic guide, patterns, and gotchas.</p>
      </div>
    </article>
  </div>

    <p style="margin:.5rem 0 0 0.5rem;">
      <a class="browse-all" href="/resources/">Browse all resources</a>
    </p>
  </div>
  </details>
</div>. -->

<!-- TimelineJS of a Visual Timeline. (broad strokes) -->
<div class="home-section home-section--writing">
 <section class="journey-timeline">
<span id="journey-timeline" class="anchor"></span>
  <h2 class="journey-section-title" style="text-align:center; margin-top: 0px;">At-a-Glance: Education & Big Moves</h2>
  <p class="timeline-intro"  style="text-align:center; font-size: 0.9em;">
    Quick visual timeline of the milestones that shaped my path — from UT Austin and MIT to
    data science and consulting.
  </p>

  <div class="timeline-embed">
    <iframe
      src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=v2%3A2PACX-1vTIz_QSIlc25C50KKxKpS1T4ROr-09sgQP0L2cLQQsEAGvAjzHPWPyQgsT2avXiNAbONHEBKAWRK61Z&width=100%25&height=520&theme=https%3A%2F%2Fbarbhs.com%2Fassets%2Fcss%2Fbhs_timeline_debug.css"
      width="100%"
      height="520"
      frameborder="0"
      allowfullscreen
    ></iframe>
  </div>
  <p style="text-align:center; margin-top: 1rem;" >
    <a class="browse-all" href="/my-journey#journey-turns" aria-label="Read more at My Journey">
      Read more at My Journey
    </a>
  </p>
</section>
</div>

<!-- =======================
     Closing CTA — bookend the homepage with a warm invitation
     ======================= -->
<div class="home-section home-section--closer">
  <div class="home-closer">
    <p class="home-closer__body">
      Made it this far? If anything resonated — a project, a principle, a half-finished thought — I'd love to hear from you.
    </p>
    <p class="home-closer__actions">
      <a class="btn btn--primary home-closer__btn" href="/contact/">Say hi <i class="fas fa-paper-plane" aria-hidden="true"></i></a>
    </p>
  </div>
</div>

<!-- {% include section_tiles.html exclude="/contact/" %} -->

<style>
/* Add hover effects for principle cards */
.principle-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
}

/* Ensure resource mini icons align with cognitive theme */
.resource-mini__icon {
  color: #4a90e2;
}

/* Add subtle animation to the cognitive principles section */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.principle-card {
  animation: fadeInUp 0.6s ease-out;
}

.principle-card:nth-child(2) {
  animation-delay: 0.1s;
}

.principle-card:nth-child(3) {
  animation-delay: 0.2s;
}

.home-section--writing {
  background: #f9fbfd;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.75rem;
}

/* Shared centered heading + subheading — applies to Featured Writing and Featured Projects so they read as a pair */
.home-section--writing .home-section__heading,
.home-section--projects .home-section__heading {
  margin-top: 0;
  text-align: center;
}

.home-section--writing .home-section__subheading,
.home-section--projects .home-section__subheading {
  margin: 0.5rem auto 1.5rem;
  max-width: 680px;
  text-align: center;
  color: #6b7280;
}

/* Featured Projects mirrors Writing's outline + internal rhythm, without the tinted background */
.home-section--projects {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.75rem;
  margin-bottom: 0.75rem; /* tighten the gap to Featured Writing — they're paired */
}

.home-section--writing {
  margin-top: 0.75rem;
}

/* Suppress the minimal-mistakes feature__wrapper bottom rule (the bar above Browse all projects) */
.home-section--projects .feature__wrapper {
  border-bottom: none;
}

.featured-projects__cta {
  text-align: center;
  margin: 1rem 0 0; /* match .featured-writing__cta's spacing */
}

.featured-writing {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
}

.featured-writing__card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  padding: 1.5rem;
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.06);
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.featured-writing__card h3 {
  margin: 0 0 0.5rem;
  line-height: 1.25;
}

.featured-writing__badge {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #4338ca;
  background: #e0e7ff;
  padding: 0.25rem 0.6rem;
  border-radius: 999px;
  width: fit-content;
  margin: 0 0 0.5rem;
}

/* =======================
   Homepage closer — warm bookend after the timeline
   ======================= */
.home-section--closer {
  margin: 1.5rem 0 0.25rem;
}

.home-closer {
  max-width: 720px;
  margin: 0 auto;
  text-align: center;
  padding: 1.25rem 1rem 0.25rem;
}

.home-closer__body {
  font-size: 1.15rem;
  line-height: 1.6;
  color: #374151;
  margin: 0 0 1.25rem;
}

.home-closer__actions {
  margin: 0;
}

.home-closer__btn {
  border-radius: 999px;
  padding-inline: 1.5rem;
}

.home-closer__btn i {
  margin-left: 0.4rem;
}

.featured-writing__badge--thinking {
  color: #7c3aed;
  background: #ede9fe;
}

.featured-writing__badge--tutorial {
  color: #0f766e;
  background: #ccfbf1;
}

.featured-writing__link {
  margin-top: auto;
  font-weight: 600;
}

.featured-writing__cta {
  text-align: center;
  padding: 1rem 0 0 0;
}

</style>
