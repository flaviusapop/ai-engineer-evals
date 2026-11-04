"""Build a concept-first wiki, without reading or modifying source transcripts.

Dependencies: Python-Markdown and bleach.
Run: uv run --with markdown --with bleach python scripts/build_wiki.py.
See templates/wiki/IMPLEMENTATION.md for interface, verification and limitations.
"""
import argparse
import html
import json
from pathlib import Path
import posixpath
from string import Template
import re

from html.parser import HTMLParser
from urllib.parse import parse_qs, unquote, urljoin, urlsplit

import bleach
import markdown

REPO = Path(__file__).resolve().parents[1]


SLUG = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
WIKILINK = re.compile(r'\[\[([a-z0-9-]+)(?:\|([^\]\n]+))?\]\]')
CITATION = re.compile(r'\[cite:([^\]\n]+)\]')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def keyed(records, key, name, slugs=False):
    require(isinstance(records, list), name + ' must be an array')
    result = {}
    for record in records:
        value = record[key]
        require(value not in result, f'Duplicate {name}: {value}')
        if slugs:
            require(bool(SLUG.fullmatch(value)), f'Invalid {name} slug: {value}')
        result[value] = record
    return result


def validate(root, registry, claim_records, source_records):
    require(registry['schema_version'] == 1, 'Unsupported schema version')
    articles = keyed(registry['articles'], 'id', 'article', True)
    sections = keyed(registry['sections'], 'id', 'section', True)
    require(articles and sections, 'Articles and sections must not be empty')
    paths = keyed(registry['reading_paths'], 'id', 'reading path', True)
    claims = keyed(claim_records, 'claim_id', 'claim')
    sources = keyed(source_records, 'id', 'source')
    for source_id, source in sources.items():
        require(bool(re.fullmatch(r'[A-Za-z0-9_-]{11}', source_id)), f'Invalid source ID format: {source_id}')
        require(source['transcript'] == f'transcripts/{source_id}.md', f'Unsafe transcript provenance path: {source_id}')
        watch = urlsplit(source['url'])
        require(watch.scheme == 'https' and watch.netloc in ('www.youtube.com', 'youtube.com', 'youtu.be'), f'Unsafe watch URL: {source_id}')
        paired = watch.path == '/' + source_id if watch.netloc == 'youtu.be' else watch.path == '/watch' and parse_qs(watch.query).get('v') == [source_id]
        require(paired, f'Watch URL/source ID mismatch: {source_id}')
    ownership, texts = {}, {}
    for article_id, article in articles.items():
        require(article['section'] in sections, f'Unknown section for {article_id}')
        for field in ['prerequisites', 'related']:
            require(len(article[field]) == len(set(article[field])), f'Duplicate {field}: {article_id}')
            require(all(x in articles and x != article_id for x in article[field]), f'Dangling or self {field}: {article_id}')
        for concept in article['concept_keys']:
            require(concept not in ownership, f'Duplicate concept ownership: {concept}')
            ownership[concept] = article_id
        expected = f'wiki/content/{article_id}.md'
        require(article['content_file'] == expected, f'Noncanonical content path: {article_id}')
        path = root / expected
        require(path.resolve().is_relative_to((root / 'wiki/content').resolve()) and not path.is_symlink(), f'Unsafe content path: {article_id}')
        require(path.is_file(), f'Missing content: {article_id}')
        texts[article_id] = path.read_text()
    actual = {p.name for p in (root / 'wiki/content').glob('*.md')}
    require(actual == {a + '.md' for a in articles}, 'Registry/content article ID sets differ')
    for path in paths.values():
        require(path['article_ids'] and len(set(path['article_ids'])) == len(path['article_ids']), 'Empty or repeated reading path')
        require(all(a in articles for a in path['article_ids']), 'Dangling reading path')
    for entry in registry['glossary']:
        require(entry['article_id'] in articles, 'Dangling glossary article')
    require(registry.get('quote_policy', 'legacy') in ('omit', 'legacy'), 'Invalid quote policy')
    for claim_id, claim in claims.items():
        require(claim['source_id'] in sources, f'Unknown claim source: {claim_id}')
        require(claim_id.startswith(claim['source_id'] + ':'), f'Claim/source ID mismatch: {claim_id}')
        ev = claim['evidence']
        require(type(ev['line_start']) is int and type(ev['line_end']) is int and 1 <= ev['line_start'] <= ev['line_end'], f'Invalid evidence line range: {claim_id}')
        if registry.get('quote_policy') == 'omit':
            require('quote' not in ev, f'Contradictory quote under omit: {claim_id}')
        elif 'quote' in ev:
            require(isinstance(ev['quote'], str) and ev['quote'].strip(), f'Invalid quote: {claim_id}')
    if 'claim_ownership' in registry or 'concept_aliases' in registry:
        mapping = registry.get('claim_ownership')
        require(isinstance(mapping, dict) and set(mapping) == set(claims), 'Incomplete claim ownership')
        require(all(unit in ownership for unit in mapping.values()), 'Invalid claim owner')
        aliases = {}
        for cid, claim in claims.items():
            aliases.setdefault(claim['concept_key'], set()).add(mapping[cid])
        require(registry.get('concept_aliases') == {k:sorted(v) for k,v in aliases.items()}, 'Claim aliases disagree with ownership')
    for article_id, text in texts.items():
        require(not re.search(r'^#\s', text, re.M), f'Metadata owns H1: {article_id}')
        for match in WIKILINK.finditer(text):
            require(match[1] in articles, f'Unknown concept link: {match[1]} in {article_id}')
        for match in CITATION.finditer(text):
            require(match[1] in claims, f'Unknown citation: {match[1]} in {article_id}')
        remaining = CITATION.sub('', WIKILINK.sub('', text))
        require('[[' not in remaining and '[cite:' not in remaining, f'Malformed wiki token in {article_id}')
    return articles, sections, paths, claims, sources, texts


def validate_coverage(root, strict, sources, articles, texts, claims, claim_ownership=None):
    path = root / 'wiki/data/coverage.json'
    if not path.exists():
        require(not strict, 'Strict source coverage requires coverage.json')
        return None
    coverage = json.loads(path.read_text())
    require(coverage['source_count'] == len(sources), 'Source coverage count disagrees with metadata')
    require(coverage['max_transcripts_per_reader'] <= 5, 'Reader coverage limit must be <=5')
    rows = keyed(coverage['sources'], 'source_id', 'coverage source')
    readers = keyed(coverage['readers'], 'batch_id', 'reader')
    require(set(rows) == set(sources), 'Source coverage ID set differs from metadata')
    if strict:
        require(len(sources) == 313, 'Strict source coverage requires exactly 313 sources')
    ownership = {}
    for batch_id, reader in readers.items():
        require(reader['status'] == 'accepted', f'Unaccepted reader: {batch_id}')
        require(0 < len(reader['source_ids']) <= coverage['max_transcripts_per_reader'], f'Too many or no sources per reader: {batch_id}')
        for source_id in reader['source_ids']:
            require(source_id in sources and source_id not in ownership, f'Duplicate or unknown source ownership: {source_id}')
            ownership[source_id] = batch_id
    require(set(ownership) == set(sources), 'Reader coverage is incomplete')
    for source_id, row in rows.items():
        require(row['reader_batch'] == ownership[source_id], f'Source reader mismatch: {source_id}')
        require(len(row['article_ids']) == len(set(row['article_ids'])) and all(a in articles for a in row['article_ids']), f'Invalid source article mapping: {source_id}')
        require(row['article_ids'] or row['limitations'], f'Unmapped source needs a limitation: {source_id}')
    if claim_ownership is not None:
        unit_articles = {unit: article_id for article_id, article in articles.items() for unit in article['concept_keys']}
        for claim_id, unit in claim_ownership.items():
            source_id = claims[claim_id]['source_id']
            article_id = unit_articles[unit]
            require(article_id in rows[source_id]['article_ids'], f'Claim primary lineage missing from source article mapping: {source_id}/{article_id}')
    for article_id, text in texts.items():
        for match in CITATION.finditer(text):
            source_id = claims[match[1]]['source_id']
            require(article_id in rows[source_id]['article_ids'], f'Citation missing from source article mapping: {source_id}/{article_id}')
    return coverage


class SafeHTML(HTMLParser):
    """Serialize sanitized Markdown, applying one external-link policy."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            href = attrs['href'] or ''
            scheme = urlsplit(href).scheme.lower()
            if href.startswith('//') or '\\' in href or scheme not in ('', 'http', 'https', 'mailto'):
                del attrs['href']
            elif scheme in ('http', 'https'):
                attrs.update(target='_blank', rel='noopener noreferrer')
        self.parts.append('<' + tag + ''.join(f' {k}="{html.escape(v or "", quote=True)}"' for k, v in attrs.items()) + '>')

    def handle_endtag(self, tag):
        self.parts.append('</' + tag + '>')

    def handle_data(self, data):
        self.parts.append(html.escape(data, quote=False))


def safe_html(rendered):
    cleaned = bleach.clean(rendered,
        tags=['p', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'blockquote', 'pre', 'code', 'strong', 'em', 'a', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'hr', 'br', 'div', 'span', 'del'],
        attributes={'a': ['href', 'title', 'class', 'aria-label'], 'h2': ['id'], 'h3': ['id'], 'h4': ['id'], 'h5': ['id'], 'h6': ['id'], 'code': ['class'], 'div': ['class'], 'ol': ['start']},
        protocols=['http', 'https', 'mailto'], strip=True)
    parser = SafeHTML()
    parser.feed(cleaned)
    return ''.join(parser.parts)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links = [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for name in ['href', 'src']:
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == 'a' and urlsplit(attrs.get('href') or '').scheme in ('http', 'https'):
            require(attrs.get('target') == '_blank' and set((attrs.get('rel') or '').split()) >= {'noopener', 'noreferrer'}, 'Unsafe external-link attributes')


def audit_links(files, sources):
    """Check every generated local URL; report anchors use metadata, never raw report text."""
    documents = {}
    for route, text in files.items():
        if route.endswith('.html'):
            doc = Links()
            doc.feed(text)
            require(len(doc.ids) == len(set(doc.ids)), f'Duplicate anchor IDs in {route}')
            documents[route] = doc
    checked = 0
    for route, doc in documents.items():
        for link in doc.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            require(not url.path.startswith('/'), f'Root-relative local link is unsafe under project hosting: {route}: {link}')
            target = posixpath.normpath(posixpath.join(posixpath.dirname(route), unquote(url.path))) if url.path else route
            if target == 'report.html':
                require(not url.fragment or unquote(url.fragment) in {'video-' + s for s in sources}, f'Unknown report anchor: {link}')
            else:
                require(target in files, f'Broken local link: {route}: {link}')
                if url.fragment and target in documents:
                    require(unquote(url.fragment) in documents[target].ids, f'Broken local anchor: {route}: {link}')
            checked += 1
    return checked


def build(root, output, strict=False, public_url='https://flaviusapop.github.io/ai-engineer-evals/', github_url='https://github.com/flaviusapop/ai-engineer-evals/blob/main/'):
    root, output = Path(root), Path(output)
    registry = json.loads((root / 'wiki/data/registry.json').read_text())
    data = validate(root, registry, json.loads((root / 'wiki/data/claims.json').read_text()), json.loads((root / 'videos.json').read_text()))
    articles, sections_by_id, paths, claims, sources, texts = data
    coverage = validate_coverage(root, strict, sources, articles, texts, claims, registry.get('claim_ownership'))
    files = {}
    e = lambda text: html.escape(str(text), quote=True)

    def write(route, text):
        files[route] = text

    ordered_sections = sorted(sections_by_id.values(), key=lambda s: (s['order'], s['id']))
    section_order = {s['id']: i for i, s in enumerate(ordered_sections)}
    ordered_articles = sorted(articles.values(), key=lambda a: (section_order[a['section']], a['order'], a['id']))
    template = Template((REPO / 'templates/wiki/page.html').read_text())

    def article_list(ids, prefix='', ordered=False):
        tag = 'ol' if ordered else 'ul'
        return '<' + tag + ' class="article-list">' + ''.join('<li><a href="' + prefix + 'articles/' + a + '.html">' + e(articles[a]['title']) + '</a><p>' + e(articles[a]['summary']) + '</p></li>' for a in ids) + '</' + tag + '>'

    def page(title, body, route='index.html', description='', section=None, article_id=None):
        prefix = '../' if '/' in route else ''
        navigation = '<ul><li><a href="' + prefix + 'index.html">Start here</a></li></ul>'
        for s in ordered_sections:
            navigation += '<p><a href="' + prefix + 'topics/' + s['id'] + '.html">' + e(s['title']) + '</a></p><ul>'
            for a in ordered_articles:
                if a['section'] == s['id']:
                    current = ' aria-current="page"' if a['id'] == article_id else ''
                    navigation += '<li><a' + current + ' href="' + prefix + 'articles/' + a['id'] + '.html">' + e(a['title']) + '</a></li>'
            navigation += '</ul>'
        navigation += '<p>Reference</p><ul>' + ''.join('<li><a href="' + prefix + target + '.html">' + label + '</a></li>' for target, label in [('glossary', 'Glossary'), ('sources', 'Sources'), ('methodology', 'Methodology')]) + '</ul>'
        breadcrumbs = '<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="' + prefix + 'index.html">Field guide</a>'
        if section:
            breadcrumbs += ' / <a href="' + prefix + 'topics/' + section + '.html">' + e(sections_by_id[section]['title']) + '</a>'
        breadcrumbs += ' / <span aria-current="page">' + e(title) + '</span></nav>'
        return template.substitute(page_title=e(title), site_title=e(registry['title']), prefix=prefix,
            heading=e(title), description=e(description), eyebrow=e(sections_by_id[section]['title'] if section else 'The concept wiki'),
            breadcrumbs=breadcrumbs, navigation=navigation, body=body,
            scripts='<script src="assets/search-data.js"></script><script src="assets/search.js"></script>' if route == 'index.html' else '')

    sections = ''.join('<section><h2><a href="topics/' + s['id'] + '.html">' + e(s['title']) + '</a></h2><p>' + e(s['description']) + '</p>' + article_list([a['id'] for a in ordered_articles if a['section'] == s['id']]) + '</section>' for s in ordered_sections)
    path_list = '<section><h2>Guided reading paths</h2><ul>' + ''.join('<li><a href="paths/' + p['id'] + '.html">' + e(p['title']) + '</a><p>' + e(p['description']) + '</p></li>' for p in paths.values()) + '</ul></section>'
    search = '<section class="search" aria-label="Search concepts"><label for="search-control">Search concepts</label><input id="search-control" type="search" placeholder="Find an idea, method or trade-off…" autocomplete="off" aria-controls="search-results" aria-describedby="search-status" disabled><p id="search-status" role="status" aria-live="polite">Search titles, summaries and article text.</p><ol id="search-results" class="article-list"></ol><noscript><p>Search needs JavaScript; all topics and reading paths remain available below.</p></noscript></section>'
    write('wiki/index.html', page(registry['title'], search + path_list + sections, description=registry['subtitle']))
    for article in ordered_articles:
        text = texts[article['id']]
        citations = []

        def cite(match):
            claim_id = match[1]
            if claim_id not in citations:
                citations.append(claim_id)
            number = citations.index(claim_id) + 1
            return f'<a class="citation" href="#evidence-{number}" aria-label="Source {number}">[{number}]</a>'

        def concept(match):
            target, label = match[1], match[2]
            return '<a href="' + target + '.html">' + e(label or articles[target]['title']) + '</a>'

        resolved = WIKILINK.sub(concept, text)
        resolved = CITATION.sub(cite, resolved)
        evidence = ''
        for number, claim_id in enumerate(citations, 1):
            claim = claims[claim_id]
            source = sources[claim['source_id']]
            ev = claim['evidence']
            transcript = github_url.rstrip('/') + '/' + source['transcript'] + f'#L{ev["line_start"]}-L{ev["line_end"]}'
            quote = '<blockquote>' + e(ev['quote']) + '</blockquote>' if ev.get('quote') else ''
            evidence += f'<li id="evidence-{number}" tabindex="-1"><h3>{e(source["title"])}</h3>{quote}<p>{e(claim["evidence_strength"])} — {e(claim.get("qualification", ""))}</p><a href="{e(source["url"])}" target="_blank" rel="noopener noreferrer">Watch original</a> · <a href="{e(transcript)}" target="_blank" rel="noopener noreferrer">Transcript lines {ev["line_start"]}–{ev["line_end"]}</a></li>'
        renderer = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])
        body = '<article class="prose">' + safe_html(renderer.convert(resolved)) + '</article>'
        toc = '<nav class="article-toc" aria-label="On this page"><h2>On this page</h2>' + safe_html(renderer.toc) + '</nav>' if renderer.toc_tokens else ''
        prerequisites = '<section><h2>Prerequisites</h2>' + article_list(article['prerequisites'], '../') + '</section>' if article['prerequisites'] else ''
        if evidence:
            body += '<details class="evidence"><summary>Sources and evidence (' + str(len(citations)) + ')</summary><ol>' + evidence + '</ol></details>'
        related = '<section><h2>Related concepts</h2>' + article_list(article['related'], '../') + '</section>' if article['related'] else ''
        backlinks = [a['id'] for a in ordered_articles if a['id'] != article['id'] and any(m[1] == article['id'] for m in WIKILINK.finditer(texts[a['id']]))]
        if backlinks:
            related += '<section><h2>Linked from</h2>' + article_list(backlinks, '../') + '</section>'
        position = ordered_articles.index(article)
        previous = ordered_articles[position - 1] if position else None
        following = ordered_articles[position + 1] if position + 1 < len(ordered_articles) else None
        continuation = '<nav class="continuation" aria-label="Continue reading"><h2>Continue reading</h2>'
        if previous:
            continuation += '<p>Previous: <a href="' + previous['id'] + '.html">' + e(previous['title']) + '</a></p>'
        if following:
            continuation += '<p>Next: <a href="' + following['id'] + '.html">' + e(following['title']) + '</a></p>'
        continuation += '</nav>'
        for path in paths.values():
            if article['id'] in path['article_ids']:
                neighbors = path['article_ids']
                offset = neighbors.index(article['id'])
                continuation += '<nav class="path-navigation" aria-label="Reading path: ' + e(path['title']) + '"><p>Reading path: <a href="../paths/' + path['id'] + '.html">' + e(path['title']) + '</a></p>'
                if offset:
                    a = neighbors[offset - 1]
                    continuation += '<p>Previous in path: <a href="' + a + '.html">' + e(articles[a]['title']) + '</a></p>'
                if offset + 1 < len(neighbors):
                    a = neighbors[offset + 1]
                    continuation += '<p>Next in path: <a href="' + a + '.html">' + e(articles[a]['title']) + '</a></p>'
                continuation += '</nav>'
        download = '<p class="download"><a download href="../content/' + article['id'] + '.md">Download Markdown</a></p>'
        route = 'articles/' + article['id'] + '.html'
        write('wiki/' + route, page(article['title'], download + prerequisites + toc + body + related + continuation, route, article['summary'], article['section'], article['id']))
        write('wiki/content/' + article['id'] + '.md', (root / article['content_file']).read_bytes())
    for section in ordered_sections:
        route = 'topics/' + section['id'] + '.html'
        body = article_list([a['id'] for a in ordered_articles if a['section'] == section['id']], '../')
        write('wiki/' + route, page(section['title'], body, route, section['description'], section['id']))
    for path in paths.values():
        route = 'paths/' + path['id'] + '.html'
        write('wiki/' + route, page(path['title'], article_list(path['article_ids'], '../', True), route, path['description']))
    glossary = '<dl>' + ''.join('<dt>' + e(g['term']) + '</dt><dd>' + e(g['definition']) + ' <a href="articles/' + g['article_id'] + '.html">' + e(articles[g['article_id']]['title']) + '</a></dd>' for g in sorted(registry['glossary'], key=lambda g: g['term'].casefold())) + '</dl>'
    write('wiki/glossary.html', page('Glossary', glossary, 'glossary.html', 'Short definitions, with links to the full concepts.'))
    mappings = {row['source_id']: row for row in coverage['sources']} if coverage else {}
    source_list = '<p>Coverage mappings ' + ('validated against the supplied reader ledger.' if coverage else 'not supplied; article links below are derived from resolved citations only.') + '</p>'
    for source in sorted(sources.values(), key=lambda s: (s['title'].casefold(), s['id'])):
        source_id = source['id']
        derived = [a['id'] for a in ordered_articles if any(claims[m[1]]['source_id'] == source_id for m in CITATION.finditer(texts[a['id']]))]
        mapped = mappings[source_id]['article_ids'] if coverage else derived
        source_list += '<details class="source-entry" id="source-' + e(source_id) + '"><summary>' + e(source['title']) + '</summary><p><a href="' + e(source['url']) + '" target="_blank" rel="noopener noreferrer">Watch original</a> · <a href="../report.html#video-' + e(source_id) + '">Original source report</a></p>'
        source_list += article_list(mapped) if mapped else '<p>No concept article mapped.</p>'
        if coverage and mappings[source_id]['limitations']:
            source_list += '<p>Limitations: ' + e('; '.join(mappings[source_id]['limitations'])) + '</p>'
        source_list += '</details>'
    write('wiki/sources.html', page('Sources', source_list, 'sources.html', 'Original talks and their concept-article mappings.'))
    coverage_note = f'Supplied coverage validated: {len(sources)} sources, {len(coverage["readers"])} accepted readers; at most {coverage["max_transcripts_per_reader"]} sources per reader.' if coverage else 'Reader coverage not supplied. This build does not assert that all source transcripts have been read.'
    methodology = '<h2>Concept-first synthesis</h2><p>Articles are canonical Markdown organized around ideas rather than individual talks. Prerequisites and links connect the concepts; the original source-video report is preserved separately.</p><h2>Evidence and provenance</h2><p>Numbered citations resolve to accepted claims, source watch URLs and GitHub transcript line ranges. Line ranges are not video timestamps. Speaker guidance and reported experience are evidence categories, not independent proof.</p><h2>Coverage</h2><p>' + e(coverage_note) + '</p><h2>Limitations</h2><p>Transcripts may contain caption errors. Rendering validates identifiers, mappings and line-range syntax; quote accuracy, actual source line counts and the quality of a synthesis require a separate source review. No raw transcript text is loaded by this generator.</p>'
    write('wiki/methodology.html', page('Methodology', methodology, 'methodology.html', 'How this guide is assembled and what its evidence can support.'))
    full = ['# ' + registry['title'], registry['subtitle'],
            'Coverage: ' + coverage_note, 'Source review and rendering limitations: ' + public_url.rstrip('/') + '/wiki/methodology.html']
    discovery = ['# ' + registry['title'], '> ' + registry['subtitle'], '', '## Guide',
                 '- [Wiki](' + public_url.rstrip('/') + '/wiki/index.html)',
                 '- [Full Markdown](' + public_url.rstrip('/') + '/wiki/llms-full.md)',
                 '- [Sources](' + public_url.rstrip('/') + '/wiki/sources.html)',
                 '- [Methodology](' + public_url.rstrip('/') + '/wiki/methodology.html)', '', '## Concepts']
    for article in ordered_articles:
        article_id = article['id']
        ids = list(dict.fromkeys(m[1] for m in CITATION.finditer(texts[article_id])))
        def md_concept(match):
            label = (match[2] or articles[match[1]]['title']).replace('[', '\\[').replace(']', '\\]')
            return '[' + label + '](' + public_url.rstrip('/') + '/wiki/articles/' + match[1] + '.html)'
        def md_cite(match):
            return '[Source ' + str(ids.index(match[1]) + 1) + '](#' + article_id + '-source-' + str(ids.index(match[1]) + 1) + ')'
        article_url = public_url.rstrip('/') + '/wiki/articles/' + article_id + '.html'
        linked_md = WIKILINK.sub(md_concept, texts[article_id])
        linked_md = re.sub(r'(\]\()(<?)([^\s)<>]+)(>?)(?=[\s)])', lambda m: m[1] + m[2] + urljoin(article_url, m[3]) + m[4], linked_md)
        linked_md = re.sub(r'^(\s{0,3}\[[^\]\n]+\]:\s*)(<?)([^\s<>]+)(>?)', lambda m: m[1] + m[2] + urljoin(article_url, m[3]) + m[4], linked_md, flags=re.M)
        resolved_md = CITATION.sub(md_cite, linked_md)
        full.extend(['## ' + article['title'], article['summary'], resolved_md])
        for n, claim_id in enumerate(ids, 1):
            claim = claims[claim_id]
            source = sources[claim['source_id']]
            ev = claim['evidence']
            transcript = github_url.rstrip('/') + '/' + source['transcript'] + f'#L{ev["line_start"]}-L{ev["line_end"]}'
            full.extend(['<a id="' + article_id + '-source-' + str(n) + '"></a>',
                         '### Source ' + str(n) + ': ' + source['title']])
            if ev.get('quote'):
                full.append('\n'.join('> ' + line for line in ev['quote'].splitlines()))
            full.extend(['Evidence: ' + claim['evidence_strength'] + '. ' + claim.get('qualification', ''),
                         '[Watch original](' + source['url'] + ') · [Transcript lines](' + transcript + ')'])
        discovery.append('- [' + article['title'] + '](' + public_url.rstrip('/') + '/wiki/articles/' + article_id + '.html): ' + article['summary'])
    write('wiki/llms-full.md', '\n\n'.join(full).rstrip() + '\n')
    write('llms.txt', '\n'.join(discovery).rstrip() + '\n')
    records = []
    for article in ordered_articles:
        text = CITATION.sub('', WIKILINK.sub(lambda m: m[2] or articles[m[1]]['title'], texts[article['id']]))
        plain = html.unescape(bleach.clean(markdown.markdown(text, extensions=['tables', 'fenced_code']), tags=[], strip=True))
        records.append({'id': article['id'], 'title': article['title'], 'summary': article['summary'],
                        'text': re.sub(r'\s+', ' ', plain).strip(), 'url': 'articles/' + article['id'] + '.html'})
    write('wiki/assets/search-data.js', 'window.WIKI_SEARCH = ' + json.dumps(records, ensure_ascii=True, sort_keys=True).replace('<', '\\u003c') + ';\n')
    for name in ['search.js', 'favicon.svg', 'wiki.css', 'wiki.js']:
        write('wiki/assets/' + name, (REPO / 'wiki/assets' / name).read_text())
    checked_links = audit_links(files, sources)
    manifest_path = output / 'wiki/build-manifest.json'
    previous = json.loads(manifest_path.read_text())['files'] if manifest_path.exists() else []
    for route in set(previous) - set(files):
        # Only remove known generated route classes, never arbitrary manifest paths.
        owned = re.fullmatch(r'wiki/(articles|topics|paths)/[a-z0-9-]+\.html|wiki/content/[a-z0-9-]+\.md', route)
        dest = output / route
        if owned and dest.resolve().is_relative_to(output.resolve()):
            if output.resolve() == root.resolve() and route.startswith('wiki/content/'):
                continue
            dest.unlink(missing_ok=True)
    write('wiki/build-manifest.json', json.dumps({'schema_version': 1, 'files': sorted(files)}, indent=2) + '\n')
    for route, text in sorted(files.items()):
        dest = output / route
        dest.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            dest.write_bytes(text)
        else:
            dest.write_text(text, encoding='utf-8')
    return {'articles': len(registry['articles']), 'sources': len(sources), 'coverage': 'validated' if coverage else 'not supplied', 'local_links_checked': checked_links}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=REPO)
    parser.add_argument('--output', type=Path, default=REPO)
    parser.add_argument('--strict', action='store_true')
    parser.add_argument('--public-url', default='https://flaviusapop.github.io/ai-engineer-evals/')
    parser.add_argument('--github-url', default='https://github.com/flaviusapop/ai-engineer-evals/blob/main/')
    args = parser.parse_args()
    print(json.dumps(build(args.root, args.output, args.strict, args.public_url, args.github_url), sort_keys=True))


if __name__ == '__main__':
    main()
