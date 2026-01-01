---
layout: archive
classes: wide
title: Tackboard Snippets
permalink: /snippets/
---

{% assign sorted_snippets = site.snippets | sort: "date" | reverse %}
{% assign garden_snippets = sorted_snippets | where: "status", "garden" %}
{% assign inbox_snippets = sorted_snippets | where: "status", "inbox" %}

<section class="snippets-board">
  <header class="snippets-board__header">
    <h2>Garden</h2>
    <p class="snippets-board__hint">Curated notes ready to reuse.</p>
  </header>

  <div class="snippets-grid" data-section="garden">
    {% for snippet in garden_snippets %}
      {% include snippet-card.html snippet=snippet %}
    {% endfor %}
  </div>
</section>

<section class="snippets-board">
  <header class="snippets-board__header">
    <h2>Inbox</h2>
    <p class="snippets-board__hint">Fresh captures waiting to be tended.</p>
  </header>

  <div class="snippets-grid" data-section="inbox">
    {% for snippet in inbox_snippets %}
      {% include snippet-card.html snippet=snippet %}
    {% endfor %}
  </div>
</section>
