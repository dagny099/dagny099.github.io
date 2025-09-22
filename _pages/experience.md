---
title: "Experience"
layout: single
classes: wide
permalink: /experience/
---

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

<script>
  const chips=[...document.querySelectorAll('.chip')];
  chips.forEach(c=>c.addEventListener('click',()=>{
    const val=c.dataset.value.toLowerCase();
    document.querySelectorAll('.role-card').forEach(card=>{
      card.style.display = (card.dataset.domain.toLowerCase()===val) ? '' : 'none';
    });
  }));
</script>
