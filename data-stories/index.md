---
title: "Data Stories"
permalink: /data-stories/
layout: single
classes: wide
description: "Narrative, visual walkthroughs of real datasets, projects, and experiments."
redirect_from:
  - /data-stories.html
---


{% include section-header.html %}

<div class="content-shell data-stories-page">
  <div class="content-hero">
    <h1>Data Stories</h1>
    <p>Guided walkthroughs of real datasets, projects, and experiments—designed to read like narratives instead of dashboards.</p>
  </div>

  <!-- STORY CARDS GRID -->
  {% assign all_pages = site.pages | where_exp: "item", "item.url contains '/data-stories/'" %}
  {% assign data_stories = all_pages | where_exp: "item", "item.url != page.url" %}

  <div class="card-grid">
  {% for story in data_stories %}
    <article class="content-card">
      <h2>{{ story.title }}</h2>
      <p class="section-lead">{{ story.description }}</p>
      <a href="{{ story.url | relative_url }}" class="card-link">Read more →</a>
    </article>
  {% endfor %}
  </div>
</div>
