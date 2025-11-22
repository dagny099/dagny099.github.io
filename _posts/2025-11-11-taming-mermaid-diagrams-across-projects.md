---
layout: single
title: Taming Mermaid Diagrams Across Projects
subtitle: From scattered snippets to a reusable visual library
permalink: /posts/organized-mermaid-life/
header:
  overlay_image: "/assets/images/midjourney/wall-worthy/sq-celestial-reflections.png"
excerpt: Treat Mermaid diagrams like <b>visual source code</b>   with a home, structure, and a tiny bit of automation. 
excerpt_display: true
tags: [mermaid, diagrams, documentation, workflow, streamlit]
classes: wide
categories: [tutorial]
pagination: 
  enabled: true
#toc: true
#toc_label: "Table of Contents"
#toc_icon: "list"
#toc_sticky: true
#author_profile: false
---

# Taming Mermaid Diagrams Across Projects

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
OVERVIEW
</div>

<img src="{{ '/assets/diagrams/scattered_vs_structured_diagram_workflow_v1.svg' | relative_url }}" alt="diagrams everywhere" style="float:left; margin: 1em 2em 1em 2em; max-width:500px; height:auto;">

If your Mermaid diagrams are scattered across notebooks, READMEs, and screenshots, this post walks you through building a **simple, reusable workflow**:

- Treat diagrams as **first-class assets** with a `/diagrams/` folder in each repo.
- Use a **consistent naming convention** and **lightweight metadata** (including `visibility`, `status`, `tags`, and optional sequence info).
- Add a **one-command script** to render all `.mmd` files to `.svg` using Mermaid CLI.
- Start a small **cross-project `diagram-index`** so you can find the right diagram later.
- Learn how to think in terms of **“diagram sequences”** to teach and tell stories.
- As a companion, there’s a **Streamlit app** (in this repo) that helps you:
  - remember the workflow,
  - explore diagrams by metadata,
  - and experiment with sequences.

You can do the entire tutorial with **one project and two or three diagrams** and still come away with a meaningful upgrade to your documentation.

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
MOTIVATION
</div>

![image-center]({{ site.url }}{{ site.baseurl }}/assets/diagrams/scattered_vs_structured_diagram_workflow_v1.svg){: .align-center}

## The Diagram Journey

This is the visual that guides the entire workflow explained in this post.

{% include figure
   image_path="assets/diagrams/diagram_journey_from_idea_to_asset_v1.svg"
   caption="A simple but powerful lifecycle for managing diagrams across projects."
   alt="Mermaid diagram showing the lifecycle from idea to reusable asset"
   width="85%"
%}

### My On-again, Off-again Relationship with Mermaid

For years my Mermaid diagrams lived everywhere _except_ where I needed them:
- a cell in a Jupyter notebook,
- a Markdown snippet in a README,
- a one-off paste into a GitHub issue,
- or a lovingly-crafted diagram that only survived as a PNG in slides.

Worse, I often had multiple versions of “the same” diagram:
- one messy but detailed version I used to think through a system,
- one cleaned-up version for presentations,
- and one experimental branch that only kind-of rendered.

Most frustratingly, when I wanted to reuse a diagram, I couldn’t quickly answer the question, *"Which version is the **most recent**, **most detailed**, and still **renders**?”*  

<div style="text-align:center; margin:1.5em 0; padding:0.75em; font-size:1.1em; font-weight:600; border-left:4px solid #1976d2">
The idea behind this post is simple: <br>
<mark>Treat Mermaid diagrams like <b>visual source code</b>   with a home, structure, and a tiny bit of automation.</mark>
</div>

{: .notice--primary .text-center}
Treat Mermaid diagrams like <b>visual source code</b>   with a home, structure, and a tiny bit of automation.

By the end of this tutorial you’ll have:  
* A `/diagrams/` folder in at least one project  
* A naming convention and metadata block for your diagrams  
* A script that renders all `.mmd` files to `.svg`  
* A tiny `diagram-index` you can grow over time  
* A mental model of **diagram sequences** for teaching and storytelling  
* As a bonus, a **Streamlit app** that demonstrates the same ideas :)


<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
Tutorial
</div>

## **Step 1 – Give diagrams a home: `/diagrams/`**

Pick one project you care about and create a `diagrams/` folder at the root.  

Move one or two Mermaid diagrams into this folder as standalone files:
```text
a-project/
    diagrams/
        data_flow_v1.0.mmd
        workout_classification_v1.0.mmd
```

Each file contains (i) **optional frontmatter metadata** , followed by a normal **Mermaid code block**. (we’ll describe further in Step 3)

<mark>From now on, when I think, “Where should I put this diagram?,” my answer is QUICK- It goes in **diagrams/**</mark>


## **Step 2 – A simple naming convention (with a visualization cheat sheet)**

Next, we want file names that are:
* predictable,
* searchable,
* and expressive enough to remind you what kind of diagram it is.

A simple pattern:
`{domain_or_area}_{diagram_type}_{topic}_v{major}.{minor}.mmd`

Examples:
* `etl_data_flow_core_v1.0.mmd`
* `llm_decision_tree_routing_v0.3.mmd`
* `platform_architecture_high_level_v1.1.mmd`
* `ml_evaluation_workflow_v1.0.mmd`

You don’t have to use every piece every time, but being explicit about **diagram type** pays off.

### **Diagram type cheat sheet**

Here’s a compact table of common Mermaid-friendly diagram types and what they’re good for (especially in data / ML / systems work):

| Diagram type | Good for | Suggested name fragment |
| ----- | ----- | ----- |
| Data flows | Showing how data moves through systems, ETL pipelines, APIs | `data_flow`, `etl_flow` |
| Technical workflows | Step-by-step processes: ingestion, training, deployment, evaluation | `workflow`, `pipeline` |
| Decision trees | Routing logic, if/else conditions, classification flows | `decision_tree`, `router` |
| Architecture diagrams | High-level components, services, and how they connect | `architecture`, `system_view` |
| Sequence diagrams | Interactions over time: requests, responses, async workflows | `sequence`, `interaction` |
| State diagrams | States of a system or entity and transitions between them | `state_machine`, `states` |
| Entity–relationship/schema | Tables, entities, fields, and relationships | `schema`, `er_diagram` |
| Knowledge graph / concept maps | Concepts, entities, and relationships across domains | `kg_view`, `concept_map` |
| Timelines / chronologies | Time-ordered events: releases, experiments, story arcs | `timeline`, `chronology` |
| UI flow / user journeys | Screens, user actions, and navigation paths | `ui_flow`, `user_journey` |
| ML pipeline & evaluation | Training/eval loops, metrics, model comparison workflows | `ml_pipeline`, `ml_eval_flow` |

<mark>When I use these fragments directly in file names, even just scanning the project's **diagrams/** folder becomes a reminder of **what kinds of visual documentation exists** and what’s missing!</mark>


## **Step 3 – Add metadata frontmatter (including visibility & sequences)**

Now we’ll turn each `.mmd` file into a **self-describing artifact** by adding a YAML frontmatter block at the top. Start simple:  
```text
---
id: data_flow_core_v1  
title: Core Data Flow  
project: my_project 
last_updated: 2025-11-19  
tags: [data, etl, pipeline]  
---
```

Then Mermaid code:
```text
flowchart LR  
    A[Source system] --> B[ETL job]  
    B --> C[Warehouse table]  
    C --> D[Dashboard]
```

### **Extended metadata (for visibility, lifecycle, and sequences)**

Once that’s working, you can expand to a richer schema that supports:
* **Visibility / permissions**
* **Status** (draft vs stable)
* **Sequences** (for teaching / storytelling)
* **Deprecation / supersedes**

For example:
```bash
---  
id: workout_classification_flow_v1  
title: Workout Classification Flow  
project: fitness_dashboard  
visibility: private            # public | internal | private  
status: stable                 # draft | stable | deprecated  
last_updated: 2025-11-19  
tags: [fitness, ml, classification, mermaid-workflow]  
sequence:`  
  group: "mermaid-diagram-workflow-post"  
  order: 2  
supersedes: workout_classification_flow_v0  
description: >  
  Shows how raw workout data flows through the ML classifier,  
  including fallback logic and UI mapping to the UI label.  
---
```

You don’t *have* to fill in every field for every diagram, but:
* `visibility`, `status`, and `last_updated` **keep your library honest**.
* `sequence.group` and `sequence.order` let you assemble **diagram sequences** for teaching or storytelling later.
* `description` is a <mark>human summary that makes a future you very happy<mark>.


## **Step 4 – A tiny script to render all diagrams**

Now let’s make sure your diagrams are easy to **preview** and reuse in docs, slides, and apps.

We’ll use the Mermaid CLI (`@mermaid-js/mermaid-cli`) to convert `.mmd` → `.svg`.

### **4.1 Install Mermaid CLI (once per project)**

At the root of your project:
`npm install --save-dev @mermaid-js/mermaid-cli`

This gives you the `mmdc` command via `npx`.

### **4.2 Render one diagram manually (sanity check)**

Try rendering a single file:
`npx mmdc -i diagrams/data_flow_v1.0.mmd -o diagrams/data_flow_v1.0.svg`

If everything is installed correctly, you should see a new SVG file appear.
You can open it in your browser or image viewer and make sure it looks right.

### **4.3 Add a “render all diagrams” script**
I like to think of this as my **“regenerate visual library”** button.

Create a small script, e.g. 
```bash
#!/usr/bin/env bash
# Save as: scripts/render_diagrams.sh

set -euo pipefail`
echo "Rendering all Mermaid diagrams in ./diagrams"`

for f in diagrams/*.mmd; do  
  base="${f%.mmd}"  
  out="${base}.svg"  
  echo "  - $f -> $out"  
  npx mmdc -i "$f" -o "$out"  
done

echo "Done!"
```

Make it executable:
```bash
chmod +x scripts/render_diagrams.sh`
```

<mark>Now you can render all diagrams at once! <br>**./scripts/render_diagrams.sh** </mark>



## **Step 5 – Per-project workflow (as a diagram sequence)**

Let’s summarize the per-project workflow visually.

Here’s a Mermaid diagram you can save as 
```mermaid
# diagrams/per_project_workflow_v1.0.mmd
---  
id: per_project_workflow_v1  
title: Per-Project Diagram Workflow  
project: mermaid_diagram_workflow  
visibility: public  
status: stable  
last_updated: 2025-11-19  
tags: [workflow, mermaid, documentation]  
sequence:  
  group: "mermaid-diagram-workflow-post"  
  order: 1  
---

flowchart LR  
    Edit[Edit .mmd file<br/>in diagrams/] --> Render[Run render_diagrams.sh]  
    Render --> Svg[(Updated .svg files)]  
    Svg --> Docs[Use diagrams in<br/>docs / slides / apps]
```

This is your **inner loop**:
1. Edit the `.mmd` file in `diagrams/`.
2. Run the render script.
3. Use the `.svg` anywhere you like.
4. Commit both `.mmd` and `.svg`.

This alone—plus consistent metadata—is already a huge upgrade.


## **Step 6 – Cross-project indexing: `diagram-index`**

>“I have diagrams in multiple repos. How do I find them later?”

Create a small, separate folder (or repo) called `diagram_index/`:
```text
diagram_index/  
    index.yaml
```

Inside `index.yaml`, start with entries for the diagrams in this tutorial:
```text
diagrams:  
  - id: per_project_workflow_v1  
    title: Per-Project Diagram Workflow  
    project: mermaid_diagram_workflow  
    repo: git@github.com:you/mermaid-diagram-workflow.git  
    path: diagrams/per_project_workflow_v1.0.mmd  
    visibility: public  
    status: stable  
    tags: [workflow, mermaid, documentation]  
    last_updated: 2025-11-19

  - id: cross_project_index_v1  
    title: Cross-Project Diagram Index  
    project: mermaid_diagram_workflow  
    repo: git@github.com:you/mermaid-diagram-workflow.git  
    path: diagrams/cross_project_index_v1.0.mmd  
    visibility: public  
    status: draft  
    tags: [index, diagrams, architecture]  
    last_updated: 2025-11-19
```

Over time, as you create “canonical” diagrams in other repos, add them here.
Even a **hand-maintained index** is enough to make your visual library feel navigable.

### **Cross-project architecture diagram**

Here’s a Mermaid diagram you can save as `diagrams/cross_project_index_v1.0.mmd`:
```mermaid
---  
id: cross_project_index_v1  
title: Cross-Project Diagram Index  
project: mermaid_diagram_workflow  
visibility: public  
status: draft  
last_updated: 2025-11-19  
tags: [index, diagrams, architecture]  
sequence:  
  group: "mermaid-diagram-workflow-post"  
  order: 3  
---

flowchart LR  
    subgraph ProjectA[Repo A]  
        A1[/diagrams/ folder/]  
    end

    subgraph ProjectB[Repo B]  
        B1[/diagrams/ folder/]  
    end

    subgraph ProjectC[Repo C]  
        C1[/diagrams/ folder/]  
    end

    Index[[diagram_index/index.yaml]]

    A1 --> Index  
    B1 --> Index  
    C1 --> Index
```

Conceptually:
* Each repo has its own `/diagrams/` folder and local workflow.
* **The `diagram_index/index.yaml` file is your **hub** for discovery.**


## **Step 7 – Before & after: the “diagram landscape”**

To make all this concrete, it helps to visualize the shift from **scattered** to **structured**.

Save this as `diagrams/scattered_vs_structured_v1.0.mmd`:
```mermaid
---  
id: scattered_vs_structured_v1  
title: Scattered vs Structured Diagrams  
project: mermaid_diagram_workflow  
visibility: public  
status: stable  
last_updated: 2025-11-19  
tags: [overview, documentation, mermaid]  
sequence:  
  group: "mermaid-diagram-workflow-post"  
  order: 0  
---

flowchart LR  
    subgraph Scattered[Before: Scattered]  
        N[Notebook cell]  
        R[README snippet]  
        I[Issue comment]  
        S[Slides-only version]  
    end

    subgraph Structured[After: Structured]  
        D[/diagrams/ folder/]  
        H[[diagram_index]]  
    end

    N --> D  
    R --> D  
    I --> D  
    S --> D  
    D --> H
```

Now you have a **diagram sequence** inside this blog’s own repo:
1. `scattered_vs_structured_v1` – problem vs target state
2. `per_project_workflow_v1` – per-project inner loop
3. `cross_project_index_v1` – multi-project architecture

The metadata (`sequence.group` and `sequence.order`) is what lets a tool—or a future you—recognize and present them as a coherent story.


## **Step 8 – A small Streamlit companion (the meta deliverable)**

In this repo, I also have a small **Streamlit app** that:
* reminds me of this workflow (checklists, code snippets, diagrams),
* reads `diagram_index/index.yaml`,
* lets me browse diagrams by `project`, `visibility`, `status`, and `tags`,
* and shows each diagram’s metadata \+ SVG preview.


It’s intentionally minimal: more of a **live note-taking surface** than a full product. But it’s enough to:
* reinforce the practice,
* demonstrate the value of a `diagram-index`,
* and give you a starting point if you want to build your own visual library UI.

Check the `streamlit_app/` folder in this repo for the example app and instructions for running it.

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
LET'S RECAP
</div>

## *Whew.* If you followed along, here's what we built
* centralized your diagrams in `/diagrams/`,
* given them metadata that your tools (and future self) can use,
* created an easy “regenerate SVGs” command,
* and taken the first step toward a **cross-project diagram index**.

That’s a lot of structure for something as simple as diagrams—but it’s structure that pays off immediately. Instead of hunting through notebooks or rewriting visuals from scratch, you’ll have a place where diagrams live, breathe, and improve over time. They become a part of your craft: tools for thinking, teaching, and remembering.


### **Where to go from here**

From here, you can gradually expand:
1. Apply the same pattern to other repos.
2. Add more metadata fields that matter to you.
3. Build a small CLI (`diagram-hub`) to:
    * scan for `.mmd` files,
    * extract frontmatter,
    * update the central `diagram_index/index.yaml`.

4. Extend the Streamlit app (or another UI) to:
    * explore diagram sequences,
    * tag diagrams for talks or blog posts,
    * track which diagrams are used where.

The important thing is that our diagrams are no longer ghosts floating around in snippets! They have a **home**, a **structure**, and a small but growing **ecosystem** around them. That’s a big win already—and a very comfortable place to iterate from.

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
NEXT TIME
</div>

In the next post, we’ll extend this workflow with lightweight automation—GitHub Actions, multi-repo syncing, and maybe even a visual index you can publish. For now, enjoy the calm of knowing your diagrams have a real home.
