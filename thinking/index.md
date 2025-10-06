---
layout: single
title: "Thinking in Public"
permalink: /thinking/
classes: wide
---

<style>
.thinking-header {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 3rem;
  text-align: center;
}
.category-section {
  margin-bottom: 4rem;
}
.category-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #e9ecef;
}
.category-icon {
  font-size: 2rem;
}
.post-grid {
  display: grid;
  gap: 1.5rem;
}
.post-card {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  position: relative;
}
.post-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.canon-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #4a90e2;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: bold;
}
.coming-soon {
  opacity: 0.7;
  border-style: dashed;
  background: #fafafa;
}
</style>

<div class="thinking-header">
  <h2 style="margin-top: 0;">The Cognitive Data Science Lens</h2>
  <p style="max-width: 700px; margin: 1rem auto; color: #495057;">
    Each piece here applies cognitive science principles to data and AI challenges. 
    This isn't just technical writing—it's a systematic exploration of how human cognition 
    shapes (and should shape) the systems we build.
  </p>
</div>

<!-- CANON SECTION -->
<div class="category-section">
  <div class="category-header">
    <span class="category-icon">📚</span>
    <div>
      <h2 style="margin: 0;">Canon: Foundational Frameworks</h2>
      <p style="margin: 0.5rem 0 0 0; color: #6c757d;">Start here. These pieces define my approach to data, AI, and system design.</p>
    </div>
  </div>
  
  <div class="post-grid">
    <div class="post-card">
      <span class="canon-badge">CANON</span>
      <h3><a href="/thinking/vision-perception-data-viz-decisions/">Vision, Perception, and Data Viz for Decision-Making</a></h3>
      <p class="post-meta">Sep 2025 · 6 min read · 🧠 High cognitive load</p>
      <p>Why great charts aren't pretty—they're perceptually efficient. Using preattentive cues, luminance over hue, and small multiples to answer one question per view.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">perception</span>
        <span class="tag">preattentive</span>
        <span class="tag">decision-support</span>
      </div>
    </div>
    
    <div class="post-card">
      <span class="canon-badge">CANON</span>
      <h3><a href="/thinking/bees-graphs-governance/">Bees, Graphs, and Governance</a></h3>
      <p class="post-meta">Sep 2025 · 7 min read · 🧠 Medium cognitive load</p>
      <p>How treating beehive photos as a knowledge graph revealed universal patterns for enterprise data governance. Sometimes the best systems emerge from the messiest domains.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">knowledge-graph</span>
        <span class="tag">governance</span>
        <span class="tag">emergence</span>
      </div>
    </div>
    
    <div class="post-card">
      <span class="canon-badge">CANON</span>
      <h3><a href="/thinking/rag-without-theater/">RAG Without the Theater</a></h3>
      <p class="post-meta">Sep 2025 · 5 min read · 🧠 Medium cognitive load</p>
      <p>Evidence-linked retrieval patterns you can defend. Skip magic prompts; use small, testable patterns that tie claims to sources.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">rag</span>
        <span class="tag">explainability</span>
        <span class="tag">production</span>
      </div>
    </div>
    
    <div class="post-card coming-soon">
      <span class="canon-badge">SOON</span>
      <h3>Why Your Dashboards Fail: A Cognitive Scientist's Perspective</h3>
      <p class="post-meta">Coming this week · 7 min read</p>
      <p>The 200-millisecond problem, working memory limits, and why humans don't want data—they want narratives. With examples from my fitness tracker redesign.</p>
    </div>
  </div>
</div>

<!-- DATA STORIES SECTION -->
<div class="category-section">
  <div class="category-header">
    <span class="category-icon">📊</span>
    <div>
      <h2 style="margin: 0;">Data Stories: Cognition in the Wild</h2>
      <p style="margin: 0.5rem 0 0 0; color: #6c757d;">Real projects where cognitive principles meet messy reality.</p>
    </div>
  </div>
  
  <div class="post-grid">
    <div class="post-card">
      <h3><a href="/data-stories/exercise-dashboard/">The Choco Effect: How a Dog Transformed My Running Data</a></h3>
      <p class="post-meta">14 years of data · Interactive visualizations</p>
      <p>When my running data collided with dog walks, it revealed how consistency beats intensity—and how life's interruptions make better data stories than perfect tracking.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">behavioral-patterns</span>
        <span class="tag">classification</span>
        <span class="tag">storytelling</span>
      </div>
    </div>
    
    <div class="post-card">
      <h3><a href="/data-stories/hive-photo-metadata-tracker/">From Owl Box to Data Pipeline: A Beekeeper's Digital Journey</a></h3>
      <p class="post-meta">4 years of photos · Computer vision</p>
      <p>How 400+ unlabeled bee photos became a knowledge graph using EXIF metadata, weather APIs, and computer vision. A masterclass in finding structure in chaos.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">computer-vision</span>
        <span class="tag">knowledge-extraction</span>
        <span class="tag">apis</span>
      </div>
    </div>
    
    <div class="post-card">
      <h3><a href="/data-stories/citation-link-prediction/">Knowledge Cartography: Finding Lost Cousins in the Academic Family Tree</a></h3>
      <p class="post-meta">8,000 papers analyzed · Graph neural networks</p>
      <p>Using TransE to predict which papers should be citing each other but aren't. When your old research becomes a treasure map to hidden connections.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">graph-ml</span>
        <span class="tag">link-prediction</span>
        <span class="tag">research</span>
      </div>
    </div>
    
    <div class="post-card coming-soon">
      <span class="coming-badge">SOON</span>
      <h3>The Convoscope Chronicles: Building Multi-Modal AI Memory</h3>
      <p class="post-meta">Coming soon</p>
      <p>Why comparing AI models side-by-side revealed the importance of cognitive load management in human-AI interfaces.</p>
    </div>
  </div>
</div>

<!-- BUILDING IN PUBLIC SECTION -->
<div class="category-section">
  <div class="category-header">
    <span class="category-icon">🛠️</span>
    <div>
      <h2 style="margin: 0;">Building & Learning in Public</h2>
      <p style="margin: 0.5rem 0 0 0; color: #6c757d;">Technical journeys, lessons learned, and works in progress.</p>
    </div>
  </div>
  
  <div class="post-grid">
    <div class="post-card">
      <h3><a href="/posts/sensor-fleet/">IoT Sensor Fleet: From Arduino to Analytics</a></h3>
      <p class="post-meta">2021 · 6-part series</p>
      <p>Building a temperature sensor network taught me that real-time data is only valuable if humans can understand it in real-time too.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">iot</span>
        <span class="tag">real-time</span>
        <span class="tag">mqtt</span>
      </div>
    </div>
    
    <div class="post-card">
      <h3><a href="/posts/getting-started-with-github-pages/">Digital Home Base Workshop Series</a></h3>
      <p class="post-meta">2024 · 4-part series</p>
      <p>Teaching others to build portfolio sites revealed how information architecture principles apply to personal branding.</p>
      <div style="margin-top: 1rem;">
        <span class="tag">tutorial</span>
        <span class="tag">jekyll</span>
        <span class="tag">portfolio</span>
      </div>
    </div>
    
    <div class="post-card coming-soon">
      <h3>From Notebook to Production: A Cognitive Approach</h3>
      <p class="post-meta">Coming soon</p>
      <p>Why the journey from Jupyter to production isn't technical—it's cognitive. Managing complexity for future-you.</p>
    </div>
  </div>
</div>

<!-- QUICK TAKES SECTION -->
<div class="category-section">
  <div class="category-header">
    <span class="category-icon">💭</span>
    <div>
      <h2 style="margin: 0;">Quick Takes & Observations</h2>
      <p style="margin: 0.5rem 0 0 0; color: #6c757d;">Shorter thoughts on data, AI, and human-system interaction.</p>
    </div>
  </div>
  
  <div class="post-grid">
    <div class="post-card coming-soon">
      <h3>The 7±2 Rule Everywhere</h3>
      <p class="post-meta">3 min read</p>
      <p>Why Miller's magic number appears in everything from Streamlit interfaces to LLM context windows.</p>
    </div>
    
    <div class="post-card coming-soon">
      <h3>Attention Mechanisms: Biology to Transformers</h3>
      <p class="post-meta">5 min read</p>
      <p>The fascinating parallels between human visual attention and transformer architecture.</p>
    </div>
    
    <div class="post-card coming-soon">
      <h3>Why Experts Make Terrible Interfaces</h3>
      <p class="post-meta">4 min read</p>
      <p>The curse of knowledge is real—and it's ruining your dashboards.</p>
    </div>
  </div>
</div>

<style>
.tag {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  font-size: 0.875rem;
  margin-right: 0.5rem;
  color: #495057;
}
</style>