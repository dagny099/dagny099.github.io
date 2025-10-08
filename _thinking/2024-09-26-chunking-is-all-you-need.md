---
layout: single
title: "7+-2 is Everywhere: Chunking is all you need"
date: 2025-09-11 00:00:00 -0600
categories: ["thinking"]
tags: ["visual-working-memory","data-visualization","visual-attention","ux-for-analytics"]
pin: true
toc: true
toc_sticky: true
classes: wide
excerpt_separator: "<!--more-->"
# Cards metadata
read_time: 7
teaser: /assets/images/bees-hero.jpg
teaser_alt: "Beehive inspection photo with notes overlay"
# Route (safe even if config permalink isn't category-based)
permalink: /thinking/why-dashboards-fail/
# Hero header (kept)
header:
  overlay_image: /assets/images/bees-hero.jpg
  overlay_filter: 0.45
---

*Long-context models can hold a million tokens. People can’t. The bottleneck has shifted from storage to sensemaking. Across 2,593 workouts, 400+ beehive inspections, and an AI comparison UI, the same pattern repeats: we act effectively when we see three to seven meaningful chunks.*


## Bigger windows, same bottleneck: sensemaking

Long-context prevents truncation, but neither humans nor models weight the middle well. Primacy and recency dominate. The practical consequence: chunking and selective retrieval still win, and interfaces must respect human attention, not just token capacity.


## Evidence across three domains

### Fitness tracker, 14 years, 2,593 workouts

- Despite 10+ activity labels, unsupervised clustering snapped to three durable groups.
    - **Fast:** runs
    - **Slow:** walks
    - **Transition:** the brisk-walk-or-jog blur
- Result: The three clusters captured the useful distinctions while minimizing labeling overhead.
- Methods note: pace and cadence features, K-means with stability checks.
- Optional stat placeholder: three clusters explained **[X%]** of variance.

### Beehive monitoring, 4 seasons, 400+ photo-inspections

- Inspections naturally cluster into ~4-hour windows for coherent event arcs.
- Five weather variables do most explanatory work: temperature, humidity, wind, pressure, cloud cover.
- In the knowledge graph, seven edge types carried the workload for practical queries like “Inspections before swarms” and “Weather factors preceding queen loss.”
- Result: The long tail of edges existed, but decision-making lived in the top 3–7.
- Optional coverage placeholder: seven edge types covered **[Y%]** of production queries.

### Convoscope interface, multi-model comparison

- Ten side-by-side models looked impressive. Users skimmed the first row and quit.
- Three model cards with five front-and-center topic chips drove engagement. The rest lived behind “More.”
- Result: Clearer comparisons, faster judgment calls, better follow-through.
- Optional engagement placeholder: 3-way comparison increased **[Z%]** dwell time or click-through.

<aside>
💡

Design takeaway: Across domains, the effective unit of attention is three to seven meaningful chunks. Design for that bandwidth, then let experts expand.

</aside>

## What 7±2 actually says

Miller’s 1956 paper wasn’t “put seven items in your navbar.” It was about channel capacity and how we overcome it with chunking. The cargo-cult rule creates flat menus and laundry lists. The correct application is to reduce extraneous cognitive load with chunking and progressive disclosure.

## Designing for the edges

Primacy and recency shape what’s noticed and remembered. Put the key idea and the next action at the edges: lead with the constraint and close with the success criterion. In dashboards, preattentive cues within ~200ms determine what gets seen.

- One message per chart.
- Three to five charts per dashboard.
- More? Paginate or tab it.

## Three design rules that actually matter

### 1) Chunk by purpose, not number

- Why: Purpose-driven groupings lower cognitive load and speed decisions.
- Ship it tomorrow: Group around the user’s decision. For a release review, organize by “Go” “Risk” “Blockers,” not by eleven KPIs.

### 2) Respect the edges

- Why: First and last positions earn disproportionate attention.
- Ship it tomorrow: Front-load constraints and context. End with the success check and action. For prompts, state guardrails first, acceptance test last.

### 3) Progressive disclosure

- Why: Start with three, expand toward seven, hide the long tail.
- Ship it tomorrow: Show 3–5 candidate answers or tiles by default. Tuck the rest behind “More” with filters and drill-ins.

## Why million-token windows still hit the same wall

- Models, like humans, show “lost in the middle” patterns. Bigger contexts reduce truncation pain but do not erase selective attention.
- Enterprise-scale artifacts exceed even large windows. Selective retrieval, summarization, and hierarchical chunking remain dominant strategies.
- The bottleneck moved from “can the model hold this?” to “can a person use what comes back?”

## Closing

The interface is the new context window. My projects keep surfacing the same constraint. 2,593 workouts collapse to three clusters. Beehive queries ride on seven edges. Three-way model comparison works best. The next leap forward won’t be bigger context windows. It will be **designing for sensemaking**: chunk by purpose, respect the edges, and let experts expand. 

## Quick stats

- Long-context is here: **128K to ~1M tokens** in production settings.
- Attention is non-uniform: primacy and recency dominate over middles.
- Selective retrieval beats brute force: write, select, compress, isolate.

<!--

## Figures and captions

1) Edge-weighted attention

- A horizontal bar with darker left and right edges, faded center.
- Caption: “Primacy and recency for humans and LLMs.”

2) Domain triptych

- Left: Pace vs cadence scatter with 3 colored clusters.
- Middle: Mini network with 7 labeled edge types, long tail grayed out.
- Right: Convoscope wireframe with 3 model cards and 5 tag chips, “More” folded.

3) Before/after microframes

- “10 model cards” vs “3 cards + More.” Mark the latter with a check.

4) Rule cards (three side-by-side)

- Title: 5 words max. One-sentence why. One-sentence how-to.
-->
---

## References (for the web version)

- “Lost in the Middle” long-context research
- George A. Miller (1956), “The Magical Number Seven, Plus or Minus Two”
- Cognition and dashboard glanceability literature
- Practical RAG and context-engineering guides

---

## Author note

I build data tools and interfaces where cognitive science meets practice. If you have counterexamples where more than seven items improved outcomes, I’d love to analyze the hierarchy that made it work.