---
layout: single
title: "AI Instruction File Evaluation Worksheet"
subtitle: "Score your CLAUDE.md, AGENTS.md, or .cursorrules in ten minutes"
permalink: /resources/ai-instructions-evaluation-worksheet/
excerpt: "A two-page printable worksheet for scoring AI assistant instruction files: a six-category, 100-point scorecard on page one, the full rubric on page two."
date: 2026-07-04
last_modified_at: 2026-07-04
tags: [claude-code, agents-md, cursorrules, evaluation, documentation, AI]
categories: ["Working with AI"]
format: Worksheet
level: Intermediate
header:
  teaser: /assets/images/resources/ai-instructions-evaluation-worksheet-teaser.png
download_url: /assets/resources/worksheet_ai_instruction_files.pdf
---

Every AI coding tool now wants a configuration file — CLAUDE.md, AGENTS.md, .cursorrules — and none of them tells you whether yours is helping or hurting. Mine grew to 800 lines before I asked. This worksheet is the measuring tool I built to answer that question, packaged so you can run it on your own file in about ten minutes.

Two pages:

- **Page 1 — the scorecard.** Six categories, 100 points, with score boxes to fill in by hand: structure, accuracy, comprehensiveness, actionability, information balance, and usability for AI. Below it, five quick checks that catch the most common problems (stale dates, linter rules, missing red flags) and the instruction math — your file's instruction count plus the tool's ~50 baseline, against the ~200 that current frontier models follow reliably.
- **Page 2 — the rubric.** What earns points and what costs them in each category, so a 14/20 means the same thing next month as it does today.

{% include resource/buttons.html %}

The grade matters less than the deductions. Write them in the margin and they become a ranked to-do list: accuracy problems first, then comprehensiveness, then balance. When I scored my own 800-line CLAUDE.md it came out 88/100, and fixing the deductions in that order cut the file by 150 lines.

The full story — where the framework came from, what the research says about instruction limits, and the six things scoring changed about how I write these files — is in [A Scoring System for AI Instruction Files](/blog/scoring-ai-instruction-files/).
