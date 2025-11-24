---
layout: single
title: "Beehive Analytics Platform"
permalink: /projects/beehive-tracker/
classes: [project, hero, wide]
author_profile: false
read_time: false
toc: true
toc_sticky: true
order: 20

# taxonomy
tags: [computer-vision, data-pipeline, api-integration, streamlit]
stack: [Python, Streamlit, Plotly, Google Cloud Vision, Open-Meteo API, Docker]
status: WIP

# Make the header a true hero
header:
  teaser: /assets/images/projects/hivetracker/card.jpg
  overlay_image: /assets/images/projects/hivetracker/hero.jpg
  overlay_filter: 0.25
  caption: "A little structure transforms photo clutter into beekeeping intelligence"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/beehive-tracker/
      class: "btn--primary"
    - label: "Read Docs"
      url: https://docs.barbhs.com/beehive-tracker/
      class: "btn--light-outline"

# For cards/site previews
excerpt: 'When honey bees unexpectedly moved into our owl box, I started photographing everything. Four years later, I had hundreds of photos scattered across devices with unhelpful names like "IMG_2847.jpg." This platform uses photo timestamps, computer vision, and weather data to automatically reconstruct our beekeeping story—turning raw documentation into structured intelligence where proper cataloging unlocks insights invisible in unorganized collections.'
last_modified_at:
url: /projects/beehive-tracker/
btn_label: "Project"
docs_url: https://docs.barbhs.com/beehive-tracker/
docs_label: "Docs"
---

{% include page__taxonomy.html %}

**30-second version:** Beehive Analytics transforms scattered inspection photos into a searchable, analyzable knowledge base. Upload photos, and the system automatically extracts timestamps, correlates weather conditions, runs computer vision to detect hive components, and renders everything on an interactive timeline—so you can finally answer questions like "what did inspections look like before the swarm?" or "how does brood pattern correlate with temperature?"

<details>
<summary><strong>2-minute version</strong></summary>

When bees moved into our owl box in 2020, I did what any curious person would do: I started documenting. Four years later, I had hundreds of photos across phones, cameras, and cloud storage—all with names like "IMG_2847.jpg" and no reliable way to search, compare, or learn from them.

The friction wasn't just organizational. I wanted to answer questions that required correlating multiple data sources: What were conditions like before the swarm? Is there a pattern between weather and foraging activity? Which frames showed early signs of problems I missed at the time?

This platform addresses that gap by treating inspection photos as structured data rather than digital clutter. The system extracts EXIF metadata (using a multi-library approach to handle diverse camera formats), enriches it with historical weather data via Open-Meteo API, runs Google Cloud Vision to detect hive components and bee activity, and stores everything in a queryable format.

The result is an interactive timeline where each inspection becomes a node with rich context—GPS coordinates, temperature, precipitation, dominant colors, detected objects—all without manual data entry. What was once a folder of mystery photos becomes a structured record of hive health over time.

</details>

---

## Problem

Beekeepers capture inspection photographs but lack systematic tools to:
- **Track patterns over time** with objective data rather than memory
- **Correlate visual observations** with environmental conditions
- **Search historical data** efficiently ("show me all inspections before swarm events")
- **Make data-driven decisions** about seasonal preparation and intervention timing

Current approaches require manual documentation. Patterns that span seasons—queen health trends, forage availability cycles, early pest indicators—rarely make it into a system of record because the overhead is too high.

### The Real Friction

| Challenge | Impact |
|-----------|--------|
| Photos scattered across devices | Can't find specific inspections when needed |
| Unhelpful filenames (IMG_2847.jpg) | No searchability without manual renaming |
| Weather context lost | "Was it hot that day?" requires separate lookup |
| Visual patterns invisible | Subtle changes over months go unnoticed |
| Manual logging abandoned | Too much friction → incomplete records |

---

## How It Works

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Upload    │───▶│    EXIF     │───▶│     GPS     │
│   Photos    │    │ Extraction  │    │ Validation  │
└─────────────┘    └─────────────┘    └─────────────┘
                                            │
       ┌────────────────────────────────────┘
       ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Weather   │◀───│  Computer   │◀───│   Color     │
│ Integration │    │   Vision    │    │  Analysis   │
└─────────────┘    └─────────────┘    └─────────────┘
       │
       ▼
┌─────────────┐    ┌─────────────┐
│  Structured │───▶│  Timeline   │
│   Storage   │    │    View     │
└─────────────┘    └─────────────┘
```

| Stage | What Happens |
|-------|--------------|
| **Photo Upload** | Multi-format support; inspection grouping wizard |
| **EXIF Extraction** | Three-library cascade (PIL → ExifRead → PyExifTool) handles diverse camera formats |
| **GPS Validation** | Coordinate normalization; location verification |
| **Color Analysis** | Dominant palette extraction for honeycomb health indicators |
| **Computer Vision** | Google Cloud Vision API: label detection, object localization, confidence scoring |
| **Weather Integration** | Open-Meteo API lookup by GPS + timestamp → temperature, precipitation, wind |
| **Structured Storage** | JSON/CSV with storage abstraction (local → S3 → GCS ready) |
| **Timeline Rendering** | Interactive Plotly timeline, calendar heatmap, photo gallery |

<details>
<summary><strong>Multi-Library EXIF Strategy</strong></summary>

Different cameras encode EXIF data differently—smartphones vs DSLRs vs action cameras. A single library fails on ~30% of real-world photos. The solution: cascade through three libraries in order of speed vs comprehensiveness.

```python
def extract_metadata(image_path):
    """Try multiple libraries with fallback."""
    metadata = {}

    # Fast path: PIL handles most smartphone photos
    metadata = try_pil_extraction(image_path)
    if has_required_fields(metadata):
        return metadata

    # Fallback: ExifRead for more formats
    metadata = merge(metadata, try_exifread(image_path))
    if has_required_fields(metadata):
        return metadata

    # Last resort: PyExifTool (most comprehensive)
    return merge(metadata, try_exiftool(image_path))
```

This approach reduced metadata extraction failures from 30% to under 5%.

</details>

<details>
<summary><strong>Weather Data Integration</strong></summary>

Open-Meteo provides historical weather data with:
- 40+ year archive
- Hourly granularity
- Free tier covering typical usage (50-100 inspections/month)
- No authentication overhead

For each photo with valid GPS and timestamp, the system fetches:
- Temperature (°C)
- Precipitation (mm)
- Cloud cover (%)
- Wind speed (km/h)
- Weather condition codes

Caching prevents redundant API calls for photos from the same location/day.

</details>

---

## What Shipped

### Core Features
- **Interactive Timeline**: Chronological inspection history with Plotly; click-to-select inspections
- **Calendar View**: Multiple modes (day grid, resource timeline, list); color-coded by photo count
- **Photo Gallery**: Grid-based browsing organized by inspection date
- **Bulk Import Wizard**: 4-step process supporting local directories, AWS S3, URL lists

### Data Extraction
- **Multi-Library EXIF**: PIL/ExifRead/PyExifTool cascade for 95%+ success rate
- **GPS Normalization**: Format validation and coordinate standardization
- **Color Palette Analysis**: Dominant color extraction using ColorThief; honeycomb health indicators
- **Timezone Handling**: Multi-format timestamp parsing with timezone support

### API Integration
- **Google Cloud Vision**: Label detection, object localization, image properties with custom confidence thresholds optimized for agricultural imagery
- **Open-Meteo Weather**: Historical weather correlation by location and timestamp
- **Rate Limiting**: Retry mechanisms for API resilience

### Infrastructure
- **Storage Abstraction**: Pluggable backends (local → S3 → GCS) without code changes
- **Session State Management**: Multi-page Streamlit navigation with persistent state
- **Docker Deployment**: Production image with health checks; Cloud Run ready
- **CSV/JSON Export**: External analysis compatibility (R/Python)

---

## Architecture

| Layer | Components | Technology |
|-------|------------|------------|
| **UI** | Multi-page app, visualizations | Streamlit 1.44+, Plotly 6.0 |
| **Processing** | Metadata extraction, analysis | PIL, ColorThief, ExifRead, PyExifTool |
| **API** | External integrations | Google Cloud Vision 3.7, Open-Meteo |
| **Storage** | Data persistence | JSON/CSV, S3-compatible abstraction |

<details>
<summary><strong>Why Streamlit?</strong></summary>

The choice of Streamlit over traditional web frameworks was deliberate:

- **80% faster development** for data-centric UIs
- **Built-in session state** handles complex multi-step workflows
- **Native Pandas/Plotly integration** without custom API layers
- **Single Python codebase** simplifies deployment and maintenance

Trade-offs accepted: less UI customization, Streamlit-specific patterns required.

</details>

<details>
<summary><strong>Storage Abstraction Pattern</strong></summary>

The storage layer uses a simple abstraction that enables seamless migration:

```python
class StorageBackend(Protocol):
    def read(self, key: str) -> bytes: ...
    def write(self, key: str, data: bytes) -> None: ...
    def list(self, prefix: str) -> list[str]: ...

# Implementations
class LocalStorage(StorageBackend): ...
class S3Storage(StorageBackend): ...
class GCSStorage(StorageBackend): ...
```

Benefits:
- Zero breaking changes during migration
- Atomic write operations with backup
- Version control friendly formats

</details>

---

## Implementation Notes

### Testing Strategy

Risk-based approach targeting high-value coverage:

| Risk Level | Examples | Testing Approach |
|------------|----------|------------------|
| **High** | Core flows, session state, API calls | Full test coverage with mocks |
| **Medium** | Secondary features, UI logic | Standard unit tests |
| **Low** | Styling, configuration | Minimal/manual testing |

All API tests use mocks—no real API calls in test suite.

### Key Design Decisions

1. **Multi-library EXIF extraction** addresses real-world camera diversity
2. **Weather integration at ingest time** enriches data before storage
3. **Storage abstraction** enables cloud migration without refactoring
4. **Confidence thresholds** tuned for agricultural imagery (bees, honeycomb, frames)

---

## What's Next

**Current Phase (Storage Optimization)**
- Cloud storage integration (S3/GCS) for production deployment
- Backup and sync strategies

**Future Enhancements**
- Graph database for relationship queries ("inspections before swarm events")
- Custom CV model trained on beekeeping-specific imagery
- Mobile-friendly capture interface
- Multi-hive comparison views
- Community data sharing (anonymized patterns)

---

## Links

[View Repository](https://github.com/dagny099/beehive-tracker/){: .btn .btn--primary}
[Read Documentation](https://docs.barbhs.com/beehive-tracker/){: .btn .btn--light-outline}
