---
layout: archive
classes: wide
permalink: /snippets/
title: "Tackboard"
---

{% assign snippets = site.snippets | sort: "date" | reverse %}
{% assign garden_snippets = snippets | where: "status", "garden" %}
{% assign inbox_snippets = snippets | where: "status", "inbox" %}

<div class="snippets-board">
  <section class="snippets-section">
    <header class="snippets-section__header">
      <h2 class="snippets-section__title">Garden</h2>
      <p class="snippets-section__subtitle">Polished ideas ready to reuse.</p>
    </header>

    {% if garden_snippets.size > 0 %}
      <div class="snippets-grid">
        {% for snippet in garden_snippets %}
          {% include snippet-card.html snippet=snippet %}
        {% endfor %}
      </div>
    {% else %}
      <p class="snippets-empty">Nothing in the Garden yet. Promote an Inbox snippet when it feels ready.</p>
    {% endif %}
  </section>

  <section class="snippets-section">
    <header class="snippets-section__header">
      <h2 class="snippets-section__title">Inbox</h2>
      <p class="snippets-section__subtitle">Fresh captures waiting for synthesis.</p>
    </header>

    {% if inbox_snippets.size > 0 %}
      <div class="snippets-grid">
        {% for snippet in inbox_snippets %}
          {% include snippet-card.html snippet=snippet %}
        {% endfor %}
      </div>
    {% else %}
      <p class="snippets-empty">Inbox is clear. Add a new snippet to start the flow.</p>
    {% endif %}
  </section>
</div>
