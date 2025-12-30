---
layout: posts
title: "Blog"
excerpt: "A writing index of tutorials, data stories, and thinking — organized so the full archive stays visible."
permalink: /blog/
header:
  opacity: "0.4"
  overlay_image: "/assets/images/flowers_02.jpg"
pagination: 
  enabled: true
---

<div class="page-shell section-stack">
  <section class="soft-hero content-slab">
    <p class="eyebrow">Writing Index</p>
    <p class="section-intro">This is the full writing archive — tutorials, data stories, and thinking in one place. Jump to a section, then scroll for the complete archive.</p>
    <nav class="meta-line writing-tabs" aria-label="Writing sections">
      <a class="pill pill--accent" href="#all-writing">All Writing</a>
      <a class="pill" href="#tutorials">Tutorials</a>
      <a class="pill" href="#data-stories">Data Stories</a>
      <a class="pill" href="#thinking">Thinking</a>
    </nav>
  </section>

  <section id="tutorials" class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">🧰 Tutorials</p>
      <p class="section-intro">Hands-on guides and build logs that show how the systems come together.</p>
    </div>
    {% assign tutorials = site.posts | where_exp: "item", "item.hidden != true" | sort: "date" | reverse %}
    <div class="cards-grid">
      {% for post in tutorials limit: 6 %}
        <article class="card-surface">
          {% if post.date %}
            <p class="card-meta">{{ post.date | date: "%b %Y" }}</p>
          {% endif %}
          <h2 class="card-title"><a class="text-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
          <p class="card-lede">{{ post.excerpt | strip_html }}</p>
          <a class="text-link" href="{{ post.url | relative_url }}">Read the tutorial →</a>
        </article>
      {% endfor %}
    </div>
    <p class="featured-writing__cta"><a class="browse-all" href="#all-writing">Browse the full archive ↓</a></p>
  </section>

  <section id="data-stories" class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">📊 Data Stories</p>
      <p class="section-intro">Narrative, visual walkthroughs of real datasets, experiments, and builds.</p>
    </div>
    {% assign all_pages = site.pages | where_exp: "item", "item.url contains '/data-stories/'" %}
    {% assign data_stories = all_pages | where_exp: "item", "item.url != '/data-stories/'" %}
    <div class="cards-grid story-grid">
      {% for story in data_stories %}
        <article class="card-surface">
          {% if story.date %}
            <p class="card-meta">{{ story.date | date: "%b %Y" }}</p>
          {% endif %}
          <h2 class="card-title"><a class="text-link" href="{{ story.url | relative_url }}">{{ story.title }}</a></h2>
          <p class="card-lede">{{ story.description | default: story.excerpt }}</p>
          <a class="text-link" href="{{ story.url | relative_url }}">Read the story →</a>
        </article>
      {% endfor %}
    </div>
    <p class="featured-writing__cta"><a class="browse-all" href="/data-stories/">View all Data Stories</a></p>
  </section>

  <section id="thinking" class="section-stack">
    <div class="section-heading">
      <p class="eyebrow">🧠 Thinking</p>
      <p class="section-intro">Essays on cognition, data systems, and AI governance.</p>
    </div>
    <div class="cards-grid thinking-grid">
      {% assign thinking_posts = site.thinking | sort: "date" | reverse %}
      {% for thought in thinking_posts limit: 6 %}
        <article class="card-surface">
          {% if thought.date %}
            <p class="card-meta">{{ thought.date | date: "%b %Y" }}</p>
          {% endif %}
          <h2 class="card-title"><a class="text-link" href="{{ thought.url | relative_url }}">{{ thought.title }}</a></h2>
          <p class="card-lede">{{ thought.excerpt | strip_html }}</p>
          <a class="text-link" href="{{ thought.url | relative_url }}">Read the essay →</a>
        </article>
      {% endfor %}
    </div>
    <p class="featured-writing__cta"><a class="browse-all" href="/thinking/">View all Thinking essays</a></p>
  </section>
</div>
