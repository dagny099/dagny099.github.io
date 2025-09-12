---
title: "Resources & Guides"
permalink: /resources/
layout: single        # <- key: uses the archive template
author_profile: false         # no sidebar; gives the grid full width
classes: resources            # lets us target styles for this page
sort_order: reverse
sort_by: date
toc: false
---
Useful, printable things: **crib sheets, checklists, templates,** and lightweight starters.  
Everything here is designed for scanning first, then download.

<div class="resource-grid">
{% assign items = site.resources | sort: 'order' %}
{% for r in items %}
  <article class="resource-card">
    <a class="resource-card__media" href="{{ r.url | relative_url }}">
      {% if r.teaser %}
        <img src="{{ r.teaser | relative_url }}" alt="{{ r.title | escape }}">
      {% else %}
        <div class="resource-card__placeholder" aria-hidden="true">
          <i class="fas {{ r.icon | default: 'fa-file-alt' }}"></i>
        </div>
      {% endif %}
    </a>
    <div class="resource-card__body">
      <h3 class="resource-card__title">
        <a href="{{ r.url | relative_url }}">{{ r.title }}</a>
      </h3>
      {% if r.excerpt %}<p class="resource-card__desc">{{ r.excerpt }}</p>{% endif %}
      <div class="resource-card__meta">
        {% if r.category %}<span class="resource-pill">{{ r.category }}</span>{% endif %}
        {% if r.level %}<span class="resource-pill">{{ r.level }}</span>{% endif %}
        {% if r.format %}<span class="resource-pill">{{ r.format }}</span>{% endif %}
      </div>
    </div>
  </article>
{% endfor %}
</div>
