#!/usr/bin/env python3
"""Build and validate the survey's literature catalogue using the standard library."""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

INTRO = {
    'sources': 'Skills draw on human supervision, external knowledge, and agent experience.',
    'synthesis': 'Four construction operations turn source evidence into reusable procedures: procedural distillation, contrastive induction, constructive compilation, and objective optimization.',
    'representations': 'Retained procedures take textual, structured, executable, internalized, or hybrid forms.',
    'utilization': 'Agents use skills through context injection, runtime invocation, and model activation, with multi-skill orchestration coordinating their use.',
    'evaluation': 'Evaluation covers five quality dimensions and benchmarks for synthesis, utilization, evolution, and security.',
    'evolution': 'Skills and their libraries evolve through refinement, reorganization, migration, and reduction.',
}

def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def anchor(part, path=()):
    return '-'.join([part['id'], *[slug(x) for x in path]])

def validate(papers, taxonomy):
    assert len(papers) == len({p['id'] for p in papers}), 'Duplicate paper ID'
    by_id = {p['id']: p for p in papers}
    all_mapped = set()
    for part in taxonomy:
        paths = set()
        for category in part['categories']:
            path = tuple(category['path'])
            assert path not in paths and path, 'Duplicate or empty category'
            paths.add(path)
            keys = category['papers']
            assert keys and len(keys) == len(set(keys)), 'Duplicate paper within a category'
            assert set(keys) <= by_id.keys(), 'Unknown paper ID'
            all_mapped.update(keys)
    assert all_mapped == by_id.keys(), 'Unmapped or missing papers'
    for paper in papers:
        assert paper['title'].strip() and paper['summary'].endswith('.'), paper['id']
        assert '\n' not in paper['summary'], paper['id']
        assert 8 <= len(paper['summary'].split()) <= 55, paper['id']
        assert re.fullmatch(r'\d{4}', str(paper['year'])), paper['id']
        for field in ('paper_url', 'code_url', 'project_url', 'data_url'):
            url = paper.get(field)
            if url:
                parsed = urlsplit(url)
                assert parsed.scheme in ('https', 'http') and parsed.hostname, (paper['id'], field)
                assert not parsed.username and not parsed.password, 'Credentials in URL'
        assert paper['paper_url'], paper['id']
        if paper.get('code_url'):
            assert paper.get('code_provenance', {}).get('evidence_url'), paper['id']
    return by_id

def render(papers, taxonomy, manifest):
    by_id = validate(papers, taxonomy)
    placements = sum(len(c['papers']) for t in taxonomy for c in t['categories'])
    categories = sum(len(t['categories']) for t in taxonomy)
    lines = [
        '<h1 align="center">Awesome-Skill-Synthesis</h1>', '',
        '<p align="center">A curated collection of research on constructing, representing, using, evaluating, and evolving reusable agent skills.</p>', '',
        '[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)', '',
        'Companion repository for **' + manifest['survey_title'] + '**.', '',
        f'This catalogue follows Figures 4, 6, 8, 10, 11, and 13 of the survey: **{len(papers)} distinct papers**, **{categories} literature categories**, and **{placements} paper-to-category mappings**. '
        'A paper can appear in several categories because it contributes to multiple parts of the skill lifecycle. '
        'The collection includes the foundational work shown in the survey taxonomies.', '',
        'Each entry gives a one-sentence description, a paper link, and an author-linked code repository when confirmed; project pages and datasets are labeled separately.', '',
        'Last synchronized with the survey: **' + manifest['synced_on'] + '**.', '',
        '## Contents', '',
        '| Part | Survey figure | Distinct papers |',
        '| --- | --- | ---: |',
    ]
    for n, part in enumerate(taxonomy, 1):
        count = len({k for c in part['categories'] for k in c['papers']})
        lines.append(f"| [{n}. {part['title']}](#{part['id']}) | Figure {part['figure']} | {count} |")
    lines += ['', 'Counts overlap across parts. [Maintenance guide](MAINTENANCE.md) · [Paper data](data/papers.json) · [Taxonomy mappings](data/taxonomy.json)', '']
    for n, part in enumerate(taxonomy, 1):
        lines += [f'<a id="{part["id"]}"></a>', '', f'## {n}. {part["title"]}', '', INTRO[part['id']], '']
        for category in part['categories']:
            title = ' / '.join(category['path'])
            lines.append(f'- [{title}](#{anchor(part, category["path"])})')
        lines.append('')
        parent = None
        for category in part['categories']:
            path = category['path']
            if len(path) == 2 and path[0] != parent:
                lines += [f'### {path[0]}', '']
            parent = path[0]
            level = '####' if len(path) == 2 else '###'
            lines += [f'<a id="{anchor(part, path)}"></a>', '', f'{level} {path[-1]}', '']
            for key in category['papers']:
                p = by_id[key]
                title = html.escape(p['title'], quote=False).replace('*', '\\*')
                links = [f'[[📝 Paper]({p["paper_url"]})]']
                for field, label in [('code_url', '💻 Code'), ('project_url', '🌐 Project'), ('data_url', '📦 Data')]:
                    if p.get(field): links.append(f'[[{label}]({p[field]})]')
                lines += [f'<!-- paper:{key} -->', f'- (*{p["year"]}*) **{title}** ' + ' '.join(links) + '  ', '  → ' + p['summary'], '']
        lines += ['[↑ Contents](#contents)', '']
    lines += [
        '## Contributing', '',
        'Contributions are welcome. Please provide the paper, its appropriate taxonomy category, a concise description of its role in skill synthesis or reuse, and an author-released implementation when available. '
        'See [MAINTENANCE.md](MAINTENANCE.md) for the update workflow.', '',
        '## Acknowledgments', '',
        'The catalogue format is inspired by [takeshiww/Awsome-Skill-Synthesis](https://github.com/takeshiww/Awsome-Skill-Synthesis). '
        'The categories and literature mappings follow the accompanying survey.', '',
        '## License', '',
        'This repository uses the [MIT License](LICENSE). Linked papers, datasets, and software retain their respective licenses.', '',
    ]
    return '\n'.join(lines)

def check_source(taxonomy, source):
    def balanced(s, start):
        depth = 1; pos = start + 1
        while pos < len(s):
            if s[pos] == '\\': pos += 2; continue
            if s[pos] == '{': depth += 1
            if s[pos] == '}': depth -= 1
            if not depth: return s[start+1:pos]
            pos += 1
        raise ValueError('Unbalanced source node')
    for part in taxonomy:
        text = (source / part['source_file']).read_text()
        for category in part['categories']:
            node = re.escape(category['source_node'])
            match = re.search(r'\\node\[[^\n]*?\(' + node + r'\)[^\n]*?\)\s*\{', text)
            assert match, (part['id'], node)
            content = balanced(text, match.end()-1)
            keys = list(dict.fromkeys(k.strip() for group in re.findall(r'\\cite\w*\{([^}]+)\}', content) for k in group.split(',')))
            assert keys == category['papers'], (part['id'], category['path'], 'Mapping differs from figure')
    print('All category mappings match the supplied survey figure sources.')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check data and README without writing files')
    parser.add_argument('--survey-source', type=Path, help='Optional local survey source directory for citation-coverage checks')
    args = parser.parse_args()
    papers = json.loads((ROOT/'data/papers.json').read_text())
    taxonomy = json.loads((ROOT/'data/taxonomy.json').read_text())
    manifest = json.loads((ROOT/'data/source_manifest.json').read_text())
    rendered = render(papers, taxonomy, manifest)
    if args.survey_source: check_source(taxonomy, args.survey_source)
    if args.check:
        assert (ROOT/'README.md').read_text() == rendered, 'README is stale; run python3 scripts/build_readme.py'
    else:
        (ROOT/'README.md').write_text(rendered)
    print(f'{len(papers)} papers; {sum(len(c["papers"]) for t in taxonomy for c in t["categories"])} mappings; README {"checked" if args.check else "written"}.')

if __name__ == '__main__':
    main()
