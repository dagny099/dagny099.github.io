---
title: "Resources & Guides"
description: "A curated library: templates, cheatsheets, guides, visual explainers, and project artifacts for building data- and cognition-aware systems."
permalink: /resources/
classes: [wide, resources-page]
author_profile: false
---

<div class="page-shell section-stack">
  <section class="soft-hero content-slab">
    <p class="eyebrow">Resources</p>
    <h1>A working library</h1>
    <p class="section-intro">The reusable parts of how I build — templates and cheatsheets you can download, guides that explain the thinking, visual explainers, and live project artifacts. Organized so you can find something useful in under a minute. New to the site entirely? <a class="text-link" href="/start-here/">Start Here</a> is the guided tour.</p>
  </section>

  <div class="content-slab">
    <div class="section-heading">
      <p class="eyebrow">Start with these</p>
      <p class="section-intro">Three short pieces that show what this library is for: verifying AI systems instead of just trusting them.</p>
    </div>
    <div class="cards-grid">
      <article class="card-surface">
        <h2 class="card-title"><a class="text-link" href="{{ '/assets/downloads/missing-layer-two-reports.pdf' | relative_url }}">The integration test</a></h2>
        <p class="card-lede">One page, five questions. Pick one real AI-assisted workflow and ask: who owns the decision, what does it cost to run, what context does it need, what quality bar must it meet, and who can override the output? Unanswered questions here are integration problems, even when adoption looks strong.</p>
        <p><a class="text-link" href="/blog/missing-layer-ai-adoption-value/">From <em>The Missing Layer</em></a></p>
      </article>
      <article class="card-surface">
        <h2 class="card-title"><a class="text-link" href="/resources/what-is-a-harness-in-ai/">What does "harness" mean in AI?</a></h2>
        <p class="card-lede">A visual decoder for a loaded term. Evaluation harness, agent harness, readiness harness, judge harness, fuzzing harness — the same word carrying baggage from five technical traditions, sorted out on one page. The model gives the power; the harness makes that power usable.</p>
        <p><a class="text-link" href="/resources/what-is-a-harness-in-ai/">View the explainer</a></p>
      </article>
      <article class="card-surface">
        <h2 class="card-title"><a class="text-link" href="/resources/memory-is-more-than-storage/">Memory is more than storage</a></h2>
        <p class="card-lede">Humans and AI agents face the same design pressure: deciding what to keep, update, and let go. Useful memory needs selection, structure, retrieval, revision, and forgetting. A one-page map, with the four papers that shaped it.</p>
        <p><a class="text-link" href="/resources/memory-is-more-than-storage/">View the explainer</a></p>
      </article>
    </div>
  </div>

  {% include infographic-gallery.html %}

  {% assign items = site.resources | sort: 'date' | reverse %}
  {% assign formats = items | map: 'format' | compact | uniq | sort %}

  <div class="content-slab">
    <div class="section-heading resource-toolbar">
      <p class="eyebrow">Templates &amp; cheatsheets</p>
      <p class="section-intro">Downloadable tools, each built around a cognitive principle — designed to scan first and download in seconds.</p>
      {% if formats.size > 1 %}
      <div class="resource-filters" id="resourceFilters" role="group" aria-label="Filter resources by type">
        <button type="button" class="rf-chip" data-format="all" aria-pressed="true">All</button>
        {% for f in formats %}
        <button type="button" class="rf-chip" data-format="{{ f | slugify }}" aria-pressed="false">{{ f }}</button>
        {% endfor %}
      </div>
      {% endif %}
    </div>

    {% include cards_grid.html variant="resource" items=items image_key="teaser" compact=true %}
    <p class="resource-empty" id="resourceEmpty" hidden>No resources match that type yet.</p>
  </div>

  <div class="content-slab">
    <div class="section-heading">
      <p class="eyebrow">Guides &amp; explainers</p>
      <h2>The thinking behind the tools</h2>
      <p class="section-intro">Longer reads, grouped by what you're trying to do.</p>
    </div>

    <div class="cards-grid">
      <article class="card-surface">
        <h2 class="card-title">AI adoption &amp; knowledge systems</h2>
        <p class="card-lede">Why AI initiatives stall, and what makes knowledge legible enough to trust a system with it.</p>
        <ul>
          <li><a class="text-link" href="/blog/missing-layer-ai-adoption-value/">The Missing Layer</a> — why adoption outruns value</li>
          <li><a class="text-link" href="/blog/ai-literacy-judgment/">AI literacy is mostly judgment</a></li>
          <li><a class="text-link" href="/ai-pulse-q2-2026/">The quiet number in KPMG's AI Pulse Q2 2026</a></li>
          <li><a class="text-link" href="/blog/metadata-matters/">Metadata Matters</a></li>
          <li><a class="text-link" href="/thinking/bees-graphs-governance/">Bees, Graphs &amp; Governance</a></li>
          <li><a class="text-link" href="/thinking/rag-approaches-observations/">RAG approaches: field observations</a></li>
        </ul>
      </article>

      <article class="card-surface">
        <h2 class="card-title">Builder guides &amp; tutorials</h2>
        <p class="card-lede">Hands-on walkthroughs from real builds — reproducible, opinionated, tested on myself first.</p>
        <ul>
          <li><a class="text-link" href="/blog/three-readers-of-your-web-page/">The Three Readers of Your Web Page</a></li>
          <li><a class="text-link" href="/blog/implementing-structured-metadata-jekyll/">Structured metadata on a Jekyll site</a></li>
          <li><a class="text-link" href="/blog/taming-mermaid-diagrams/">How I Organized My Mermaid Life</a></li>
          <li><a class="text-link" href="/blog/poetry-of-python/">Reproducible Python environments with Poetry</a></li>
          <li><a class="text-link" href="/blog/aws-cli-tutorial-launch-rds-for-ec2-access/">Intro to the AWS CLI</a></li>
          <li><a class="text-link" href="/blog/deploy-jekyll-gh-actions/">GitHub Actions for Jekyll</a></li>
        </ul>
      </article>

      <article class="card-surface">
        <h2 class="card-title">Demos &amp; project artifacts</h2>
        <p class="card-lede">Live systems and the documentation that keeps them honest — the verification layer, in public.</p>
        <ul>
          <li><a class="text-link" href="https://twin.barbhs.com">The Digital Twin</a> — ask it about my work</li>
          <li><a class="text-link" href="/compare-models/">Comparing models for the twin</a></li>
          <li><a class="text-link" href="/graphrag-reference/">GraphRAG reference</a></li>
          <li><a class="text-link" href="/resources/resume-data-schema/">Resume data schema</a></li>
          <li><a class="text-link" href="/experience/">Experience JSON</a> — my resume as structured data</li>
          <li><a class="text-link" href="https://docs.barbhs.com">Docs portal</a> — project documentation hub</li>
        </ul>
      </article>
    </div>
  </div>
</div>

<script>
(function () {
  var bar = document.getElementById('resourceFilters');
  if (!bar) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.cards--resource .card'));
  var empty = document.getElementById('resourceEmpty');
  bar.addEventListener('click', function (e) {
    var btn = e.target.closest('button');
    if (!btn) return;
    bar.querySelectorAll('button').forEach(function (b) {
      b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
    });
    var f = btn.dataset.format;
    var shown = 0;
    cards.forEach(function (c) {
      var match = f === 'all' || c.dataset.format === f;
      c.classList.toggle('rf-hidden', !match);
      if (match) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
  });
})();
</script>
