---
layout: single
title: "Resources & Guides"
description: "Reusable templates, guides, briefs, and cheatsheets for building data– and cognition–aware systems."
permalink: /resources/
classes: wide
author_profile: false
---

<div class="content-shell resources-page">
  <div class="content-hero">
    <h1>Resources & Guides</h1>
    <p>Practical tools for immediate use—checklists, crib sheets, and templates designed for scanning first, then download. Each one applies a specific cognitive principle to make your work clearer and more effective.</p>
  </div>

  {% assign items = site.resources | sort: 'date' | reverse %}
  {% include cards_grid.html variant="resource" items=items image_key="teaser" compact=true %}
  
</div>



