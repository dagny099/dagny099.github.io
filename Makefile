# Makefile for Jekyll Site Maintenance
# Usage: make <target>

.PHONY: help sitemap install serve

help:  ## Show this help message
	@echo "Jekyll Site Maintenance Commands"
	@echo "================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install Python dependencies for scripts
	pip install -r scripts/requirements.txt

sitemap:  ## Generate/update sitemap diagram
	python scripts/generate_sitemap.py

serve:  ## Start local Jekyll server
	bundle exec jekyll serve

build:  ## Build Jekyll site
	bundle exec jekyll build

clean:  ## Clean Jekyll build artifacts
	bundle exec jekyll clean
