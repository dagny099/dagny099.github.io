---
layout: single
section: data-stories
title: "ChronoScope Data Story: Turning Text into Visuals, Part 1"
permalink: /data-stories/building-personal-resume-2026/
date: 2026-01-02
last_modified_at: 2026-01-02
header:
  overlay_image: /assets/images/bees_pollen.jpg
  overlay_filter: 0.5
  teaser: /assets/images/bees_pollen_th.jpg
excerpt: ""
tags: []
stack: []
classes: [story-page]
breadcrumbs: false
author_profile: false
status: draft  
published: false

---

**Working Title:** 
- “Building a Personal Timeline From my Resume(s) and Unlocking Knowledge from the Data"
- “Getting more from visuals than words: What I Learned by Letting LLMs Munch 10 of my Resumes"


## Story Arc Summary

**Hook:** As a cognitive scientist fascinated with learning, I’ve been tantalized by the idea of turning text into visual and graphical representations for a long time (see Data Sketching; Postcards work; that other YT guy). That idea coupled with my current main activity being seeking my next professional job (read: Job searching most days), has me wondering about the value I could unlock by turning my various resumes into more structured representations. 

**Conflict:** I have a lot of different versions of my resume, purposefully tailoring the phrasing of different skills or activities from each role such that it best suits the role I’m applying for. As a Data Scientist and Technical Consultant for the past 12 years, I have multiple experiences across different domains- health care, data management, business management consulting- which translates into a LOT of different versions of my resume.  

**Solution:** LLM-powered timeline extraction from personal documents (my resumes!). 

**Discovery:** Surprising insights about skills evolution and overlap, narrative, and identifying what I enjoy most

**Resolution:** Tool that transforms chaos into visual clarity (Plotly interactive timeline) and that I enjoy looking at! Practice developing and evaluating an LLM powered app that benefits me directly! Also: A Timeline JS artifact that I’ll publish on my website (link here), demonstrating the power of data-interoperability.

**Target Length:**
- Personal Blog: 3,500-4,000 words
- Medium: 2,500-3,000 words (condensed version)

---

## Opening: The Personal Hook (400-500 words)

### Section 1: “Patterns Everywhere but Spending Too Much Time Applying for Jobs"

**Narrative Beat:** Establish relatable problem through specific anecdote

> * It’s summertime in Texas and it’s HOT. Which is fine because what I need to do is to bask in the luxury of air conditioning while searching for my next career move. I’ve got about 12 collective years of professional experience across the healthcare, software, and business management consulting industries. These days, anyone on the job hunt has probably perceived that there are PATTERNS in JOB DESCRIPTIONS, within and across industries. At the same time, the “job hunt best practices” recommend ensuring that an applicant’s submission is tailored to the SPECIFIC ROLE at the company. What’s a data scientist and AI/ML engineer to do???
>
> * Well, the first answer was to see if I could get by with 1-2 resumes, for the top two types of gigs I was applying for. The resulting crickets led me to create 3-4 resumes with aptly named files and configurable sections. That led to a handful of interviews before the holidays. *
>
> * New year, new tactic: Convert my LLM-powered app into a tool to achieve the goal of preparing better job applications with less manual effort AND an opportunity to practice my long-standing fascination with TURNING TEXT INTO VISUAL REPRESENTATIONS. *


**Key Elements:**
- My specific need to find a job, which could encompass different industries.
- I have different resumes, often with inconsistent and uninformative file titles, hindering discoverability and slowing editing. Also leading to file chaos (annoying!)
- Universal appeal: Apply for jobs, little to no response. Relatable frustration with time spent applying for jobs.
- AH HA MOMENT: Structured representations can be much more useful than purely textual ones (so many refs). Let’s see if I can make something useful (interactive timeline) and beautiful (Timeline JS exportable version) out of several versions of my resume. 

### Section 2: "The Resume Problem"

**Narrative Beat:** Even a data scientist’s own data management can be chaotic, lots of versions, unhelpful filenames. Gah! 

> *I have three versions of my resume on my computer. According to Resume v1, My Technical Consulting featured these main highlights: “project management”, “leading workshops”, and “business process mapping”. There’s a cover Letter from 2019 says I "managed the cloud transition initiative throughout 2017-2018." LinkedIn (updated 2020) lists it as "2016-2018.”* Bottom line: over time, my resumes have gotten a little out of sync in terms of some date discrepancies, and there’s of course the problem of highlighting different applicable skills from different positions according to the job a persons is applying to. 
>
> *Which jobs and activities should I feature across my career trajectory, given that I'm applying for Job X?*

**Visual Element:** Screenshot mockup showing 3 document snippets with highlighted contradictions

**The Reality Check:**
- 📄 **5+ versions** of resume/CV across computers and cloud storage
- 🗓️ **Inconsistent dates** across documents (same events, different years)
- 🎭 **Characterization of past experiences can depend on target role** - am I a "technical leader" or "strategic manager"?
- 🤷 **How to hone in the important stuff** - Given my target audience, how can I represent myself authentically and efficiently? Also, can we turn this into a structured representation that we can visualize? 

**Transition:** "As someone who builds real applications for real people, this is exactly the kind of challenge I enjoy. Let’s design a solution."

---

## Act 1: The Beautiful Mess (600-700 words)

### Section 3: "The Document Disaster"

**Narrative Beat:** Show the full scope of the problem

<details open markdown="1">
<summary><strong>📊 The Data Archaeology Challenge</strong></summary>

When you're building a career, document organization feels like a luxury. But looking back, I realized this chaos was hiding critical insights:

- **Temporal patterns:** Are my dates actually consistent across documents?
- **Narrative evolution:** How does my professional story change based on audience?
- **Discrepancies:** When documents (or my memory) disagree, how should I settle on “an answer” to remain consistent going forward?

The irony: I help organizations wrangle their messy data for a living. Yet my own professional timeline was a disaster.
</details>

**Specific Examples (Edit with Real Data):**
- Resume folder: `resume_final.docx`, `resume_final_v2.docx`, `resume_FINAL_FOR_REAL.docx`
- Cover letters named by company vs. by date vs. by role
- LinkedIn profile updated sporadically with no version control
- Old portfolio site with yet another timeline variant

### Section 4: "The Hypothesis"

**Narrative Beat:** Introduce the technical solution

> *Every digital document contains metadata—creation dates, modification times, embedded timestamps. More importantly, the documents themselves are data: structured text describing events, dates, roles, and achievements.*
>
> *What if I could extract all events from all my documents, reconcile the contradictions, and let the data tell me the truth?*

**The Technical Insight:**
- LLMs can extract structured events from unstructured text
- Document metadata provides additional timing clues
- Automated extraction avoids human memory bias
- Visual timelines make contradictions obvious

**Approach Overview:**
```python
# Conceptual pipeline
documents = load_all_career_documents()
events = llm_extract_timeline_events(documents)
timeline = reconcile_contradictions(events)
visualize_with_confidence_scores(timeline)
```

**Why This Works:**
- Retroactive: works on years of unorganized documents
- Unbiased: LLM doesn't have my memory baggage
- Comprehensive: processes hundreds of pages in minutes
- Revealing: highlights contradictions I didn't see

---

## Act 2: Building the Machine (700-800 words)

### Section 5: "Teaching Machines to Read Resumes"

**Narrative Beat:** Show the technical solution in action

**The Pipeline:**
1. **Document Ingestion** - Upload PDFs, Word docs, text files
2. **LLM Extraction** - GPT-4 identifies events, dates, descriptions
3. **Date Normalization** - Parse fuzzy dates ("Summer 2017" → "2017-06-01")
4. **Deduplication** - Reconcile same event mentioned in multiple docs
5. **Confidence Scoring** - How certain is the system about each event?
6. **Timeline Visualization** - Interactive Plotly charts

**Sample LLM Prompt (Show the Transparency):**
```
You are analyzing a professional resume. Extract all career events with:
- Event name/title
- Start date (parse flexibly: "2015", "Jan 2015", "Spring 2015")
- End date (or "present")
- Description
- Key skills mentioned

Return as structured JSON.
```

**Technical Deep-Dive (Collapsible):**
<details markdown="1">
<summary><strong>🔧 Implementation Details</strong></summary>

- **LLM Model:** GPT-4 via OpenAI API
- **Date Parsing:** python-dateutil for flexible parsing
- **Storage:** JSON-based timeline with source tracking
- **Visualization:** Plotly for interactive charts
- **Framework:** Streamlit for rapid prototyping

**Key Decisions:**
- Why LLMs over regex: resumes have too much format variance
- Why JSON storage: simple, portable, version-controllable
- Why Plotly: interactivity reveals patterns static charts miss
</details>

### Section 6: "The First Timeline Emerges"

**Narrative Beat:** The moment of discovery

> *I ran ChronoScope on my five most recent career documents. Within 30 seconds, I had my answer about the cloud migration project: the documents disagreed.*
>
> *Resume v1 said 2016-2017. Cover letter said 2017-2018. LinkedIn said 2016-2018. But here's what I didn't expect: the system also found a 6-month gap in my timeline that I'd completely forgotten about.*

**🎯 VISUALIZATION 1 PLACEMENT: Skills Evolution Timeline**

**Why here:** This is the first "aha moment" - show what the machine saw that I didn't

**Caption:**
*"My skills evolution over 15 years. Notice anything? I stopped mentioning R after 2014 without realizing it. 'Leadership' didn't appear until 2016, now dominates every document. The machine saw patterns I wasn't consciously tracking."*

**Narrative Reaction:**
> *Seeing this chart was surreal. I didn't consciously decide to become a "leader" instead of a "coder." It just... happened. The documents remember the shift, even though I don't remember making it.*

---

## Act 3: The Questions That Emerged (900-1000 words)

### Section 7: "Question 1: Could my system reliably extract structured data from my resumes?"

**Narrative Beat:** Yes, there’s plenty of structure in resumes (even different ones) to **extract Events**, track their **Source Documents** (important for evaluation and reconciliation), and annotate events with **Timeline properties** (key for visualization).

> Since most resumes don’t contain ALL of my professional experiences by now, it was great to get the benefit of the aggregation of my professional story by having my LLM app “munch” through several versions of my resume

**🎯 VISUALIZATION 2 PLACEMENT: Table showing statistics of extracted Events and Document counts, grouped by Application Type**

**Why here:** Directly supports the unstructured text (resume) to structured representation (Events, Documents)

**Caption:**
*”All in all, the most expansive version of my professional career spans 8 jobs, over 12 years, extracted from 6 resumes. There was a high degree of consistency, and it was great to have the system “discover” any date discrepancies across documents I fed it.“*

**Reflection:**
- Wow, I’ve done a lot of stuff
- I really appreciate having the “WHEN” of things so well specified, especially since recruiters seem to need to know that.
- Although this project is focused on understanding the “whole ball of wax” with respect to the WHEN of things, I realize the richness of being able to associate the “WHAT” (content of my description of each job). I can smell follow-up project #2… :)

<details markdown="1">
<summary><strong>🧠 The Psychology of Timeline Memory</strong></summary>

Research shows we reconstruct memories rather than replaying them. Career timelines are especially prone to:

- **Compression bias:** Gaps feel shorter in memory than they were
- **Narrative smoothing:** We unconsciously create coherent stories
- **Recency effects:** Recent events are detailed, distant ones are vague
- **Motivated reasoning:** We remember timelines that support our self-image

Documents don't have these biases. They're frozen moments of "what I believed when I wrote this."
</details>

### Section 8: "Question 2: Who Am I Trying to Impress?"

**Narrative Beat:** Discover how narrative shifts by audience

> *The cloud migration project appeared in four documents. Each described it differently:*
>
> - *Resume v1 (for technical roles): "Led technical migration to AWS infrastructure"*
> - *Cover Letter (for management role): "Managed cross-functional cloud adoption initiative"*
> - *LinkedIn (public audience): "Directed enterprise cloud strategy and transformation"*
>
> *Same project. Same months. Same human. Three completely different stories.*

**🎯 VISUALIZATION 3 PLACEMENT: Narrative Shapeshifter**

**Why here:** Shows the pattern across multiple events

**Caption:**
*"How the same events get reframed across documents. Cloud migration emphasized technical skills (9/10) in Resume v1, but strategic vision (9/10) on LinkedIn. Was I a technologist or a strategist? Apparently depends on who's reading."*

**Reflection:**
- We tailor narratives to audience (not deception, just framing)
- Over time, the framing becomes our identity
- Which version is "real"? Maybe all of them? None of them?

**The Bigger Question:**
> *If my professional narrative changes according to whom I tell it, what does that say about identity? Are we our resumes? Our memories? The stories we tell ourselves?*

### Section 9: "Question 3: What Can Machines See That We Miss?"

**Narrative Beat:** Unexpected patterns from LLM analysis

**Surprising Discoveries:**

1. **Skills I Forgot I Had**
   - R programming: dominant 2010-2013, never mentioned after 2015
   - Docker/Kubernetes: learned in 2015, barely mentioned in later docs
   - SQL: consistently present but never highlighted

2. **The Leadership Inflection Point**
   - "Leadership" first appears: 2016 (Cloud Migration Project)
   - Becomes top skill by: 2019 (first management role)
   - Now dominates: 70% of recent documents emphasize it
   - I don't remember deciding to become a "leader"—it emerged

3. **Date Contradictions Beyond Cloud Migration**
   - Python learning: Resume says "proficient since 2010", cover letter says "began 2011"
   - First job end date: August vs. September (1-month discrepancy)
   - Multiple projects with overlapping vs. sequential date ranges

4. **The Sabbatical Erasure**
   - Only mentioned in LinkedIn (public)
   - Completely absent from resumes and cover letters
   - When recounting career from memory: forgotten entirely
   - The machine remembered what I didn't

**Philosophical Moment:**
> *The LLM sees the documents as data, not as stories I'm trying to tell. Let's use the AI to extract and give structure to the data, while only **I** can actually complete the story about who I am.*

---

## Act 4: The Technical Build (600-700 words)

### Section 10: "How ChronoScope Works"

**Narrative Beat:** Show the technical architecture (for technical readers)

**System Components:**

1. **Document Processor**
   - Accepts PDF, DOCX, TXT, Markdown
   - Extracts text while preserving structure
   - Classifies document type (resume, cover letter, etc.)

2. **LLM Event Extractor**
   - GPT-4 API with structured output
   - Custom prompts for different document types
   - Confidence scoring for each extraction
   - Handles fuzzy dates ("Summer 2017", "Fall semester")

3. **Timeline Store**
   - JSON-based persistence
   - Event deduplication across documents
   - Source tracking (which doc mentioned this event)
   - Contradiction detection (same event, different dates)

4. **Visualization Engine**
   - Interactive Plotly timelines
   - Skills evolution stacked area charts
   - Table of extracted Events, Documents
   - Document source network graphs

5. **Streamlit UI**
   - Drag-and-drop document upload
   - Real-time processing with progress indicators
   - Interactive filtering and exploration
   - Export to TimelineJS, JSON, or images

<details markdown="1">
<summary><strong>🔧 Complete Pipeline Code</strong></summary>

```python
from chrono_scope import DocumentProcessor, TimelineStore, TimelineVisualizer

# 1. Initialize components
processor = DocumentProcessor(api_key="YOUR_OPENAI_KEY")
store = TimelineStore("timeline_events.json")

# 2. Process documents
documents = ["resume_v1.pdf", "cover_letter.docx", "linkedin_export.txt"]
for doc in documents:
    events = processor.extract_events(doc)
    store.add_events(events, source=doc)

# 3. Detect contradictions
contradictions = store.find_contradictions()

# 4. Visualize
viz = TimelineVisualizer()
timeline_fig = viz.create_timeline(store.get_all_events())
skills_fig = viz.create_skills_evolution(store.get_all_events())
gaps_fig = viz.create_gap_analysis(store.get_all_events())

# 5. Export for web
timeline_fig.write_html("my_timeline.html")
```
</details>

**Why Streamlit?**
- Rapid prototyping (idea → working app in hours)
- No frontend coding required
- Easy deployment (Streamlit Cloud, Hugging Face Spaces)
- Perfect for data science tools

**Cost Considerations:**
- GPT-4 API: ~$0.03 per resume (typically 1-3k tokens)
- Processing 10 documents: ~$0.30
- Reasonable for personal use, needs controls for public demo

---

## Act 5: The Bigger Picture (500-600 words)

### Section 11: "What This Means Beyond Resumes"

**Narrative Beat:** Universal implications

**Core Principles That Apply Everywhere:**

**🔄 Retroactive Structure Discovery**
Sometimes the best datasets already exist—they just need the right tools to reveal their structure.

**Examples Beyond Resumes:**
- Family photo collections (metadata timelines like beehive story)
- Email archives (relationship networks over time)
- Journal entries (mood and theme tracking)
- Financial records (spending pattern evolution)

**🤖 LLM-Powered Analysis**
Modern AI can provide sophisticated analysis without building custom models from scratch.

**When to use LLMs:**
- Unstructured text needs structure
- Format varies too much for regex
- Domain expertise embedded in language
- Small data (not Big Data)

**📊 Domain Translation**
Raw AI results become valuable when combined with subject matter expertise.

**The Translation Layer:**
- LLM extracts events → Beekeeping/career domain knowledge interprets
- Generic "dates and text" → Meaningful "career inflection points"
- Computer sees patterns → Human provides context

**📈 Progressive Enhancement**
Start with basic organization, layer on advanced analysis as patterns emerge.

**The Roadmap:**
1. Organize chaos → structured timeline
2. Detect contradictions → reconcile discrepancies
3. Find patterns → skills evolution, gaps, narrative shifts
4. Ask bigger questions → identity, memory, truth

### Section 12: "Try It Yourself"

**Narrative Beat:** Call to action with low barrier

**The Interactive Demo**

🔗 **[ChronoScope Timeline Explorer](PLACEHOLDER_URL)** - Explore my real timeline with interactive visualizations

**What You Can Do:**
- Filter by date range, skills, document type
- Click events to see source documents and LLM reasoning
- Compare how narratives shift across document types
- Export visualizations for your own use

**Want to Process Your Own Documents?**

**Option 1: Use the Demo App (Limited)**
- Upload 1-2 documents
- See your timeline in 30 seconds
- Privacy-first: processed in-browser where possible

**Option 2: Clone the Repository (Full Control)**
- Complete ChronoScope codebase on GitHub
- Run locally with your own OpenAI API key
- Process unlimited documents
- Customize visualizations and prompts

🐙 **[GitHub Repository](https://github.com/YOUR_USERNAME/chronoscope)**

<details markdown="1">
<summary><strong>🚀 Quick Start Guide</strong></summary>

```bash
# Clone and install
git clone https://github.com/YOUR_USERNAME/chronoscope
cd chronoscope
pip install -r requirements.txt

# Configure API key
export OPENAI_API_KEY="your-key-here"

# Run Streamlit app
streamlit run chrono_scope/ui/streamlit_app.py

# Upload your resumes and explore!
```

**What You'll Need:**
- Python 3.11+ environment
- OpenAI API key ($5 free credit for new accounts)
- Your career documents (resume, CV, cover letters)
- Curiosity about what patterns might be hiding
</details>

---

## Conclusion: The Truth About Truth (400-500 words)

### Section 13: "Documents vs. Memory: Which Wins?"

**Narrative Beat:** Philosophical resolution

> *So, did the cloud migration happen in 2016-2017 or 2017-2018? ChronoScope can't answer that. What it can do is show me that I've told both stories with conviction, and reveal when each framing served a purpose.*
>
> *The documents aren't "truth"—they're frozen narratives from specific moments in time. My Resume v1 emphasized technical leadership because I was applying for senior IC roles. Cover Letter emphasized strategic management because I wanted to move into management. LinkedIn balanced both because the audience was everyone.*
>
> *All three are "true" in the sense that they reflect what I believed—or wanted to convey—when I wrote them. None is objectively true in the sense of "this is exactly what happened."*

**The Real Insight:**
- We are not our timelines
- We are not our narratives
- We are the messy, contradictory, evolving humans who create them

**The Dad Argument Redux:**
> *As for whether we moved in 2003 or 2004? I still don't know. But now I know why we'll never agree: we each have our own timeline, frozen in memory at the moment we stopped paying attention. Neither is more real than the other.*
>
> *What ChronoScope gave me isn't the truth. It's something better: awareness that there are multiple truths, and they're all worth examining.*

**What's Next:**
- Part 2: Advanced features (multi-person timelines, relationship graphs)
- Part 3: The validation framework (comparing LLM accuracy across models)
- Part 4: The community (what patterns emerge across hundreds of users)

---

## Closing: The Invitation

**Final Paragraph:**

> *Whether you're drowning in career documents, family photos, or journal entries, the same principle applies: your data has stories to tell, if you know how to listen. Sometimes the most interesting discoveries aren't about finding the truth—they're about realizing you've been telling different truths all along.*
>
> *What stories are hiding in your documents? Build your timeline and find out.*

**Call-to-Action:**
- 🔗 Try the demo: [ChronoScope Explorer](PLACEHOLDER_URL)
- 🐙 Clone the code: [GitHub](https://github.com/YOUR_USERNAME/chronoscope)
- 💬 Share your discoveries: Tag #ChronoScope with your timeline insights
- 📧 Questions? barbara@barbhs.com

---

## Author Bio

*Barbara is a Certified Data Management Professional (CDMP) who discovered that the intersection of data science, LLMs, and personal storytelling raises more interesting questions than it answers. When not arguing with her dad about dates, she helps organizations untangle their messy data. Follow her work at [barbhs.com].*

---

## SEO & Metadata

**Primary Keywords:**
- Personal timeline visualization
- LLM document extraction
- Resume timeline analysis
- Career timeline tool
- Memory vs. data accuracy

**Secondary Keywords:**
- Plotly timeline charts
- Streamlit data apps
- OpenAI API projects
- Document processing with AI
- Professional narrative analysis

**Meta Description (Personal Blog):**
"I built an LLM-powered timeline to settle arguments with my dad about dates—and discovered my own resumes contradict each other. A data scientist's journey into memory, narrative, and truth."

**Meta Description (Medium):**
"My resumes tell different stories about the same events. Here's what happened when I built an AI tool to extract my career timeline from documents—and found a 6-month gap I'd completely forgotten."

**Estimated Reading Time:**
- Personal Blog: 18-20 minutes
- Medium: 12-15 minutes

**Target Publish Date:**
- Personal Blog: [YOUR DATE]
- Medium Syndication: +1 week after blog

---

## Assets Checklist

**Visualizations:**
- [ ] Viz 2: Narrative Shapeshifter (grouped bar chart)
- [ ] Viz 4: Skills Evolution (stacked area chart)
- [ ] Viz 5: Gap Analysis (Gantt chart)

**Screenshots/Images:**
- [ ] ChronoScope UI screenshot (document upload)
- [ ] Sample timeline visualization
- [ ] Document contradiction example (side-by-side)
- [ ] Mobile-responsive fallback images

**Code Snippets:**
- [ ] Sample LLM prompt
- [ ] Quick start installation code
- [ ] Event extraction example

**Interactive Elements:**
- [ ] Embedded Plotly HTML files
- [ ] Link to live demo app
- [ ] Link to GitHub repository

**Supporting Materials:**
- [ ] Jupyter notebook with full analysis
- [ ] Sample synthetic dataset (for readers to try)
- [ ] Video walkthrough (optional)

---

## Adaptation Notes for Medium

**Changes for Medium Version:**

1. **Cut 30-40%:**
   - Condense technical deep-dive sections
   - Remove some collapsible details
   - Shorter code snippets

2. **Adjust Opening:**
   - Hook needs to grab in first 3 sentences
   - Medium readers won't know you, need stronger intro

3. **Visualization Considerations:**
   - Embed images as fallbacks (Medium's iframe support is limited)
   - Link to "full interactive version" on personal blog

4. **Reduce External Links:**
   - Medium algorithm penalizes external links
   - Save GitHub/demo links for conclusion only

5. **Add Engagement Hooks:**
   - "Clap if you've had this experience"
   - "Follow for Part 2 on [topic]"
   - Highlight option at key insights

6. **SEO Optimization:**
   - Broader keywords ("organize career documents" vs. "LLM timeline extraction")
   - More accessible language (less jargon)
   - Stronger personal narrative thread

---

**NEXT STEPS:**
2. Generate all 3 visualizations with synthetic data
3. Write full draft following this outline
4. Create demo app with API cost controls
5. Test with real documents and refine
6. Publish to personal blog
7. Adapt and syndicate to Medium
