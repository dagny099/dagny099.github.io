---
layout: single
title: "Midjourney Image Tracker"
description: "Organize and analyze image generations from Midjourney with metadata, tagging, and image download tools."
permalink: /projects/midjourney-extension/
classes: [project, wide]
author_profile: false
read_time: false
toc: true
toc_sticky: true
toc_label: "Contents"
toc_icon: "bookmark"
order: 10
tags: [Chrome Extension, JavaScript, Browser Tools, Midjourney, AI Art]
categories: ["Data Products & Interfaces"]
stack: [JavaScript, Chrome Extension (Manifest V3), Chrome Storage API, MutationObserver]
status: WIP
header:
  teaser: assets/images/portfolio/mj-extension-popup.png
  overlay_image: assets/images/portfolio/mj-extension-hero.png
  overlay_filter: 0.25
  caption: "Never lose track of the Midjourney images that sparked your imagination"
  actions:
    - label: "View Repo"
      url: https://github.com/dagny099/mj-extension
      class: "btn--primary"
    - label: "Read Docs"
      url: https://github.com/dagny099/mj-extension/tree/main/docs
      class: "btn--light-outline"
excerpt: "Midjourney's interface makes it easy to generate images but hard to track favorites across sessions. I built a Chrome extension that adds one-click bookmarking with intelligent URL deduplication—so the images worth revisiting are always one click away."
url: /projects/midjourney-extension/
btn_label: "Project"
docs_url: https://github.com/dagny099/mj-extension/tree/main/docs
docs_label: "Documentation"
---

**A lightweight Chrome extension that injects bookmark buttons directly into Midjourney pages.** Hover over any image, click once to save it, and export your collection as a standalone HTML gallery you can browse offline. The core trick: intelligent URL standardization that recognizes the same image across thumbnail, full-size, and grid formats—preventing the duplicate clutter that plagues manual bookmarking.

{% include page__taxonomy.html %}

<details>
<summary><strong>Read the 2-minute overview</strong></summary>

<br>

**What triggered the build:** After generating hundreds of Midjourney images, I realized I had no reliable way to curate favorites. The native interface shows everything chronologically with no persistent bookmarking. I kept losing track of images I wanted to revisit for style inspiration or iteration.

**Notable constraints:**
- Must work without backend infrastructure (all storage local)
- Cannot rely on Midjourney's internal APIs (they're undocumented and change frequently)
- Must handle dynamically-loaded content as users scroll
- URL formats vary wildly: thumbnails, full-res PNGs, WebP variants, grid composites

**What shipped:** A Manifest V3 Chrome extension with hover-activated bookmarks, a popup gallery for quick review, and export functionality that generates self-contained HTML files. The URL standardization logic handles every format I've encountered without false positives.

</details>

---

## What Shipped

- **One-click bookmarking** via hover-activated buttons injected directly onto Midjourney images
- **Smart URL normalization** that converts thumbnails (`0_0_640_N.webp`), full-size (`0_0.png`), and grid formats (`grid_0.png`) to a canonical form—eliminating duplicates automatically
- **Popup gallery** showing all saved images at a glance with remove functionality
- **HTML export** that generates a standalone, offline-viewable gallery file
- **Text export** for plain URL lists (useful for batch downloading via external tools)
- **Cross-page support** working across Midjourney's create, explore, and archive pages

## Why It Matters

Midjourney users generate far more images than they can remember. The friction of manually copying URLs or taking screenshots creates a gap between "images I made" and "images worth keeping." This extension closes that gap with zero disruption to the existing workflow—hover, click, done.

The URL standardization solves a real pain point: Midjourney serves the same image at different resolutions and formats depending on context. Without normalization, you'd bookmark the same image three times without realizing it.

## How It Works

The extension uses Chrome's Manifest V3 architecture with four coordinated components:

| Component | Role |
|-----------|------|
| **content.js** | Injects hover buttons onto Midjourney images via MutationObserver |
| **background.js** | Service worker managing storage and message routing |
| **popup.js** | Gallery interface in the extension popup |
| **shared.js** | URL standardization logic shared across all contexts |

**Message flow:**
1. User hovers over image → content script extracts URL
2. Click triggers `SAVE_URL` message → background script standardizes and stores
3. Popup requests `GET_URLS` → background returns deduplicated list
4. Export triggers `EXPORT_URLS` → generates downloadable file

**URL standardization example:**
```
Input:  cdn.midjourney.com/uuid/0_0_640_N.webp?method=shortest
Input:  cdn.midjourney.com/uuid/0_0.png
Output: cdn.midjourney.com/uuid/0_0.jpeg  (canonical form)
```

## Implementation Notes

**Performance optimizations:**
- **Debounced hover events** (200ms) prevent excessive processing during rapid mouse movement
- **In-memory Set** in background script enables O(1) duplicate detection
- **Content script caching** with 5-second TTL minimizes message passing overhead
- **Lazy button creation** only instantiates UI when images are actually hovered

**Security posture:**
- **Minimal permissions:** `activeTab`, `storage`, `downloads`, `tabs`
- **Domain-restricted:** only activates on `*.midjourney.com`
- **No external calls:** all data stays in `chrome.storage.local`
- **CSP-compliant:** no inline scripts

**Extension context handling:**
The content script includes recovery logic for context invalidation (common when extensions reload):
```javascript
function isExtensionContextValid() {
    try {
        chrome.runtime.getURL('');
        return true;
    } catch (e) {
        return false;
    }
}
```

## What I'd Do Next

- **Chrome Web Store publication** — packaging and submission in progress
- **Metadata capture** — store prompt text alongside image URLs (requires parsing Midjourney's DOM structure)
- **Tag/folder organization** — let users categorize bookmarks beyond a flat list
- **Sync across devices** — migrate from `chrome.storage.local` to `chrome.storage.sync`
- **Firefox port** — adapt Manifest V3 for Firefox's extension APIs

## Screens & Artifacts

*Note: Screenshots to be added to `assets/images/portfolio/` after Chrome Web Store submission.*

- Extension popup showing bookmarked images
- Hover button overlay on Midjourney explore page
- Exported HTML gallery rendered in browser
- User flow diagram: [mj-extension-user-journey-diagram.png](https://github.com/dagny099/mj-extension/blob/main/docs/images/mj-extension-user-journey-diagram.png)

---

## Links

[View Repository](https://github.com/dagny099/mj-extension){: .btn .btn--primary}
[Technical Docs](https://github.com/dagny099/mj-extension/tree/main/docs){: .btn .btn--light-outline}

**Deep dives:**
- [URL Standardization Logic](https://github.com/dagny099/mj-extension/blob/main/docs/url-standardization.md)
- [API Reference](https://github.com/dagny099/mj-extension/blob/main/docs/api-reference.md)
- [Development Guide](https://github.com/dagny099/mj-extension/blob/main/docs/development-guide.md)
