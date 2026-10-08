# Works spike: books and articles connected to guests and hosts

Date: 2026-10-08. Plan reference: `podcast-graph-pilot.md` section 11A.
Evidence: `works-spike/reference_mentions.yml` (hand-labeled reference set) and
`works-spike/openlibrary_probe.py` (the lookup used below).

## Questions the spike had to answer

1. Tier 1: how many works do the show notes of the 13 seed episodes actually mention?
2. Tier 2: can a catalog tell us which works a guest wrote, for three test people?
3. Network: which sources are reachable, and on what terms?

## 1. Tier 1: works mentioned in the show notes

Read by hand from the full Apple descriptions (the reference set):

| | Count |
|---|---|
| Titled works mentioned | 13, in 4 of 13 episodes |
| ...from one episode (Lenny's, Elizabeth Stone) | 9 (3 recommended books, 5 articles, 1 newsletter) |
| Works by the guest themselves | 3 titled (Serrano's *Grokking Machine Learning*, O'Reilly's two Substacks) |
| Untitled pointers ("the paper he co-authored", "her TED Talk", "a presentation at…") | 3 |
| Episodes with no work of any kind | 6 (all Catalog & Cocktails, 3 SuperDataScience, Burns) |

What this means:
- **The layer will be lopsided.** Shows that publish reference lists (Lenny's) dominate.
  SuperDataScience notes point to `superdatascience.com/<n>` "Additional materials" pages,
  which probably list more, but those pages are unreachable from the cloud session.
- **Guest-authored works surface in Tier 1 on their own**, so Tier 1 and Tier 2 meet:
  the notes give the title, a catalog gives the metadata.
- **Two kinds of extraction.** Link-structured lists (Amazon links, newsletter paths) are
  easy for rules. Prose mentions ("Bainbridge's ironies of automation", "between the two
  editions of Grokking Machine Learning") need an LLM. A rules pass written after reading
  the notes caught the Lenny's links and three phrase patterns; it is overfit by
  construction, so it is not a fair baseline. The fair test is an LLM extractor scored
  against `reference_mentions.yml`, which belongs in session B (swappable LLMs).
- **Transcripts would change the picture.** Lenny's links a full transcript in every
  episode; Knowledge Graph Insights puts much of the transcript in the description.
  Mentions in conversation are far richer than show notes. That joins up with the
  transcript pipeline in Neo4j-GraphRAG-Podcast-Knowledge-Base, later.

## 2. Tier 2: "works by this person" from a catalog

Open Library author search for the three test people:

| Person | Author-search matches | What the top record contains |
|---|---|---|
| Luis Serrano | 91 | Record `OL8459156A` mixes at least four people: *Grokking Machine Learning*, *Lignin Chemistry*, Portuguese novels, religious comics |
| David Burns (BrowserStack) | 58 | Record `OL360063A` (61 works) mixes the Selenium author with the psychiatrist (*Feeling Good Together*, *Sentirse Bien*), biophysics, number theory, SAP accounting, beekeeping |
| Tim O'Reilly | 2 | 42 works, mostly O'Reilly series he edited; his own book *WTF?* sits under a separate "Tim OReilly" record |

Title lookups did much better: *Grokking Machine Learning*, *Selenium 2 Testing Tools*,
*Thinking in Systems* each resolved at rank 1 with ISBNs. One caution: the partial title
"WTF? What's the Future" ranked Brian Solis's *WTF?: What's the Future of Business?* first;
the right book was second. *Ironies of Automation* (a 1983 paper) is not in Open Library.

**Conclusion: never list a person's works from an author record.** Author records merge
namesakes, which is exactly the David Burns problem we predicted, inside the catalog
itself. Anchor on a title instead (from the show notes, or confirmed by me), use the
catalog only for metadata (ISBN, year, link), check that the catalog's author name matches,
and link the work to our own person id.

## 3. Sources and network

| Source | For | Status from the cloud session |
|---|---|---|
| Open Library | books | Reachable after allowlisting; drops about 1 request in 3, so retries are required |
| OpenAlex | papers, articles | Reachable, but now **requires an API key**: keyless calls share a daily budget per IP, and the shared cloud IP had used it up (`429`, resets midnight UTC). GitHub Action runners share IPs too. |
| Google Books | books | `429`: same shared-quota problem without a key |
| Crossref | papers (DOIs) | Not tested (not allowlisted); keyless, a reasonable fallback for papers |
| Wikidata, show websites, Lenny's transcripts | people, references | Blocked (not allowlisted) |

Newsletters, talks and Substacks have no catalog; their record is title + URL from the notes.

## Recommendation for the build session

1. **Data file** `_data/podcast_works.yml`, one entry per work:
   ```yaml
   - id: grokking_machine_learning
     title: Grokking Machine Learning
     type: book            # book | article | paper | newsletter | talk
     authors: [luis_serrano]          # our person ids, when the author is in the graph
     authors_outside: []              # plain names otherwise (e.g. Donella H. Meadows)
     year: 2021
     url: <publisher or catalog page>
     ids: {isbn: "...", openlibrary: OL25456853W}
     source: openlibrary              # or show_notes, manual
     mentions:                        # one per episode that mentions it
       - {listen: 2026-09-08-superdatascience-word-gravity-..., kind: by_guest}
   ```
   Untitled pointers are not stored until a title is confirmed.
2. **Seed it from the reference set**: about 13 works, with Open Library metadata for the
   five books. That is enough to build and judge the "Works" toggle on real data.
3. **Extend add-listen**: after guests and topics, list works mentioned in the notes and
   ask which to keep. Titles only; the catalog lookup fills metadata.
4. **Model guests' podcasts as shows** (Burns' *BrowserStack Talks*), the same pattern as
   Linear Digressions.
5. **Before papers**: get a free OpenAlex API key (store as an environment secret) or
   allowlist `api.crossref.org`.

## Open questions for me

- Are recommended books from a host's standard segment (Lenny's "Recommended books") as
  interesting as works the guest discussed? They will dominate counts.
- Should Tier 2 ever go beyond works the notes mention, given the catalog problem above?
  My lean: only when I add one by hand.
