---
layout: single
title: "Resources & Guides"
description: "Reusable templates, guides, briefs, and cheatsheets for building data– and cognition–aware systems."
permalink: /resources/
classes: [wide, resources-page]
author_profile: false
---

<div class="page-shell section-stack">
  <section class="soft-hero content-slab">
    <p class="eyebrow">Resources</p>
    <h1>Why These Resources Exist</h1>
    <p class="section-intro">Practical tools you can use today: <strong>checklists, crib sheets, and templates</strong> designed for scanning first, then download. Each one applies a cognitive principle to make your work clearer and more effective.</p>
  </section>

  <div class="content-slab">
    {% assign items = site.resources | sort: 'date' | reverse %}
    {% include cards_grid.html variant="resource" items=items image_key="teaser" compact=true %}
  </div>
</div>
