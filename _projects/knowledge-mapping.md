---
layout: single
title: "Knowledge Network Mapping"
permalink: /projects/knowledge-mapping/
classes: [project, hero, wide]    
author_profile: false
read_time: false
# Optional: right rail ToC for the deep dive (auto-generates from headings)
toc: true
toc_sticky: true
order: 40

# taxonomy
tags: [knowledge-graph, cv]
stack: [Python, Neo4j, FastAPI]
status: WIP

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
      url: https://github.com/dagny099/beehive-tracker/
      class: "btn--primary"
    - label: "Read Docs"
      url: https://docs.barbhs.com/beehive-tracker/
      class: "btn--light-outline"

# For cards/site previews
excerpt: "Fifteen years after publishing a paper on visual attention, I got curious about where those ideas had traveled. One nostalgic afternoon of data exploration became a full-scale research archaeology project. Starting with a single paper, I watched my citation network grow to over 8,000 documents, then built machine learning models to predict which papers should be talking to each other but aren't. The results revealed hidden bridges between research communities that made me wonder how many breakthrough collaborations we're missing."
last_modified_at: 
# CTAs
url: /projects/beehive-tracker/
btn_label: "Project"
docs_url: https://docs.barbhs.com/beehive-tracker/
docs_label: "Docs"
---

## Problem
Apiary notes get trapped in photos and paper. Patterns (queen health, forage, pests) rarely make it into a system of record.

## Approach
- Extract EXIF + local weather; light CV to detect frames (brood, pollen, mite checks).
- Model as a graph: Hives, Inspections, Observations, Conditions.
- Friendly UI for queries (“show inspections before swarm events”).

## Impact
- Fewer missed signals, better seasonal prep, richer handoff notes.
