---
layout: single
title: "Vision, Perception, and Data Viz for Decision‑Making — Designing for How People Actually See"
subtitle: "Leveraging preattentive processing and gestalt principles for perceptually efficient data visualization"
date: 2025-09-11 00:00:00 -0600
last_modified_at: 2025-01-15
categories: ["thinking"]
tags: ["perception","preattentive","gestalt","color","luminance","uncertainty","small-multiples","decision-support"]
excerpt: "Great charts aren't pretty; they're perceptually efficient. Use preattentive cues, luminance over hue, and small multiples to answer one question per view—with uncertainty visible. Design for decisions, not decoration."
pin: true
toc: true
toc_sticky: true
#classes: wide
# Cards metadata
read_time: 6
teaser: /assets/images/vision-hero.jpg
teaser_alt: "Perception diagram with luminance and small multiples"
# Route
permalink: /thinking/vision-perception-data-viz-decisions/
# Hero header (kept)
header:
  overlay_image: /assets/images/vision-hero.jpg
  overlay_filter: 0.45
---

**Abstract (30 sec).** Great charts aren’t pretty; they’re *perceptually efficient*. Use preattentive cues, luminance over hue, and small multiples to answer **one question per view**—with uncertainty visible. Design for decisions, not decoration.
<!--more-->

<details><summary><strong>Overview (2 min)</strong></summary>

- **Premise.** The visual system is fast but picky: some encodings “pop,” others require reading.  
- **Implication.** Encode what matters with **position, length, and luminance**; reserve color for grouping.  
- **Practice.** Ask a question; choose one visual grammar that answers it; show uncertainty; annotate the takeaway.

</details>

## 1) Preattentive features: what pops in ~200 ms
- **Fast channels:** position on a common scale, length, orientation, luminance contrast.  
- **Slower or risky:** area, angle, rainbow palettes.  
- **Rule of thumb:** make the *answer* live on a fast channel (e.g., position or length).

> Debug test: Blur the chart to 10–20 px. Does the pattern still read? If not, you’re over‑encoding.

## 2) Gestalt & grouping: help the eye chunk
- Use **proximity** and **similarity** (consistent hues/weights) to bundle related traces.  
- Leverage **enclosure** (light boxes) for subpanels instead of heavy gridlines.  
- Remove chart junk; emphasize data ink.

## 3) Color & luminance: show structure, not noise
- **Prefer luminance** steps for magnitude; **use hue** to label categories.  
- Avoid more than ~6 categorical hues; add **direct labels** to cut legend scanning.  
- Ensure dark‑mode and color‑blind safe contrasts.

## 4) Small multiples > everything in one plot
- If you’re answering **“how did X change across A, B, C?”**, show aligned **small multiples**.  
- Keep axes consistent; share zero baselines where meaningful; annotate the local story.

## 5) Uncertainty belongs on the page
- Use **bands, intervals, and counts**; avoid false certainty.  
- Summaries should say *“estimate ± interval”* rather than a single number.  
- Consider **scented** interactions (hover reveals data density or intervals).

## 6) Question‑first layout
**Write the question first**, then pick an encoding:

- “Are we improving week‑over‑week?” → aligned line charts with weekly deltas and a reference band.  
- “Which cohort underperforms?” → sorted bars with direct labels; highlight the cohort of interest.  
- “What changed after the intervention?” → pre/post small multiples with annotations.

## 7) A minimal style guide (copy/paste)
- Title answers the question; subtitle names scope and date window.  
- One highlight color; everything else gray.  
- Direct labels on endpoints; legends only when necessary.  
- Tight y‑axis bounds with clear zero handling; gridlines faint.  
- One **callout box** per chart: “So what?” in a sentence.

## 8) From notebook to product without tears
- **Spec** the view as *question → encoding → interaction → annotation*.  
- Add **unit tests** for transforms that feed charts (no silent data shifts).  
- Ship a **print‑safe** version (leaders still circulate PDFs).

---

### Downloadables (optional)
- “Question → Encoding” crib sheet (PDF)  
- Color & contrast checklist (PDF)  
- Small‑multiples starter (PNG templates)

**CTA.** Want the crib sheet? Email me and I’ll share the kit I use when building decision dashboards.
