---
layout: single
title: "ChronoScope: AI-Powered Timeline Builder"
permalink: /projects/chronoscope/
classes: [project]
author_profile: false
read_time: false
toc: true
toc_sticky: true
toc_label: "Contents"
toc_icon: "clock"
order: 4
tags: [NLP, GenAI, OpenAI, Streamlit, Visualization, Document Processing, Timeline, Plotly]
categories: ["Data Products & Interfaces"]
stack: [Python, Streamlit, Plotly, OpenAI GPT, PyMuPDF, pdfplumber, TimelineJS, NetworkX, MkDocs]
status: WIP
header:
  teaser: assets/images/portfolio/chronoscope-teaser.png
  overlay_image: assets/images/portfolio/chronoscope-timeline.png
  overlay_filter: 0.25
  caption: "Transform your documents into interactive timelines"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/chrono-scope
      class: "btn--primary"
    - label: "Documentation"
      url: https://chronoscope-docs.github.io
      class: "btn--light-outline"
excerpt: "Your career story is scattered across resumes, cover letters, and LinkedIn profiles—but seeing the full arc requires manual assembly. ChronoScope extracts life events from documents using AI and renders them as interactive timelines, with all processing happening locally so your data never leaves your machine."
url: /projects/chronoscope/
btn_label: "Project"
docs_url: https://chronoscope-docs.github.io
docs_label: "Documentation"
---

Drop a resume, cover letter, or personal document into ChronoScope and watch your career materialize as an interactive timeline. **The differentiator: privacy-first architecture where all extraction happens locally**, plus a validation system that assigns confidence scores instead of blindly trusting AI output. Export to TimelineJS for polished presentations or explore relationships in a knowledge graph.

{% include page__taxonomy.html %}

---

## Why This Matters

**The gap between "I have documents" and "I can see my journey."** Resumes are optimized for job applications, not reflection. Cover letters highlight specific moments. LinkedIn profiles follow a rigid format. None of them show the full arc of your professional life—the threads connecting education to career pivots to skill development.

**Manual timeline creation is tedious.** You could build one by hand, copying dates and descriptions into a spreadsheet. Most people don't, because the effort doesn't justify the insight.

**AI extraction changes the equation.** Feed ChronoScope your documents and it identifies events, dates, locations, and people automatically. But AI can hallucinate—so ChronoScope includes confidence scoring and validation to catch extraction errors before they become timeline artifacts.

---

## How It Works

```
📄 Upload Document → 🤖 AI Extraction → ✅ Validation → 📊 Visualization → 💾 Export
```

### Extraction Pipeline

| Stage | What Happens |
|-------|--------------|
| **Upload** | Accept PDF, TXT, or DOCX; detect document type (resume, cover letter, personal statement) |
| **Extract** | GPT identifies events with dates, locations, people, and context |
| **Fallback** | If LLM fails, rule-based parser extracts structured data |
| **Validate** | Quality checks assign confidence scores; flag uncertain extractions |
| **Store** | Events saved to local JSON with deduplication |
| **Visualize** | Render as Plotly timeline, priority matrix, or network graph |
| **Export** | Download as TimelineJS (6 color schemes, 10 fonts) or Excel |

<details>
<summary><strong>TimelineEvent data model</strong></summary>

```python
@dataclass
class TimelineEvent:
    id: str                    # Unique identifier
    title: str                 # Event name
    description: str           # What happened
    start_date: datetime       # When it started
    end_date: Optional[datetime]  # When it ended (if known)
    location: Optional[str]    # Where it happened
    category: str              # Education, Work, Achievement, etc.
    people: List[str]          # People involved
    tags: List[str]            # User-defined tags
    priority: int              # 1-10 importance rating
    confidence: float          # AI confidence score (0-1)
    source_document: str       # Which document this came from
```

</details>

---

## What Shipped

### Core Features

- **AI-powered extraction** from PDF, TXT, and DOCX using OpenAI GPT with context-aware document classification
- **Dual extraction strategy** — LLM primary with rule-based fallback when API fails
- **Interactive Plotly visualizations** — Timeline charts, priority matrices, and temporal distribution views with filtering and tooltips
- **TimelineJS export** with 6 professional color schemes and 10 font combinations
- **Knowledge graph** — NetworkX visualization showing relationships between events, people, and places (JSON-based + optional Neo4j)
- **User notes** — Capture thoughts alongside your timeline with persistent storage
- **Multi-document processing** — Combine events from multiple sources into unified timeline
- **Quality validation** — Confidence scoring and completeness checks

### Privacy Architecture

All processing happens locally:
- Documents parsed on your machine
- OpenAI API calls send only extracted text (not files)
- Event data stored in local JSON files
- No telemetry, no cloud storage, no data retention

---

## Architecture

### Core Components

| Component | Purpose |
|-----------|---------|
| **DocumentProcessor** | Context-aware extraction with LLM + fallback |
| **TimelineStore** | JSON persistence with filtering, deduplication, CRUD |
| **TimelineVisualizer** | Plotly charts with interactive tooltips |
| **UserNotesStore** | Persistent notes with metadata tracking |

<details>
<summary><strong>Data flow diagram</strong></summary>

```
Document Upload
      ↓
DocumentProcessor
      ├── Document type detection (resume, cover letter, personal)
      ├── LLM extraction (OpenAI GPT)
      │       ↓
      │   (If API fails)
      │       ↓
      └── Fallback parser (rule-based)
              ↓
         Validation
              ↓
         TimelineStore
              ├── Deduplication
              ├── JSON persistence
              └── Filtering/querying
                     ↓
              TimelineVisualizer
                     ↓
              Streamlit UI
```

</details>

### Storage Pattern

**JSON-based with backup/restore:**
- `timeline_events.json` — Single source of truth for events
- `user_notes.json` — User annotations with metadata
- Automatic backup before destructive operations
- Error recovery with graceful fallback

---

## Implementation Notes

### Streamlit Lessons Learned

Building ChronoScope surfaced hard-won lessons about Streamlit's reactive model. These patterns are now codified in the project's [development guide](https://github.com/dagny099/chrono-scope/blob/main/STREAMLIT_BEST_PRACTICES.md):

**The Golden Rules:**

| Rule | Why It Matters |
|------|----------------|
| **Every widget needs an explicit `key`** | Streamlit auto-generates keys by execution order; adding conditionals breaks them |
| **Check file hash before processing** | File uploaders persist across reruns; without deduplication, you get duplicate events |
| **Justify every `st.rerun()`** | Each rerun executes the entire script; multiple reruns cause loops |
| **Cache expensive computations** | Code in main body runs on every rerun; use hash-based caching |

**Widget key registry pattern:**
```python
# Naming convention: {section}_{purpose}
st.selectbox("Color scheme", options, key="export_color_scheme")
st.date_input("Date range", value, key="filter_date_range")
st.slider("Priority", 1, 10, key="filter_priority")
```

**File deduplication pattern:**
```python
file_hash = hashlib.md5(file.read()).hexdigest()
file.seek(0)  # Reset pointer after hashing

if file_hash in st.session_state.processed_files:
    continue  # Skip already-processed file

process_file(file)
st.session_state.processed_files[file_hash] = metadata
```

These patterns eliminated a class of bugs where events were reprocessed on every UI interaction.

---

## What's Next

- **LLM transparency features** — Show extraction reasoning alongside results
- **Formal test suite** — pytest coverage for DocumentProcessor, TimelineStore
- **Performance optimization** — Cache LLM responses to avoid redundant API calls
- **Enhanced date parsing** — Better handling of ambiguous dates and ranges
- **Mobile-responsive design** — Timeline viewing on smaller screens

---

## Use Cases

| Scenario | How ChronoScope Helps |
|----------|----------------------|
| **Career portfolio** | Visualize your professional journey for interviews or self-reflection |
| **Academic timeline** | Track education milestones, publications, research evolution |
| **Life story** | Document personal achievements and memories in chronological context |
| **Project history** | Chart project evolution, deliverables, and team contributions |
| **Team retrospective** | Combine individual timelines into collective achievement visualization |

---

## Screens & Artifacts

*Screenshots from the Streamlit interface:*

- Main timeline view with interactive Plotly chart
- Advanced settings panel with export options
- TimelineJS exported presentation

See [docs/assets/images/](https://github.com/dagny099/chrono-scope/tree/main/docs/assets/images) for interface screenshots.

---

## Links

[View Repository](https://github.com/dagny099/chrono-scope){: .btn .btn--primary}
[Documentation](https://chronoscope-docs.github.io){: .btn .btn--light-outline}

**Developer resources:**
- [Architecture Overview](https://github.com/dagny099/chrono-scope/blob/main/docs/developer/architecture.md)
- [Streamlit Best Practices](https://github.com/dagny099/chrono-scope/blob/main/STREAMLIT_BEST_PRACTICES.md) — Hard-won lessons from debugging
- [ROADMAP.md](https://github.com/dagny099/chrono-scope/blob/main/ROADMAP.md) — Development phases and future plans

---

*Note: ChronoScope is in beta. Core extraction and visualization features are stable; LLM transparency and testing infrastructure are in progress.*
