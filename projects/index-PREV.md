---
layout: single
title: "Projects"
permalink: /projects/
classes: wide
---
<style>
.cards{
  --gap: 1rem;
  display: grid;
  gap: var(--gap);
  grid-template-columns: 1fr;  /* Single column = full width rows */
}

@media (min-width: 768px) {
  .cards{
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  /* Grid on larger screens */
  }
}

/* Narrow cards: stack so both CTAs are always visible */
@media (max-width: 420px){
  .card--project .card__footer .cta-row{ grid-template-columns: 1fr; }
}

</style>

{% comment %}
Unified card grid over the `_projects` collection.
If your project docs include a teaser image, set `image_path:` (or `teaser:`) in each file.
This grid will show a nice placeholder if images are missing.

{% endcomment %}

{% assign items = site.projects | sort: 'order' | default: site.projects %}

{% include cards_grid.html variant="project" items=items image_key="image_path" cta_label="30-sec view"  %}
