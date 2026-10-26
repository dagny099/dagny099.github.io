---
layout: post
classes: wide
title: How I Organized My Mermaid Life
subtitle: A cross project workflow for humans with too many ideas
date: 2025-10-11
last_modified_at: 2026-10-26
permalink: /blog/taming-mermaid-diagrams/
redirect_from:
  - /posts/organized-mermaid-life/
  - /tutorial/taming-mermaid-diagrams-across-projects/
header:
  teaser: /assets/diagrams/diagram_journey_from_idea_to_asset_v1.svg
excerpt: Treat Mermaid diagrams like <b>visual source code</b> with a home, structure, and a tiny bit of automation.
excerpt_display: true
tags: [documentation, diagrams, workflow, visual-code, tutorial]
stack: [Mermaid.js, Streamlit, Markdown, Git]
read_time: false
categories: [tutorial]
---

*Updated October 2026. The metadata examples in the first version were missing the `---` lines Mermaid needs, so every one of them failed to render, on this page and in the render script. They're fixed below, and every diagram on this page was rendered by the companion repo's own script from the files in that repo. The [companion repo](https://github.com/dagny099/mermaid-diagram-workflow) is now public.*

## Overview

If your Mermaid diagrams are scattered across notebooks, READMEs, and screenshots, this post walks you through building a **simple, reusable workflow**:

- Treat diagrams as **first-class assets** with a `/diagrams/` folder in each repo.
- Use a **consistent naming convention** and **lightweight metadata** (including `visibility`, `status`, `tags`, and optional sequence info).
- Add a **one-command script** to render all `.mmd` files to `.svg` using Mermaid CLI.
- Start a small **cross-project `diagram-index`** so you can find the right diagram later.
- Learn how to think in terms of **"diagram sequences"** to teach and tell stories.
- As a companion, there's a **Streamlit app** in the [companion repo](https://github.com/dagny099/mermaid-diagram-workflow) that helps you:
  - remember the workflow,
  - explore diagrams by metadata,
  - and experiment with sequences.

You can do the entire tutorial with **one project and two or three diagrams** and still come away with a meaningful upgrade to your documentation.

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
MOTIVATION
</div>

![Before and after: diagrams scattered across a notebook cell, a README snippet, an issue comment and a slides-only version, all gathered into one diagrams/ folder that feeds a diagram index]({{ '/assets/diagrams/scattered_vs_structured_diagram_workflow_v1.svg' | relative_url }}){: .align-center}

## The Diagram Journey

This is the visual that guides the entire workflow explained in this post.

{% include figure
   image_path="assets/diagrams/diagram_journey_from_idea_to_asset_v1.svg"
   caption="A simple but powerful lifecycle for managing diagrams across projects."
   alt="Mermaid diagram showing the lifecycle from a diagram idea, to a rough sketch, to the diagrams folder, to metadata, to a rendered SVG, to the diagram index, to use in docs, slides and apps"
%}

### My On-again, Off-again Relationship with Mermaid

For years my Mermaid diagrams lived everywhere _except_ where I needed them:
- a cell in a Jupyter notebook,
- a Markdown snippet in a README,
- a one-off paste into a GitHub issue,
- or a lovingly-crafted diagram that only survived as a PNG in slides.

Worse, I often had multiple versions of "the same" diagram:
- one messy but detailed version I used to think through a system,
- one cleaned-up version for presentations,
- and one experimental branch that only kind-of rendered.

Most frustratingly, when I wanted to reuse a diagram, I couldn't quickly answer the question, *"Which version is the **most recent**, **most detailed**, and still **renders**?"*

{: .notice--primary .text-center}
The idea behind this post is simple: treat Mermaid diagrams like <b>visual source code</b>, with a home, structure, and a tiny bit of automation.

By the end of this tutorial you'll have:
* A `/diagrams/` folder in at least one project
* A naming convention and metadata block for your diagrams
* A script that renders all `.mmd` files to `.svg`
* A tiny `diagram-index` you can grow over time
* A mental model of **diagram sequences** for teaching and storytelling
* As a bonus, a **Streamlit app** that demonstrates the same ideas :)

Everything below lives in the [companion repo](https://github.com/dagny099/mermaid-diagram-workflow), so you can clone it and follow along with real files.

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
Tutorial
</div>

## **Step 1 – Give diagrams a home: `/diagrams/`**

Pick one project you care about and create a `diagrams/` folder at the root.

Move one or two Mermaid diagrams into this folder as standalone files:
```text
a-project/
    diagrams/
        data_flow_core_v1.mmd
        per_project_workflow_v1.mmd
```

Each file contains **optional metadata** at the top, followed by **plain Mermaid code**. (We'll get to the metadata in Step 3.)

<mark>From now on, when I think, "Where should I put this diagram?", my answer is QUICK: it goes in <b>diagrams/</b></mark>


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

You don't have to use every piece every time. The minor version is optional, too: the diagrams in the companion repo are just `_v1`. Being explicit about **diagram type** is the part that pays off.

### **Diagram type cheat sheet**

Here's a compact table of common Mermaid-friendly diagram types and what they're good for (especially in data / ML / systems work):

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

<mark>When I use these fragments directly in file names, even just scanning the project's <b>diagrams/</b> folder becomes a reminder of <b>what kinds of visual documentation exist</b> and what's missing!</mark>


## **Step 3 – Add metadata front matter (including visibility & sequences)**

Now we'll turn each `.mmd` file into a **self-describing artifact** by adding a block of YAML at the top, between two `---` lines. Mermaid calls this *front matter*. Start simple. Here's the whole of `diagrams/data_flow_core_v1.mmd` (minus its colors):

```text
---
id: data_flow_core_v1
title: Core Data Flow
project: mermaid_diagram_workflow
last_updated: 2026-10-26
tags: [data, etl, pipeline]
---
flowchart LR
    A[Source system] --> B[ETL job]
    B --> C[Warehouse table]
    C --> D[Dashboard]
```

The two `---` lines are not optional, and the first version of this post left them out. Here's what Mermaid 11, Mermaid 12, and the Mermaid CLI all do with each way of writing the metadata:

| How the metadata is written | What Mermaid does |
| ----- | ----- |
| YAML between `---` lines (above) | Renders the diagram and ignores keys it doesn't know |
| `%% id: data_flow_core_v1` comment lines | Renders, but tools can't read the comments as YAML |
| Bare `id: data_flow_core_v1` lines, no `---` | Fails: `No diagram type detected` |

One more thing worth knowing: Mermaid reads *one* of these keys itself. `title` gets drawn above the diagram, which is why the diagrams on this page have headings. If you'd rather keep the title out of the picture, name the key something else, like `name`.

### **Extended metadata (for visibility, lifecycle, and sequences)**

Once that's working, you can expand to a richer schema that supports:
* **Visibility / permissions**
* **Status** (draft vs stable)
* **Sequences** (for teaching / storytelling)
* **Deprecation / supersedes**

For example:
```text
---
id: workout_classification_flow_v1
title: Workout Classification Flow
project: fitness_dashboard
visibility: private            # public | internal | private
status: stable                 # draft | stable | deprecated
last_updated: 2025-11-19
tags: [fitness, ml, classification]
sequence:
  group: fitness-dashboard-walkthrough
  order: 2
supersedes: workout_classification_flow_v0
description: >
  Shows how raw workout data flows through the ML classifier,
  including fallback logic and the mapping to UI labels.
---
flowchart LR
    ...
```

You don't *have* to fill in every field for every diagram, but:
* `visibility`, `status`, and `last_updated` **keep your library honest**.
* `sequence.group` and `sequence.order` let you assemble **diagram sequences** for teaching or storytelling later.
* `description` is a <mark>human summary that makes a future you very happy</mark>.


## **Step 4 – A tiny script to render all diagrams**

Now let's make sure your diagrams are easy to **preview** and reuse in docs, slides, and apps.

We'll use the Mermaid CLI (`@mermaid-js/mermaid-cli`) to convert `.mmd` → `.svg`.

### **4.1 Install Mermaid CLI (once per project)**

At the root of your project:

```bash
npm install --save-dev @mermaid-js/mermaid-cli
```

This gives you the `mmdc` command via `npx`.

### **4.2 Render one diagram manually (sanity check)**

Try rendering a single file:

```bash
npx mmdc -i diagrams/data_flow_core_v1.mmd -o diagrams/data_flow_core_v1.svg
```

If everything is installed correctly, you should see a new SVG file appear.
You can open it in your browser or image viewer and make sure it looks right.

### **4.3 Add a "render all diagrams" script**
I like to think of this as my **"regenerate visual library"** button.

Save this as `scripts/render_diagrams.sh`:
```bash
#!/usr/bin/env bash
# Render every Mermaid file in diagrams/ to an SVG next to it.
set -euo pipefail

echo "Rendering all Mermaid diagrams in ./diagrams"
for f in diagrams/*.mmd; do
  out="${f%.mmd}.svg"
  echo "  - $f -> $out"
  npx mmdc -i "$f" -o "$out" --quiet
done
echo "Done!"
```

Make it executable:
```bash
chmod +x scripts/render_diagrams.sh
```

<mark>Now you can render all diagrams at once: <b>./scripts/render_diagrams.sh</b></mark>

Here it is running in the companion repo, turning five `.mmd` files into five `.svg` files:

{% include figure image_path="/assets/videos/mermaid-render-terminal.svg" alt="Terminal recording in the mermaid-diagram-workflow repo. cat shows per_project_workflow_v1.mmd with YAML front matter between --- lines followed by a flowchart. ls diagrams lists five .mmd files. ./scripts/render_diagrams.sh prints one line per file as it renders each to SVG, then Done. ls diagrams now lists each .mmd next to its new .svg." caption="A real session in the companion repo: one file's front matter, the folder before, the script, and the folder after." %}

Because of `set -euo pipefail`, the script stops at the first diagram that fails to render, so a broken file can't hide behind a "Done!".


## **Step 5 – Per-project workflow (as a diagram sequence)**

Let's summarize the per-project workflow visually. Save this as `diagrams/per_project_workflow_v1.mmd`:

```text
---
id: per_project_workflow_v1
title: Per-Project Diagram Workflow
project: mermaid_diagram_workflow
visibility: public
status: stable
last_updated: 2026-10-26
tags: [workflow, mermaid, documentation]
sequence:
  group: mermaid-diagram-workflow-post
  order: 2
description: >
  The inner loop: edit a .mmd file, render it, use the SVG anywhere.
---
flowchart LR
    Edit[Edit .mmd file<br/>in diagrams/] --> Render[Run render_diagrams.sh]
    Render --> Svg[(Updated .svg files)]
    Svg --> Docs[Use diagrams in<br/>docs / slides / apps]
```

which renders as:

![Per-Project Diagram Workflow: edit .mmd file in diagrams/, run render_diagrams.sh, updated .svg files, use diagrams in docs, slides and apps]({{ '/assets/diagrams/per_project_workflow_v1.svg' | relative_url }}){: .align-center}

This is your **inner loop**:
1. Edit the `.mmd` file in `diagrams/`.
2. Run the render script.
3. Use the `.svg` anywhere you like.
4. Commit both `.mmd` and `.svg`.

This alone, plus consistent metadata, is already a huge upgrade.


## **Step 6 – Cross-project indexing: `diagram-index`**

>"I have diagrams in multiple repos. How do I find them later?"

Create a small, separate folder (or repo) called `diagram_index/`:
```text
diagram_index/
    index.yaml
```

Inside `index.yaml`, start with entries for the diagrams in this tutorial. These two are straight from the companion repo:
```yaml
diagrams:
  - id: per_project_workflow_v1
    title: Per-Project Diagram Workflow
    project: mermaid_diagram_workflow
    repo: https://github.com/dagny099/mermaid-diagram-workflow
    path: diagrams/per_project_workflow_v1.mmd
    visibility: public
    status: stable
    tags: [workflow, mermaid, documentation]
    sequence:
      group: mermaid-diagram-workflow-post
      order: 2
    last_updated: 2026-10-26

  - id: cross_project_index_v1
    title: Cross-Project Diagram Index
    project: mermaid_diagram_workflow
    repo: https://github.com/dagny099/mermaid-diagram-workflow
    path: diagrams/cross_project_index_v1.mmd
    visibility: public
    status: draft
    tags: [index, diagrams, architecture]
    sequence:
      group: mermaid-diagram-workflow-post
      order: 3
    last_updated: 2026-10-26
```

Over time, as you create "canonical" diagrams in other repos, add them here.
Even a **hand-maintained index** is enough to make your visual library feel navigable.

A hand-maintained index can also drift, and mine did. Every `path` in my first version pointed at a file name I'd since changed, so the Streamlit explorer showed "SVG missing" for every diagram, and nothing flagged it. If a `path` doesn't match a real file, nothing downstream can find it. (That drift is exactly what the automation ideas at the end of this post would catch.)

### **Cross-project architecture diagram**

Here's the picture of that setup. Save it as `diagrams/cross_project_index_v1.mmd`:
```text
---
id: cross_project_index_v1
title: Cross-Project Diagram Index
project: mermaid_diagram_workflow
visibility: public
status: draft
last_updated: 2026-10-26
tags: [index, diagrams, architecture]
sequence:
  group: mermaid-diagram-workflow-post
  order: 3
description: >
  Each repo keeps its own diagrams/ folder; one index.yaml points at all of them.
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

![Cross-Project Diagram Index: three repos, each with its own diagrams/ folder, all pointing to one diagram_index/index.yaml]({{ '/assets/diagrams/cross_project_index_v1.svg' | relative_url }}){: .align-center}

Conceptually:
* Each repo has its own `/diagrams/` folder and local workflow.
* The `diagram_index/index.yaml` file is your **hub** for discovery.


## **Step 7 – Before & after: the "diagram landscape"**

To make all this concrete, it helps to visualize the shift from **scattered** to **structured**. That's the diagram at the top of this post, and it lives in the repo as `diagrams/scattered_vs_structured_diagram_workflow_v1.mmd`. Here's a simplified version of it (the repo's copy adds colors and emoji):
```text
---
id: scattered_vs_structured_v1
title: Scattered vs Structured Diagrams
project: mermaid_diagram_workflow
visibility: public
status: stable
tags: [overview, documentation, mermaid]
sequence:
  group: mermaid-diagram-workflow-post
  order: 1
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

Now you have a **diagram sequence** inside this blog's own repo:
1. `scattered_vs_structured_v1` – problem vs target state
2. `per_project_workflow_v1` – per-project inner loop
3. `cross_project_index_v1` – multi-project architecture

The metadata (`sequence.group` and `sequence.order`) is what lets a tool, or a future you, recognize and present them as a coherent story.


## **Step 8 – A small Streamlit companion (the meta deliverable)**

The [companion repo](https://github.com/dagny099/mermaid-diagram-workflow) also has a small **Streamlit app** (`streamlit_app/app.py`) that:
* reminds me of this workflow (checklists, code snippets, diagrams),
* reads `diagram_index/index.yaml`,
* lets me browse diagrams by `project`, `visibility`, `status`, and `tags`,
* shows each diagram's metadata and SVG preview,
* lays out a sequence group in order, as a storyboard,
* and has a **New Diagram** wizard that writes a correctly named `.mmd` file with its front matter already filled in.

Here it is in action: searching the explorer, previewing a diagram, walking the sequence from this post, and using the wizard to start a new diagram for a fitness dashboard.

<video controls muted playsinline preload="metadata" poster="{{ '/assets/images/mermaid-app-walkthrough-poster.jpg' | relative_url }}" style="width:100%; border:1px solid #ddd; border-radius:8px;">
  <source src="{{ '/assets/videos/mermaid-app-walkthrough.mp4' | relative_url }}" type="video/mp4">
  A 38-second walkthrough of the Mermaid Diagram Workflow Helper app.
</video>

Recording that walkthrough is how the wizard's own bug turned up: it wrapped the new diagram in a Markdown `mermaid` code fence, which a `.mmd` file can't contain, so the render script failed on every file it created. It's fixed in the repo now. Using your own tool on camera turns out to be a decent test.

It's intentionally minimal: more of a **live note-taking surface** than a full product. But it's enough to:
* reinforce the practice,
* demonstrate the value of a `diagram-index`,
* and give you a starting point if you want to build your own visual library UI.

To run it, clone the repo and follow the quickstart in its README:

```bash
git clone https://github.com/dagny099/mermaid-diagram-workflow.git
cd mermaid-diagram-workflow
npm install
./scripts/render_diagrams.sh
pip install streamlit pyyaml python-frontmatter
streamlit run streamlit_app/app.py
```

<div style="font-variant: small-caps; font-size: 0.9rem; color:#555; margin-top:3rem;">
LET'S RECAP
</div>

## *Whew.* If you followed along, here's what we built
* centralized your diagrams in `/diagrams/`,
* given them metadata that your tools (and future self) can use,
* created an easy "regenerate SVGs" command,
* and taken the first step toward a **cross-project diagram index**.

That's a lot of structure for something as simple as diagrams, but it's structure that pays off immediately. Instead of hunting through notebooks or rewriting visuals from scratch, you'll have a place where diagrams live, breathe, and improve over time. They become a part of your craft: tools for thinking, teaching, and remembering.


### **Where to go from here**

From here, you can gradually expand:
1. Apply the same pattern to other repos.
2. Add more metadata fields that matter to you.
3. Build a small CLI (`diagram-hub`) to:
    * scan for `.mmd` files,
    * extract front matter,
    * update the central `diagram_index/index.yaml`.

   The first two already exist in the repo: `scan_diagrams()` in `diagram_hub/scan.py` reads the front matter from every diagram in a project. Writing the index from it is the missing piece, and it would have caught my drifted paths.
4. Extend the Streamlit app (or another UI) to:
    * explore diagram sequences,
    * tag diagrams for talks or blog posts,
    * track which diagrams are used where.

The important thing is that our diagrams are no longer ghosts floating around in snippets! They have a **home**, a **structure**, and a small but growing **ecosystem** around them. That's a big win already, and a very comfortable place to iterate from.
