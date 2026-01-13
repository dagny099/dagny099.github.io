---
layout: single
title: "Digital Home Base Workshop Part 4- A Data Scientist's Reflections of Workshop to Web"
subtitle: "Lessons learned about automation, visibility, and technical documentation"
date: 2024-08-18
sitemap:
    priority: 0.5
permalink: /blog/post-deployment-reflextions/
redirect_from:
  - /posts/post-deployment-reflextions/
  - /tutorial/post-deployment-reflextions/
header:
  overlay_image: "/assets/images/midjourney/wall-worthy/sq-celestial-reflections.png"
excerpt: What started as a simple website project turned into valuable insights about how we approach and document technical processes. Join me for some "aha!" moments about automation, visibility, and technical documentation.
excerpt_display: false
tags: [reflection]
classes: [wide]
categories: [tutorial]
pagination: 
  enabled: true
---

*This is the fourth post in my website-building series, but it's a bit different. Instead of a how-to guide, it's a pause for reflection – because sometimes the most valuable learning happens when we stop to think about what we **think** we learned versus what we **actually** learned.* 

## 🤔 The Moment of Truth 

**What I Thought Was Happening:** Before diving into GitHub Actions, my mental model was simple:  
1. I push code  
2. *Something happens*  
3. My site updates  

That middle step? Pure magic. ✨ And as a data scientist, I should know better – we don't trust black boxes in our models, so why was I comfortable with one in my deployment process?

**What's Actually Happening Now:**  With GitHub Actions, the process is:   
1. I push code  
2. A visible, configurable workflow kicks in:  
   - Jekyll builds the site  
   - Tests run (if I want them to)  
   - Custom checks execute (if I need them)  
   - Deployment happens  
3. My site updates  

The difference? **Transparency and control**. Just like how we prefer interpretable models to black-box ones, having visibility into our deployment process is invaluable.

### 💎 The Real Value Proposition

Here's what I realized was the actual value of adding GitHub Actions:

1. **Visibility** 👀
   - Every step of the build process is logged
   - Errors are traceable and debuggable
   - No more wondering why something broke

2. **Control** 🎮
   - Custom build steps
   - Ability to add tests
   - Power to modify the deployment process

3. **Extensibility** 🔧
   - Can add automated testing
   - Potential for custom validations
   - Ability to integrate with other tools

### 🧠 Lessons for Technical Documentation 

This experience taught me something important about technical writing and documentation: **the "why" is just as important as the "how"**. In my previous post, I showed you how to set up GitHub Actions, but I hadn't fully grasped the why myself.

**What I'll Strive to Do Better:****
1. **Start with the Why**: Begin with clear motivation and context
2. **Show the Evolution**: Demonstrate how and why things change
3. **Highlight True Value**: Focus on what we gain, not just what we do
4. **Question Assumptions**: Challenge the "magic" in our technical processes
5. **Document the Journey**: Share both successes and realizations

For data scientists and developers, this means:  
- Treating our deployment pipelines with the same rigor as our data pipelines  
- Looking for opportunities to add visibility to "magical" processes  
- Building systems we can debug, extend, and understand  

[Home](/)
