---
layout: single
title: "Projects"
permalink: /projects/
classes: wide
---

{% comment %}
Unified card grid over the `_projects` collection.
If your project docs include a teaser image, set `image_path:` (or `teaser:`) in each file.
This grid will show a nice placeholder if images are missing.
{% endcomment %}

{% assign items = site.projects | sort: 'order' | default: site.projects %}
{% include cards_grid.html variant="project" items=items image_key="image_path" cta_label="30-sec view" %}
