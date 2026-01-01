#!/usr/bin/env python3
"""
Metadata Validation Script for Jekyll Site
Validates front matter consistency across posts, projects, and other collections.

Usage:
    python scripts/validate_metadata.py
    python scripts/validate_metadata.py --collection posts
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import argparse
from datetime import date, datetime


class MetadataValidator:
    """Validates Jekyll front matter metadata across content collections."""

    # Required fields by collection type
    REQUIRED_FIELDS = {
        'posts': ['title', 'date', 'excerpt', 'tags', 'categories'],
        'projects': ['title', 'permalink', 'excerpt', 'tags', 'stack', 'status', 'header'],
        'data-stories': ['layout', 'title', 'excerpt', 'permalink', 'date', 'tags', 'stack', 'header'],
        'thinking': ['title', 'date', 'excerpt', 'tags', 'categories', 'permalink', 'header'],
        'resources': ['title', 'permalink', 'excerpt', 'date', 'tags', 'format', 'level'],
        'snippets': ['title', 'date', 'status', 'source_type', 'source_title', 'highlight'],
        'pages': ['title', 'permalink'],
        'drafts': ['title', 'excerpt']
    }

    # Recommended fields
    RECOMMENDED_FIELDS = {
        'posts': ['subtitle', 'header.overlay_image', 'header.teaser', 'stack', 'last_modified_at'],
        'projects': ['last_modified_at', 'header.teaser', 'header.actions', 'docs_url', 'docs_label'],
        'data-stories': ['last_modified_at', 'header.teaser'],
        'thinking': ['subtitle', 'last_modified_at', 'header.overlay_image', 'teaser'],
        'resources': ['subtitle', 'last_modified_at', 'header.teaser', 'download_url', 'categories', 'cognitive_principle'],
        'snippets': ['last_modified_at', 'takeaway', 'tags', 'topics', 'source_creator', 'source_url', 'source_locator', 'impact', 'header.teaser'],
        'pages': ['excerpt', 'header'],
        'drafts': ['tags', 'date', 'subtitle'],
        'all': []
    }

    def __init__(self, base_path: str = '.'):
        self.base_path = Path(base_path)
        self.issues = defaultdict(list)
        self.stats = defaultdict(int)
        self.collection_paths = {
            'posts': self.base_path / '_posts',
            'projects': self.base_path / '_projects',
            'portfolio': self.base_path / '_portfolio',
            'snippets': self.base_path / '_snippets',
            'thinking': self.base_path / '_thinking',
            'resources': self.base_path / '_resources',
            'data-stories': self.base_path / 'data-stories',
            'pages': self.base_path / '_pages',
            'drafts': self.base_path / '_drafts'
        }
        self.excluded_files = {'index.md', 'README.md', 'TEMPLATE.md'}

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

    def validate_list_field(self, field_name: str, value, file_issues: List[str]):
        """Validate list fields (tags, topics, categories) for type and formatting."""
        if value is None:
            return
        if not isinstance(value, list):
            file_issues.append(f"Field '{field_name}' should be a list")
            return
        non_strings = [item for item in value if not isinstance(item, str)]
        if non_strings:
            file_issues.append(f"Field '{field_name}' should contain only strings")

    def is_valid_date(self, value) -> bool:
        """Validate date strings or parsed YAML date/datetime objects."""
        if isinstance(value, (date, datetime)):
            return True
        date_str = str(value)
        pattern = r'^\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2}:\d{2})?(?:\s*(?:Z|[+-]\d{2}:?\d{2}))?$'
        return re.match(pattern, date_str) is not None

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
                if len(plain_text) < 150:
                    file_issues.append(f"Excerpt too short ({len(plain_text)} chars, recommend 150-300)")
                elif len(plain_text) > 300:
                    file_issues.append(f"Excerpt too long ({len(plain_text)} chars, recommend 150-300)")

        # Validate tags (should use hyphens, not spaces)
        tags_value = front_matter.get('tags')
        self.validate_list_field('tags', tags_value, file_issues)
        if isinstance(tags_value, list):
            bad_tags = [tag for tag in tags_value if isinstance(tag, str) and ' ' in tag]
            if bad_tags:
                file_issues.append(f"Tags with spaces (use hyphens): {bad_tags}")

        topics_value = front_matter.get('topics')
        self.validate_list_field('topics', topics_value, file_issues)
        categories_value = front_matter.get('categories')
        self.validate_list_field('categories', categories_value, file_issues)

        # Validate dates
        if 'date' in front_matter:
            date_value = front_matter['date']
            if not self.is_valid_date(date_value):
                file_issues.append(f"Invalid date format: {date_value} (use YYYY-MM-DD or YYYY-MM-DD HH:MM:SS ±ZZZZ)")

        if collection == 'snippets' and 'status' in front_matter:
            status = front_matter['status']
            if status not in {'inbox', 'garden'}:
                file_issues.append(f"Invalid snippet status: {status} (use inbox or garden)")

        return {
            'file': str(file_path.relative_to(self.base_path)),
            'issues': file_issues,
            'metadata': front_matter
        }

    def validate_collection(self, collection: str) -> List[Dict]:
        """Validate all files in a collection."""
        collection_path = self.collection_paths.get(collection, self.base_path / f"_{collection}")

        if not collection_path.exists():
            print(f"Warning: Collection path {collection_path} does not exist")
            return None

        results = []
        # For pages, check both .md and .html files
        file_patterns = ['*.md']
        if collection == 'pages':
            file_patterns.append('*.html')

        for pattern in file_patterns:
            for file in collection_path.rglob(pattern):
                if file.name in self.excluded_files:
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

    collections = ['posts', 'projects', 'snippets', 'data-stories', 'thinking', 'resources', 'pages', 'drafts']

        if args.collection:
            collections = [args.collection]

    all_results = {}
    for collection in collections:
        print(f"Validating {collection}...")
        results = validator.validate_collection(collection)
        if results is None:
            continue
        all_results[collection] = results

    validator.print_report(all_results)


if __name__ == '__main__':
    main()
