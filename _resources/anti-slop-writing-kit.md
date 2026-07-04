---
layout: single
title: "The Anti-Slop Writing Kit"
subtitle: "Get LLM writing help without the tell-tale AI rhetoric"
permalink: /resources/anti-slop-writing-kit/
excerpt: "A paste-in constraint block, a two-pass workflow, and a self-edit checklist for getting writing help from an LLM without the 'it's not X, it's Y' constructions and emphasis cues that give it away."
date: 2026-07-04
last_modified_at: 2026-07-04
tags: [writing, llm, prompts, editing]
categories: ["Working with AI"]
format: Kit
level: Beginner
toc: true
toc_sticky: true
toc_label: "In the kit"
---

LLM-assisted writing has a recognizable accent: the "it's not X, it's Y" contrast, the emphasis cue that announces importance instead of earning it, the three-adjective stack added for rhythm. I use these tools for my own drafts every day, so I built a kit to catch the accent before it ships. It has three parts: a constraint block you paste into any writing prompt, two practices that make the constraints actually work, and a checklist for auditing your own drafts.

## 1. The prompt addendum

Paste this into any writing-help prompt:

```text
WRITING CONSTRAINTS — read before drafting:

Default to concrete specifics over rhetorical moves. Whenever you're tempted
to reach for a contrast, an analogy, or an emphasis cue, reach for a real
detail, example, or mechanism instead.

- No "it's not X, it's Y" constructions or variants ("never X, but Y"; "isn't
  about X, it's about Y"; "the X isn't the point, the Y is"). If a contrast is
  truly needed, state the real thing directly, and at most once in the piece.

- Don't open by announcing background or credentials ("As a...", "Coming
  from...", "With my background in..."). Let expertise show through how the
  problem is analyzed, not through a label.

- No glib equivalence analogies ("it's exactly like...", "we've seen this
  movie before", "think of it as...") unless the comparison is precise and
  load-bearing. One real example beats one borrowed analogy.

- No emphasis cues that announce importance instead of earning it ("This is
  the part I'd underline", "The key point is", "Notice that...", "Make no
  mistake", "Here's the thing"). Cut them; let the sentence carry its own
  weight.

- No three-item adjective or clause stacks for rhythm ("fast, confident, and
  wrong"). Pick the one that's true.

- Don't milk a slogan. If a line sounds quotable, use it once and move on.

- Go easy on em-dashes, hedging filler ("it's worth noting", "to some
  extent"), and empty intensifiers ("truly", "really", "incredibly").

Voice: plain, direct prose with a real point of view. If a sentence could
appear in anyone's article on this topic, it's too generic — rewrite it as
something only I could have written.
```

## 2. Stronger than the addendum alone

**Add a positive voice anchor.** Negative constraints suppress the obvious tells but don't teach your cadence. Paste 200–300 words of your own past writing alongside the constraints: "Match the voice in this sample." Do both for real lift.

**Make it persistent.** Trim the addendum and put it in your writing style settings so it applies automatically without re-pasting. (In ChatGPT, the equivalent is custom instructions; in Claude, a style or project instructions.)

**Use two passes.** Generation and editing are different jobs. Draft first, then run a second prompt: "Audit this draft against the constraints and flag every violation with a specific fix." The audit pass catches what slips through generation.

## 3. The self-edit checklist

Run your own drafts against this before they ship:

- Search for "not ... it's" / "isn't ... it's" / "never ... but" — is each one earned, and is there more than one?
- Does the opening announce who I am instead of showing how I think?
- Any "it's exactly like / same as / think of it as"? Replace with a real example.
- Any "the key point / notice that / make no mistake / here's the thing"? Delete.
- Any three-adjective or three-clause stacks? Cut to one.
- Any quotable line restated or stretched into a paragraph? Use once, move on.
- Em-dash count: is each one doing real work, or just rhythm?
- The generic test: could any competent writer on this topic have written this sentence? If yes, make it specifically mine.
