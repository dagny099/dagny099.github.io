---
layout: single
title: "Is Your Knowledge Ready for AI?"
subtitle: "A short diagnostic for teams building AI on top of documents, workflows, decisions, and institutional memory"
permalink: /resources/knowledge-legibility-diagnostic/
excerpt: "Fifteen questions across five dimensions — findability, structure, provenance, ownership, and verification — to check whether your organizational knowledge is in good enough shape for AI to use and for humans to verify."
date: 2026-07-04
last_modified_at: 2026-07-04
tags: [knowledge-systems, ai-readiness, rag, evaluation, metadata]
categories: ["Knowledge Systems"]
format: Diagnostic
level: Beginner
toc: true
toc_sticky: true
toc_label: "The diagnostic"
download_url: /assets/resources/diagnostic_knowledge_legibility.pdf
---

Before an AI system can answer from your organization's knowledge, that knowledge has to be findable, structured, traceable, owned, and checkable. Most teams evaluate the model first. The model is usually fine. The documents, spreadsheets, tickets, and unwritten decisions underneath it are usually where the trouble starts.

This diagnostic is fifteen questions across those five dimensions. It takes about twenty minutes with the right people in the room, and it will tell you more about your AI readiness than a vendor demo will.

{% include resource/buttons.html %}

## Who this is for

- Teams exploring RAG, AI assistants, workflow automation, or internal knowledge tools
- Leaders whose AI pilot sounds promising in the demo but is hard to trust in practice
- Anyone who suspects the model isn't the real bottleneck

There's a companion to this diagnostic: [the integration test]({{ '/assets/downloads/missing-layer-two-reports.pdf' | relative_url }}) asks whether an AI-assisted *workflow* is ready — who owns the decision, who can override the output. This one asks whether the *knowledge underneath* that workflow is ready. They fail independently.

## How to use it

Pick one real workflow or knowledge domain — customer support answers, pricing rules, compliance procedures, engineering runbooks. Not "our knowledge" in general; one specific domain where you're considering AI.

Answer each question **yes**, **no**, or **not sure** for that domain. "Not sure" counts as a finding, and it's often the most useful one: it means nobody in the room knows, which is its own answer.

Answer honestly. Nobody scores this, and flattering answers only postpone the same discoveries to a more expensive stage.

## The five dimensions

### 1. Findability

*Can people and systems find the knowledge they need?*

Knowledge spread across Slack, email, Drive, Confluence, tickets, spreadsheets, and people's heads is invisible to a retrieval system — and half-invisible to your own team. If humans have to ask around to find the current answer, an AI will retrieve whichever version it happens to reach.

**Q1.** If a new teammate needed the current answer to a routine question in this domain — a policy, a rate, a procedure — could they find it without asking anyone?

**Q2.** Is there one agreed first place to look for this domain, or are there several plausible "sources of truth"?

**Q3.** When an answer changes, does the old version get retired or clearly marked — or does it stay findable alongside the new one?

**Weak signals:** the real answer lives in a long Slack thread; two teams maintain parallel spreadsheets; the wiki page everyone distrusts still ranks first in search.

### 2. Structure

*Is the knowledge in a form AI systems can use?*

Retrieval and reasoning work far better over knowledge with visible structure: named entities, consistent categories, explicit rules. Knowledge buried in prose, PDFs, screenshots, and threads forces the AI to reconstruct that structure on every query — and it will reconstruct it differently each time.

**Q4.** Could the core facts of this domain be laid out as a table, checklist, or set of rules without losing what matters?

**Q5.** Is the same concept called the same name everywhere it appears — or is it "customer" in one system, "account" in another, and "client" in the contract?

**Q6.** Are the decision rules written down as rules, or would someone have to reconstruct them from prose, screenshots, and old email threads?

**Weak signals:** the critical constraint exists only as a paragraph in a 40-page PDF; categories mean different things to different teams; the process diagram is a photo of a whiteboard from 2023.

### 3. Provenance

*Can you trace where knowledge came from?*

An AI answer is only checkable if it points back to a source, and a source is only trustworthy if you can tell who wrote it, when, and with what authority. Decisions that were made in a meeting and remembered rather than recorded have no provenance at all.

**Q7.** Pick a key document in this domain: can you tell who wrote it, when it was last updated, and whether it's still current?

**Q8.** If an AI answered a question from your documents today, could you trace that answer back to the specific passage that supports it?

**Q9.** When a significant decision gets made in this domain, is it recorded somewhere a person — or a system — could find it a year later?

**Weak signals:** documents with no date or author; drafts and finals living side by side; "we decided this in Q3" with nothing written down; approval status that exists only in someone's memory.

### 4. Ownership

*Who maintains the knowledge?*

Knowledge without an owner drifts. Outdated pages persist because deleting them is nobody's job; contradictions get resolved informally by whoever notices; maintenance happens after something breaks. An AI system makes this worse, because it surfaces the stale and contradictory material at scale — and when it does, someone has to be responsible for fixing the source.

**Q10.** For each major source in this domain, can you name the person responsible for keeping it current?

**Q11.** When two sources disagree, is there a defined way to resolve it — or does it depend on who notices and how much they care?

**Q12.** Has anything in this domain been updated in the last quarter for a reason other than something breaking?

**Weak signals:** the definitive doc was written by someone who left; "everyone" owns the wiki, so no one does; the AI pilot surfaced errors months ago and the sources still say the same thing.

### 5. Verification

*How would you know whether an AI answer is right?*

This is the dimension teams skip, and the one that determines whether anyone ends up trusting the system. Without known-correct answers to test against, a definition of unacceptable error, and a review path for high-stakes outputs, "the answers look good" is the only quality bar — and it's not one.

**Q13.** Do you have even ten questions from this domain with known-correct answers you could test an AI against?

**Q14.** Could your team agree on which errors are merely annoying and which are unacceptable — and write that down?

**Q15.** If the AI gives a confident wrong answer in a high-stakes situation, who catches it, how fast, and can they override it?

**Weak signals:** quality gets judged by vibes in a demo; nobody has written down what "good" means; there's no path for a domain expert to challenge or correct an answer; the plan for errors is "we'll review outputs for a while."

## How to read your answers

There's no score. Fifteen questions can't measure an organization to two decimal places, and pretending otherwise would tell you less than the pattern of your answers already does.

- **Mostly yes.** Your knowledge may be ready for a narrow, well-scoped AI use case in this domain. Start small, keep the verification questions (Q13–Q15) answered in writing, and expand from what you can check.
- **Mixed.** Common, and workable — but the gaps will surface as "AI problems" if you build first. You likely need some cleanup, modeling, or ownership decisions before a build, in whichever dimensions came up weak.
- **Mostly no, or mostly not sure.** You probably need a knowledge audit before relying on AI outputs in this domain. Building now means paying engineers to discover these same gaps one incident at a time.

What each weak dimension tends to mean:

- **If findability is weak**, the AI will answer from whichever version it retrieves — including the ones your team knows to ignore. Consolidating to one source of truth per domain matters more than any retrieval technique.
- **If structure is weak**, expect inconsistent answers to identical questions. The fix is modeling work — naming entities, making rules explicit, turning prose into tables and schemas — and it's work a model can't do for you reliably.
- **If provenance is weak**, you can't cite sources, which means humans can't verify answers, which means trust never forms — even when the answers are right.
- **If ownership is weak**, any cleanup you do decays. The system's quality will quietly track the staleness of its worst-maintained source.
- **If verification is weak**, you have no way to distinguish a system that works from one that sounds like it works. Fix this one regardless of the others; it's the cheapest to start and the most expensive to skip.

## What to do next

Five steps, all doable without a consultant:

1. **Pick one knowledge domain** — the one where AI help would matter most, not the tidiest one.
2. **Identify the current source of truth** for it. If there are several, choose one and say so out loud.
3. **Mark the contradictions and missing owners** you found in Q10–Q12. A list is enough.
4. **Write a small golden question set** — ten real questions with answers a domain expert signs off on. This becomes your test the day any AI touches this domain.
5. **Decide what should not be automated yet**, and write that down too. A short "not yet" list prevents the most expensive category of mistake.

## Related resources

- [The integration test]({{ '/assets/downloads/missing-layer-two-reports.pdf' | relative_url }}) — the companion diagnostic for the workflow layer, from [The Missing Layer](/blog/missing-layer-ai-adoption-value/)
- [Memory is more than storage](/resources/memory-is-more-than-storage/) — why useful knowledge systems need selection, structure, revision, and forgetting
- [What does "harness" mean in AI?](/resources/what-is-a-harness-in-ai/) — the machinery that turns a capable model into a checkable system
- [Metadata Matters](/blog/metadata-matters/) — the structure dimension, in depth
- [Comparing models for the digital twin](/blog/twin-evaluate-models/) and the [GraphRAG reference](/graphrag-reference/) — what verification looks like on a real system I run

---

If you worked through this and found more "no" and "not sure" than you expected, that's the diagnostic doing its job. These are the questions a [Knowledge Legibility Audit](/work-with-me/) answers with evidence instead of estimates — tracing where your knowledge actually lives, what state it's in, and whether to build now, fix things first, or wait.
