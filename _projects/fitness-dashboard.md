---
layout: single
title: "Self-Hosted Workout Intelligence"
permalink: /projects/fitness-dashboard/
classes: [project, hero, wide]    
author_profile: false
read_time: false
# Optional: right rail ToC for the deep dive (auto-generates from headings)
toc: true
toc_sticky: true
order: 10

# taxonomy
tags: [analytics, habits]
stack: [Python, Pandas, Altair]      # optional 
status: Active

# Make the header a true hero
header:
  # card image used on /projects/ (and any archive grids)
  teaser: /assets/images/projects/hivetracker/card.jpg

 # banner image for the big hero at the top of the page
  overlay_image: /assets/images/projects/hivetracker/hero.jpg   # swap in a real banner
  overlay_filter: 0.25
  caption: "A little bit of metadata can go a long way"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/fitness-dashboard/
      class: "btn--primary"
    - label: "Read Docs"
      url: https://docs.barbhs.com/fitness-dashboard/
      class: "btn--light-outline"

# For cards/site previews
excerpt: 'For years, I meticulously tracked every run. Metrics are, of course, paramount to a former athlete and current data scientist. But a puppy landing on my doorstep transformed my exercise world overnight. What started as pristine running data became (an irritainingly unlabeled) mix of actual runs but more frequent dog walks. It’s spurned my quest to make my exercise data meaningful again. From developing classification models to distinguish runs from walks and dashboards to explore how adding a four-legged training partner redefined what "consistency" actually means, this exploration of *the Choco effect* is an open field of study 🐕'
last_modified_at: 
# CTAs
url: /projects/fitness-dashboard/
btn_label: "Project"
docs_url: https://docs.barbhs.com/fitness-dashboard/
docs_label: "Docs"
---

## Problem
I had scattered CSVs and subjective training notes. No single weekly view, no trend break detection, and no way to keep promises to “future me.”

## Approach
- Normalize inputs into a tidy model (sessions, metrics, deltas).
- Compute **consistency** and **trend-breaks** with transparent rules.
- Human-centered visuals that emphasize *decisions* rather than dashboards.

## Impact
- Weekly ritual, not a one-off report.
- Early warning on form/volume changes.
- Reduced decision debt and easier experimentation.
