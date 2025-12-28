---
layout: single
title: "Digital Home Base Workshop Part 1- Assembly Required: Getting Started with GitHub Pages"
subtitle: "Build a professional portfolio site using GitHub Pages and Jekyll - version control for data professionals"
date: 2024-07-28
last_modified_at: 2024-07-28
sitemap:
    priority: 0.5
permalink: /blog/getting-started-with-github-pages/
redirect_from:
  - /posts/getting-started-with-github-pages/
  - /tutorial/getting-started-with-github-pages/
header:
  overlay_image: "/assets/images/midjourney/wall-worthy/inceptiony-girl-central-grandiose-scifi-feel.png"
excerpt: "Learn how to create a beautiful, professional website using GitHub Pages – perfect for data professionals who love version control and markdown."
excerpt_display: false
classes: [wide]
tags: [static-site, portfolio, website-building, tutorial]
stack: [Jekyll, GitHub Pages, Markdown, Git]
categories: [tutorial]
pagination: 
  enabled: true
---

As a data scientist, you're probably comfortable with Jupyter notebooks and GitHub repositories. But let's be honest – sending someone a repo link isn't exactly the most elegant way to showcase your work. What if you could have a beautiful, professional website that's as easy to update as pushing to a repository? Enter GitHub Pages.

## Digital Home Base Motivations

Back in 2020, I was drowning in a sea of options for building my online presence. WordPress felt bloated, Medium wasn't customizable enough, and hand-coding a responsive website seemed like overkill. That's when I discovered GitHub Pages, and it turned out to be the perfect solution for a data professional's needs.

![image-left]({{ site.url }}{{ site.baseurl }}/assets/images/series-website/so-many-options-for-a-data-sci.png){: .align-right style="max-width: 400px"} 

What makes it click for data people? It's version control native (if you can git push, you can update your website), Markdown-based (just like your notebooks!), and perfect for embedding visualizations and code snippets. Plus, it's free, secure (HTTPS by default), and looks professional with custom domain support.

What makes it click for data people? It's version control native (if you can `git push`, you can update your website), Markdown-based (just like your notebooks!), and perfect for embedding visualizations and code snippets. Plus, it's free, secure (HTTPS by default), and looks professional with custom domain support.

## The Building Blocks: Understanding Your Site

Before we dive into setup, let's peek at what makes up a GitHub Pages site:

```
yoursite.github.io/
├── _config.yml           # Your site's control center
├── index.md              # Your homepage
├── _posts/               # Where your blog posts live
├── _pages/               # Static pages (About, Portfolio)
├── _data/               # Site data files
│   └── navigation.yml   # Navigation structure
└── assets/             # Images and other media
```

Think of it like a well-organized data project: your configuration goes in `_config.yml`, your content lives in `_posts` and `_pages`, and all your assets have their proper place. Simple, right?

## Quick Start Guide

### Prerequisites
- Basic Git knowledge (if you can commit and push, you're ready)
- A GitHub account
- A text editor
- Basic terminal familiarity

### Step 1: Create Your Repository
1. Log into GitHub
2. Create a new repository named `yourusername.github.io` -- The name is crucial – it must match this format exactly!

### Step 2: Set Up Your Theme
We'll use Minimal Mistakes (clean, professional, great for data visualization). Fork the [starter repository](https://github.com/mmistakes/mm-github-pages-starter), rename it to `yourusername.github.io`, and:

```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:yourusername/yourusername.github.io.git
git push -u origin main
```


### Step 3: Initial Configuration
The `_config.yml` file is your website's control center. Here's a minimal configuration to get started:

### Step 3: Configure
In `_config.yml`, set up your basics:

```yaml
title: Your Name
subtitle: "Data Scientist | Machine Learning Engineer"
description: "Personal website and blog about data science"
url: "https://yourusername.github.io"
```


### Step 4: Add Your First Content
Create your first blog post:
1. Create a new file in `_posts/2024-02-15-first-post.md`
2. Add front matter and content:

```markdown
 ---
 title: "Why Every Data Scientist Needs a Blog"
 date: 2024-02-15
 categories:
   - blog
 tags:
   - data science
   - writing
   - career
 ---

Your content here in Markdown format...
```

Don't overthink it – start with something like "Why I Love Data" or "My Journey into Machine Learning". The beauty of GitHub Pages is you can always update it later!

### Step 5: Deploy Your Site

1. Push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Add initial content"
   git push origin main
   ```

2. Enable GitHub Pages:
   - Go to your repository settings
   - Navigate to "Pages"
   - Under "Build and deployment", select:
     - Source: "Deploy from a branch"
     - Branch: "main" (or your preferred branch)
   - Click Save

3. Wait a few minutes for GitHub to build your site
4. Visit `https://yourusername.github.io` to see your live site!

## Common Gotchas
- Repository must be named exactly `yourusername.github.io`
- Always check your YAML indentation in `_config.yml`
- Be patient after pushing – builds take a few minutes
- When local testing and not seeing an expected change, it can be helpful to delete "_site" and rebuild again. 


## Next Steps

In [Post 2: Jekyll Deep Dive](/posts/understanding-your-jekyll-site/), we'll explore:
- Setting up your local development environment
- Customizing your theme
- Working with collections and layouts
- Adding dynamic features
- Optimizing for search engines

In other posts, I'd like to cover: 
- **Content Organization**: Set up collections for projects and papers
- **Local Testing**: Set up a local development environment (we'll cover this in Post 2)
- **Analytics**: Add Google Analytics to track your reach


## Resources
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Minimal Mistakes Theme Guide](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)

> "Your work is only as visible as your ability to share it effectively."   
