---
title: "Beehive Tracker"
permalink: /projects/beehive-tracker/
layout: single
classes: wide
category: ["Data Products & Interfaces","Graphs & Knowledge Systems"]
tags: ["python","streamlit","neo4j","computer-vision","weather","knowledge-graph"]
role: "Data Scientist & Builder"
timeframe: "2024–2025"
stack: ["Python","Streamlit","Neo4j","OpenCV","Weather API"]
status: "Active"
repo: "https://github.com/dagny099/beehive-tracker/tree/main"
docs: "https://docs.barbhs.com/beehive-tracker/"
teaser: /assets/images/beehive-card.jpg
---

**30‑second summary.** EXIF + weather + CV → a living beekeeping knowledge base. Friendly UI atop a graph that connects photos, conditions, and hive events.

<details><summary><strong>Read the 2‑minute overview</strong></summary>

**Problem.** Photos and notes pile up with no structure; hard to learn from seasons.  
**Approach.** Extract EXIF, run light CV, enrich with weather, and store relationships in a graph for fast querying.  
**Impact.** Faster pattern‑finding (foragers, brood trends); better timing for interventions.  
**Governance.** Clear data model, exportable records, and documented provenance.

</details>

### Deep dive
- **Problem.** Unstructured observations ≠ actionable knowledge.  
- **Approach.** Pipeline from image → metadata → graph; timeline + filters UI.  
- **Impact.** Season‑over‑season learning; shareable insights.  
- **Governance.** Schema diagrams, versioned transforms, and environment setup.

**Links.** [GitHub]({{ page.repo }}) · [Docs]({{ page.docs }})