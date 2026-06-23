---
title: "Resources & Guides"
description: "Reusable templates, guides, briefs, and cheatsheets for building data– and cognition–aware systems."
permalink: /resources/
classes: [wide, resources-page]
author_profile: false
---

<div class="page-shell section-stack">
  <section class="soft-hero content-slab">
    <p class="eyebrow">Resources</p>
    <h1>Practical tools you can use today</h1>
    <p class="section-intro">Checklists, crib sheets, and templates — each built around a cognitive principle, designed to scan first and download in seconds.</p>
  </section>

  {% assign items = site.resources | sort: 'date' | reverse %}
  {% assign formats = items | map: 'format' | compact | uniq | sort %}

  <div class="content-slab">
    <div class="section-heading resource-toolbar">
      <p class="eyebrow">Downloadable tools</p>
      {% if formats.size > 1 %}
      <div class="resource-filters" id="resourceFilters" role="group" aria-label="Filter resources by type">
        <button type="button" class="rf-chip" data-format="all" aria-pressed="true">All</button>
        {% for f in formats %}
        <button type="button" class="rf-chip" data-format="{{ f | slugify }}" aria-pressed="false">{{ f }}</button>
        {% endfor %}
      </div>
      {% endif %}
    </div>

    {% include cards_grid.html variant="resource" items=items image_key="teaser" compact=true %}
    <p class="resource-empty" id="resourceEmpty" hidden>No resources match that type yet.</p>
  </div>

  {% include infographic-gallery.html %}
</div>

<script>
(function () {
  var bar = document.getElementById('resourceFilters');
  if (!bar) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.cards--resource .card'));
  var empty = document.getElementById('resourceEmpty');
  bar.addEventListener('click', function (e) {
    var btn = e.target.closest('button');
    if (!btn) return;
    bar.querySelectorAll('button').forEach(function (b) {
      b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
    });
    var f = btn.dataset.format;
    var shown = 0;
    cards.forEach(function (c) {
      var match = f === 'all' || c.dataset.format === f;
      c.classList.toggle('rf-hidden', !match);
      if (match) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
  });
})();
</script>
