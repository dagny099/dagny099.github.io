---
layout: single
title: "RAG Without the Theater — Evidence‑Linked Retrieval Patterns You Can Defend"
subtitle: "Building retrieval-augmented systems that cite auditable evidence and fail honestly"
date: 2025-09-11 00:00:00 -0600
last_modified_at: 2025-01-15
categories: ["Thinking", "AI Systems"]
tags: ["rag","retrieval","evaluation","prompting","governance","prod-readiness"]
excerpt: "Retrieval‑augmented generation shines when answers cite evidence you can audit. Skip magic prompts; use small, testable patterns that tie claims to sources and fail honestly when evidence is thin."
pin: true
toc: true
toc_sticky: true
classes: wide
header:
  overlay_image: /assets/images/rag-hero.jpg
  overlay_filter: 0.45
---

**Abstract (30 sec).** Retrieval‑augmented generation shines when **answers cite evidence** you can audit. Skip magic prompts; use small, testable patterns that tie claims to sources and fail **honestly** when evidence is thin.
<!--more-->

<details><summary><strong>Overview (2 min)</strong></summary>

- **Goal.** Useful, defensible answers: grounded text + citations + uncertainty when needed.  
- **Method.** Treat RAG as a *pipeline*: normalize → retrieve → compose → verify → cite.  
- **Discipline.** Evaluate faithfulness, coverage, and *answerability*—then tune retrieval *before* clever prompting.

</details>

## 1) Anti‑patterns to avoid
- **“Prompt harder.”** Masking poor retrieval with verbose prompts.  
- **“Vector monoculture.”** One embedding space for everything.  
- **“Citation cosplay.”** Dumping links that weren’t actually used to craft the answer.

## 2) Three small patterns that carry far

### A) **Attribution‑First Compose**
*Compose from snippets you’ve actually retrieved; attach cites at the sentence level.*

- Retrieve `k` passages with score + source.  
- Compose answer *only* from those passages.  
- Emit a **claims→evidence** map.

**Why**: prevents unsupported statements; reviewers can audit fast.

### B) **Query Routing (Cheap & Cheerful)**
*Route queries to the right retriever/index before embedding.*

- Simple router: keyword heuristics + intent classifier.  
- Separate indexes for policy, product, code, etc.  
- Fall back to a general index if confidence is low.

**Why**: improves recall without inflating context windows.

### C) **Hybrid Retrieval with “Must‑Include” Filters**
*Blend sparse + dense; enforce filters like date, author, or section.*

- BM25 (sparse) + embeddings (dense) with weighted merge.  
- Hard filters: `date > last_policy_update` or `doc_type: FAQ`.  
- Deduplicate near‑identical chunks pre‑compose.

**Why**: fewer near‑duplicate distractors; fresher, on‑topic evidence.

## 3) Guardrails & evaluation you can explain

### Minimal eval set (start here)
- 25–50 real queries with **gold citations**.  
- Label: **faithfulness** (0/1), **coverage** (0–2), **answerable?** (Y/N).  
- Track retrieval metrics (recall@k, MRR) and answer metrics (exact‑cite rate).

### CI‑style checks
- **Regression** on recall@k when indexes change.  
- **Drift** alarms when answers cite stale sources.  
- **Red‑team** prompts for jailbreaking and over‑claiming.

## 4) Production notes
- **Chunking:** align to semantic units (sections), store **char offsets** for precise cites.  
- **Metadata:** source, version, updated_at → enables “freshness” filters.  
- **Transparency UI:** show citations inline; let users expand the passage.  
- **Honest fallback:** if coverage < threshold → *“Insufficient evidence”* with suggested queries.

## 5) A reference flow (print + pin on a wall)
```
User Q
  → Normalize (lowercase, strip boilerplate, detect intent)
  → Route (policy|product|code|general)
  → Retrieve (hybrid; filters; top-k)
  → Compose (from retrieved; sentence-level cites)
  → Verify (faithfulness; coverage; answerable?)
  → Output (answer + cites + confidence + follow-ups)
```

---

### Downloadables (optional)
- Starter eval sheet (CSV)
- Query router rules (YAML)
- Claims→Evidence template (MD)

**CTA.** Want the eval starter kit? Email me; I’ll share a lean, no‑nonsense pack.