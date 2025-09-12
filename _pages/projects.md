---
layout: single
title: Projects
permalink: /projects/
author_profile: false
toc: false
classes: wide
---

<div class="project-grid">
  {%- assign items = site.projects | sort: 'date' | reverse -%}
  {%- for p in items -%}
  <article class="project-card">
    <a class="project-card__media" href="{{ p.url | relative_url }}">
      {%- if p.teaser -%}
        <img src="{{ p.teaser | relative_url }}" alt="">
      {%- else -%}
        <div class="project-card__placeholder" aria-hidden="true">🧩</div>
      {%- endif -%}
    </a>
    <div class="project-card__body">
      <h3 class="project-card__title"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
      <p class="project-card__excerpt">
        {{ p.excerpt | default: p.summary | default: p.description | strip_html | normalize_whitespace | truncate: 160 }}
      </p>
    </div>
  </article>
  {%- endfor -%}
</div>
