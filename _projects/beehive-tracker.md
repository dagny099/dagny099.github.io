---
layout: single
title: "Beehive Tracker — A living knowledge base"
excerpt: "EXIF + weather + CV → structured apiculture insights; a friendly UI over a knowledge graph."
date: 2024-10-10
permalink: /projects/beehive-tracker/
# Visuals
teaser: /assets/images/teasers/beehive.jpg
teaser_alt: "Beehive and field notes"
# Meta (cards)
tags: [knowledge-graph, cv]
stack: [Python, Neo4j, FastAPI]
status: WIP
order: 20
# CTA
cta_label: "30-sec view"
cta_url: /projects/beehive-tracker/
---

## Problem
Apiary notes get trapped in photos and paper. Patterns (queen health, forage, pests) rarely make it into a system of record.

## Approach
- Extract EXIF + local weather; light CV to detect frames (brood, pollen, mite checks).
- Model as a graph: Hives, Inspections, Observations, Conditions.
- Friendly UI for queries (“show inspections before swarm events”).

## Impact
- Fewer missed signals, better seasonal prep, richer handoff notes.
