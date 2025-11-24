---
layout: single
title: "Self-Hosted Workout Intelligence"
permalink: /projects/fitness-dashboard/
classes: [project, hero, wide]
author_profile: false
read_time: false
toc: true
toc_sticky: true
order: 10

# taxonomy
tags: [machine-learning, data-pipeline, etl, analytics, streamlit]
stack: [Python, Streamlit, MySQL, scikit-learn, Plotly, AWS Lambda, AWS RDS]
status: Active

# Make the header a true hero
header:
  teaser: /assets/images/projects/fitness-dashboard/card.jpg
  overlay_image: /assets/images/projects/fitness-dashboard/hero.jpg
  overlay_filter: 0.25
  caption: "14 years of runs, walks, and one transformative rescue dog"
  actions:
    - label: "Live App"
      url: https://workouts.barbhs.com/
      class: "btn--primary"
    - label: "View Repo"
      url: https://github.com/dagny099/fitness-dashboard/
      class: "btn--light-outline"
    - label: "Read Docs"
      url: https://docs.barbhs.com/fitness-dashboard/
      class: "btn--light-outline"

# For cards/site previews
excerpt: 'For years, I meticulously tracked every run—metrics are paramount to a former athlete and current data scientist. But a rescue puppy landing on my doorstep in 2018 transformed my exercise world overnight. What started as pristine running data became an irritatingly unlabeled mix of actual runs and frequent dog walks. This project reclaimed my data: an ML-powered classification system that distinguishes runs from walks, a cloud ETL pipeline for automated ingestion, and interactive dashboards that reveal how adding a four-legged training partner redefined what "consistency" actually means.'
last_modified_at:
url: /projects/fitness-dashboard/
btn_label: "Project"
docs_url: https://docs.barbhs.com/fitness-dashboard/
docs_label: "Docs"
---

{% include page__taxonomy.html %}

**30-second version:** This is a full-stack fitness analytics platform that transforms 14 years of workout data into actionable intelligence. An AWS-based ETL pipeline ingests MapMyRun exports, ML models automatically classify workouts as runs vs. dog walks, and a multi-page Streamlit dashboard surfaces trends, anomalies, and personalized insights—all self-hosted for complete data ownership.

<details>
<summary><strong>2-minute version</strong></summary>

After a decade of tracking every run, I had data but no insights. The metrics lived in a fitness app I didn't control, in a format I couldn't query, with no way to answer questions like "how has my consistency changed over time?" or "what patterns predict my best performances?"

Then in June 2018, a chocolate lab puppy named Choco arrived. Suddenly my pristine running data became contaminated with daily dog walks—all logged as generic "walks" with no distinction from actual training runs. My fitness app couldn't tell the difference. Neither could I, months later, when trying to analyze my running progress.

This project started as a classification problem: build an ML model to distinguish real runs from pup walks based on pace, distance, and duration patterns. It evolved into a complete analytics platform:

- **Cloud ETL Pipeline**: Upload a CSV to S3, Lambda processes and enriches the data, RDS stores it for querying
- **ML Classification**: K-means clustering identifies workout types (real_run, pup_walk, mixed, outlier) with era-based smart defaults
- **Multi-Dimensional Analytics**: Consistency scoring, trend detection, anomaly identification, and forecasting
- **Interactive Dashboard**: Six specialized views including "The Choco Effect"—a data story showing how one dog transformed my exercise patterns

The result? A 4x increase in workout frequency post-Choco, a complete shift in workout composition, and finally, a way to answer "am I actually more consistent now, or does it just feel that way?"

**Live at [workouts.barbhs.com](https://workouts.barbhs.com)**

</details>

---

## The Problem: When a Puppy Breaks Your Data

I had 14 years of running data. Clean, consistent, trackable. Then Choco arrived.

| Before Choco (2011-2018) | After Choco (2018-Present) |
|--------------------------|----------------------------|
| ~4 workouts/month | ~16 workouts/month |
| 95% focused running | Mixed runs + daily dog walks |
| Clear activity labels | Everything labeled "Walk" |
| Easy to analyze | Impossible to distinguish |

The real problem wasn't the data volume—it was **data quality degradation**. My fitness app treated a 3-mile training run the same as a 20-minute pup walk around the block. Trend analysis became meaningless. Progress tracking broke. I couldn't answer basic questions:

- Am I actually running *more* or just walking the dog?
- Has my running pace improved or degraded?
- What does "consistency" even mean now?

### The Deeper Friction

| Challenge | Impact |
|-----------|--------|
| No workout classification | Can't separate training from dog walks |
| Data locked in app | No custom queries or analysis |
| Manual exports only | No automated pipeline |
| Platform dependency | Years of data held hostage |
| No intelligence layer | Raw numbers, no insights |

---

## The Solution: Full-Stack Fitness Intelligence

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        Cloud ETL Pipeline                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │ MapMyRun │───▶│    S3    │───▶│  Lambda  │───▶│   RDS    │          │
│  │   CSV    │    │  Bucket  │    │   ETL    │    │  MySQL   │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘          │
│                                        │                                 │
│                                        ▼                                 │
│                               ┌──────────────┐                          │
│                               │     SNS      │                          │
│                               │ Notification │                          │
│                               └──────────────┘                          │
│                                        │                                 │
└────────────────────────────────────────┼────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     Intelligence & Analytics Layer                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │   K-Means    │  │    Trend     │  │   Anomaly    │                   │
│  │ Classifier   │  │  Detection   │  │  Detection   │                   │
│  └──────────────┘  └──────────────┘  └──────────────┘                   │
│         │                 │                 │                            │
│         └─────────────────┴─────────────────┘                            │
│                           │                                              │
│                           ▼                                              │
│                  ┌──────────────────┐                                   │
│                  │  Consistency     │                                   │
│                  │  Analyzer        │                                   │
│                  └──────────────────┘                                   │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
                                         │
                                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        Streamlit Dashboard                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐           │
│  │    Main    │ │   Choco    │ │   Trends   │ │  Calendar  │           │
│  │ Dashboard  │ │   Effect   │ │  Analysis  │ │    View    │           │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘           │
│                                                                          │
│  ┌────────────┐ ┌────────────┐                                          │
│  │    SQL     │ │   Model    │                                          │
│  │  Explorer  │ │ Management │                                          │
│  └────────────┘ └────────────┘                                          │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## How It Works

### Data Pipeline

| Stage | What Happens |
|-------|--------------|
| **Export** | Download workout history CSV from MapMyRun |
| **Upload** | Move to S3 bucket (triggers Lambda) |
| **Extract** | Parse CSV, validate schema, extract workout IDs |
| **Transform** | Clean data, normalize formats, deduplicate by workout ID |
| **Load** | Insert new records to AWS RDS MySQL |
| **Notify** | SNS notification with row counts |

<details>
<summary><strong>ETL Processing Details</strong></summary>

The Lambda function handles incremental updates by tracking workout IDs:

```python
class WorkoutProcessor:
    """Processes workout data and identifies new records."""

    def process_file(self, file_key: str, existing_ids: List) -> Tuple[int, List[str]]:
        """Process new workout file and identify new records."""
        df = self.storage.read_file(file_key)
        WorkoutDataValidator.validate_dataframe(df)

        # Extract workout IDs from URLs
        new_df = df[~df['workout_id'].isin(existing_ids)]
        new_workout_ids = new_df['workout_id'].tolist()

        return len(new_df), new_workout_ids
```

Key transformations:
- Extract workout_id from MapMyRun URL (used as primary key)
- Convert duration strings to seconds
- Normalize pace formats
- Validate required fields

</details>

### ML Classification System

The intelligence service uses K-means clustering to automatically categorize workouts:

| Classification | Pace Range | Typical Pattern |
|----------------|------------|-----------------|
| **real_run** | 8-12 min/mi | Focused training sessions |
| **pup_walk** | 20-28 min/mi | Dog walking adventures |
| **mixed** | Variable | Combined activities |
| **outlier** | Extreme values | Data quality issues |

<details>
<summary><strong>Era-Based Smart Defaults</strong></summary>

When clustering has insufficient data (<5 workouts), the system uses era-based defaults:

```python
# The Choco Effect Date: June 1, 2018
choco_date = datetime(2018, 6, 1)

# Smart fallback hierarchy:
# 1. Primary: K-means ML clustering (requires ≥5 workouts)
# 2. Secondary: Era-based defaults (medium confidence: 0.5)
#    - Pre-Choco (before 2018-06-01): defaults to real_run
#    - Post-Choco (after 2018-06-01): defaults to pup_walk
# 3. Tertiary: Rule-based classification by pace thresholds
```

This leverages the behavioral pattern: before Choco, I primarily ran. After Choco, walks dominated.

</details>

### Consistency Scoring

Multi-dimensional analysis across four factors:

| Dimension | What It Measures |
|-----------|------------------|
| **Frequency** | Workouts per time period |
| **Timing** | Regularity of workout days/times |
| **Performance** | Stability of pace and distance |
| **Streaks** | Consecutive active days/weeks |

---

## What Shipped

### Dashboard Views

- **AI Intelligence Hub**: Daily briefing with personalized insights, recommendations, and performance summary
- **The Choco Effect**: Data story visualization showing pre/post transformation with interactive timeline
- **Monthly Dashboard**: Calendar view with workout density heatmap and weekly aggregations
- **Trends Analysis**: Statistical trend detection with confidence intervals and forecasting
- **SQL Explorer**: Direct database queries with syntax highlighting and result export
- **Model Management**: View and adjust ML classification parameters

### ML/AI Features

- **K-Means Workout Classifier**: Automatic categorization based on pace, distance, and duration clustering
- **Trend Detection**: Statistical analysis of performance over configurable time windows
- **Anomaly Detection**: IQR, z-score, and modified z-score methods for outlier identification
- **Consistency Scoring**: Multi-dimensional analysis of workout patterns
- **Intelligence Briefing**: Automated generation of personalized insights and recommendations
- **Algorithm Transparency**: Full visibility into how each AI feature makes decisions

### Data Infrastructure

- **Cloud ETL Pipeline**: S3 → Lambda → RDS with SNS notifications
- **Environment-Aware Config**: Automatic switching between dev (local MySQL) and prod (AWS RDS)
- **Incremental Updates**: Workout ID tracking prevents duplicate entries
- **Data Validation**: Schema enforcement and error handling at ingestion
- **Export Capabilities**: CSV/JSON export for external analysis

### Developer Experience

- **Development Mode**: Auth bypass for testing (`STREAMLIT_DEV_MODE=true`)
- **MkDocs Documentation**: Comprehensive user and developer guides
- **Pytest Suite**: Risk-based testing with comprehensive mocking
- **Systemd Deployment**: Production deployment with service management

---

## The Choco Effect: A Data Story

The centerpiece of this project is "The Choco Effect" dashboard—a portfolio-quality demonstration of how one dog transformed 14 years of fitness data.

### The Transformation

| Metric | Pre-Choco (7 years) | Post-Choco (6.5 years) | Change |
|--------|---------------------|------------------------|--------|
| Total Workouts | ~340 | ~1,250 | 3.7x |
| Workouts/Month | ~4 | ~16 | 4x |
| Avg Pace | ~9 min/mi | ~18 min/mi | Slower (walks!) |
| Avg Distance | ~4 mi | ~2 mi | Shorter, more frequent |

### What The Data Shows

The transformation timeline reveals:

1. **Dramatic frequency increase**: From sporadic runner to daily walker
2. **Pace bifurcation**: Clear separation between run pace and walk pace clusters
3. **Consistency improvement**: More regular, smaller efforts vs. infrequent big efforts
4. **Activity composition shift**: From 95% runs to 70% walks + 30% runs

<details>
<summary><strong>The Choco Effect Visualization</strong></summary>

The dashboard creates an interactive timeline showing:
- Monthly workout frequency (bar chart with pre/post coloring)
- Average pace over time (line chart showing the bifurcation)
- Vertical marker at June 2018: "Choco Arrives"
- Before/after comparison cards with key metrics
- AI classification breakdown (pie chart)
- Sample classifications with confidence scores

</details>

---

## Architecture

| Layer | Components | Technology |
|-------|------------|------------|
| **Data Ingestion** | ETL pipeline, validation | AWS Lambda, S3, SNS |
| **Storage** | Workout database | AWS RDS (MySQL) |
| **Intelligence** | Classification, analytics | scikit-learn, scipy |
| **Visualization** | Interactive charts | Plotly, Streamlit |
| **UI** | Multi-page dashboard | Streamlit 1.44+ |
| **Infrastructure** | Deployment, config | Docker, systemd, TOML |

<details>
<summary><strong>Why Streamlit?</strong></summary>

Streamlit was chosen for rapid data app development:

- **Native Pandas/Plotly integration** without custom API layers
- **Built-in session state** for multi-step workflows
- **Multi-page navigation** with minimal configuration
- **Caching decorators** for performance optimization
- **Single Python codebase** simplifies deployment

Trade-offs accepted: Less UI customization than React, Streamlit-specific session patterns.

</details>

<details>
<summary><strong>Project Structure</strong></summary>

```
src/
├── config/              # Environment-aware configuration
│   ├── database.py      # Database connection settings
│   ├── app.py           # Application configuration
│   └── logging_config.py
├── services/            # Business logic layer
│   ├── database_service.py    # Centralized DB operations
│   └── intelligence_service.py # AI/ML engine
├── utils/               # Analytics utilities
│   ├── statistics.py          # Statistical analysis
│   ├── consistency_analyzer.py # Multi-dimensional scoring
│   └── data_filters.py        # Shared filtering logic
├── views/               # Streamlit pages
│   ├── dash.py          # Monthly dashboard
│   ├── choco_effect.py  # The Choco Effect story
│   ├── fitness-overview.py # SQL query interface
│   ├── login.py         # Authentication
│   └── tools/           # Analysis tools
│       ├── trends.py    # Statistical trends
│       ├── history.py   # Workout history
│       └── mapping.py   # Geographic viz
└── streamlit_app.py     # Main entry point
```

</details>

---

## Implementation Notes

### Performance Benchmarks

| Operation | Target | Actual |
|-----------|--------|--------|
| AI Classification (1K+ workouts) | <5s | ~3s |
| Intelligence Brief generation | <3s | ~2s |
| Algorithm Transparency loading | <3s | ~1s |
| Page load (all views) | <2s | <1.5s |

### Key Design Decisions

1. **Workout ID as primary key**: Extracted from MapMyRun URLs for deduplication
2. **Era-based classification defaults**: Leverages known behavioral shift at Choco arrival
3. **Unified data filtering**: Shared utilities prevent inconsistencies between views
4. **Risk-based testing**: Focus coverage on high-risk paths (core flows, session state, API calls)

### Defensive Programming Patterns

The codebase emphasizes robustness:

```python
# Type conversion with fallback
if isinstance(week_num, str):
    try:
        week_num = int(week_num)
    except ValueError:
        week_num = 1  # Safe fallback

# Division by zero prevention
if pre_choco_freq == 0:
    transformation_text = "∞x increase - started from zero!"
else:
    transformation_factor = post_choco_freq / pre_choco_freq
```

---

## What's Next

**Active Development**
- Integration with Apple Health or Garmin APIs for automated ingestion
- Weather data enrichment for performance correlation
- Geographic visualization of workout routes

**Future Enhancements**
- Mobile-responsive dashboard improvements
- Goal setting and progress tracking features
- Community data sharing (anonymized patterns)
- Custom ML model training on personal data

---

## Links

[Live Dashboard](https://workouts.barbhs.com/){: .btn .btn--primary}
[View Repository](https://github.com/dagny099/fitness-dashboard/){: .btn .btn--light-outline}
[Read Documentation](https://docs.barbhs.com/fitness-dashboard/){: .btn .btn--light-outline}

---

## Related

- **[The Choco Effect Data Story](/data-stories/choco-effect/)** — Deep dive into the before/after analysis
- **[learn_pytest](https://github.com/dagny099/learn_pytest/)** — Testing patterns developed for this project
