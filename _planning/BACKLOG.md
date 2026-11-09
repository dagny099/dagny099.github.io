# Writing backlog

Things worth coming back to after the quality round. This is a place to park ideas so they
stop competing for attention, not a to-do list with deadlines. Lives in `_planning/` (not published).

Started 2026-11-09.

## Questions I keep coming back to

**How does the nature of a stored representation shape how it gets retrieved, especially in a given context?**
(Barbara's words, 2026-11-09: a question she's perennially interested in.)

- Where it already shows up: the GraphRAG migration post (chunks vs. typed graph nodes, "describes vs. mentions"),
  the dissertation work on contextual guidance (scene context steering where people look before they find the target),
  and *Three Readers* (metadata as retrieval cues).
- Claude's observation, for Barbara to accept or reject: this may be the through-line of the whole site. The
  vision essay, GraphRAG, and the metadata posts are each a version of it.

## Posts to return to

- **GraphRAG migration: add the real side-by-side.** Barbara has most of the data; about an hour to put it in place.
  Same questions, vector answer vs. graph answer, with the entities each cited. The post's title promises this
  comparison, and right now it doesn't show one.
- **Digital Twin model comparison: the scored follow-up.** The May post promises rubric scores on a 15-question subset.
- **Scoring AI instruction files: the second project.** The post promises a React + Flask comparison ("I'll report back").
- **Mermaid automation (post 2).** A full outline exists in the companion repo:
  `blog/Blog_mermaid-2-automation_post_outline.md` (GitHub Actions rendering, auto-indexing, catching index drift).
- **Moving off RDS.** The fitness dashboard's database is being re-architected; the decision itself could be a post.

## Ideas not yet written

- **An economics-based framework for evaluating different kinds of goods.** Parked at the start of the quality round.

## Deferred polish (only if it stops being polish)

- GraphRAG: screencast of filtering the reference doc's entity browser.
- Model comparison: a short clip of the Twin answering the same question under each model.
- Metadata trilogy: fold *Metadata Matters* into a short "why I care" opener for the other two.
- Companion repo: `diagram_hub/__init.py__` is misnamed (works anyway as a namespace package); the wizard's
  diagram-type caption doesn't update until the form is submitted.
