---
layout: single
title: "Resources & Guides"
permalink: /resources/
classes: wide
author_profile: false
---

## Resources Built on Cognitive Science

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); 
            padding: 2rem; border-radius: 12px; margin-bottom: 2rem;">
  <h3 style="margin-top: 0;">Why These Resources Exist</h3>
  <p>After 15+ years studying how humans process information—from MIT eye-tracking 
  labs to production dashboards—I've built tools that apply cognitive principles to 
  real data challenges. These aren't just templates. They're cognitive tools that 
  respect how humans actually think, attention works, and memory organizes information.</p>
  
  <p><strong>Each resource is tagged with the cognitive principle it applies:</strong></p>
  <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
    <span style="background: white; padding: 0.5rem 1rem; border-radius: 20px;">
      👁️ Perception & Visual Processing
    </span>
    <span style="background: white; padding: 0.5rem 1rem; border-radius: 20px;">
      🧠 Working Memory & Cognitive Load
    </span>
    <span style="background: white; padding: 0.5rem 1rem; border-radius: 20px;">
      🔄 Pattern Recognition
    </span>
    <span style="background: white; padding: 0.5rem 1rem; border-radius: 20px;">
      📊 Information Architecture
    </span>
  </div>
</div>

[Then keep your existing resources but add cognitive tags to each]

Useful, printable things: **crib sheets, checklists, templates,** and lightweight starters.  
Everything here is designed for scanning first, then download.

{% assign items = site.resources | sort: 'date' | reverse %}
{% include cards_grid.html variant="resource" items=items image_key="teaser" compact=true %}

