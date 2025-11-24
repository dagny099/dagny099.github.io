---
layout: single
title: "Multi-Provider AI Chat"
permalink: /projects/convoscope/
classes: [project, hero, wide]
author_profile: false
read_time: false
toc: true
toc_sticky: true
order: 30

# taxonomy
tags: [llm, multi-provider, chat, model-comparison, streamlit]
stack: [Python, Streamlit, LiteLLM, OpenAI, Anthropic, Google Gemini]
status: Active

# Make the header a true hero
header:
  teaser: /assets/images/projects/convoscope/card.jpg
  overlay_image: /assets/images/projects/convoscope/hero.jpg
  overlay_filter: 0.25
  caption: "Switch providers, compare models, keep your conversations"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/convoscope
      class: "btn--primary"
    - label: "Read Docs"
      url: https://docs.barbhs.com/convoscope/
      class: "btn--light-outline"

# Gallery (keep if images exist)
gallery:
  - url: /assets/images/projects/convoscope/s1.jpg
    image_path: /assets/images/projects/convoscope/s1.jpg
    alt: "Chat interface"
    title: "Chat"
  - url: /assets/images/projects/convoscope/s2.jpg
    image_path: /assets/images/projects/convoscope/s2.jpg
    alt: "Model comparison"
    title: "Compare"

# For cards/site previews
excerpt: "When OpenAI has an outage, my work shouldn't stop. Convoscope is a multi-provider chat application that routes requests across OpenAI, Anthropic, and Google with automatic fallback—plus a model comparison tool for evaluating which provider actually performs better on specific tasks. Self-hosted, with full conversation history you control."
last_modified_at:
url: /projects/convoscope/
btn_label: "Project"
docs_url: https://docs.barbhs.com/convoscope/
docs_label: "Docs"
---

{% include page__taxonomy.html %}

**30-second version:** Convoscope is a self-hosted chat application that works with OpenAI, Anthropic, and Google Gemini simultaneously. If one provider goes down or rate-limits you, it automatically switches to another. It also includes a model comparison tool for running the same prompt against multiple models with blind scoring—so you can actually measure which model works better for your use case.

<details>
<summary><strong>2-minute version</strong></summary>

I kept running into the same problem: I'd be deep in a work session using GPT-4, and OpenAI would have an outage. Or I'd hit rate limits. Or I'd wonder if Claude would actually be better for this particular task but have no systematic way to compare.

Commercial chat interfaces lock you into one provider. They don't let you switch mid-conversation, and your conversation history lives on their servers in their format.

Convoscope solves this by abstracting across providers:

- **Automatic fallback**: OpenAI down? Requests route to Anthropic. Anthropic down? Google Gemini. No manual intervention needed.
- **Model comparison**: Run the same prompt against 2-4 models simultaneously, score them blind (randomized A/B/C labels), and log results for later analysis.
- **Your data**: Conversations save as JSON files on your machine. Export to HTML for sharing. No vendor lock-in.

It's built with Streamlit and uses LiteLLM for the provider abstraction layer. The architecture is intentionally simple—file-based storage, modular services, comprehensive tests—because this is a tool I actually use, not a demo.

</details>

---

## Problem

Single-provider LLM tools have a reliability problem:

| Issue | Impact |
|-------|--------|
| Provider outages | Work stops until service recovers |
| Rate limits | Throttled mid-session with no alternative |
| Model uncertainty | "Is Claude better for this?" becomes untestable guesswork |
| Data lock-in | Conversation history trapped in provider interface |
| No comparison baseline | Can't systematically evaluate model performance |

When you're using AI tools for actual work, these aren't minor inconveniences—they're workflow blockers.

---

## How It Works

### Provider Routing

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   OpenAI    │────▶│  Anthropic  │────▶│   Google    │
│   (GPT-4)   │     │  (Claude)   │     │  (Gemini)   │
└─────────────┘     └─────────────┘     └─────────────┘
       │                  │                   │
       └──────────────────┴───────────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │  LiteLLM      │
                  │  Abstraction  │
                  └───────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │  Streamlit    │
                  │  Interface    │
                  └───────────────┘
```

The system checks which providers have valid API keys at startup, then routes requests through the fallback chain. If a request fails (timeout, rate limit, server error), it automatically retries with the next available provider.

### Model Comparison

The comparison tool runs the same prompt against multiple models simultaneously:

1. **Select models**: Choose 2-4 models from available providers
2. **Submit prompt**: Same input goes to all selected models
3. **Blind scoring**: Responses appear with randomized labels (A, B, C) to reduce bias
4. **Rate responses**: 5-point rubric for correctness, usefulness, clarity, safety, overall
5. **Reveal and log**: See which model was which, results saved to JSONL

This creates a personal dataset of model performance across your actual use cases—not benchmarks, but real tasks.

### Conversation Management

| Feature | How It Works |
|---------|--------------|
| **Auto-save** | Conversations persist after each exchange |
| **Manual save** | Name and save specific conversations |
| **Load previous** | Browse and resume past conversations |
| **Export** | Generate styled HTML for sharing |
| **Backup** | Atomic writes with rollback on corruption |

All data stays on your machine as JSON files.

---

## What Shipped

### Chat Features
- **7+ models across 3 providers**: GPT-4o, GPT-4o-mini, GPT-3.5-turbo, Claude 3.5 Sonnet, Claude 3 Haiku, Gemini 2.5 Flash, Gemini 2.5 Pro
- **Provider selection**: Switch providers/models mid-session
- **20+ preset system prompts**: Code reviewer, writing editor, research assistant, etc.
- **Custom system prompts**: Define your own personas
- **Temperature control**: Adjust creativity/determinism
- **Automatic fallback**: Seamless provider switching on failures

### Comparison Features
- **Side-by-side comparison**: 2-4 models on same prompt
- **Blind scoring interface**: Randomized labels reduce evaluator bias
- **5-point rubric**: Structured evaluation criteria
- **Latency tracking**: Response time per model
- **Cost estimation**: Token counts with provider pricing
- **JSONL logging**: Append-only results for analysis
- **Results viewer**: Filter by date, tags, models

### Data Management
- **Conversation persistence**: Auto-save, manual save, load
- **HTML export**: Styled export with FontAwesome icons
- **JSON storage**: Portable, version-control friendly
- **Backup system**: Corruption detection and recovery

---

## Architecture

| Layer | Component | Technology |
|-------|-----------|------------|
| **UI** | Chat interface, comparison views | Streamlit |
| **Provider Abstraction** | Unified API across providers | LiteLLM |
| **Services** | LLM routing, conversation management | Python modules |
| **Storage** | Conversation history, comparison results | JSON, JSONL files |

<details>
<summary><strong>Service Layer</strong></summary>

**LLM Service** handles provider routing:
- Checks API key availability at startup
- Validates model names against provider
- Implements retry logic with exponential backoff
- Normalizes error responses across providers

**Conversation Manager** handles persistence:
- Atomic file writes (temp file + rename)
- JSON validation on load
- Filename sanitization
- Auto-backup before destructive operations

</details>

<details>
<summary><strong>Why These Choices</strong></summary>

**Streamlit over React**: Faster development for a tool I use myself. Trade-off is less UI customization.

**LiteLLM for abstraction**: Handles the differences between OpenAI, Anthropic, and Google APIs. One interface, multiple providers.

**File-based storage over database**: Simpler deployment, easier to back up, portable. For a personal tool, the scale doesn't require a database.

**JSONL for comparison results**: Append-only logging prevents accidental data loss. Easy to analyze with pandas.

</details>

---

## Supported Models

| Provider | Models | Notes |
|----------|--------|-------|
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-3.5-turbo | Requires `OPENAI_API_KEY` |
| **Anthropic** | claude-3-5-sonnet, claude-3-haiku | Requires `ANTHROPIC_API_KEY` |
| **Google** | gemini-2.5-flash, gemini-2.5-pro | Requires `GOOGLE_API_KEY` |

The system works with any subset of these—if you only have an OpenAI key, it runs with just OpenAI (no fallback, but still functional).

---

## What's Next

**Current focus:**
- Additional model support as providers release new versions
- Improved comparison analytics (aggregate trends over time)
- Prompt library management

**Possible future:**
- Streaming responses for long generations
- Conversation branching (fork from any point)
- Cost tracking dashboard

---

## Links

[View Repository](https://github.com/dagny099/convoscope){: .btn .btn--primary}
[Read Documentation](https://docs.barbhs.com/convoscope/){: .btn .btn--light-outline}
