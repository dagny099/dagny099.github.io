---
layout: posts
title: "Data Science posts by Tags"
permalink: /data-science/
header:
  image: "/assets/images/gunnison-photo-01.jpg"
---
<!--- This is an HTML comment in Markdown

{% include base_path %}
{% include group-by-array collection=site.posts field="tags" %}

{% for tag in group_names %}
  {% assign posts = group_items[forloop.index0] %}
  <h2 id="{{ tag | slugify }}" class="archive__subtitle">{{ tag }}</h2>
  {% for post in posts %}
    {% include archive-single.html %}
  {% endfor %}
{% endfor %}

 -->