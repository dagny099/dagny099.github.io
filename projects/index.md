---
title: "Projects"
description: "A portfolio of technical builds and cognitive science–informed systems, from AI evaluation tools to behavioral data platforms and knowledge graphs."
permalink: /projects/
classes: [wide, project-page]
---

<div class="page-shell section-stack">
  <section class="soft-hero">
    <p class="eyebrow">Portfolio</p>
    <h1>Systems That Think Like Humans Think</h1>
    <p class="card-lede">Applied cognitive science across data products, model evaluation tools, and knowledge graphs. Each build makes complex information easier to see, compare, and act on.</p>
    <!-- div class="meta-line">
      <span class="pill pill--accent">Shipping builds</span>
      <span class="pill">Behaviorally informed UX</span>
      <span class="pill">Evidence you can show</span>
    </div -->
  </section>

  <nav class="filter-nav" aria-label="Project filters">
    <button class="filter-chip" data-filter="all" aria-pressed="true">All projects</button>
    <button class="filter-chip" data-filter="perception" aria-pressed="false">Visual &amp; Perception</button>
    <button class="filter-chip" data-filter="memory" aria-pressed="false">Memory &amp; Organization</button>
    <button class="filter-chip" data-filter="attention" aria-pressed="false">Attention &amp; Focus</button>
    <button class="filter-chip" data-filter="learning" aria-pressed="false">Learning &amp; Adaptation</button>
  </nav>

  <section class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">🎯 Currently Shipping</p>
      <p class="section-intro">Active projects with live users. Each respects cognitive load and the way people actually scan, sort, and decide.</p>
    </div>

    <div class="project-grid">
      <article class="project-card" data-tags="perception,attention">
        <div class="project-card__heading">
          <h3 class="card-title">Fitness Intelligence Platform</h3>
          <span class="pill pill--accent">Behavioral Patterns</span>
        </div>
        <p class="card-lede">Production classifier that collapses 14 years of workouts into 3 cognitively usable categories.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Intensity bands that match how athletes self-label effort when distracted.</li>
          <li><strong>Tech:</strong> Python, AWS Lambda, MySQL, Streamlit.</li>
          <li><strong>Cognitive insight:</strong> The 7±2 rule becomes 3 workable buckets when cognitive load spikes.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/projects/fitness-dashboard/">Case study →</a>
          <a class="text-link" href="https://workouts.barbhs.com">Live demo →</a>
          <a class="text-link" href="https://github.com/dagny099/fitness-dashboard">GitHub →</a>
          <a class="text-link" href="https://docs.barbhs.com/fitness-dashboard/">Documentation →</a>
        </div>
      </article>

      <article class="project-card" data-tags="attention,learning">
        <div class="project-card__heading">
          <h3 class="card-title">Convoscope: Multi-Modal AI Comparison</h3>
          <span class="pill pill--accent">Model Evaluation</span>
        </div>
        <p class="card-lede">Side-by-side AI output comparison that caps choices to working memory limits, not vendor hype.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Progressive disclosure that defaults to 3 options, tolerates 5, and gracefully hides the rest.</li>
          <li><strong>Tech:</strong> Streamlit, OpenAI/Anthropic/Google APIs, PostgreSQL.</li>
          <li><strong>Cognitive insight:</strong> Horizontal comparisons reduce cognitive load versus scrolling long chat transcripts.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/projects/convoscope/">Case study →</a>
          <a class="text-link" href="https://convoscope.barbhs.com">Live demo →</a>
          <a class="text-link" href="https://github.com/dagny099/convoscope">GitHub →</a>
          <a class="text-link" href="https://docs.barbhs.com/convoscope/">Documentation →</a>
        </div>
      </article>

      <article class="project-card" data-tags="memory,perception">
        <div class="project-card__heading">
          <h3 class="card-title">Beehive Knowledge Graph</h3>
          <span class="pill pill--accent">Metadata Integration</span>
        </div>
        <p class="card-lede">Four years of photos turned into a queryable memory system that mirrors how beekeepers recall outcomes.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> 7 relationship types that match domain experts' mental models (weather → outcomes).</li>
          <li><strong>Tech:</strong> Neo4j, Google Cloud Vision, Python, Weather APIs.</li>
          <li><strong>Cognitive insight:</strong> Association-first navigation beats chronological browsing for decision recall.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/projects/beehive-tracker/">Case study →</a>
          <a class="text-link" href="https://beestory.barbhs.com">Live demo →</a>
          <a class="text-link" href="https://github.com/dagny099/beehive-tracker">GitHub →</a>
          <a class="text-link" href="https://docs.barbhs.com/beehive-tracker/">Documentation →</a>
        </div>
      </article>
    </div>
  </section>

  <section class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">🔬 Research &amp; Exploration</p>
      <p class="section-intro">Experiments where cognitive science theory meets model behavior and knowledge graphs.</p>
    </div>
    <div class="project-grid">
      <article class="project-card" data-tags="learning,memory">
        <div class="project-card__heading">
          <h3 class="card-title">Academic Citation Network Prediction</h3>
          <span class="pill">Knowledge Graph</span>
        </div>
        <p class="card-lede">Predicting missing citations across 8,000 papers to map what researchers notice—and overlook.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Attention-like link patterns in scholarly discovery surfaced via graph embeddings.</li>
          <li><strong>Tech:</strong> Graph Neural Networks, PyTorch, Neo4j, Semantic Scholar API.</li>
          <li><strong>Cognitive insight:</strong> Academic attention mirrors visual attention—predictable and bias-prone.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/data-stories/citation-link-prediction/">Data story →</a>
          <a class="text-link" href="https://cartography.barbhs.com">Live demo →</a>
          <a class="text-link" href="https://github.com/dagny099/citation-compass">GitHub →</a>
          <a class="text-link" href="https://docs.barbhs.com/citation-network/">Documentation →</a>
        </div>
      </article>
    </div>
  </section>

  <section class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">🧠 More Builds &amp; Evaluations</p>
      <p class="section-intro">Additional systems that translate cognition into better retrieval, summarization, and decision support.</p>
    </div>
    <div class="project-grid">
      <article class="project-card" data-tags="memory,attention">
        <div class="project-card__heading">
          <h3 class="card-title">ChronoScope: AI-Powered Timeline Builder</h3>
          <span class="pill">Temporal Extraction</span>
        </div>
        <p class="card-lede">Turns resumes and letters into interactive timelines with confidence scores so dates and events stay trustworthy.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Local-first document parsing plus validation that flags uncertain extractions.</li>
          <li><strong>Tech:</strong> Python, Streamlit, PyMuPDF, TimelineJS.</li>
          <li><strong>Cognitive insight:</strong> Time-based narratives help people anchor memory and spot gaps faster.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/projects/chronoscope/">Case study →</a>
          <a class="text-link" href="https://github.com/dagny099/chrono-scope">GitHub →</a>
          <a class="text-link" href="https://chronoscope-docs.github.io">Documentation →</a>
        </div>
      </article>

      <article class="project-card" data-tags="memory,learning">
        <div class="project-card__heading">
          <h3 class="card-title">Poolula Platform: RAG-Powered BI</h3>
          <span class="pill">RAG Evaluation</span>
        </div>
        <p class="card-lede">Natural-language BI with a built-in test harness so answers are measured before they're trusted.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Structured SQL answers blended with document citations and accuracy scores.</li>
          <li><strong>Tech:</strong> FastAPI, SQLModel, ChromaDB, Claude.</li>
          <li><strong>Cognitive insight:</strong> Trust emerges when evidence is surfaced alongside the response.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/projects/poolula-platform/">Case study →</a>
          <a class="text-link" href="https://github.com/dagny099/poolula-platform">GitHub →</a>
        </div>
      </article>

      <article class="project-card" data-tags="attention,learning">
        <div class="project-card__heading">
          <h3 class="card-title">CareerCraft: Job Application Assistant</h3>
          <span class="pill">Applied GenAI</span>
        </div>
        <p class="card-lede">Guides applicants through tailored cover letters with ATS gap analysis to reduce cognitive overload.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Iterative GPT prompts plus keyword scoring before applications go out.</li>
          <li><strong>Tech:</strong> Streamlit, OpenAI API, AWS EC2.</li>
          <li><strong>Cognitive insight:</strong> Progressive disclosure lets people focus on one improvement at a time.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/projects/careercraft/">Case study →</a>
          <a class="text-link" href="https://careercraft.barbhs.com">Live demo →</a>
          <a class="text-link" href="https://github.com/dagny099/assistant_author">GitHub →</a>
        </div>
      </article>
    </div>
  </section>

  <section class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">📚 Foundational Builds</p>
      <p class="section-intro">Earlier systems that shaped my approach to attention management, progressive disclosure, and information architecture.</p>
    </div>
    <div class="project-grid">
      <article class="project-card" data-tags="attention,learning">
        <div class="project-card__heading">
          <h3 class="card-title">IoT Temperature Sensor Fleet (2021)</h3>
          <span class="pill">Streaming Interfaces</span>
        </div>
        <p class="card-lede">Distributed sensor network that revealed how real-time data must be chunked for rapid comprehension.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Live readings organized by urgency, not chronology, to reduce alert fatigue.</li>
          <li><strong>Tech:</strong> Microcontrollers, MQTT, Python dashboards.</li>
          <li><strong>Cognitive insight:</strong> Progressive disclosure turns noisy streams into actionable signals.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/posts//temp-sensor-00/">6-part series →</a>
        </div>
      </article>

      <article class="project-card" data-tags="memory,learning">
        <div class="project-card__heading">
          <h3 class="card-title">Digital Portfolio Workshop Series (2024)</h3>
          <span class="pill">Information Architecture</span>
        </div>
        <p class="card-lede">Hands-on sessions that codified a repeatable IA for data portfolios.</p>
        <ul class="project-highlights">
          <li><strong>What you'll see:</strong> Reusable IA templates and GitHub Pages workflows that mirror how readers skim.</li>
          <li><strong>Tech:</strong> Jekyll, GitHub Pages, markdown-driven templates.</li>
          <li><strong>Cognitive insight:</strong> Chunked navigation and consistent widths reduce decision fatigue.</li>
        </ul>
        <div class="project-links">
          <a class="text-link" href="/posts/getting-started-with-github-pages/">Part 1 →</a>
          <a class="text-link" href="/posts/understanding-your-jekyll-site/">Part 2 →</a>
          <a class="text-link" href="/posts/deploy-jekyll-gh-actions/">Part 3 →</a>
          <a class="text-link" href="/posts/post-deployment-reflextions/">Part 4 →</a>
        </div>
      </article>
    </div>
  </section>

  <section class="soft-hero">
    <p class="eyebrow">The Cognitive Thread</p>
    <h2 class="card-title">Technology succeeds when it aligns with how humans naturally think.</h2>
    <p class="card-lede">Whether it's limiting options to reduce cognitive load, organizing knowledge by association, or chunking live data into usable groups—each build prioritizes how people perceive and decide.</p>
    <a class="text-link" href="/contact/">Let's connect →</a>
  </section>
</div>

<script>
  const filterButtons = document.querySelectorAll('.project-page .filter-chip');
  const projectCards = document.querySelectorAll('.project-page .project-card');

  function setFilter(key){
    projectCards.forEach(card => {
      const tags = (card.dataset.tags || '').split(',');
      const show = key === 'all' || tags.includes(key);
      card.classList.toggle('is-hidden', !show);
    });
  }

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const key = btn.dataset.filter;
      filterButtons.forEach(b => b.setAttribute('aria-pressed', b === btn));
      setFilter(key);
    });
  });

  setFilter('all');
</script>
