---
layout: archive
title: "     "
sitemap:
  priority: 1.0
  changefreq: weekly
author_profile: true
header: 
  overlay_image: "/assets/images/rock_mts_bw.jpg"
  opacity: 0.1
  # overlay_color: "#0090cb"

feature_row:
  - url: "/portfolio/"
    image_path: /assets/images/portfolio_thumbnail_desertMJ.jpg
    title: "Portfolio"
    excerpt: "Explore my collection of projects showcasing expertise in Data Science and AI, including web apps, data visualizations, and ML projects."
    btn_class: "btn--primary"
    btn_label: "Visit"
  - url: "/research/"
    image_path: /assets/images/model_img_th.jpg
    title: "Research"
    excerpt: "How do we search in familiar scenes? Insights into cognitive processing by studing spatial patterns in eye movements and relationship to memory."
    btn_class: "btn--primary"
    btn_label: "Visit"
  - url: "/blog/"
    image_path: /assets/images/resume_thumbnail_woman2.jpg
    title: "Blog"
    excerpt: "Thoughts and insights on data science, human behavior, and the technology that connects them. Content re-tagging in progress, updates soon."
    btn_class: "btn--primary"
    btn_label: "Visit"
---

{% include feature_row %}

<h3 class="archive__subtitle" style="margin: 0;">{{ site.data.ui-text[site.locale].recent_posts | default: "Recent Posts" }}</h3>

{% if paginator %}
  {% assign posts = paginator.posts %}
{% else %}
  {% assign posts = site.posts %}
{% endif %}

<!-- <p>Number of posts assigned: {{ posts | size }}</p> -->

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}">
<div style="font-size: 0.8em;">
  {% for post in posts limit: 5 %}
    {% include archive-single.html type=entries_layout %}
  {% endfor %}
</div>
</div>

{% include paginator.html %}
