---
title: "Experience"
layout: single
classes: wide
permalink: /experience/
header:
  overlay_color: "#1e3a5f"
  overlay_filter: 0.7
excerpt: "Detailed role history with highlights and technology tags."
---

<p style="text-align: center; margin-bottom: 1.5rem;">
  <a href="/my-journey/" style="color: #4a90e2;">← Back to My Journey</a> for the narrative version
</p>

<div id="filters" class="filters">
  <strong>Filter:</strong>
  {% assign domains = site.data.barbara_resume_golden.display.filters.domains %}
  {% for d in domains %}
    <button class="chip" data-filter="domain" data-value="{{ d }}">{{ d }}</button>
  {% endfor %}
</div>

<div id="roles">
  {% assign roles = site.data.barbara_resume_golden.experience %}
  {% for r in roles %}
    <article class="role-card" data-domain="{{ r.domains | first }}" data-tags="{{ r.tags | join: ' ' }}">
      <h3>{{ r.title }} — <span class="employer">{{ r.employer }}</span></h3>
      <p class="dates">
        {{ r.start_date }} → {{ r.end_date | default: "Present" }}
        {% if r.location %} • {{ r.location }}{% endif %}
      </p>
      <ul class="highlights">
        {% for h in r.highlights limit:3 %}<li>{{ h }}</li>{% endfor %}
      </ul>
      <div class="tags">
        {% for t in r.tags %}<span class="tag">{{ t }}</span>{% endfor %}
      </div>
    </article>
  {% endfor %}
</div>

<p style="text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e5e7eb; font-size: 0.9rem; color: #6c757d;">
  Curious about the data architecture powering this page?
  <a href="/resources/resume-data-schema/" style="color: #4a90e2; text-decoration: none;">View the JSON schema documentation →</a>
</p>

<script>
  const chips=[...document.querySelectorAll('.chip')];
  chips.forEach(c=>c.addEventListener('click',()=>{
    const val=c.dataset.value.toLowerCase();
    document.querySelectorAll('.role-card').forEach(card=>{
      card.style.display = (card.dataset.domain.toLowerCase()===val) ? '' : 'none';
    });
  }));
</script>
