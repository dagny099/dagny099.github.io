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
  <span class="hero-headline">
    The best systems don't just work.<br>They make sense.
  </span>

  <span class="hero-subheadline">
  I build AI and data systems — and help teams adopt them — so complex work becomes easier to understand, verify, and trust.
  </span>

  <span class="hero-ctas hero-ctas--centered">
    <a class="btn hero-btn hero-btn--ghost" href="/contact/">
      Let's Connect &nbsp;<i class="fas fa-paper-plane"></i>
    </a>
  </span>

header:
  overlay_image: /assets/images/hero-banner.png
  overlay_filter: "rgba(12, 31, 27, 0.2)"   # rgba string — your include's gradient branch
  overlay_color: "#124B42"                   # fallback while image loads
  caption: Applied AI · Knowledge Systems · Strategy & Adoption · MIT PhD in Cognitive Science
  profile_image: /assets/images/biopic/bhs-new-headshot-v1.png

# Updated project descriptions with cognitive angles
feature_row:
  - image_path: /assets/images/teasers/proj-fitness-v1-1024x768.jpg
    alt: "Fitness Dashboard"
    title: "Self-Hosted Workout Intelligence"
    excerpt: >
      <strong>14 years of workouts. One classifier. Every conclusion shows its work.</strong><br><br>
      When my running history collided with daily dog walks, everything got logged as a "run" —
      including the 30-minute sniff safaris. So I built the full pipeline
      (CSV export → <i class="fab fa-aws"></i> Lambda → <i class="fas fa-database"></i> MySQL → Streamlit)
      with an ML classifier that tells real runs from walks.
      <br><br>
      <em>The part I'd defend in a design review: every insight is one click away from exactly how it was calculated — confidence scores included.</em>
    url: /projects/fitness-dashboard/
    btn_label: "Project"
    docs_url: https://docs.barbhs.com/fitness-dashboard/
    docs_label: "Docs"

  - image_path: /assets/images/teasers/proj-cartographer-v1-1024x768.jpg
    alt: "Concept Cartographer"
    title: "Concept Cartographer"
    excerpt: >
      <strong>Chat and watch the conversation become a structured graph. </strong><br><br>
      Every turn, a single structured LLM call returns both the conversational answer and the
      extracted concepts and relationships, growing a map across the conversation.
      Over 30 nodes, new concepts must connect to an existing node — so it stays
      a map, not a junk drawer. Export a PNG image or copy the JSON into a graphDB.
      <br><br>
      <em>The part I'd defend in a design review: one call extracts narrative and ontology simultaneously — about half the latency and cost of the obvious two-call approach.</em>
    url: https://concept-cartographer.com/
    btn_label: "Live demo"
    docs_url: https://github.com/dagny099/concept-cartography-gradio
    docs_label: "Source"
   
  - image_path: /assets/images/teasers/proj-beehive-v1-1024x768.jpg
    alt: "Beehive Tracker"
    title: "Beehive Analytics Platform"
    excerpt: >
      <strong>Four years of hive photos, turned into a record I can actually query.</strong><br><br>
      The bees don't keep records. So <i class='fas fa-camera'></i> EXIF metadata, Google Cloud
      Vision, and <i class='fas fa-cloud-sun'></i> weather APIs turn my inspection photos into a
      knowledge graph with a query UI — when swarms happened, which seasons produced, what
      weather preceded trouble.
      <br><br>
      <em>The part I'd defend in a design review: a real multimodal pipeline — image metadata, vision API, color analysis, weather correlation — serving a craft I practice every week.</em>
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
        A 12-week curriculum turning RDF, OWL, SPARQL, and modern knowledge graphs into practical, project-based learning—with readable explanations and honest tradeoffs.
      </p>

      <p class="current-feature__actions" style="padding-bottom: 1rem;">
        <a class="btn btn--primary" href="https://curriculum.barbhs.com" target="_blank" rel="noopener">Explore the curriculum ↗</a>
        <a class="current-feature__secondary" href="https://curriculum.barbhs.com/modules/01-foundations/" target="_blank" rel="noopener">See Module 1 →</a>
      </p>

      <div class="current-feature__progression">
        <p class="current-feature__status">Currently on Module 1 of 4:</p>
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

    </div>

    <aside class="current-feature__thesis" aria-label="Thesis behind this series">
      <p class="current-feature__thesis-body">Some AI problems need probability. Some need structure. Good design begins with knowing the difference.</p>
      <p class="current-feature__thesis-aside">
        <!-- TODO: replace placeholder with real Buttondown subscribe URL once configured -->
        <a href="https://buttondown.com/barbarahs" target="_blank" rel="noopener">Get course updates →</a>
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
      <p class="duo-row__eyebrow">HOW I WORK</p>
      <h3 class="duo-row__title">Find the shared model</h3>
      <p class="duo-row__body">
        Before a team can automate a workflow, people need a common picture of the problem. I surface the language, assumptions, decisions, and constraints the architecture has to support.
      </p>
      <p class="duo-row__actions">
        <a class="duo-row__link" href="/my-journey/#cognitive-foundation">Read about my approach →</a>
      </p>
    </div>

    <div class="duo-row__card duo-row__card--twin">
      <p class="duo-row__eyebrow">Interactive</p>
      <h3 class="duo-row__title">Try my Digital Twin</h3>
      <p class="duo-row__body">
        Ask an AI grounded in my projects, writing, and frameworks. Use it to explore my work, unpack a difficult idea, or see how I reason through an ambiguous problem.
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
  color: #1B6B5E;
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
  background: #F6F3EC;
  border: 1px solid #E3DDD2;
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
  max-width: 720px;
  text-align: center;
  color: #5C5A53;
}

/* Featured Projects mirrors Writing's outline + internal rhythm, without the tinted background */
.home-section--projects {
  background: #ffffff;
  border: 1px solid #E3DDD2;
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
  border: 1px solid #E3DDD2;
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
  color: #124B42;
  background: #E2EFEA;
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
  color: #2E2C28;
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
  color: #B5503A;
  background: #F9E4DD;
}

.featured-writing__badge--tutorial {
  color: #1B6B5E;
  background: #E2EFEA;
}

.featured-writing__link {
  margin-top: auto;
  font-weight: 600;
}

.featured-writing__cta {
  text-align: center;
  padding: 1rem 0 0 0;
}

/* Hero headline hierarchy */
.page__hero--overlay .page__lead {
  max-width: 780px;
  margin-bottom: 0;
  font-size: 1rem;
}

.hero-headline {
  display: block;
  font-size: clamp(1.75rem, 2.4vw, 2.55rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
}

.hero-subheadline {
  display: block;
  max-width: 720px;
  margin-top: 0.75rem;
  font-size: clamp(1rem, 1.3vw, 1.2rem);
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.88);
}

.hero-ctas {
  display: block;
  margin-top: 1.35rem;
}

/* =======================
   Homepage rail alignment
   Align hero + body sections to the same visual grid
   ======================= */

:root {
  --home-rail-width: 1080px;
  --home-rail-gutter: 1.75rem;
}

.home .home-section {
  max-width: var(--home-rail-width);
  margin-left: auto;
  margin-right: auto;
}

/* Let the "Currently" and "How I work / Interactive" cards span the full
   1080px rail so they line up with Featured Projects/Writing (whose padding
   is internal). Without this they inherit .home-section's --page-edge inset
   and read ~96px narrower. */
.home .home-section--currently,
.home .home-section--duo {
  padding-inline: 0;
}

.home .page__hero--overlay .wrapper {
  max-width: var(--home-rail-width);
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--home-rail-gutter);
  padding-right: var(--home-rail-gutter);
}

@media (max-width: 900px) {
  .home .home-section,
  .home .page__hero--overlay .wrapper {
    max-width: none;
    margin-left: 1rem;
    margin-right: 1rem;
  }
}

</style>
