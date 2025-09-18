---
layout: single
title: "Thinking in Public"
permalink: /thinking/
classes: wide
---

{% comment %}
Essays live in `_thinking/` (you've declared the collection in _config.yml).
We sort by date (newest first) and render with the *post* card variant.
{% endcomment %}

{% assign thinking_docs = site.thinking | sort: "date" | reverse %}

{% assign pinned = thinking_docs | where: "pin", true | sort: "date" | reverse %}
{% if pinned.size > 0 %}
<div class="notice--primary"><strong>Canon</strong> — foundational essays I recommend starting with.</div>
<ul>
{% for post in pinned %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>({{ post.date | date: "%b %Y" }})</small></li>
{% endfor %}
</ul>
<hr/>
{% endif %}

{% include cards_grid.html variant="post" items=thinking_docs %}
