---
layout: splash
classes: home
title: "Barbara Hidalgo-Sotelo, PhD"
author_profile: false
excerpt: >
  Exploring messy data, intelligent systems, and what it means to make meaning—through the lens of a cognitive scientist who builds things people actually use.

  <p class="hero-ctas hero-ctas--pinned">
  <a class="btn hero-btn hero-btn--primary" href="/projects/">View Projects</a>
  <a class="btn hero-btn hero-btn--ghost" href="/contact/">Contact</a>
  </p>

header:
  overlay_filter: 0.7;
  overlay_color: "#1e3a5f"
  caption: Austin, TX · Data Scientist · PhD Cognitive Science, MIT · Human-Centered AI · Explainable Systems

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
     How I Think Section (NEW)
     ======================= -->
<div class="home-section" style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); padding: 0.05rem; border-radius: 12px; margin: 0;">
  <h2 style="text-align: center; margin: 1rem;">🧠 How I Think About Data</h2>
  
  <div style="max-width: 850px; margin: 0 auto; text-align: center; line-height: 1.4;">
    <p style="font-size: 0.9em; margin-bottom: 1.5rem;">
      My <strong>MIT research on visual attention</strong> taught me that humans don't just see data—they construct meaning from patterns. <br><br>
      <b>I solve data problems through a cognitive lens</b>—across healthcare, federal consulting, and cloud platforms. These solutions aren't just technically sound, but designed with human cognition in mind: how attention functions, how memory organizes, and how understanding builds in layers.<br><br>      
      This cognitive approach shapes everything I build: from dashboards optimized for natural eye movements to ML systems that explain their reasoning, and data products that work the way humans think.
    </p>
    
    <div style="margin: 1rem;">
      <a href="/my-journey/#cognitive-foundation" class="btn btn--primary">Learn About My Approach</a>
     <!-- <a href="/thinking/why-dashboards-fail/" class="btn btn--light">Read: Why Dashboards Fail</a> -->
    </div>
  </div>
</div>

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
     Cognitive Principles (NEW)
     ======================= -->
<div class="home-section" style="margin: 3rem 0;">
  <h2 style="text-align: center; margin-bottom: 2rem;">Cognitive Principles in Practice</h2>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; max-width: 1000px; margin: 0 auto;">
    
    <div class="principle-card" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-left: 4px solid #4a90e2; text-align: center; transition: transform 0.3s;">
      <div style="font-size: 2.5rem; margin-bottom: 1rem;">👁️</div>
      <h3 style="color: #4a90e2; margin-bottom: 0.8rem;">Vision Drives Understanding</h3>
      <p style="color: #6c757d; margin-bottom: 1rem; min-height: 60px;">
        Design for scanning, not reading. Your brain decides what matters in 200ms.
      </p>
      <a href="/resources/visual-decision-making/" style="color: #4a90e2; text-decoration: none; font-weight: 500;">
        See the Perception Guide →
      </a>
    </div>
    
    <div class="principle-card" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-left: 4px solid #50c878; text-align: center; transition: transform 0.3s;">
      <div style="font-size: 2.5rem; margin-bottom: 1rem;">🧠</div>
      <h3 style="color: #50c878; margin-bottom: 0.8rem;">Attention is Limited</h3>
      <p style="color: #6c757d; margin-bottom: 1rem; min-height: 60px;">
        Use it wisely. Humans can track 7±2 things—design within this constraint.
      </p>
      <a href="/projects/convoscope/" style="color: #50c878; text-decoration: none; font-weight: 500;">
        See Convoscope Example →
      </a>
    </div>
    
    <div class="principle-card" style="background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-left: 4px solid #e17b47; text-align: center; transition: transform 0.3s;">
      <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔄</div>
      <h3 style="color: #e17b47; margin-bottom: 0.8rem;">Patterns Beat Numbers</h3>
      <p style="color: #6c757d; margin-bottom: 1rem; min-height: 60px;">
        Humans think in stories. Show the narrative, not just the statistics.
      </p>
      <a href="/projects/fitness-dashboard/" style="color: #e17b47; text-decoration: none; font-weight: 500;">
        See Fitness Story →
      </a>
    </div>
    
  </div>
</div>

<!-- =======================
     Resources & Guides
     ======================= -->
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
</div>

<!-- =======================
     What I'm Exploring (NEW mini section)
     ======================= -->
<div class="home-section" style="background: white; border: 1px solid #e9ecef; border-radius: 12px; padding: 2rem; margin: 2rem 0;">
  <h3 style="text-align: center; color: #495057; margin-bottom: 1.5rem;">🔬 Currently Exploring</h3>
  <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
    <span style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.95em;">
      AI Explainability
    </span>
    <span style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.95em;">
      Knowledge Graphs
    </span>
    <span style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.95em;">
      Human-AI Collaboration
    </span>
    <span style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.95em;">
      Attention Mechanisms in LLMs
    </span>
    <span style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.95em;">
      Data Product Design
    </span>
  </div>
  <p style="text-align: center; margin-top: 1.5rem; color: #6c757d;">
    Interested in discussing any of these? <a href="/contact/">Let's connect</a>
  </p>
</div>

{% include section_tiles.html exclude="/contact/" %}

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
</style>