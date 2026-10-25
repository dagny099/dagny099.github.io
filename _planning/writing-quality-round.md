# Writing quality round: targets

Status: audit done 2026-10-19. Tier 0 applied 2026-10-19 (branch `claude/modest-euler-h1vu2b`, not yet merged).

Tier 0 decisions from Barbara: Choco is "he". Cut the "got burned" anecdote. Convoscope was a design call, not an
observed result. Hive numbers are 23 inspections from 400+ photos over 4 years.
Still to click-check: humanlayer.dev post URL, github.com/dagny099/citation-compass, cartography.barbhs.com.
Left for later: the empty "Inspired by CloudWolf" heading (Tier 3); the unverified "seven edge types" and
"five weather variables" claims in the chunking essay.
Tier 1 progress: Poetry post rewritten 2026-10-19 (decisions: keep Poetry, fixed for 2.x; open on the
"seamless switching" feeling; keep Jupyter; diagram + terminal cast). Every command re-run on Poetry 2.4.3 and
direnv 2.32.1 in the cloud container. Assets: `assets/diagrams/poetry-direnv-layers-v1.svg`,
`assets/videos/poetry-direnv-terminal.svg` (recorded from a real shell, paths shortened to `~/projects`).
Barbara to check: the "Why I bother" paragraph (re-entry after months away) is my wording of her motivation;
the 0.7 s vs 0.04 s timing came from the Linux container, not her Mac.

New findings while doing Tier 1 (add to Tier 2 fixes):
- Hero and og:image for *Three Readers* and *Implementing Structured Metadata* point at `assets/images/posts/`,
  which does not exist. The two posts about social preview images have broken social preview images.
- AWS CLI post's banner `assets/images/blog/aws-cli-banner.jpg` does not exist.
- `assets/videos/inside_hive_800px_7sec.gif` is 44 MB, on the hive story the homepage features. Convert to MP4/WebM.
- `_includes/figure` ignores its `width` parameter, so `width="85%"` in the Mermaid post does nothing.

Local build recipe (the sandbox blocks the GitHub API that jekyll-github-metadata calls):
`LANG=C.UTF-8 LC_ALL=C.UTF-8 bundle exec ruby -E UTF-8 -e 'require "jekyll"; require "jekyll-github-metadata"; Jekyll::GitHubMetadata::Client.class_eval { def internet_connected?; false; end }; load Gem.bin_path("jekyll","jekyll")' -- build -d <dir>`

AWS CLI post (2026-10-25): Barbara's RDS instance has been shut down and the architecture is being rethought
elsewhere; she chose a full rewrite anyway, with no mention of the shutdown. Verified by extracting the post's own
bash blocks and running them against moto (AWS emulator) in bash and zsh; `aws configure sso` prompts checked on the
real CLI 2.38.5; MariaDB client TLS flags and the RDS CA bundle URL checked. Not verifiable here: Identity Center
console labels, the real TLS handshake, real provisioning times. Bugs the old version had: `--subnet-ids $SUBNET_IDS`
fails in zsh (macOS default); only one command used `--profile`; `pip install awscli` is v1; no cleanup.
Possible future post: the migration off RDS, once decided.

Lives in `_planning/` (not published).

Scope: every piece a visitor can reach today. That is 24 published posts
(`_posts/`, minus the unpublished stock-ticker post), 4 essays in `_thinking/`,
and 3 published data stories. Resources and snippets are left for a later pass.

Ranking rule: **how visible the piece is × how far it falls short.** Pieces linked
from the homepage or `/start-here/` come first, because those are the ones a
visitor reads first.

---

## How the pieces sort

| Bucket | Meaning | Who does the work |
|---|---|---|
| **Fix** | Errors, contradictions, visible placeholders. Mechanical. | Claude, Barbara approves the diff |
| **Elevate** | The argument works. It needs the graphic, data, or screencast it promises. | Claude builds media, Barbara checks the facts |
| **Rewrite** | The facts are fine but the piece reads like a template. It needs Barbara's own angle. | Barbara thinks it through, Claude drafts and edits |
| **Retire** | A stub, or overtaken by later work. Unpublish it or fold it into another piece. | Barbara decides, Claude does it |

---

## Tier 0: credibility fixes (do first, about one session)

These are small, but a careful reader who finds one will doubt the rest.

1. **Chunking essay shows template placeholders** (`_thinking/2024-09-26-chunking-is-all-you-need.md`).
   The page literally prints `[X%]`, `[Y%]` and `[Z%]`. Its Convoscope claim ("Users skimmed the first row
   and quit") has no data behind it. It also says "400+ beehive inspections," while the hive data
   story says **23 inspections from 400+ photos**. → Fill in real numbers or remove the claims. Fix the hive count.
2. **Scoring post cites the wrong source** (`2026-07-04-scoring-ai-instruction-files.md`). The figures
   "150–200 instructions" and "~50 in the system prompt" are credited to Anthropic's best-practices post. As far
   as I recall they come from HumanLayer's "Writing a good CLAUDE.md." **Verify before changing.** The post
   also has an internal contradiction: it says "past 500 lines, ask hard questions," but its happy ending is a
   650-line file. Either explain why 650 is fine here or reword the ending.
3. **The judgment post misdescribes the model comparison** (`2026-06-26-ai-literacy-judgment.md`). It says
   "I scored both on the same 58 questions" and "I picked whichever read better that afternoon, and that's
   how I got burned." The comparison post says it was **not human-scored**, and it describes a careful,
   controlled run. As written, the two posts tell different stories about the same work. Either name the
   real moment you got burned or soften the anecdote.
4. **Model comparison overclaims** (`2026-05-12-twin-evaluate-models.md`). The claim that Gemini "surfaces
   hallucinations just as reliably" conflicts with the post's own caveat that accuracy wasn't scored. Cut it or qualify it.
5. **Choco story gives the dog two pronouns** (`data-stories/exercise-dashboard.md`): "my Labrador … he" in
   one paragraph, "a rescue dog who had her own ideas" in the next. A `> [VISUALIZATION: The Consistency
   Revolution]` placeholder is also visible on the page.
6. **Citation story mislabels its method** (`data-stories/citation-link-prediction.md`). The title says
   "graph neural networks," but TransE is a knowledge-graph embedding, and the "if A→B and B→C" explanation
   describes transitivity, which TransE doesn't model. It also still shows "[Coming this weekend with the code]"
   and "[Launching next week at knowledgemap.barbhs.com]." On a piece about your own research field, this
   one matters most.
7. **AWS CCP post gets the cert name wrong.** It says "Cloud Certified Professional." The certification is
   "Certified Cloud Practitioner."
8. **Missing-layer post leans on a contested stat.** The MIT "95% of pilots fail" figure is widely disputed on
   method. Keep it with a hedge, or drop it. The post also refers to itself as "the AI Pulse post," which reads like a leftover.

## Tier 1: most promoted, weakest pieces

`/start-here/` sends new visitors to three tutorials that read like unedited exports. They are the
first thing many people read, and they read least like you.

| Piece | What's wrong (observed) | Bucket |
|---|---|---|
| **Poetry toolkit** `/blog/poetry-of-python/` | Pasted from Notion: an empty `#` heading, `<aside>` tags, steps written twice, `git clone` in a `python` code block, the "Direvnv" typo. It clones `PyMesh` and then `cd`s into `beehive-tracker`. Two `.envrc` recipes contradict each other. The Jupyter table ignores Poetry entirely. It relies on `poetry shell`, which Poetry 2 removed. The banner is the AWS image. Ends with an unkept "Coming Soon." | **Done 2026-10-19:** rewritten for Poetry 2.x, tested end to end, new diagram and terminal cast. |
| **AWS CLI → RDS** `/blog/aws-cli-tutorial-.../` | A visible "*Visual Suggestion:*" line. Google-Docs escapes (`\!`) throughout. A four-backtick fence that may break the code block below it. Uses `pip install awscli` (v1, where AWS recommends the v2 installer). Your personal profile name `baba-geocue-admin` is printed in the commands. Generic tone ("career superpower," "grab your coffee"). Promised follow-up never came. | **Done 2026-10-25:** full rewrite. Fitness-dashboard opening (past tense, no status note, per Barbara), connect-from-EC2 test with TLS, cleanup section, network diagram, cropped MapMyRun screenshot. |
| **Mermaid life** `/blog/taming-mermaid-diagrams/` (also on the homepage) | The same SVG appears twice and the tagline appears twice. Stray backticks (`set -euo pipefail\``, `sequence:\``), an unclosed `<mark>`, and "save as" with no filename. **Probably renders broken:** the site runs Mermaid on every `language-mermaid` block, and three of those blocks start with bare YAML lines (`id: …`). Mermaid can't parse that, so they'd show error boxes, on a post about keeping diagrams tidy. (Not yet checked in a browser.) It points to a Streamlit app "in this repo" with no link. | **Fix + Elevate.** Fix the blocks, link the real repo, add a 30-second screencast of the render script and index. |
| **GH Actions series**, parts 1–4 | Part 1 repeats a paragraph and has two "Step 3" headings. Part 3's workflow also deploys on `pull_request` (a real bug), and it says repo-wide read/write permissions are "required," which they aren't. Part 4 has a stray `****`. Emoji-heavy. Links point to old `/posts/` URLs that redirect. Part 4, the reflection, is the only part with a thought of your own in it. | **Fix parts 1–3; rewrite part 4** as the series' opening argument ("I didn't trust a black box in my deploy any more than in my model"). |
| **Vision & perception essay** `/thinking/vision-perception-.../` (homepage + Start Here) | Correct, but generic. Any good dataviz blog could have published it. Same Abstract / Overview / Downloadables / "Email me" layout as the other two Sept-2025 essays. | **Rewrite: the single biggest opportunity.** You did eye-movement research on how context guides visual search (the 2009 paper in your citation story). No generic dataviz post can say that. Let it open the essay, with one real figure from that work. |

## Tier 2: good bones, needs its graphics (where I can help most)

| Piece | What's missing | Proposed media |
|---|---|---|
| **Three Readers of Your Web Page** | Four "> **Suggested graphic —**" production notes are **visible on the live page**. The prose is strong and the knowledge-graph framing is distinctive. | Build the four SVGs it already specifies (hero fan-out, three-stage pipeline, myth-buster card, triple graph). This is the highest return on effort in the whole round. |
| **GraphRAG migration** | The title promises "same questions, two retrieval systems," but the post shows **no side-by-side answers**, and it admits the evaluation hasn't been run. No images. | A two-column figure: one query, vector answer vs. graph answer, with the entities each one cited. Plus a screencast of filtering the reference doc's entity browser. A retitle may also be needed if the comparison stays qualitative. |
| **Model comparison** | Fine as is. The promised rubric scores (May) aren't out yet. The banner image is reused from the Poetry post. | Optional: a 20-second clip of the Twin answering the same question under each model. |
| **Choco effect** | Calendar heatmap is a placeholder. | Build the heatmap, if the workout data is in the repo or can be shared. |
| **Metadata matters** | Says it was "published on 2025-11-15"; the date field says 2025-11-7. Recommends HowTo schema, which Google stopped showing as rich results in 2023. Partly duplicates *Three Readers*. | Fix, then see Tier 3. |

## Tier 3: retire or consolidate decisions (yours)

- **Sensor Fleet, 7 posts.** Parts 1–6 run 38–125 words each, with "Things You'll Need: - - -" and baby-bee
  placeholder photos. Part 2 links a dead Heroku dashboard (Heroku's free tier ended in 2022).
  Options: (a) unpublish parts 1–6 and keep the intro as a project retrospective; (b) fold everything into
  one "what I built in 2021 and what I'd do now" post. Leaving seven empty pages visible is the worst choice.
- **Recreational 3D Printing** (96 words, "More to come soon") and **AWS CCP badge** (220 words, ends on an
  empty heading). Each could become a snippet or an item on the journey timeline, or be unpublished.
- **The three Sept-2025 `_thinking` essays.** All share one template, including "Downloadables (optional)"
  and "Email me for the starter pack." Some of those downloads already exist in `_resources/`
  (`color-contrast-checklist`, `question-encoding-cribsheet`, `small-multiples-template`), so link them
  and delete the email offer. *Bees, Graphs, and Governance* overlaps the hive data story. *RAG Without the
  Theater* has been overtaken by your Twin posts, which actually do what it recommends. Consider
  folding it into those.
- **The metadata trilogy** (*Metadata Matters*, *Three Readers*, *Implementing Structured Metadata*). Three
  posts on one subject. *Three Readers* has the best thesis. Consider turning *Metadata Matters* into a short
  "why I care" opening that links to the other two.

## The unique-thought test

Observation: the posts that read most like you share a lens. You treat messy information as something to
make legible, and you bring a cognitive scientist's view of how people and machines retrieve meaning. *Three
Readers* (sameAs as entity reconciliation; metadata as retrieval cues), *GraphRAG* (the "describes vs.
mentions" ranking problem), and the *Scoring* post (instructions as a finite attention budget) all have it.

Interpretation: the weakest posts aren't weak because they're tutorials. They're weak because nothing in
them could only have come from you. A suggested bar for every piece this round: **one claim, figure, or
failure that only you could have written.** If a piece can't meet it, retire it.

## Open threads

- Decisions needed from Barbara: the Sensor Fleet option (a/b); whether the Poetry post is rewritten or retired;
  whether the Sept-2025 essays are rewritten or folded into other pieces.
- To verify before editing: the source of the instruction-count figures; whether the Mermaid blocks really
  render as errors (check in a headless browser); whether the Choco workout data is available.
- Deferred to a separate turn: rescuing unpublished ideas, starting with the economics framework for
  evaluating different kinds of goods.
- Out of scope this round: `_resources/`, `_snippets/`, `_projects/`.
