---
layout: post
classes: wide
title: "What I Learned Running 58 Questions Through Two LLMs"
subtitle: "A behavioral comparison of GPT-4.1 and Gemini 2.5 Flash inside my Digital Twin."
date: 2026-05-12
permalink: /blog/twin-evaluate-models/
header:
  overlay_image: "/assets/images/new-ml-ai-starter-flow.png"
  overlay_filter: 0.5
excerpt: "A 58-question behavioral comparison of GPT-4.1 and Gemini 2.5 Flash inside a Digital Twin reveals two distinct professional personalities—and a practical decision framework for when to use each."
excerpt_display: true

tags: [LLM, evaluation, digital-twin, RAG, AI, GPT-4, Gemini]
stack: [GPT-4.1, Gemini 2.5 Flash, Python, OpenAI API, Google AI]
categories: [data-science]

---

## Contents

1. [The setup](#the-setup)
2. [The two personalities](#the-two-personalities)
3. [The numbers that mattered](#the-numbers-that-mattered)
4. [When to use which model](#when-to-use-which-model)
5. [Where I'm being cautious](#where-im-being-cautious)
6. [What I'm doing next](#what-im-doing-next)

## The setup

I built a Digital Twin that visitors can talk to at [twin.barbhs.com](https://twin.barbhs.com). It runs on a small retrieval pipeline: a knowledge base of documents I wrote about myself, embedded into a vector store, retrieved per query, and handed to an LLM with a system prompt that sets the Twin's voice.

Once the pipeline was working, I wanted to know whether the choice of underlying model actually changes how the Twin feels to a visitor. So I built a 58-question evaluation set, covering biographical facts, project walkthroughs, methodology questions, and the kinds of open-ended questions a recruiter or technical peer might ask. Then I ran the same set against two models while holding everything else constant.

The models compared:

* GPT-4.1 (OpenAI)
* Gemini 2.5 Flash (Google)

Same retrieval setup, same top-k, same system prompt, same vector store, same temperature (0.6). Only the model varied.

## The two personalities

I expected one model to be cleanly better. What I found was that the two behaved like different kinds of professional. Both competent, but oriented toward different goals.

GPT-4.1 read like a portfolio guide. It set context, surfaced related projects without being asked, framed answers strategically, and invited the visitor to keep exploring. Asked how my cognitive science background informs my AI work, it built a short narrative arc connecting the two.

Gemini 2.5 Flash read like an efficient answer engine. Direct, accurate, especially good at bounded factual questions. Asked where I got my PhD, it just answered. No setup, no framing, no pivot to a related project.

Neither pattern is inherently better. They are suited to different jobs.

## The numbers that mattered

{% include figure image_path="/assets/images/llm-comparison-metrics.png" alt="Bar chart comparing GPT-4.1 and Gemini 2.5 Flash across response length, follow-up invitations, concept mentions, and cost" caption="Key behavioral metrics across 58 paired responses. GPT-4.1 is the conversational guide; Gemini 2.5 Flash is the efficient answer engine." class="align-right" %}

A few patterns stood out across the 58 paired responses.

* Average response length: GPT-4.1 was 225 words, Gemini was 181.
* Follow-up invitations (phrases like "happy to share more"): GPT-4.1 had 40, Gemini had 10.
* Project and concept mentions per response: GPT-4.1 averaged 1.93, Gemini 1.57.
* Full-sweep cost: GPT-4.1 cost about $0.49, Gemini about $0.18.

The follow-up gap is the one I find most consequential. For a public Twin where many visitors don't know what to ask next, an answer that ends with a specific suggestion is dramatically more useful than one that simply finishes.

The cost gap matters in the opposite direction. At roughly one third the cost per sweep, Gemini becomes the better choice for running the whole evaluation after a knowledge-base edit, just to confirm nothing broke.

The [full quantitative report](/compare-models/) covers per-question paired metrics, content-overlap diagnostics, and breakdowns by question category.

## When to use which model

The split I've landed on:

For the public Twin at twin.barbhs.com, the default is GPT-4.1. The richer framing and follow-up invitations are worth the extra cost when a recruiter or hiring manager is the visitor.

For regression sweeps after a knowledge-base change or system-prompt change, the default is Gemini 2.5 Flash. It's fast, cheap, and surfaces hallucinations just as reliably as the more expensive model.

The principle generalizes. Model choice isn't a single quality decision. It's a personality decision matched to a use case.

## Where I'm being cautious

A few things to flag before anyone overgeneralizes from this.

This was a model behavior comparison, not a human-scored bakeoff. The review CSVs include columns for accuracy, specificity, voice fidelity, and overall score, but I left them blank in this pass. I'm filling them in across a smaller, higher-value subset next.

The lexical coverage score I used is a smoke test, not a correctness measure. It checks whether the response touches required terms. It cannot tell me if the answer was true, well-framed, or in my voice.

Token counts across providers aren't directly comparable. Gemini reported more completion tokens despite shorter word counts. I treated word count and estimated dollar cost as the more interpretable measures.

Finally, longer doesn't always mean better. GPT-4.1's expansiveness helps on open-ended questions but can feel excessive on a simple factual one. The next round of prompt work will need response-mode rules by question type.

## What I'm doing next

Three things are on the list.

1. **A high-value subset.** I've chosen 15 of the 58 questions as the ones that most determine whether the Twin helps a visitor understand my work. Future evaluations will score these manually.

2. **A real rubric.** The six dimensions are accuracy, specificity, voice fidelity, strategic usefulness, grounding, and follow-up quality. The rubric structure is in the full report; the scores arrive in the next round.

3. **Response-mode rules.** Closed factual questions should stay concise. Project walkthroughs should carry a narrative arc. Recruiter questions should lead with value and follow with proof. The current prompt doesn't differentiate. The next version will.

---

*If you want to see the full paired comparison, including per-question diagnostics and the methodology behind the metrics, the [full quantitative report](/compare-models/) lives alongside this post.*
