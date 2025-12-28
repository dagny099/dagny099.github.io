#!/usr/bin/env python3
"""
Metadata Validation Script for Jekyll Site
Validates front matter consistency across posts, projects, and other collections.

Usage:
    python scripts/validate_metadata.py
    python scripts/validate_metadata.py --collection posts
    python scripts/validate_metadata.py --fix-issues
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import argparse


class MetadataValidator:
    """Validates Jekyll front matter metadata across content collections."""

    # Required fields by collection type
    REQUIRED_FIELDS = {
        'posts': ['layout', 'title', 'date', 'excerpt', 'tags', 'categories'],
        'projects': ['layout', 'title', 'permalink', 'excerpt', 'tags', 'stack', 'status', 'header'],
        'portfolio': ['title', 'excerpt', 'date', 'tags', 'header'],
        'data-stories': ['title', 'excerpt', 'permalink', 'date', 'tags', 'stack', 'header'],
        'thinking': ['layout', 'title', 'date', 'excerpt', 'tags', 'toc'],
        'resources': ['layout', 'title', 'permalink', 'excerpt', 'tags', 'format', 'level'],
        'pages': ['layout', 'title', 'permalink'],
        'drafts': ['layout', 'title', 'excerpt']
    }

    # Recommended fields
    RECOMMENDED_FIELDS = {
        'posts': ['subtitle', 'header.overlay_image', 'stack', 'last_modified_at'],
        'projects': ['last_modified_at', 'header.teaser', 'header.actions'],
        'data-stories': ['last_modified_at', 'header.teaser'],
        'pages': ['excerpt', 'header'],
        'drafts': ['tags', 'date', 'subtitle'],
        'all': ['last_modified_at']
    }

    def __init__(self, base_path: str = '.'):
        self.base_path = Path(base_path)
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)

    def extract_front_matter(self, file_path: Path) -> Tuple[Dict, str]:
        """Extract YAML front matter from a markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match front matter between --- markers
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(pattern, content, re.DOTALL)

        if not match:
            return {}, content

        try:
            front_matter = yaml.safe_load(match.group(1))
            return front_matter or {}, content
        except yaml.YAMLError as e:
            return {'_yaml_error': str(e)}, content

    def get_nested_value(self, data: Dict, key: str):
        """Get nested dictionary value using dot notation (e.g., 'header.teaser')."""
        keys = key.split('.')
        value = data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return None
        return value

    def validate_file(self, file_path: Path, collection: str) -> Dict:
        """Validate a single file's metadata."""
        file_issues = []
        front_matter, _ = self.extract_front_matter(file_path)

        if '_yaml_error' in front_matter:
            file_issues.append(f"YAML parsing error: {front_matter['_yaml_error']}")
            return {'file': str(file_path), 'issues': file_issues, 'metadata': {}}

        # Check required fields
        required = self.REQUIRED_FIELDS.get(collection, [])
        for field in required:
            value = self.get_nested_value(front_matter, field)
            if value is None or value == '':
                file_issues.append(f"Missing required field: {field}")

        # Check recommended fields
        recommended = self.RECOMMENDED_FIELDS.get(collection, []).copy()
        recommended.extend(self.RECOMMENDED_FIELDS.get('all', []))
        # Remove duplicates while preserving order
        recommended = list(dict.fromkeys(recommended))
        missing_recommended = []
        for field in recommended:
            value = self.get_nested_value(front_matter, field)
            if value is None or value == '':
                missing_recommended.append(field)

        if missing_recommended:
            file_issues.append(f"Missing recommended: {', '.join(missing_recommended)}")

        # Validate excerpts (should be 150-300 chars)
        if 'excerpt' in front_matter:
            excerpt = front_matter['excerpt']
            if isinstance(excerpt, str):
                # Strip HTML tags for length calculation
                plain_text = re.sub(r'<[^>]+>', '', excerpt)
                if len(plain_text) < 50:
                    file_issues.append(f"Excerpt too short ({len(plain_text)} chars, recommend 150-300)")
                elif len(plain_text) > 400:
                    file_issues.append(f"Excerpt too long ({len(plain_text)} chars, recommend 150-300)")

        # Validate tags (should use hyphens, not spaces)
        if 'tags' in front_matter and isinstance(front_matter['tags'], list):
            bad_tags = [tag for tag in front_matter['tags'] if isinstance(tag, str) and ' ' in tag]
            if bad_tags:
                file_issues.append(f"Tags with spaces (use hyphens): {bad_tags}")

        # Check for stack field in technical content
        if collection in ['posts', 'projects', 'portfolio', 'data-stories']:
            if 'stack' not in front_matter:
                file_issues.append("Missing 'stack' field for technology tracking")

        # Validate dates
        if 'date' in front_matter:
            date_str = str(front_matter['date'])
            if not re.match(r'\d{4}-\d{2}-\d{2}', date_str):
                file_issues.append(f"Invalid date format: {date_str} (use YYYY-MM-DD)")

        return {
            'file': str(file_path.relative_to(self.base_path)),
            'issues': file_issues,
            'metadata': front_matter
        }

    def validate_collection(self, collection: str) -> List[Dict]:
        """Validate all files in a collection."""
        # Handle special path cases
        if collection == 'posts':
            collection_path = self.base_path / '_posts'
        elif collection == 'data-stories':
            collection_path = self.base_path / 'data-stories'
        elif collection == 'pages':
            collection_path = self.base_path / '_pages'
        elif collection == 'drafts':
            collection_path = self.base_path / '_drafts'
        else:
            collection_path = self.base_path / f"_{collection}"

        if not collection_path.exists():
            print(f"Warning: Collection path {collection_path} does not exist")
            return []

        results = []
        # For pages, check both .md and .html files
        file_patterns = ['*.md']
        if collection == 'pages':
            file_patterns.append('*.html')

        for pattern in file_patterns:
            for file in collection_path.glob(pattern):
                if file.name == 'index.md':
                    continue

                result = self.validate_file(file, collection)
                if result['issues']:
                    results.append(result)
                    self.stats['files_with_issues'] += 1
                else:
                    self.stats['files_ok'] += 1

                self.stats['total_files'] += 1

        return results

    def print_report(self, results: Dict[str, List[Dict]]):
        """Print a formatted validation report."""
        print("\n" + "="*80)
        print("METADATA VALIDATION REPORT")
        print("="*80 + "\n")

        print(f"Total files checked: {self.stats['total_files']}")
        print(f"Files with issues:   {self.stats['files_with_issues']}")
        print(f"Files OK:            {self.stats['files_ok']}")
        print()

        for collection, issues_list in results.items():
            if not issues_list:
                print(f"\n✓ {collection.upper()}: All files pass validation")
                continue

            print(f"\n{'─'*80}")
            print(f"⚠️  {collection.upper()} ({len(issues_list)} files with issues)")
            print(f"{'─'*80}")

            for item in issues_list:
                print(f"\n📄 {item['file']}")
                for issue in item['issues']:
                    print(f"   • {issue}")

        print("\n" + "="*80)

        if self.stats['files_with_issues'] == 0:
            print("🎉 All metadata validation checks passed!")
        else:
            print(f"⚠️  Found issues in {self.stats['files_with_issues']} files")
        print("="*80 + "\n")


def main():
    """Main entry point for the validation script."""
    parser = argparse.ArgumentParser(description='Validate Jekyll metadata consistency')
    parser.add_argument('--collection', type=str, help='Validate specific collection only')
    parser.add_argument('--base-path', type=str, default='.', help='Base path to Jekyll site')

    args = parser.parse_args()

    validator = MetadataValidator(args.base_path)

    collections = ['posts', 'projects', 'portfolio', 'data-stories', 'thinking', 'resources', 'pages', 'drafts']

    if args.collection:
        collections = [args.collection]

    all_results = {}
    for collection in collections:
        print(f"Validating {collection}...")
        results = validator.validate_collection(collection)
        if results:
            all_results[collection] = results

    validator.print_report(all_results)


if __name__ == '__main__':
    main()
