---
layout: single
title: "What Happened When I Asked the Same Questions of Two Retrieval Systems"
subtitle: "Rebuilding my Digital Twin's retrieval layer on a graph — what changed, what it cost, and what I'm learning along the way."
date: 2026-05-16
permalink: /blog/twin-graphrag-migration/
header:
  overlay_image: "/assets/images/new-ml-ai-starter-flow.png"
  overlay_filter: 0.5
excerpt: "A walkthrough of migrating my Digital Twin from ChromaDB vector retrieval to a Neo4j-backed GraphRAG pipeline — the queries that used to be impossible, the trade-offs I made, and a working reference doc with all 167 canonical entities embedded as a filterable table."
excerpt_display: true

tags: [LLM, evaluation, digital-twin, RAG, GraphRAG, Neo4j, knowledge-graph, AI]
stack: [Neo4j, ChromaDB, Python, OpenAI embeddings, Cypher, GPT-4.1]
categories: [data-science]

---

## Contents

1. [The question that broke the old system](#the-question-that-broke-the-old-system)
2. [Same questions, two retrieval systems](#same-questions-two-retrieval-systems)
3. [Three problems, three architectural moves](#three-problems-three-architectural-moves)
4. [What the new system gives up](#what-the-new-system-gives-up)
5. [The reference doc, and why it earns its own paragraph](#the-reference-doc-and-why-it-earns-its-own-paragraph)
6. [Where I'm being cautious](#where-im-being-cautious)
7. [What I'm doing next](#what-im-doing-next)

## The question that broke the old system

A few weeks ago, I was running test queries through my Digital Twin and asked it: *which of your projects use knowledge graphs?*

The Twin answered the way it always does — with confidence. It surfaced ten chunks of text, the retriever passed them to the model, and the model wrote a fluent paragraph that mentioned, more or less, every project where the phrase "knowledge graph" appeared in my knowledge base.

The paragraph was wrong. Not factually wrong about any individual project, but wrong about which projects to include. It missed Resume Graph Explorer because that project's walkthrough talks about RDF and ontologies more than it uses the phrase "knowledge graph." It included a project that mentioned knowledge graphs in passing without actually using one.

This wasn't a model failure. It was a retrieval failure — and a specific kind I couldn't fix by improving the prompt or swapping the model. The system was being asked to answer a question about relationships ("which projects use X") using a tool that only knows how to find text similarity. No amount of model tuning fixes that.

So I rebuilt the retrieval layer on a graph.

## Same questions, two retrieval systems

The premise of this post is similar to an earlier post, [model comparison](/blog/twin-evaluate-models/): ask the same questions and keep everything the same except one variable, see what changes. In that post, *the variable was the **language model**.* The retrieval pipeline, model parameters, and tech stack were held constant. 

In this post, *the variable is the **retrieval architecture**.* The LLM is the same.

The old system embeds the knowledge base into ChromaDB, chunked at roughly 900 characters per piece, and retrieves by vector similarity. The new system loads the same knowledge base into Neo4j, but it stores complete sections as the retrieval unit, promotes Projects, Skills, Methods, Technologies, and Concepts to first-class graph nodes with named edges between them, and ranks results with a hybrid score that mixes vector similarity with graph signals.

The difference shows up clearly on three query types-

**Factual questions about a specific project** — *"Tell me about Resume Graph Explorer."* Both systems answer. The old one returns five or six chunks that often start or end mid-thought; the model stitches them. The new one returns the complete section that describes the project, in one piece.

**Questions about relationships** — *"Which projects use knowledge graphs?"* The old system approximates; the new system traverses one edge type and returns the list. This is the category that was structurally impossible before.

**Questions that span multiple projects** — *"What other projects use similar methods to Resume Graph Explorer?"* The old system can't reason about "similar methods" at all. The new system follows shared-method edges between project nodes and returns the actual pairs.

## Three problems, three architectural moves

The migration plan started from three concrete failure modes in the old system, and each one drove a specific architectural move in the new one.

**Wrong granularity.** Nine-hundred-character chunks fragment thoughts. A description of a project's evaluation methodology might end mid-sentence; the next chunk picks up in the middle of a metric definition. The model can usually recover, but the user experience reflects the seams. The new system uses complete H2 sections (typically 2,000–3,000 characters) as the retrieval unit, keeping fine-grained chunks as optional children.

**Missing connections.** The relationships between projects and the skills, methods, and technologies they demonstrate were implicit in text only. There was no way to ask the system "show me every project that uses Neo4j" except by hoping the text near "Neo4j" mentioned every relevant project. The new system makes those relationships explicit — Skills, Methods, Technologies, Publications, and Concepts are typed nodes connected to Projects by typed edges (`DEMONSTRATES`, `USES_METHOD`, `USES_TECHNOLOGY`).

**Poor ranking.** Pure vector distance can't tell whether a section *describes* a topic or merely *mentions* it. Two sections that both contain the phrase "Bayesian reasoning" score similarly in vector space even if one is a dedicated treatment and the other is a passing reference. The new system ranks with a hybrid score: 60% vector similarity, 25% boost for sections that explicitly describe a project, 10% for sections rich in entity mentions, 5% for substantial length over fragments.

The numbers are calibrated guesses. They'll need empirical tuning once the evaluation harness has run against the new pipeline. The point isn't that 60/25/10/5 is correct — it's that multi-signal ranking is the kind of thing a graph schema enables and a flat vector index doesn't.

## What the new system gives up

If GraphRAG were strictly better, the model comparison framing would feel forced. It isn't. The new system is more capable in specific dimensions and more expensive in others, and the honest version of this post names both.

**Operational complexity.** One database becomes two — Neo4j alongside the existing OpenAI embedding calls. One query language becomes two — Cypher in addition to the vector index calls. Local development now requires a running Neo4j instance; deployment requires hosting it. The old system was a Python script and a flat file directory. The new one is infrastructure.

**Entity extraction is a new failure surface.** The graph is only as good as the entities it contains. Pulling Skills, Methods, and Technologies out of project walkthroughs is an LLM extraction step, which means it has its own quality problems. In my current canonical entity file, acronyms got Title-Cased instead of left uppercase (`Rdf` instead of `RDF`, `Openai` instead of `OpenAI`). Some names appeared in multiple type pools — `RAG` as both a Skill and a Method, `RDF` as a Skill, Method, *and* Technology. None of these are catastrophic; some are even semantically reasonable. But each is a real artifact that the old system didn't have, because the old system didn't try to extract structure from text.

**A manual curation step.** Concepts — the cognitive science frameworks like Bayesian reasoning, contextual priors, Marr's levels of analysis — couldn't be extracted reliably from project walkthroughs the way Skills could. They live in my philosophical writing, scattered across many sections. So I curated them by hand: 20 canonical concepts from a raw list of 377 candidates. Until the canonicalization pipeline gets a read-and-preserve step, that curation is fragile — easy to overwrite on the next rebuild.

I share these as artifacts of an honest in-progress system, not as embarrassments. The new system is real enough to have real problems. The old system was simpler partly because it was doing less.

## The reference doc, and why it earns its own paragraph

Every architectural decision in this migration lives in [a standalone reference document](/graphrag-reference/) — a single HTML page with the schema diagram, the hybrid scoring formula, the four resolved decisions and their trade-offs, and a glossary that defines RAG, GraphRAG, Cypher, and the rest of the jargon as I use them.

It also embeds the live canonical entity data. All 167 entity nodes — Skills, Methods, Technologies, Concepts — are loaded into a filterable table you can search across names and alt-labels, sort by role or stage, and expand to see the full alt-label list. The same data the graph is built from, browsable without writing a Cypher query.

I wanted that to exist for two reasons. First, when I talk about this work in interviews, I'd rather point to a reference than re-explain every time. Second, the work of making data legible to humans — not just to machines — is the thing I care most about as an applied AI practitioner. The doc itself is an instance of the practice.

## Where I'm being cautious

A few things to flag before anyone overgeneralizes from this post.

This isn't a head-to-head with scored answers yet. I have a five-battery evaluation plan covering granularity, relationship-query success, ranking quality, latency, and regression against the existing 50-question eval suite. None of those have been run end-to-end against the new system at the time of writing. The architectural argument is sound. The empirical argument is in progress.

The scoring weights are educated guesses. The 60/25/10/5 split has loose theoretical motivation but no empirical optimization behind it yet. Phase 5 of the migration plan calls for tuning these against the evaluation harness once the graph is fully populated. Until then, treat the formula as a working hypothesis.

The MENTIONS edge signal saturates in practice. The current ranking caps the entity-richness bonus at five mentions per section. Real data shows the median section has nine mentions and the mean is just under ten — about 75% of sections sit above the cap. The signal is effectively binary in production right now. The fix is straightforward; the lesson is that I had a calibrated intuition about what the data would look like, and the data disagreed.

GraphRAG isn't automatically better for everything. For short factual questions where the answer lives in one place in the knowledge base, vector retrieval is fast and entirely adequate. The cases where graph traversal earns its keep are relationship questions and ranking questions where multiple signals matter. The principle generalizes from the model-comparison post: this is an architecture decision matched to a use case, not a quality decision applied uniformly.

## What I'm doing next

Three things are on the list.

1. **Run the evaluation harness end-to-end.** Score the new system against the same 50-question battery the old system passes at roughly 85%. The graph migration must not regress that number, and ideally improves on it for relationship-style queries.

2. **Tune the scoring weights against real query data.** The 60/25/10/5 starting values need to be tested. If the project-described boost is doing most of the work, that tells me something. If entity-richness barely matters, that tells me something different.

3. **Fix the entity extraction quality issues.** The acronym casing fix is a one-line change in the deterministic phase of canonicalization. The cross-type pool bleed for things like RDF needs a tighter extraction prompt. Both are scheduled for the next rebuild.

The deeper goal is the one underneath the model-comparison post and this one and every project I build: making messy data legible — not just to the machines that index it, but to the humans who depend on it. A graph is one specific bet about how to do that. The reference doc is another. Both are how I show my work.

---

*The [full GraphRAG reference document](/graphrag-reference/) lives alongside this post, complete with the schema, the scoring formula, the four resolved architectural decisions, the embedded canonical entity browser, and the migration items I'm carrying forward.*
