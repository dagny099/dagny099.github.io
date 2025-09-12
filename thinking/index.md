---
layout: posts
title: "Thinking in Public"
permalink: /thinking/
classes: wide
---

<!-- Pinned canon posts: set `pin: true` in a post's front matter to include it here -->
{% assign pinned = site.posts | where: "pin", true | sort: "date" | reverse %}
{% if pinned.size > 0 %}
<div class="notice--primary">
  <strong>Canon</strong> — foundational essays I recommend starting with.
</div>
{% for post in pinned %}
- <a href="{{ post.url | relative_url }}">{{ post.title }}</a> <small>({{ post.date | date: "%b %Y" }})</small>
{% endfor %}
---
{% endif %}

<!-- The standard posts list will follow per `layout: posts` -->
