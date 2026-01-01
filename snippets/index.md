---
layout: archive
title: Tackboard
permalink: /snippets/
classes: wide
---

{% assign snippets_sorted = site.snippets | sort: "date" | reverse %}
{% assign garden_snippets = snippets_sorted | where: "status", "garden" %}
{% assign inbox_snippets = snippets_sorted | where: "status", "inbox" %}

<section class="snippet-board">
  <h2 class="archive__subtitle">Garden</h2>
  <div class="snippet-board__grid">
    {% for snippet in garden_snippets %}
      {% include snippet-card.html snippet=snippet %}
    {% endfor %}
  </div>
</section>

<section class="snippet-board">
  <h2 class="archive__subtitle">Inbox</h2>
  <div class="snippet-board__grid">
    {% for snippet in inbox_snippets %}
      {% include snippet-card.html snippet=snippet %}
    {% endfor %}
  </div>
</section>
