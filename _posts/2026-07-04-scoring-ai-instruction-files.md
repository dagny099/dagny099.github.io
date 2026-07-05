---
layout: post
classes: wide
title: "A Scoring System for AI Instruction Files"
subtitle: "My CLAUDE.md grew to 800 lines before I asked whether it was helping. A six-category framework gave me an answer — and cut the file by 150 lines."
date: 2026-07-04
last_modified_at: 2026-07-04
permalink: /blog/scoring-ai-instruction-files/
canonical_url: https://barbhs.com/blog/scoring-ai-instruction-files/
description: "A six-category, 100-point framework for evaluating CLAUDE.md, AGENTS.md, and .cursorrules files — with the before-and-after from scoring my own."
excerpt: "How do you know whether your AI instruction file is helping or hurting? I built a six-category scoring framework, ran my own 800-line CLAUDE.md through it, and cut 150 lines."
excerpt_display: true
tags: [claude-code, agents-md, cursorrules, AI, evaluation, documentation, developer-tools, LLM]
categories: [data-science]
toc: false
read_time: false
---

<p class="post-byline">
  By Barbara Hidalgo-Sotelo
  <span class="post-byline__sep">·</span>
  <time datetime="2026-07-04">July 4, 2026</time>
  <span class="post-byline__sep">·</span>
  6 min read
</p>

My CLAUDE.md file said "Last Updated: November 2025." The date was wrong. The file telling Claude Code how to work on my project was giving the AI false information about itself, and I only noticed by accident. If I couldn't keep one date field accurate, how was I going to maintain three AI configuration files across three different tools?

That small bug turned into a bigger question: how do you know whether your AI instruction file is helping or hurting? I couldn't find an answer anywhere, so I built a way to measure it.

## Three files, one project

The file in question belongs to ChronoScope, a project I've been building with Claude Code. It started as one CLAUDE.md. Then I added Cursor for quick UI tweaks, which wanted a .cursorrules file. Then the AGENTS.md convention came along, and adopting it seemed prudent.

Three configuration files, three tools, all describing the same project. Every refactor meant updating three files. And the CLAUDE.md kept growing: 400 lines, 600 lines, 800 lines. Every developer I compared notes with had a version of the same story, and none of us could say where the line was between thorough and bloated.

## What the research says about size

Anthropic's [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) gave me the first hard number: frontier models follow roughly 150–200 instructions with reasonable consistency, and Claude Code's own system prompt already accounts for about 50 of them.

My CLAUDE.md contained roughly 150 individual instructions. Add the baseline 50 and I was sitting at 200 — right at the ceiling.

Instruction count wasn't the only problem. Every line of the file is processed on every interaction, so size is a performance cost, not just a reading cost. And when I looked at what those lines actually contained — Plotly tooltip font sizes, pixel-perfect color codes — much of it wasn't AI instruction at all. It was design documentation disguised as AI instructions.

## The framework: six categories, 100 points

Since I couldn't find evaluation criteria for AI instruction files, I wrote my own. Six categories:

| Category | Points | What it measures |
|---|---|---|
| Structure & organization | 20 | Can the AI find information quickly? Clear sections? |
| Accuracy & currentness | 20 | Working examples, correct paths, no stale claims |
| Comprehensiveness | 20 | Architecture, security, troubleshooting covered |
| Actionability | 20 | Copy-paste examples, do/don't comparisons |
| Information balance | 10 | Right level of detail — neither sparse nor smothering |
| Usability for AI | 10 | Quick start, red flags, links out to deeper resources |

ChronoScope's CLAUDE.md scored 88/100. Four things cost it the twelve points:

- The wrong "Last Updated" date (−5, accuracy)
- An incomplete "Session State Management" stub (−3, comprehensiveness)
- No security guidance (−2, comprehensiveness)
- Overly detailed UI specifications (−2, balance)

What saved the score: a "Streamlit golden rules" section with copy-paste examples, a red-flags section telling the AI when to stop and ask, and a real troubleshooting section.

A B+ sounds fine until you see the breakdown. The value of scoring isn't the grade — it's that "make the file better" becomes a ranked to-do list: fix the accuracy problems first, complete the stub, then thin the UI section.

## Six things the scoring changed

**1. Conciseness is a performance property.** I had assumed more documentation meant better assistance. But every token is processed on every interaction, and most of my 800 lines were unnecessary most of the time. I moved the detailed Streamlit patterns to a separate STREAMLIT_BEST_PRACTICES.md and referenced it instead of duplicating it. The file went from 800 lines to 650 — about a fifth shorter — and Claude Code's responses got noticeably snappier without 150 lines of tooltip specifications to parse each time.

**2. Code style belongs to linters.** My file specified an 88-character line length, double quotes, and import ordering. That's what Black, Prettier, and ESLint are for — deterministic tools doing a deterministic job. All of it got replaced with one line: run `black .` before committing.

**3. Red flags prevent expensive assumptions.** When an AI assistant is unsure, it doesn't ask — it guesses confidently. I watched Claude Code make architectural decisions I never intended, because I had never told it when to stop. So the file now has an explicit section: stop and ask when requirements are vague, when multiple valid approaches exist, when a change touches the database schema or breaks an API. Of everything on this list, this section changed day-to-day work the most.

**4. Dates are promises you'll break.** The bug that started all this. "Last Updated" fields, "as of Q4" qualifiers, timestamped examples — they all rot, and a wrong date actively misleads a reader that takes the file at face value. I removed the date field entirely, changed literal timestamps in examples to descriptions like "ISO 8601 timestamp," and made review trigger-based (major architectural change) instead of calendar-based.

**5. Start at 50 lines, not 800.** The best sections of my CLAUDE.md were written after bugs, after friction, after the third time something went wrong the same way. The worst sections were written speculatively, before any of that. If I were starting today the whole file would be a quick start, an architecture sketch, a handful of critical rules, a troubleshooting list, and a pointer to deeper docs — and it would grow only when real friction demanded it.

**6. The framework doesn't care which tool you use.** CLAUDE.md, AGENTS.md, .cursorrules — the questions are identical. Is it accurate? Is it actionable? Is it comprehensive without being bloated? Does it help the AI work faster? These conventions are young and still moving; the evaluation criteria are more durable than any one file format.

## Score your own file

The five-minute version, no printout required:

1. **Count the lines.** Under 100 is probably too minimal. 100–500 is the healthy range. Past 500, start asking hard questions; past 800, the file is almost certainly working against you.
2. **Run the quick checks.** A "Last Updated" date? Remove it. Pixel-level UI specs? Move them to a design doc. Code style rules? Delegate to a linter. No security section? Add one. No red-flags section telling the AI when to ask? That's the first thing to write.
3. **Do the instruction math.** Estimate the individual instructions in your file and add roughly 50 for the tool's own system prompt. Over 200 total, and you're past what current models follow reliably — split detailed content into separate referenced files.

If you'd rather score properly, the full version is a free download: the [AI instruction file evaluation worksheet](/resources/ai-instructions-evaluation-worksheet/) — a two-page PDF with the 100-point scorecard on page one and the complete rubric on page two.

My own file, after the fixes: 650 lines, an estimated 94/100, no date fields left to lie to anyone.

## What's next

I'm applying the same framework to a second project — a React and Flask stack this time instead of Streamlit — to see which patterns hold when the tech changes: whether React work needs different instruction patterns, whether the instruction ceiling behaves the same across models, whether full-stack projects genuinely need longer files. I'll report back.

And I'd genuinely like to compare notes. How long is your instruction file? If you run it through the categories above, what score does it get, and where did the points go? Evaluation only gets interesting when there's more than one data point — that was true when I [ran 58 questions through two LLMs](/blog/twin-evaluate-models/), and it's true here.

## Sources

- [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) — Anthropic
- [How I use every Claude Code feature](https://blog.sshh.io/p/how-i-use-every-claude-code-feature) — Shrivu Shankar
- [Your first AI project attempt will be 95% garbage](https://www.sanity.io/blog/first-attempt-will-be-95-garbage) — Sanity.io
- [Keep your AGENTS.md in sync](https://kau.sh/blog/agents-md/) — Kaushik Gopal
