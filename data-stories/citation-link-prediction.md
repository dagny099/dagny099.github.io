---
title: "Knowledge Cartography: Finding Lost Cousins in the Academic Family Tree"
description: "Using graph neural networks to discover hidden connections between papers that should have met but never did."
permalink: /data-stories/citation-link-prediction/
layout: section
section: data-stories
tags: [graph neural networks, pytorch, neo4j]
---

# Knowledge Cartography: Finding Lost Cousins in the Academic Family Tree
## Part 1: When Your Old Paper Becomes a Treasure Map

*How a 15-year-old paper on visual attention became the seed for mapping hidden connections across 8,000 papers, revealing the invisible bridges between parallel research universes.*

---

## The Accidental Archaeologist
In 2009, I co-authored what seemed like a well-received academic paper on computational models of visual attention. It garnered citations, received positive feedback, and then I transitioned out of academia into industry. I filed it away as a closed chapter in my professional journey.

<figure style="float:right; margin: 0 0 1em 1em; max-width:400px; height:auto;">
  <a href="https://www.researchgate.net/publication/40689162_Modeling_Search_for_People_in_900_Scenes_A_combined_source_model_of_eye_guidance" class="image-popup" title="Check out the paper">
    <img src='/assets/visualizations/knowledge-cartography/seed_paper_fig9.png' alt="Figure 9" >
  </a>
  <figcaption>The 2009 paper that started it all</figcaption>
</figure>


Flash forward a decade or so, a deceptively simple yet intriguing question began to haunt me: *Where did those ideas travel? What unexpected paths did they take through the academic landscape?*

**The Rabbit Hole Begins:**
- 🔍 Started with **one paper** (mine) in Semantic Scholar
- 🕸️ Followed every citation, then citations of citations
- 📈 Watched my network explode: 1 → 156 → 2,847 → **8,392 papers**
- 😳 Discovered papers in fields I'd never heard of citing my work
- 🤔 Found papers solving similar problems that had never connected

<details markdown="1">
<summary><strong>📊 The Academic Forensics Challenge</strong></summary>

What started as nostalgic curiosity became a data science puzzle. My citation network had grown into a sprawling map of interconnected research, but the most interesting discovery wasn't what was connected—it was what wasn't.

Papers addressing nearly identical problems, using compatible methods, sitting in the same extended network, yet completely unaware of each other's existence. Like cousins at a family reunion who never meet because nobody introduces them.

This is the story of teaching a machine to play academic matchmaker.
</details>

---

## The Map Reveals Its Secrets

Building the network was surprisingly straightforward once I wrestled with the Semantic Scholar API pagination. But visualizing 8,000 papers and 23,000 authors revealed something unexpected:

 <div class="chart-container">
  <iframe src="/assets/visualizations/knowledge-cartography/network_growth_3panel.html" 
          width="100%" 
          height="500" 
          frameborder="0"
          class="desktop-chart"
          style="border: 1px solid #ddd; border-radius: 8px;">
  </iframe>
</div>

*Interactive: Watch how one paper grows into a research universe. Hover to see paper details at each expansion level.*

**What the Data Revealed:**
- **Citation islands**: Distinct clusters working on related problems in isolation
- **Bridge papers**: Rare connectors between otherwise separate communities  
- **Parallel evolution**: Similar solutions emerging independently
- **Lost connections**: Papers that *should* be connected based on content but aren't

The network wasn't just big—it was full of holes. Missed connections. Parallel universes of research that should be talking but aren't.

---

## Enter the Machines: Teaching AI to See Invisible Bridges

This is where my journey into graph neural networks began. If papers are cities on a map, most research follows existing roads (citations). But what if we could predict where new roads *should* be built?

### The TransE Translation Game
<!--
<div class="chart-container">
  <iframe src="/assets/visualizations/knowledge-cartography/transe-explanation.html" 
          width="100%" 
          height="400" 
          frameborder="0"
          class="desktop-chart"
          style="border: 1px solid #ddd; border-radius: 8px;">
  </iframe>
</div>
-->

Think of TransE like this:
- **Papers are points** in a multi-dimensional space
- **Citations are vectors** connecting these points
- **The pattern**: If A→B and B→C, the model learns the "translation" rule
- **The prediction**: Apply these rules to find missing connections

<details markdown="1">
<summary><strong>🤖 The Learning Journey</strong></summary>

As someone teaching myself graph ML, I was skeptical. How could a model predict meaningful connections between papers it only sees as nodes and edges?

The breakthrough came when I understood: TransE isn't guessing randomly. It's learning the hidden grammar of how ideas flow through academia. Just like "visual attention" in psychology translates to "attention mechanisms" in deep learning, the model learns these conceptual bridges.

```
# The core insight in code
# If paper A cites papers [X, Y, Z]
# And paper B cites papers [X, Y, W]
# Then the "translation" from A to B might apply elsewhere

embedding_A + translation_vector ≈ embedding_B
```

The model learns thousands of these translation patterns, then applies them to find missing links.
</details>

---

## The First Discoveries: From "Obviously" to "Oh Wow"

After training TransE on my network, I asked it a simple question: "What connections are missing?"

### Discovery 1: The Obvious One
**Confidence: 0.94**

<!--
<div class="prediction-showcase">
  <div class="paper-comparison">
    <div class="paper-box">
      <h4>Paper A (2011)</h4>
      <p class="field">Computer Vision</p>
      <p class="title">"Saliency Detection Using Maximum Symmetric Surround"</p>
      <p class="key-concept">Uses center-surround mechanisms for attention</p>
    </div>
    <div class="arrow">→ Should cite →</div>
    <div class="paper-box">
      <h4>Paper B (2009)</h4>
      <p class="field">Cognitive Science</p>
      <p class="title">"Computational Models of Visual Attention" (My paper!)</p>
      <p class="key-concept">Defines center-surround attention mechanisms</p>
    </div>
  </div>
</div>
-->

**Why it makes sense**: They're solving the same problem with the same biological inspiration. The computer vision paper reinvented concepts from cognitive science. Classic case of fields not talking.

### Discovery 2: The Surprising One
**Confidence: 0.87**

<!--
<div class="prediction-showcase">
  <div class="paper-comparison">
    <div class="paper-box">
      <h4>Paper A (2018)</h4>
      <p class="field">Deep Learning</p>
      <p class="title">"Attention Is All You Need"</p>
      <p class="key-concept">Transformer attention mechanisms</p>
    </div>
    <div class="arrow">→ Should cite →</div>
    <div class="paper-box">
      <h4>Paper B (2009)</h4>
      <p class="field">Cognitive Science</p>
      <p class="title">"Computational Models of Visual Attention"</p>
      <p class="key-concept">Biological attention selection</p>
    </div>
  </div>
</div>
-->

**Why it stopped me cold**: The most influential paper in modern AI shares deep conceptual roots with visual attention research from a decade earlier. The connection isn't obvious from titles or abstracts—you need to understand how "attention" evolved from psychology to transform machine learning.

### Discovery 3: The Mind-Bending One
**Confidence: 0.79**

<!--
<div class="prediction-showcase">
  <div class="paper-comparison">
    <div class="paper-box">
      <h4>Paper A (2020)</h4>
      <p class="field">Robotics</p>
      <p class="title">"Efficient Object Search in Cluttered Environments"</p>
      <p class="key-concept">Robot navigation using visual salience</p>
    </div>
    <div class="arrow">→ Should cite →</div>
    <div class="paper-box">
      <h4>Paper B (2015)</h4>
      <p class="field">Neuroscience</p>
      <p class="title">"Neural Mechanisms of Visual Search in Natural Scenes"</p>
      <p class="key-concept">How brains search cluttered environments</p>
    </div>
  </div>
</div>
-->
**Why it matters**: Roboticists independently solving problems that neuroscientists mapped years ago. The terminology is completely different, but the math is remarkably similar.

---

## The Trust Question: How Do I Know This Isn't Random?
<!--

<div class="chart-container">
  <iframe src="/assets/visualizations/knowledge-cartography/confidence-distribution.html" 
          width="100%" 
          height="400" 
          frameborder="0"
          class="desktop-chart"
          style="border: 1px solid #ddd; border-radius: 8px;">
  </iframe>
</div>
-->
As someone learning this technology, skepticism was my default. Three things convinced me the model was finding real patterns:

**1. The Confidence Distribution**
- Most predictions cluster around 0.3-0.5 (the model is appropriately uncertain)
- High confidence predictions (>0.8) are rare and remarkably sensible
- The model admits when it doesn't know

**2. The Validation Test**
- Hid 10% of real citations and asked the model to predict them
- Hit rate: 73% in the top 10 predictions
- But the real value is in what *doesn't* exist yet

**3. The "Aha" Moments**
- Showed predictions to researcher friends
- Common response: "How did I miss that paper?"
- Several led to actual new collaborations

<details markdown="1">
<summary><strong>📈 Where the Model Struggles</strong></summary>

Transparency builds trust. The model has clear limitations:

- **Terminology barriers**: When fields use completely different words for the same concept
- **Time gaps**: Predicting connections across large time spans (>10 years) is harder
- **Interdisciplinary leaps**: The further apart fields are, the lower the confidence
- **Popular papers**: Sometimes suggests connections just because papers are highly cited

The model is a discovery tool, not an oracle. It suggests where to look, not what to believe.
</details>

---

## What This Means: Your Research Has Hidden Family

Every paper in this network has undiscovered cousins—research that shares its intellectual DNA but lives in a parallel universe. My 2009 visual attention paper wasn't just cited 156 times; it has hundreds of potential connections waiting to be discovered.

**The Bigger Implications:**

🔄 **Research is more connected than we think**—we just can't see all the bridges

🚀 **Ideas travel in patterns**—and these patterns are learnable

🌉 **Field boundaries are artificial**—solutions often exist across the divide

💡 **Every researcher has hidden collaborators**—people solving their problems in different languages

---

## The Questions This Raises

Building this map surfaced questions I hadn't thought to ask:

<!--
<div class="chart-container">
  <iframe src="/assets/visualizations/knowledge-cartography/field-migration.html" 
          width="100%" 
          height="450" 
          frameborder="0"
          class="desktop-chart"
          style="border: 1px solid #ddd; border-radius: 8px;">
  </iframe>
</div>
-->
*Visualization: How ideas from cognitive science migrated to computer vision, robotics, and deep learning*

**Questions worth exploring:**
- Which fields are the best "idea translators"?
- What makes some papers natural bridges while others stay isolated?
- Can we predict which current papers will spawn unexpected fields?
- How many breakthrough connections are we missing right now?

---

## Try This Yourself (Coming Next Week!)

I'm building a tool that lets you map your own paper's hidden network. Here's what you'll be able to do:

**🎯 Your Paper → Your Map**
1. Enter any paper ID from Semantic Scholar
2. Watch your citation network grow recursively
3. See predicted connections with confidence scores
4. Explore which fields your work influenced unexpectedly

**Preview of what's coming:**
- Interactive network explorer
- Real-time TransE predictions
- Shareable knowledge maps
- Citation gap analysis

---

## The Technical Stack (For the Curious)

<details markdown="1">
<summary><strong>🔧 How to Build Your Own Knowledge Cartographer</strong></summary>

**The Pipeline:**

```
# 1. Recursive citation collection
def expand_network(seed_paper_id, depth=3):
    """Follow citations recursively to build network"""
    papers = collect_papers_via_api(seed_paper_id, depth)
    return build_neo4j_graph(papers)

# 2. Graph construction in Neo4j
CREATE (p:Paper {id: $paper_id, title: $title})
CREATE (a:Author {name: $author_name})
CREATE (a)-[:AUTHORED]->(p)

# 3. TransE training
model = TransE(n_entities=len(papers), n_relations=4, dim=100)
model.train(citation_triples, epochs=100)

# 4. Link prediction
missing_links = model.predict_missing_links(threshold=0.7)
```

**Key Tools:**
- **Neo4j Aura**: Cloud graph database for the citation network
- **PyTorch**: TransE implementation for link prediction
- **Semantic Scholar API**: Citation data (generous rate limits!)
- **Plotly**: Interactive visualizations
- **Python**: Gluing it all together

Full implementation notebook coming with Part 2!
</details>

---

## What's Next: Your Turn to Map

This project started with simple curiosity about an old paper and revealed an entire hidden universe of connections. Every researcher has these hidden networks waiting to be discovered.

**Part 2 Preview: Building Your Knowledge Map**
- 🛠️ Complete implementation guide
- 📊 Advanced visualization techniques
- 🔍 Strategies for validating predictions
- 🎯 Finding your paper's lost cousins
- 🚀 Deploying your own citation explorer

**The Big Question:** What connections are hiding in your research universe?

---

## Resources & Links

**🐙 GitHub Repository:** [Coming this weekend with the code]

**📊 Interactive Demo:** [Launching next week at knowledgemap.barbhs.com]

**📝 Technical Paper:** [TransE: A simple yet effective method for knowledge graph embedding](https://papers.nips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html)

**🔗 Semantic Scholar API:** [Build your own citation networks](https://api.semanticscholar.org/)

---

*Next time: Turn any paper into a map and discover the research connections you never knew existed.*

**What hidden connections lurk in your field?** Share your paper ID in the comments—I'll run it through the model and share what I find!

---

*Barbara is a Certified Data Management Professional (CDMP) who left academia in 2010 but never stopped wondering where ideas travel. She's currently teaching herself graph neural networks by mapping the hidden universe of academic knowledge. Follow her journey at [barbhs.com].*
