---
layout: single
title: "Resources & Guides"
permalink: /resources/
classes: wide
author_profile: false
---

Useful, printable things: **crib sheets, checklists, templates,** and lightweight starters.  
Everything here is designed for scanning first, then download.

{% assign items = site.resources | sort: 'date' | reverse %}
{% include cards_grid.html variant="resource" items=items image_key="teaser" compact=true %}
