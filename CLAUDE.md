# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal website built with Jekyll, using the Minimal Mistakes theme, and hosted on GitHub Pages. It serves as a portfolio and blog for a data scientist, featuring project showcases, articles, and visualizations.

## Development Commands

### Local Development
- `bundle install` - Install Ruby dependencies
- `bundle exec jekyll serve` - Start local development server at http://localhost:4000
- `bundle exec jekyll build` - Build the site for production

### GitHub Pages Deployment
The site automatically deploys to GitHub Pages when changes are pushed to the master branch. The live site is available at https://barbhs.com.

## Architecture

### Jekyll Structure
- `_config.yml` - Main Jekyll configuration file with site settings, theme configuration (Minimal Mistakes), plugins, and collections
- `_posts/` - Blog posts in Markdown format
- `_portfolio/` - Portfolio project pages (custom collection)
- `_pages/` - Static pages
- `_layouts/` - Custom HTML layouts extending the theme
- `_includes/` - Reusable HTML components
- `_data/` - YAML data files for site content
- `_sass/` - Custom SCSS styles
- `assets/` - Images, documents, CSS, and JavaScript files
- `_site/` - Generated site output (excluded from version control)

### Theme and Styling
- Uses Minimal Mistakes remote theme (version 4.27.1) with "air" skin
- Custom styling through SCSS in `_sass/` directory
- Logo and branding assets in `assets/images/`

### Content Organization
- **Portfolio Collection**: Custom Jekyll collection for project showcases with permalink structure `/portfolio/:title/`
- **Blog Posts**: Traditional Jekyll posts with pagination (3 per page)
- **Data Stories**: Special content category for data visualization projects
- **Explorations**: Documentation of various technical experiments

### Key Features
- Google Analytics integration (G-VPLSBQSHER)
- Search functionality using Lunr.js
- Author profile with social media links
- Breadcrumb navigation
- Responsive design with custom masthead logo
- PDF document hosting for academic papers and resume

## Content Management

### Adding New Portfolio Items
Create markdown files in `_portfolio/` directory. The collection is configured to output individual pages at `/portfolio/:title/`.

### Blog Posts
Standard Jekyll posts in `_posts/` directory using YAML front matter for metadata.

### Assets
- Images organized by category in `assets/images/`
- Academic documents in `assets/docs/`
- Custom visualizations in `assets/visualizations/`

## Deployment

The site uses GitHub Pages with the github-pages gem for dependency management. No custom build process is required - Jekyll automatically builds the site when changes are pushed to the master branch.