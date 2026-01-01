---
layout: archive
permalink: /snippets/
title: Tackboard
classes: wide
---

{% comment %}
Tackboard board view. Adjust headings or ordering if you want different sections.
{% endcomment %}

{% assign sorted_snippets = site.snippets | sort: "date" | reverse %}
{% assign garden_snippets = sorted_snippets | where: "status", "garden" %}
{% assign inbox_snippets = sorted_snippets | where: "status", "inbox" %}

<section class="snippets-board">
  <header class="snippets-board__header">
    <h2>Garden</h2>
    <p class="snippets-board__hint">Curated, distilled ideas ready for reuse.</p>
  </header>
  <div class="snippets-grid">
    {% for snippet in garden_snippets %}
      {% include snippet-card.html snippet=snippet %}
    {% endfor %}
  </div>
</section>

<section class="snippets-board">
  <header class="snippets-board__header">
    <h2>Inbox</h2>
    <p class="snippets-board__hint">Fresh captures waiting for synthesis.</p>
  </header>
  <div class="snippets-grid">
    {% for snippet in inbox_snippets %}
      {% include snippet-card.html snippet=snippet %}
    {% endfor %}
  </div>
</section>
