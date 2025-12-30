---
title: "Site Architecture & Content Sitemap"
excerpt: "Visual guide to site organization using Mermaid diagrams - how content hubs, blog series, and collections connect on barbhs.com"
permalink: /site-architecture/
layout: single
classes: wide extra-wide
#sidebar:
#  nav: "diagram-workflow"   # key defined in _data/navigation.yml
#toc: true
#toc_label: "Navigation"
#toc_icon: "map"
#breadcrumbs: false
---
<div style="height: 1px; background: #e5e5e5; margin:1rem 0;"></div>

This page is a **visual guide** to how content is organized on barbhs.com.  
I use diagrams (rendered from Mermaid and exported as SVG) to keep the site structure understandable both for myself and for visitors.

Below, you’ll see a layered approach:
1. A high-level [**top‑level structure**](#1-toplevel-site-structure-highlevel-overview) diagram  
2. Focused diagrams for [**modern collections**](#content-hubs) and [**notes & experiments architecture**](#notes-experiments-architecture)  
3. An [**interactive full sitemap**](#4-full-detailed-sitemap-with-clickable-links-) that exposes all the detail

I try to keep this page current, which doesn't always happen, but see Last Updated date at the bottom. See also this post about how to generate these diagrams and related workflow tips.

<div style="height: 1px; background: #e5e5e5; margin:1rem 0;"></div>

## 1. Top‑Level Site Structure: High‑Level Overview 

This diagram shows only the **primary navigation hubs** and major content areas.  
It’s the fastest way to understand what lives where on barbhs.com and what's being transitioned.

<div class="diagram-full-width" style="text-align:center; margin: 2rem 0;" >
  <a href="{{ '/assets/diagrams/site_map_overview_v1.0.svg' | relative_url }}" target="_blank">
    <img src="{{ '/assets/diagrams/site_map_overview_v1.0.svg' | relative_url }}"
         alt="Full site map"
         style="max-width:100%; height:auto;">
  </a>
  <p style="font-size:0.85rem; color:#444;">Click to open the high-resolution diagram in a new tab.</p>
</div>

{: style="text-align: left; font-size:.75em;"}
Color convention for diagram nodes:  
🟣 <span style="color: purple;">**Home** </span><br>
🔵 <span style="color: blue;">**Modern Collections/Hubs:**  Projects, Data Narratives, Essays &amp; Perspectives, Resources</span><br>
🟠 <span style="color: orange;">**Legacy Collections:** Portfolio and Supplementary Content (content being migrated, as of Nov 2025)</span><br>


## 2. Content Hubs: Projects, Data Narratives, Essays &amp; Perspectives, Resources {#content-hubs}

The **heart of the site** is a set of modern content collections:
- **Projects** –> Hands‑on, end‑to‑end builds with demos and documenation  
- **Data Narratives** –> Narrative-style, visual walkthroughs of real datasets  
- **Essays &amp; Perspectives** –> Essays and conceptual pieces  
- **Resources** – reusable templates, guides, and references  

The diagram below zooms into these collections and their key items, plus the legacy Portfolio.

<div class="diagram-full-width" style="text-align:center; margin: 2rem 0;">
  <a href="{{ '/assets/diagrams/site_map_collections_v1.0.svg' | relative_url }}" target="_blank">
    <img src="{{ '/assets/diagrams/site_map_collections_v1.0.svg' | relative_url }}"
         alt="Full site map"
         style="max-width:100%; height:150px;">
  </a>
  <p style="font-size:0.85rem; color:#444;">Click to open the high-resolution diagram in a new tab.</p>
</div>

{: style="text-align: left; font-size:.75em;"}
Color convention for diagram nodes:  
🔵 <span style="color: blue;">**Content hubs:** Projects, Data Narratives, Essays &amp; Perspectives, Resources</span><br>
🟣 <span style="color: purple;">**Data Narratives:** Technical narratives and case studies</span><br>
🟢 <span style="color: green;">**Essays &amp; Perspectives:** Writing, e.g. essays and conceptual pieces</span><br>
🔴 <span style="color: red;">**WIP:** Projects, mostly, in progress but sharable-state</span><br>
🟠 <span style="color: orange;">**Legacy Content:** Largely blogs including series and individual posts</span><br>


## 3. Notes &amp; Experiments Architecture: Series, Individual Posts, and Archives {#notes-experiments-architecture}

The **Notes &amp; Experiments** archive is the longest-running part of the site and contains:
- multi‑part **series** (like Website Building and Sensor Fleet),
- **individual posts** (e.g., project write‑ups, reflections),
- and archive pages (by tag and category).

This diagram shows how the pieces fit together:

<div class="diagram-full-width" style="text-align:center; margin: 2rem 0;">
  <a href="{{ '/assets/diagrams/site_map_blog_architecture_v1.0.svg' | relative_url }}" target="_blank">
    <img src="{{ '/assets/diagrams/site_map_blog_architecture_v1.0.svg' | relative_url }}"
         alt="Notes & experiments architecture diagram showing series, individual posts, and archives"
         style="max-width:100%; height:auto;">
  </a>
  <p style="font-size:0.85rem; color:#444;">Click to open the full notes &amp; experiments architecture diagram in a new tab.</p>
</div>

## 4. Full Detailed Sitemap, with Clickable Links 🔗

The diagrams above give you **usable mental models** without overwhelming detail.  
If you’d like to see everything at once, the full sitemap below exposes all the nodes and links.

One cool think about the diagram is that (many) of the nodes are **clickable links!** 
Hover over nodes to see tooltips with additional context:

  <div class="diagram-full-width" style="text-align:center; margin:2rem 0;">
    <a href="{{ '/assets/diagrams/site_map_full_v1.0.svg' | relative_url }}" target="_blank">
      <img src="{{ '/assets/diagrams/site_map_full_v1.0.svg' | relative_url }}"
           alt="Full detailed sitemap of barbhs.com"
           style="max-width:100%; height:auto;">
    </a>
    <p style="font-size:0.85rem; color:#444;">Open the full‑size sitemap in a new tab to zoom and explore every branch.</p>
  </div>


<div style="height: 1px; background: #e5e5e5; margin:2rem 0;"></div>

## How I Maintain This Map

<span class="material-symbols-outlined" style="font-size:24px; position:relative; top:4px;"> account_tree</span>
This sitemap isn’t a one‑off artifact; it’s part of my content workflow:  
- I keep the **Mermaid source files** for each diagram in a `/diagrams/` folder.  
- I export updated **SVGs** whenever the structure changes.  
- I treat this page as a **living document** that evolves as the site does.  

<span class="material-symbols-outlined" style="font-size:24px; position:relative; top:4px;"> bookmark_check</span>
In practice, when I...  
- Add a major new section (e.g., a new collection or series), <mark>I update the relevant diagram and regenerate the SVG</mark>.  
- Refactor navigation, this page is where <mark>I sanity‑check whether the new structure is still coherent.</mark>. 

<div style="height: 1px; background: #e5e5e5; margin:1rem 0;"></div>

{: .text-center}
If you’re building your own site or knowledge base, I recommend:  
<span class="material-symbols-outlined" style="font-size:24px; position:relative; top:4px;"> keyboard_arrow_right</span>
Starting with a **high‑level diagram** like the one at the top of this page  
<span class="material-symbols-outlined" style="font-size:24px; position:relative; top:4px;"> keyboard_arrow_right</span>
Adding **focused sub‑maps** for your most important content hubs  
<span class="material-symbols-outlined" style="font-size:24px; position:relative; top:4px;"> keyboard_arrow_right</span>
Keeping one **full, detailed sitemap** off to the side for periodic review  

{: .text-center}
It’s a small investment that makes your content ecosystem much easier to grow and maintain.

---

*Last updated: 2025-11-21*
