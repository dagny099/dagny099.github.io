# README

Hola! 👋 Thanks for visting the GitHub repository for my personal website. This is where I host the code for my personal website, which serves as my portfolio and blog.

## Visit My Website

You can check out my website at: https://barbhs.com

## About My Site

This website is my digital hub where I share projects, articles, and my musings as a data scientist. It's built with [Jekyll](https://jekyllrb.com/), a static site generator, uses the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme, and is hosted on [GitHub Pages](https://pages.github.com/).  

## Features

- 📊 Portfolio showcasing my data science projects
- 📝 Blog where I write about data science, knowledge organization, and on occasion current events
- 🐝 Custom design to reflect my personal interests
- ✓ Metadata validation script to ensure content quality and SEO optimization
- 🧩 Snippets collection (added 12/11/25) for short, reusable insights
- 💼 **JSON-powered resume architecture** (added 04/08/26) - single source of truth for professional experience


## How It's Built

Back in 2020, I was searching for a way to have a digital "home base" that would be aesthetically attractive, easy to update, and minimize the annoying parts of coding a responsive modern webpage. That's when I found [GitHub Pages sites](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) and I've been an enthusiastic advocate ever since.  

**GitHub Pages** is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website. It's an excellent choice for projects like personal websites, portfolios, and project documentation for several reasons:

🆓 Pricetag = $0 
🔒 Secure (HTTPS by default)  
🔗 Direct integration with GitHub repositories  
🚀 Easy deployment through git push  
🎛️ Custom domain support, yay!


**Jekyll** was new to me and I'm very glad to have learned it. It takes simple text files (written in Markdown) and processes them through templatees to generate a complete, static HTML website. Jekyll allows me to focus on creating content while it handles the complexities of site generation, just like I wanted.

I recommend anyone with a similar requirement set for their webpage to do the GitHub Pages exercise on [GitHub Skills](https://github.com/skills/github-pages).


## Metadata Validation

This repository includes a Python script to validate content metadata and ensure consistency across all blog posts, portfolio items, and data stories. Good metadata improves SEO, social media sharing, and content organization.

**Quick start:**
```bash
# Validate all content
python scripts/validate_metadata.py

# Validate specific collection
python scripts/validate_metadata.py --collection posts
```

The script checks for:
- Required fields (title, excerpt, tags, dates)
- Excerpt length (150-300 chars is ideal for SEO)
- Tag formatting (hyphens not spaces)
- Date format consistency (YYYY-MM-DD or full timestamp)
- Technology stack for technical content
- Header images for visual content

For more details on metadata best practices, see the [metadata validation script documentation](scripts/README.md) or read the blog post on [why metadata matters](/blog/metadata-matters/).

## Resume Data Architecture

This site uses a **data-driven resume system** where professional experience is stored in a single JSON file (`_data/barbara_resume_golden.json`) that serves as the source of truth for multiple outputs:

- 🌐 **[/experience/](/experience/)** - Dynamic filtering of work history with tags and domains
- 📄 **PDF Resume** - Professional summary document
- 📊 **Future outputs** - TimelineJS visualizations, API endpoints, automated LinkedIn sync

**Why this approach?**
- ✅ Single source of truth prevents version drift
- ✅ Structured data enables automation and filtering
- ✅ Version controlled via Git
- ✅ Easy to query, transform, and generate outputs

**Key files:**
- `_data/barbara_resume_golden.json` - Main data file (490 lines, 8 sections)
- `_data/barbara_resume_golden_SCHEMA.json` - JSON Schema for validation
- `_pages/experience.md` - Template that renders the experience page
- `_resources/resume-data-schema.md` - Full documentation

**Learn more:** [Resume Data Schema Documentation](/resources/resume-data-schema/)

## Local Development

If you're interested in how this site is set up or want to use it as a template for your own:

1. Clone this repository
2. Make sure you have Jekyll installed (see [Jekyll Installation Guide](https://jekyllrb.com/docs/installation/))
3. Run `bundle install` to install dependencies
4. Run `bundle exec jekyll serve` or `bundle exec jekyll serve --port 4000` to start the local server
5. Visit `http://localhost:4000` in your browser

**Before committing new content:**
```bash
# Validate your metadata
python scripts/validate_metadata.py
```

## Questions or Suggestions?

Feel free to open an issue if you have any questions about this repository or suggestions for my website. I'm always open to feedback and new ideas!
