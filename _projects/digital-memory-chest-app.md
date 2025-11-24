---
layout: single
title: "Digital Memory Chest: AI-Powered Memorial Tributes"
permalink: /projects/digital-memory-chest/
classes: [project]
author_profile: false
read_time: false
toc: true
toc_sticky: true
toc_label: "Contents"
toc_icon: "heart"
order: 2
tags: [AI, NLP, Computer Vision, Streamlit, Memorial, Whisper, CLIP, OpenAI, Anthropic]
categories: ["Data Products & Interfaces"]
stack: [Python, Streamlit, SQLModel, Whisper, CLIP ViT-B/32, OpenAI API, Anthropic API, SQLite, PostgreSQL]
status: WIP
header:
  teaser: assets/images/portfolio/memory-chest-teaser.png
  overlay_image: assets/images/portfolio/memory-chest-gallery.png
  overlay_filter: 0.3
  caption: "Preserving memories with respect and care"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/digital-memory-chest
      class: "btn--primary"
    - label: "Documentation"
      url: https://github.com/dagny099/digital-memory-chest/tree/main/docs
      class: "btn--light-outline"
excerpt: "When someone passes, their memories live scattered across phones, hard drives, and shoeboxes. Digital Memory Chest helps families gather those fragments—photos, videos, voice recordings—and transforms them into a lasting tribute. AI handles the tedious work (transcription, organization, narrative generation) so families can focus on remembering."
url: /projects/digital-memory-chest/
btn_label: "Project"
docs_url: https://github.com/dagny099/digital-memory-chest/tree/main/docs
docs_label: "Documentation"
---

Grief is not the time for tedious organization work. **Digital Memory Chest uses AI to lift that burden**—automatically transcribing voice recordings, tagging photos, and weaving memories into coherent narratives—while keeping sensitive content private by design. Families contribute memories through secure links, and the system generates a timeline that honors the person's journey.

{% include page__taxonomy.html %}

---

## Why This Matters

**Memories fragment across time and technology.** Photos on old phones. Voice messages in forgotten apps. Videos on drives that no one has opened in years. When someone passes, gathering these fragments feels both urgent and overwhelming.

**Manual organization is the last thing grieving families need.** Sorting hundreds of files, transcribing recordings, writing captions—these tasks demand emotional energy that's already depleted.

**AI can help without feeling intrusive.** The key is respectful design: locally processed content, carefully crafted prompts that produce empathetic narratives, and privacy controls that keep sensitive memories secure. Digital Memory Chest applies AI where it reduces burden, not where it might feel cold or inappropriate.

---

## How It Works

```
📤 Upload Memories → 🤖 AI Processing → 📖 Story Generation → 🔗 Family Sharing
```

### The Pipeline

| Stage | What Happens |
|-------|--------------|
| **Upload** | Photos, videos, audio recordings, or text memories added to a "chest" |
| **Processing** | Async AI pipeline extracts metadata, generates thumbnails |
| **Transcription** | Whisper converts audio/video to searchable text |
| **Tagging** | CLIP classifies images with memorial-appropriate labels |
| **Narrative** | LLM generates respectful timeline, themes, and story |
| **Sharing** | Secure tokens let family contribute with moderation approval |

<details>
<summary><strong>AI pipeline details</strong></summary>

**Transcription (Whisper)**
- Local Whisper model or OpenAI API
- Handles audio files and video soundtracks
- Output stored as searchable text with timestamps

**Image Classification (CLIP ViT-B/32)**
- Zero-shot classification with memorial-appropriate labels
- Categories: family gatherings, celebrations, travel, portraits, nature, etc.
- No training required—works out of the box

**Story Generation (OpenAI/Anthropic)**
- Carefully crafted prompts for empathetic tone
- Generates: chronological timeline, recurring themes, narrative summary
- Graceful fallback to templates when APIs unavailable

</details>

---

## What Shipped

### Core Features

- **Professional memorial interface** with dignified design, elegant card layouts, and respectful hover interactions
- **Rich media support** — Photos, videos, audio recordings, and text memories with unified presentation
- **AI transcription** — Whisper-based audio/video → text conversion
- **AI image tagging** — CLIP zero-shot classification with memorial-appropriate labels
- **Story generation** — LLM-created narratives with timeline and thematic analysis
- **Collaborative sharing** — Secure contribution links with moderation workflow
- **Demo mode** — One-command setup creates sample memorial for "Eleanor Thompson"

### Production Readiness

- **Database**: SQLModel works seamlessly with SQLite (development) and PostgreSQL (production)
- **Storage**: Abstracted layer supports local files and S3-compatible storage
- **AI fallbacks**: Template-based narratives when APIs are unavailable
- **Error handling**: Async processing with progress tracking and graceful degradation

---

## Architecture

### Core Models

| Model | Purpose |
|-------|---------|
| **Chest** | Memorial container — person's name, life dates, hero image |
| **Asset** | Individual memory — file, AI-extracted metadata, thumbnails |
| **Contribution** | User-submitted memory pending moderation |
| **Story** | Generated narrative with timeline and themes |

<details>
<summary><strong>Project structure</strong></summary>

```
src/
├── config.py              # Centralized configuration
├── db/
│   ├── models.py          # SQLModel definitions
│   └── operations.py      # Database queries and CRUD
├── ai/
│   ├── transcription.py   # Whisper integration
│   ├── image_tagging.py   # CLIP classification
│   ├── media_processor.py # Unified async processing
│   └── story_generation.py # LLM narrative creation
└── ui/                    # Streamlit components

app.py                     # Main application
scripts/
├── seed_demo_data.py      # Demo memorial setup
└── ...
```

</details>

### Data Flow

```
Upload → Save file + extract metadata → Generate thumbnail
           ↓
       Queue for AI processing
           ↓
       Transcription (if audio/video)
           ↓
       Image tagging (if photo)
           ↓
       Update asset metadata
           ↓
       Story generation (on demand)
           ↓
       Display in Gallery with filters
```

---

## Privacy & Security

Memorial content is deeply personal. The architecture reflects that sensitivity:

### Privacy-First Design

| Principle | Implementation |
|-----------|----------------|
| **Share tokens over public IDs** | Contributions use unguessable tokens, not sequential IDs |
| **Local processing options** | Whisper can run locally; no data leaves your machine |
| **Minimal PII storage** | Only what's necessary for the memorial |
| **Moderation workflow** | Contributions require approval before appearing |
| **Soft deletes** | Nothing permanently destroyed without explicit action |

### Contribution Flow

```
Family member receives share link
        ↓
Uploads memory with optional note
        ↓
Contribution enters moderation queue
        ↓
Chest owner reviews and approves
        ↓
Memory appears in Gallery
```

This prevents unwanted content while enabling collaborative memory gathering.

---

## Implementation Notes

**Async processing with progress tracking:**
- Media processing runs asynchronously
- Users see real-time progress for large uploads
- Failed processing gracefully falls back to unprocessed display

**Graceful AI fallbacks:**
```python
# Story generation with fallback chain
try:
    narrative = await generate_with_openai(memories)
except APIError:
    try:
        narrative = await generate_with_anthropic(memories)
    except APIError:
        narrative = generate_template_based(memories)
```

**Database portability:**
- SQLModel abstracts SQLite vs. PostgreSQL
- Same models work in development and production
- Migration path built-in for scaling

**Respectful prompt engineering:**
- LLM prompts emphasize empathy and dignity
- Avoid generic platitudes; focus on specific memories
- Tone calibrated for memorial context

---

## What's Next

- **Enhanced moderation workflow** — Batch approval, contributor attribution
- **Export formats** — PDF memory book, printable timeline
- **Multi-language support** — Transcription and narratives in multiple languages
- **Relationship mapping** — Visualize connections between people in memories
- **Timeline refinement** — Better date extraction from photo EXIF and context

---

## Demo

```bash
# One-command demo with sample data
git clone https://github.com/dagny099/digital-memory-chest
cd digital-memory-chest
pip install -r requirements.txt
python run_demo.py
```

Creates a complete memorial for "Eleanor Thompson" with sample photos, videos, and generated narratives. Opens at `http://localhost:8501`.

---

## Links

[View Repository](https://github.com/dagny099/digital-memory-chest){: .btn .btn--primary}
[Documentation](https://github.com/dagny099/digital-memory-chest/tree/main/docs){: .btn .btn--light-outline}

**Quick links:**
- [Installation Guide](https://github.com/dagny099/digital-memory-chest/blob/main/docs/getting-started/installation.md)
- [Gallery Guide](https://github.com/dagny099/digital-memory-chest/blob/main/docs/user-guide/gallery.md)
- [Privacy & Security](https://github.com/dagny099/digital-memory-chest/blob/main/docs/user-guide/privacy.md)
- [Developer Setup](https://github.com/dagny099/digital-memory-chest/blob/main/docs/developer/setup.md)

---

*This application handles sensitive memorial content. Built with respect for those using it during difficult times.*
