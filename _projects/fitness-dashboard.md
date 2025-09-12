---
title: "Fitness Dashboard"
permalink: /projects/fitness-dashboard/
layout: single
classes: wide
category: ["Data Products & Interfaces","Analytics & Experimentation"]
tags: ["python","streamlit","plotly","dashboard","time-series","evaluation"]
role: "Data Scientist & Builder"
timeframe: "2024–2025"
stack: ["Python","Streamlit","Plotly","Pandas"]
status: "Active"
repo: "https://github.com/dagny099/your-fitness-repo"
docs: ""
teaser: /assets/images/fitness-card.jpg
---

**30‑second summary.** From CSV sprawl to weekly, explainable training insights—consistency metrics, pace deltas, and trend‑break detection drive better decisions than “just another chart.”

<details><summary><strong>Read the 2‑minute overview</strong></summary>

**Problem.** Scattershot workout exports made it hard to answer simple questions: *Am I getting faster? Where did training slip?*  
**Approach.** A Streamlit app that ingests exports, standardizes fields, classifies sessions (run/walk/hybrid), and surfaces weekly deltas and “what changed?” callouts.  
**Impact.** Clear trend views and consistency prompts improved adherence and pace.  
**Governance.** Reproducible env (Poetry/direnv), documented pipeline; data never leaves your machine.

</details>

### Deep dive
**Problem → Approach → Impact → Governance**  
- **Problem.** No feedback loop; manual spreadsheet gymnastics.  
- **Approach.** ETL + metrics (weekly aggregates, z‑score outlier nudges), clean UI components.  
- **Impact.** Faster insight cycle; more consistent training weeks.  
- **Governance.** Versioned configs, environment management, README with setup in under 5 minutes.

**Links.** [GitHub]({{ page.repo }}){% if page.docs %} · [Docs]({{ page.docs }}){% endif %}