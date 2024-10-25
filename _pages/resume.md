---
title: "Resume"
permalink: /resume/
header:
  overlay_image: "/assets/images/rock_mts_lake_reflections.jpg"
---
## Summary
{{ site.data.resume.summary }}

## Skills
{% for skill in site.data.resume.skills %}
- **{{ skill | first }}**: {{ skill | last }}
{% endfor %}

## Experience
{% for job in site.data.resume.experience %}
### {{ job.role }} at {{ job.company }}
**{{ job.period }}**
{% for responsibility in job.responsibilities %}
- {{ responsibility }}
{% endfor %}
{% endfor %}

## Education
{% for edu in site.data.resume.education %}
- **{{ edu.degree }}** – {{ edu.institution }}
{% endfor %}

## Certifications
{% for cert in site.data.resume.certifications %}
- {{ cert }}
{% endfor %}
