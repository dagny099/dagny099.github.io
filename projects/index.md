---
layout: single
title: "Projects"
permalink: /projects/
classes: wide
---

<style>
.projects-header {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 3rem;
  text-align: center;
}
.filter-nav {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin: 2rem 0;
  flex-wrap: wrap;
}
.filter-btn {
  padding: 0.5rem 1rem;
  background: white;
  border: 1px solid #dee2e6;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s;
}
.filter-btn.active {
  background: #4a90e2;
  color: white;
  border-color: #4a90e2;
}
.project-section {
  margin-bottom: 4rem;
}
.cognitive-badge {
  display: inline-block;
  background: #4a90e2;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  margin-left: 0.5rem;
}
</style>

<div class="projects-header">
  <h1>Systems That Think Like Humans Think</h1>
  <p style="max-width: 700px; margin: 1rem auto; color: #495057;">
    Each project applies cognitive science principles to real-world data challenges. 
    From visual attention patterns to memory organization, these aren't just technical 
    builds—they're explorations of how human cognition can shape better systems.
  </p>
</div>

<!-- Progressive Disclosure Navigation -->
<div class="filter-nav">
  <button class="filter-btn active" onclick="showAll()">All Projects</button>
  <button class="filter-btn" onclick="filterBy('perception')">Visual & Perception</button>
  <button class="filter-btn" onclick="filterBy('memory')">Memory & Organization</button>
  <button class="filter-btn" onclick="filterBy('attention')">Attention & Focus</button>
  <button class="filter-btn" onclick="filterBy('learning')">Learning & Adaptation</button>
</div>

## 🎯 Currently Shipping
*Active projects where cognitive principles meet production code*

### Fitness Intelligence Platform <span class="cognitive-badge">Attention Patterns</span>
**Cognitive Principle**: Pattern recognition through contrast and repetition

When 14 years of running data collided with dog walks, I discovered that human behavior naturally clusters into 3 categories—not the 10+ my app offered. The ML classifier doesn't just sort workouts; it mirrors how humans actually categorize effort levels when cognitive load is high (like during exercise).

**Technical**: Python, AWS Lambda, MySQL, Streamlit  
**Cognitive Insight**: The 7±2 rule emerges naturally in behavioral data  
[→ View Project](/projects/fitness-dashboard/) | [→ Live Demo](https://fitness.barbhs.com) | [→ GitHub](https://github.com/dagny099/fitness)

---

### Convoscope: Multi-Modal AI Comparison <span class="cognitive-badge">Working Memory</span>
**Cognitive Principle**: Cognitive load management through progressive disclosure

Comparing AI outputs revealed a fundamental limit: humans can effectively compare 3 options, tolerate 5, and get overwhelmed by 7+. This interface respects working memory constraints while managing infinite AI possibilities.

**Technical**: Streamlit, OpenAI/Anthropic/Google APIs, PostgreSQL  
**Cognitive Insight**: Side-by-side comparison reduces cognitive load vs. sequential evaluation  
[→ View Project](/projects/convoscope/) | [→ Documentation](https://docs.barbhs.com/convoscope/)

---

### Beehive Knowledge Graph <span class="cognitive-badge">Associative Memory</span>
**Cognitive Principle**: Human memory is associative, not chronological

Four years of photos became queryable knowledge by modeling how beekeepers actually recall events—through associations (weather→outcomes) rather than dates. The system's 7 relationship types emerged naturally from how humans connect observations.

**Technical**: Neo4j, Google Cloud Vision, Python, Weather APIs  
**Cognitive Insight**: Domain expertise is about relationships, not isolated facts  
[→ View Project](/projects/beehive-tracker/) | [→ Documentation](https://docs.barbhs.com/beehive/)

---

## 🔬 Research & Exploration
*Where cognitive science theory meets data science practice*

### Academic Citation Network Prediction <span class="cognitive-badge">Attention Networks</span>
**Cognitive Principle**: Attention mechanisms in knowledge discovery

Using TransE to predict missing citations in a network of 8,000 papers. The model learns "attention patterns" in research—which ideas researchers notice and which they overlook, despite relevance.

**Technical**: Graph Neural Networks, PyTorch, Neo4j, Semantic Scholar API  
**Cognitive Insight**: Academic attention follows predictable patterns, just like visual attention  
[→ Data Story](/data-stories/citation-link-prediction/) | [→ Jupyter Notebooks](https://github.com/dagny099/citation)

---

## 📚 Foundational Builds
*Earlier projects that established my cognitive approach*

### IoT Temperature Sensor Fleet (2021)
**Cognitive Principle**: Real-time data needs real-time comprehension

Built a distributed sensor network that taught me: streaming data is only valuable if humans can process it at the speed it arrives. Led to my focus on progressive disclosure and attention management.

[→ 6-Part Series](/posts/sensor-fleet/)

### Digital Portfolio Workshop Series (2024)  
**Cognitive Principle**: Information architecture as cognitive architecture

Teaching others to build portfolio sites revealed how cognitive principles apply to personal branding and content organization.

[→ 4-Part Series](/posts/getting-started-with-github-pages/)

---

## The Cognitive Thread

Every project here demonstrates the same truth: **the best technical solution considers human cognition first**.

Whether it's chunking workout data into 3 categories, limiting AI comparisons to working memory capacity, or organizing beehive observations like human memory works—the pattern is consistent. Technology succeeds when it aligns with how humans naturally think.

**Want to discuss building something that works the way humans think?** [Let's connect →](/contact/)