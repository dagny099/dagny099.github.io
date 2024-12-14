---
title: "Academic Citation Network Link Prediction using PyTorch"
excerpt: ""
date: 2024-06-15 # Change this to control the order
classes: [wide, portfolio-page]
category: Project
tags: [arduino, temp sensor, mqtt]
# permalink: /temp-sensor-00/
header:
  overlay_color: "#4649e5"
  # overlay_image: "/assets/images/tempsensor_pic_th.jpg"
  teaser: assets/images/portfolio/eyemodel_Viz_teaser.jpg
---

{: style="margin-top: 0px; margin-top: 0px; padding-top: 0px;"} 
**Overview:**
This project explores the challenge of uncovering hidden connections in academic citation networks. Citation networks often suffer from incompleteness (imagine... ), with missed citations that obscure valuable relationships between researchers and ideas. By representing the network as a knowledge graph, this project develops a PyTorch-based link prediction model using graph embeddings to predict likely citations between papers.

**Motivation:**
Citation networks are fundamental for understanding the evolution of knowledge. However, gaps in these networks hinder researchers from discovering relevant literature and potential collaborations. This project aims to address this issue by:
- Identifying missing citations.
- Highlighting influential research ("citation power").
- Exploring clusters and subfields in the network.
- Analyzing temporal trends in citation patterns.
- Uncovering "knowledge gaps" between disconnected papers.

**Dataset and Scope:**
- **Seed Paper**: 2009 eye-tracking paper.
- **Nodes**: ~500 academic papers, authors, and research topics.
- **Edges**: ~1,000 relationships, including:
  - "Cites": Paper A cites Paper B.
  - "Authored by": Paper A authored by Author X.
  - "Belongs to topic": Paper A categorized under cognitive science.
- The dataset includes papers that:
  - Cite the seed paper (424 papers).
  - Are cited by the seed paper.
  - Form meaningful connections between these two sets.

**Methodology:**
1. **Data Collection and Preprocessing**
   - Gather citation and metadata using Semantic Scholar API.
   - Organize data into triples: `subject-predicate-object`.

2. **Knowledge Graph Construction**
   - Nodes: Papers, authors, and topics.
   - Edges: Relationships ("cites," "authored by," "belongs to topic").

3. **Model Implementation**
   - Model: TransE for graph embeddings.
   - Framework: PyTorch.
   - Training: 80% of triples for training, 20% for testing.
   - Negative Sampling: Generate realistic negative samples for model evaluation.

4. **Evaluation Metrics**
   - Mean Rank (MR): Measures ranking performance.
   - Mean Reciprocal Rank (MRR): Rewards high-ranking correct predictions.
   - Hits@K: Fraction of true links in the top K predictions.

5. **Insight Generation**
   - "Citation Power": Identify hubs using centrality metrics.
   - "Citation Clusters": Use community detection algorithms to explore subfields.
   - "Temporal Trends": Analyze the growth or decline of the seed paper’s influence over time.
   - "Knowledge Gaps": Predict links to fill gaps between clusters.

**Results and Visualizations:**
- **Graph Visualizations**: Display clusters, influential nodes, and predicted links using NetworkX and Matplotlib.
- **Embedding Space**: Visualize graph embeddings to demonstrate clustering and relationships.
- **Temporal Trends**: Plot citations over time, highlighting the seed paper’s influence.
- **Predicted Links**: Showcase examples of missing citations predicted by the model.

**Key Outcomes:**
- Demonstrated PyTorch implementation skills through graph embeddings.
- Illustrated understanding of knowledge graph concepts by constructing and analyzing the citation network.
- Generated actionable insights, including identifying influential papers and uncovering gaps in citation patterns.
- Delivered interpretable predictions and engaging visualizations suitable for portfolio presentation.

**Future Directions:**
- Extend the dataset to include additional papers and relations.
- Experiment with advanced models like RotatE or graph neural networks (GCNs).
- Integrate the model with real-time APIs for dynamic citation recommendations.
- Explore cross-domain applications, such as biomedical knowledge graphs or social networks.

---

**Portfolio Value:**
This project highlights technical proficiency in PyTorch, graph-based modeling, and knowledge graph analytics. By addressing a meaningful real-world challenge, it demonstrates the ability to derive insights from data and communicate findings effectively. The combination of technical rigor and practical application makes it a standout addition to any data science portfolio.

---
### Updated Roadmap for the Academic Citation Network Link Prediction Project

#### **Core Objectives**
1. **Demonstrate PyTorch Skills**: Implement a graph embedding model using PyTorch.
2. **Show Understanding of Knowledge Graph Concepts**: Construct and analyze a citation network as a knowledge graph.
3. **Create Something Explainable in an Interview**: Provide interpretable outputs, example queries, and insights.
4. **Keep It Doable in 1–2 Days**: Start small with meaningful results while leaving room for scalability.

---

### **Roadmap FOR RESULTS**

#### **1. Example Insights**
- **"Citation Power"**:
   - Use centrality measures like PageRank or degree centrality to identify the most influential papers.
   - Visualize hubs in the citation network.

- **"Citation Clusters"**:
   - Apply community detection algorithms (e.g., Louvain) to group papers into subfields.
   - Highlight connections between subfields (e.g., cross-discipline citations).

- **"Temporal Trends"**:
   - Analyze citation counts over time for the seed paper and its neighbors.
   - Create a time-series visualization showing the rise or decline of influence.

- **"Knowledge Gaps"**:
   - Use the link prediction model to identify potential connections between disconnected clusters.
   - Provide examples of predicted links that fill these gaps.

---

### **Proposed Milestones**

#### **Phase 1: Data Collection and Preparation**
- Gather citation data around the seed paper (citing papers, references, connecting papers).
- Organize data into a graph-friendly format (e.g., triples: `subject-predicate-object`).

#### **Phase 2: Knowledge Graph Construction**
- Construct the graph with nodes (papers) and edges (relations like "cites").
- Add metadata to nodes (e.g., titles, publication years) for later analysis.

#### **Phase 3: Model Implementation**
- Train a TransE model in PyTorch for link prediction.
- Evaluate the model with metrics like Mean Rank and Hits@K.

#### **Phase 4: Insight Generation and Visualization**
- **"Citation Power"**: Compute and visualize influential nodes (e.g., top 10 hubs).
- **"Citation Clusters"**: Detect and describe communities.
- **"Temporal Trends"**: Plot citation trends over time.
- **"Knowledge Gaps"**: Highlight predicted links and their implications.

#### **Phase 5: Documentation and Presentation**
- Write a compelling project report including:
   - The problem statement.
   - Methodology (data, model, evaluation).
   - Insights and results.
- Create visualizations to make the results engaging and intuitive.

---

---
# FOCUS ON TOOLS ...

## **Tools to EXPLORE and he ROLES they play**
Each tool in your pipeline has a specific purpose, depending on the task. Here's how they fit into your project:

#### **1. Data Representation and Manipulation**
   **Tools:** Pandas, NetworkX, RDFLib
   - These tools **organize** and **represent** your data before feeding it into models.
   - **Pandas**: Use for tabular storage of triples and preprocessing (e.g., splitting data, creating negative samples).
   - **NetworkX**: Useful for visualizing the graph structure and calculating graph-level metrics like degree or centrality.
   - **RDFLib**: Specialized for semantic web graphs with SPARQL querying capabilities.

#### **2. Graph Data Libraries**
   **Tools:** PyTorch-Geometric, DGL
   - These libraries handle **graph representation** in a machine-learning-friendly format.
   - For example, **PyTorch-Geometric** converts your graph into tensors (e.g., edge indices, edge features), ready for training with models like GCN or GAT.
   - They also provide utilities for batching, sampling, and data augmentation.

#### **3. Embedding Models**
   **Tools:** PyKEEN, DGL, PyTorch-Geometric
   - These tools are used to **train embeddings** for nodes and relationships.
   - For example:
     - **PyKEEN**: Prebuilt algorithms like TransE, DistMult, or RotatE for knowledge graph embeddings.
     - **DGL**: Build custom graph neural networks (GNNs) for embeddings.
     - **PyTorch-Geometric**: Allows you to implement GNNs like GraphSAGE or RGCN.

#### **4. Model Training and Link Prediction**
   **Tools:** PyTorch, PyKEEN
   - **PyTorch**: Core deep learning framework for building and training models.
   - **PyKEEN**: High-level abstraction for training specific link prediction models.

#### **5. Evaluation**
   **Tools:** PyKEEN Evaluators, Custom PyTorch Scripts
   - Evaluate your trained model’s ability to predict missing links.
   - Tools like PyKEEN simplify the evaluation process with metrics like **Mean Rank** and **Hits@K**.

#### **6. Visualization**
   **Tools:** NetworkX, Matplotlib, Plotly
   - Visualize the structure of the knowledge graph, embedding space, and predicted links.

---

### **How to Think About Evaluating the Model**
Evaluating a link prediction model involves two key questions:
1. **How well does the model predict missing links?**
2. **Does it generalize to unseen data?**

#### **Key Evaluation Metrics**
1. **Mean Rank (MR):**
   - Measures how high the correct prediction ranks among all possible links.
   - Lower is better.
   - Example:
     - For a true link `("Paper A", "cites", "Paper B")`, suppose the rank is 5 out of 100 predictions. The rank contributes 5 to the Mean Rank.

2. **Mean Reciprocal Rank (MRR):**
   - Uses reciprocal ranks to emphasize high-ranking predictions.
   - Formula: \( MRR = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \frac{1}{rank_i} \)
   - Example:
     - For a rank of 5, the reciprocal is \( \frac{1}{5} = 0.2 \).
     - A higher MRR means better performance.

3. **Hits@K:**
   - Measures the proportion of true links that appear in the top \(K\) predictions.
   - Example:
     - Hits@10: What percentage of true links are in the top 10?

4. **ROC-AUC (Optional for Binary Classifiers):**
   - Used when casting link prediction as a binary classification task (link/no link).
   - Measures the trade-off between true positive rate and false positive rate.

#### **Evaluation Workflow**
1. **Prepare Data for Testing:**
   - Create a **test set** of triples (e.g., 20% of the graph edges).
   - Generate **negative samples**: These are fake triples like `("Paper A", "cites", "Nonexistent Paper")` to test the model's discriminative power.

2. **Perform Predictions:**
   - For each test triple (e.g., `("Paper A", "cites", ?)`):
     - Rank all possible entities (e.g., all papers) based on predicted likelihood.

3. **Compute Metrics:**
   - **Rank Metrics**: Mean Rank and MRR.
   - **Top-K Metrics**: Hits@K.
   - Analyze these metrics to assess performance.

#### **Practical Tips for Evaluation**
- **Baselines Matter**: Compare your model with simpler baselines like random or common neighbors.
- **Interpretable Predictions**: Visualize the top predictions to confirm their validity.
- **Negative Sampling**:
  - Ensure negative samples are realistic.
  - Example: Instead of linking `Paper A` to a totally unrelated entity, sample from papers in the same topic domain.

---

### **Entry Point for Link Prediction**

#### **Step 1: Start Small**
- Begin with tools like **PyKEEN** or **PyTorch-Geometric**. Both provide straightforward ways to build embeddings and perform link prediction.

#### **Step 2: Define Goals**
- Decide on:
  - The number of triples you’ll train on.
  - Relationships you want to predict (e.g., "cites").
  - Metrics that matter (e.g., MRR, Hits@10).

#### **Step 3: Iterative Evaluation**
- Train a simple model (e.g., TransE) and evaluate using rank-based metrics.
- Visualize predictions and tweak parameters.

---

### **Setting Reasonable Numbers for Triples**

For a **small-scale project** (1-2 days), here’s what would be manageable:

1. **Nodes (Entities):** Aim for **200–500 nodes**, representing papers, authors, or topics.
   - Example: Start with 50–100 papers, their authors, and potentially 2–3 topic nodes.

2. **Triples:**
   - **Base Relation ("cites"):** 500–1,000 triples.
     - Example: Each paper cites 5–10 others on average.
   - **Additional Relations:** Add 100–300 triples per type, such as:
     - `"authored by"`: Links papers to their authors.
     - `"belongs to topic"`: Links papers to a research area.

   **Total:** 700–1,500 triples.

3. **Graph Density:** Keep it **sparse** to make link prediction meaningful:
   - Density \(D = \frac{|E|}{|N|(|N| - 1)}\): Should be below \(0.1\).

---


