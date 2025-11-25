---
title: "Data Stories"
permalink: /data-stories/
layout: single
classes: [wide, story-page]
description: "Narrative, visual walkthroughs of real datasets, projects, and experiments."
redirect_from:
  - /data-stories.html
---

<div class="page-shell section-stack">
  <section class="soft-hero content-slab">
    <p class="eyebrow">Data Stories</p>
    <h1>Evidence you can scroll</h1>
    <p class="section-intro">Narrative walkthroughs, visual demos, and experiments. Each story pairs the build with the cognitive principle it proves in the real world.</p>
  </section>

  {% assign all_pages = site.pages | where_exp: "item", "item.url contains '/data-stories/'" %}
  {% assign data_stories = all_pages | where_exp: "item", "item.url != page.url" %}

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
</div>
