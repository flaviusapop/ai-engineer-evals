"""TEST-ONLY synthetic wiki acceptance. Never publishes fixture research.
Run: uv run --with markdown --with bleach --with playwright python tests/test_wiki.py -v
"""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = Path(os.environ.get('TMPDIR', Path.home() / '.hermes/cache/scratch'))


def fixture(root):
    """Clearly synthetic, small input dataset; never production coverage."""
    (root / 'wiki/data').mkdir(parents=True)
    (root / 'wiki/content').mkdir()
    registry = {
        'schema_version': 1, 'title': 'TEST ONLY Field Guide', 'subtitle': 'Synthetic fixture',
        'sections': [{'id': 'foundations', 'title': 'Foundations', 'description': 'Test topics', 'order': 1}],
        'articles': [
            {'id': 'first', 'title': 'First concept', 'section': 'foundations', 'order': 1,
             'summary': 'A test introduction.', 'content_file': 'wiki/content/first.md',
             'prerequisites': [], 'related': ['second'], 'concept_keys': ['first-key']},
            {'id': 'second', 'title': 'Second concept', 'section': 'foundations', 'order': 2,
             'summary': 'A test continuation.', 'content_file': 'wiki/content/second.md',
             'prerequisites': ['first'], 'related': [], 'concept_keys': ['second-key']}],
        'reading_paths': [{'id': 'start', 'title': 'Start here', 'description': 'Test path', 'article_ids': ['first', 'second']}],
        'glossary': [{'term': 'Fixture', 'definition': 'Synthetic test evidence.', 'article_id': 'first'}]}
    claims = [{'claim_id': 'TEST0000001:c01', 'source_id': 'TEST0000001', 'concept_key': 'first-key',
               'topic': 'test', 'title': 'Test claim', 'explanation': 'Synthetic claim.',
               'kind': 'principle', 'evidence_strength': 'speaker_guidance',
               'evidence': {'line_start': 10, 'line_end': 12, 'quote': 'Synthetic exact quote & <text>.'},
               'qualification': 'Test only.', 'related_concepts': []}]
    videos = [{'id': 'TEST0000001', 'title': 'Synthetic source',
               'url': 'https://www.youtube.com/watch?v=TEST0000001', 'transcript': 'transcripts/TEST0000001.md'}]
    for name, data in [('wiki/data/registry.json', registry), ('wiki/data/claims.json', claims), ('videos.json', videos)]:
        (root / name).write_text(json.dumps(data))
    (root / 'wiki/content/first.md').write_text('## A useful question\n\nTest-only heliotrope evidence [cite:TEST0000001:c01]. See [[second|the next concept]].\n\n### Detail\n\n- First step\n- Second step\n\n| Item | Value |\n| --- | --- |\n| Test | Yes |\n\n```python\nprint("test")\n```\n')
    (root / 'wiki/content/second.md').write_text('## Continue\n\nStart with [[first]].\n')
    return registry


def load_builder():
    path = ROOT / 'scripts/build_wiki.py'
    if not path.exists():
        raise AssertionError('Missing concept-wiki generator scripts/build_wiki.py')
    spec = importlib.util.spec_from_file_location('build_wiki', path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WikiTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='wiki-test-', dir=SCRATCH)
        self.root = Path(self.temp.name)
        self.registry = fixture(self.root)
        self.out = self.root / 'site'

    def tearDown(self):
        self.temp.cleanup()

    def build(self, **kwargs):
        return load_builder().build(self.root, self.out, **kwargs)

    def test_rejects_inconsistent_claim_ownership_and_aliases(self):
        self.registry['claim_ownership'] = {'TEST0000001:c01':'first-key'}
        self.registry['concept_aliases'] = {'first-key':['first-key']}
        path = self.root / 'wiki/data/registry.json'
        path.write_text(json.dumps(self.registry))
        self.build()
        for field, value in [('claim_ownership', {}), ('claim_ownership', {'TEST0000001:c01':'second-key'}), ('concept_aliases', {'first-key':['second-key']})]:
            changed=json.loads(json.dumps(self.registry)); changed[field]=value; path.write_text(json.dumps(changed))
            with self.subTest(field=field,value=value), self.assertRaises(ValueError): self.build()

    def test_coverage_requires_uncited_canonical_primary_lineage(self):
        self.registry['claim_ownership'] = {'TEST0000001:c01': 'first-key'}
        self.registry['concept_aliases'] = {'second-key': ['first-key']}
        (self.root / 'wiki/data/registry.json').write_text(json.dumps(self.registry))
        claims_path = self.root / 'wiki/data/claims.json'
        claims = json.loads(claims_path.read_text())
        claims[0]['concept_key'] = 'second-key'  # Original suggestion is not ownership.
        claims_path.write_text(json.dumps(claims))
        (self.root / 'wiki/content/first.md').write_text('## No inline citations\n')
        coverage = {'source_count': 1, 'max_transcripts_per_reader': 5,
                    'readers': [{'batch_id': 'test', 'source_ids': ['TEST0000001'], 'status': 'accepted'}],
                    'sources': [{'source_id': 'TEST0000001', 'reader_batch': 'test',
                                 'article_ids': ['second'], 'limitations': []}]}
        path = self.root / 'wiki/data/coverage.json'
        path.write_text(json.dumps(coverage))
        with self.assertRaisesRegex(ValueError, 'primary'):
            self.build()
        coverage['sources'][0]['article_ids'].append('first')
        path.write_text(json.dumps(coverage))
        (self.root / 'wiki/content/second.md').write_text('## Context\n\n[cite:TEST0000001:c01]')
        self.build()  # Both canonical primary and contextual citations are legitimate.

    def test_omit_policy_renders_provenance_without_quote(self):
        self.registry['quote_policy'] = 'omit'
        (self.root / 'wiki/data/registry.json').write_text(json.dumps(self.registry))
        path = self.root / 'wiki/data/claims.json'
        claims = json.loads(path.read_text())
        del claims[0]['evidence']['quote']
        path.write_text(json.dumps(claims))
        self.build()
        article = (self.out / 'wiki/articles/first.html').read_text()
        full = (self.out / 'wiki/llms-full.md').read_text()
        self.assertIn('#L10-L12', article)
        self.assertIn('#L10-L12', full)
        self.assertNotIn('<blockquote>', article)
        self.assertNotIn('\n> ', full)
        methodology = (self.out / 'wiki/methodology.html').read_text()
        self.assertNotIn('exact excerpts', methodology)
        self.assertIn('transcript line ranges', methodology)
        claims[0]['evidence']['quote'] = 'contradiction'
        path.write_text(json.dumps(claims))
        with self.assertRaisesRegex(ValueError, 'quote'):
            self.build()

    def test_renders_categorized_entry_and_canonical_article(self):
        self.build()
        entry = (self.out / 'wiki/index.html').read_text()
        article = (self.out / 'wiki/articles/first.html').read_text()
        self.assertIn('TEST ONLY Field Guide', entry)
        self.assertIn('topics/foundations.html', entry)
        self.assertIn('First concept', article)
        self.assertIn('<table>', article)
        self.assertIn('<code', article)
        self.assertEqual((self.out / 'wiki/content/first.md').read_bytes(), (self.root / 'wiki/content/first.md').read_bytes())

    def test_resolves_citations_and_internal_concept_links(self):
        self.build()
        article = (self.out / 'wiki/articles/first.html').read_text()
        self.assertNotIn('[cite:', article)
        self.assertNotIn('[[second', article)
        self.assertIn('href="second.html"', article)
        self.assertIn('href="#evidence-1"', article)
        self.assertIn('id="evidence-1"', article)
        self.assertIn('Synthetic exact quote &amp; &lt;text&gt;.', article)
        self.assertIn('transcripts/TEST0000001.md#L10-L12', article)
        self.assertIn('speaker_guidance', article)
        self.assertIn('Test only.', article)
        self.assertIn('<details', article)

    def test_rejects_inconsistent_canonical_inputs_before_writing(self):
        cases = {
            'duplicate article': lambda r: r['articles'].append(dict(r['articles'][0])),
            'unsafe slug': lambda r: r['articles'][0].update(id='../escape'),
            'duplicate concept': lambda r: r['articles'][1].update(concept_keys=['first-key']),
            'unknown section': lambda r: r['articles'][0].update(section='missing'),
            'dangling prerequisite': lambda r: r['articles'][0].update(prerequisites=['missing']),
            'dangling related': lambda r: r['articles'][0].update(related=['missing']),
            'dangling path': lambda r: r['reading_paths'][0].update(article_ids=['missing']),
            'dangling glossary': lambda r: r['glossary'][0].update(article_id='missing'),
            'unsafe content path': lambda r: r['articles'][0].update(content_file='transcripts/TEST0000001.md'),
        }
        for label, mutation in cases.items():
            with self.subTest(case=label):
                data = json.loads(json.dumps(self.registry))
                mutation(data)
                (self.root / 'wiki/data/registry.json').write_text(json.dumps(data))
                with self.assertRaises(ValueError):
                    self.build()
                self.assertFalse(self.out.exists())
        (self.root / 'wiki/data/registry.json').write_text(json.dumps(self.registry))
        for token in ['[[missing]]', '[cite:TEST0000001:missing]', '[[first']:
            (self.root / 'wiki/content/second.md').write_text(token)
            with self.subTest(token=token), self.assertRaises(ValueError):
                self.build()
        (self.root / 'wiki/content/second.md').write_text('## Safe\n')
        (self.root / 'wiki/content/unregistered.md').write_text('Test only')
        with self.assertRaises(ValueError):
            self.build()

    def test_sanitizes_untrusted_markdown_and_external_links(self):
        malicious = '''## Safety

<script>window.compromised=true</script>
<img src=x onerror="window.compromised=true">
[bad](javascript:alert%281%29)
[encoded](java&#x73;cript:alert%281%29)
[data](data:text/html,bad)
[good](https://example.org/?a=1&b=2)
[[second|<img src=x onerror=alert(1)>]]
'''
        (self.root / 'wiki/content/second.md').write_text(malicious.replace('[[second|', '[[first|'))
        self.build()
        article = (self.out / 'wiki/articles/second.html').read_text()
        self.assertNotIn('<script>', article)
        self.assertNotIn('<img', article)
        self.assertNotIn('href="javascript:', article)
        self.assertNotIn('href="data:', article)
        self.assertIn('rel="noopener noreferrer"', article)
        self.assertIn('target="_blank"', article)
        self.assertIn('href="first.html"', article)

    def test_strict_accepts_313_synthetic_single_source_readers(self):
        # Synthetic coverage partition only; this is not the actual corpus.
        ids = [f'TEST{i:07d}' for i in range(1, 314)]
        coverage = {'source_count': 313, 'max_transcripts_per_reader': 5,
                    'readers': [{'batch_id': f'test-{i}', 'source_ids': [s], 'status': 'accepted'} for i, s in enumerate(ids)],
                    'sources': [{'source_id': s, 'reader_batch': f'test-{i}', 'article_ids': ['first'], 'limitations': []} for i, s in enumerate(ids)]}
        (self.root / 'wiki/data/coverage.json').write_text(json.dumps(coverage))
        try:
            result = load_builder().validate_coverage(self.root, True, dict.fromkeys(ids), {'first': {}}, {}, {})
        except ValueError as error:
            self.fail(f'Valid synthetic partition rejected: {error}')
        self.assertEqual(len(result['readers']), 313)

    def test_strict_source_coverage_enforces_all_313_unique_owned_sources(self):
        with self.assertRaisesRegex(ValueError, 'coverage'):
            self.build(strict=True)
        # Synthetic 313-row coverage is a gate fixture, not a production claim.
        videos = json.loads((self.root / 'videos.json').read_text())
        videos += [{'id': f'TEST{i:07d}', 'title': f'Test source {i}',
                    'url': f'https://www.youtube.com/watch?v=TEST{i:07d}',
                    'transcript': f'transcripts/TEST{i:07d}.md'} for i in range(2, 314)]
        ids = [v['id'] for v in videos]
        readers = [{'batch_id': f'test-reader-{i // 5}', 'source_ids': ids[i:i + 5], 'status': 'accepted'} for i in range(0, 313, 5)]
        coverage = {'source_count': 313, 'max_transcripts_per_reader': 5, 'readers': readers,
                    'sources': [{'source_id': s, 'reader_batch': f'test-reader-{i // 5}', 'article_ids': ['first'], 'limitations': []} for i, s in enumerate(ids)]}
        (self.root / 'videos.json').write_text(json.dumps(videos))
        path = self.root / 'wiki/data/coverage.json'
        path.write_text(json.dumps(coverage))
        self.assertEqual(self.build(strict=True)['sources'], 313)
        for label, mutate in {
            'duplicate owner': lambda c: c['readers'][1]['source_ids'].__setitem__(0, ids[0]),
            'incomplete reader coverage': lambda c: c['readers'][0]['source_ids'].pop(),
            'too many per reader': lambda c: c['readers'][0]['source_ids'].append(ids[5]),
            'missing source': lambda c: c['sources'].pop(),
            'unaccepted reader': lambda c: c['readers'][0].update(status='pending'),
            'wrong ownership': lambda c: c['sources'][0].update(reader_batch='test-reader-1'),
            'dangling article': lambda c: c['sources'][0].update(article_ids=['absent']),
            'contradicted citation map': lambda c: c['sources'][0].update(article_ids=['second']),
        }.items():
            changed = json.loads(json.dumps(coverage))
            mutate(changed)
            path.write_text(json.dumps(changed))
            with self.subTest(case=label), self.assertRaises(ValueError):
                self.build(strict=True)

    def test_all_reading_routes_and_article_navigation(self):
        self.build()
        required = ['index.html', 'articles/first.html', 'articles/second.html', 'topics/foundations.html',
                    'paths/start.html', 'glossary.html', 'sources.html', 'methodology.html']
        for route in required:
            with self.subTest(route=route):
                self.assertTrue((self.out / 'wiki' / route).is_file(), route)
        article = (self.out / 'wiki/articles/first.html').read_text()
        for text in ['On this page', '#a-useful-question', 'Related concepts', 'Linked from',
                     'Continue reading', 'Section navigation', 'Breadcrumb', 'Download Markdown']:
            self.assertIn(text, article)
        second = (self.out / 'wiki/articles/second.html').read_text()
        self.assertIn('Prerequisites', second)
        self.assertIn('Previous', second)
        sources = (self.out / 'wiki/sources.html').read_text()
        self.assertIn('../report.html#video-TEST0000001', sources)
        self.assertIn('articles/first.html', sources)
        self.assertIn('not supplied', (self.out / 'wiki/methodology.html').read_text())

    def test_deterministic_llm_exports_resolve_every_token(self):
        self.build()
        full = (self.out / 'wiki/llms-full.md').read_text()
        discovery = (self.out / 'llms.txt').read_text()
        self.assertNotIn('[cite:', full)
        self.assertNotIn('[[', full)
        self.assertIn('https://flaviusapop.github.io/ai-engineer-evals/wiki/articles/second.html', full)
        self.assertIn('Synthetic exact quote', full)
        self.assertIn('#L10-L12', full)
        self.assertIn('wiki/llms-full.md', discovery)
        self.assertIn('https://flaviusapop.github.io/ai-engineer-evals/wiki/index.html', discovery)
        before = {p.relative_to(self.out): p.read_bytes() for p in self.out.rglob('*') if p.is_file()}
        self.build()
        self.assertEqual(before, {p.relative_to(self.out): p.read_bytes() for p in self.out.rglob('*') if p.is_file()})

    def test_rejects_unsafe_source_provenance_and_invalid_claims(self):
        videos = json.loads((self.root / 'videos.json').read_text())
        claims = json.loads((self.root / 'wiki/data/claims.json').read_text())
        for label, change in {
            'unsafe watch URL': lambda v, c: v[0].update(url='javascript:alert(1)'),
            'mismatched watch ID': lambda v, c: v[0].update(url='https://www.youtube.com/watch?v=OTHER000001'),
            'invalid source ID': lambda v, c: v[0].update(id='not-eleven'),
            'unsafe transcript URL': lambda v, c: v[0].update(transcript='../private.md'),
            'unknown claim source': lambda v, c: c[0].update(source_id='missing'),
            'duplicate claim': lambda v, c: c.append(dict(c[0])),
            'invalid line range': lambda v, c: c[0]['evidence'].update(line_start=0),
            'reversed lines': lambda v, c: c[0]['evidence'].update(line_end=1),
        }.items():
            v, c = json.loads(json.dumps(videos)), json.loads(json.dumps(claims))
            change(v, c)
            (self.root / 'videos.json').write_text(json.dumps(v))
            (self.root / 'wiki/data/claims.json').write_text(json.dumps(c))
            with self.subTest(case=label), self.assertRaises(ValueError):
                self.build()

    def test_rejects_every_broken_local_link_or_anchor_before_emitting_files(self):
        for broken in ['[missing](missing.html)', '[missing anchor](first.html#not-a-heading)', '[escape](../../../private.txt)']:
            (self.root / 'wiki/content/second.md').write_text('## Continue\n\n' + broken)
            with self.subTest(link=broken), self.assertRaisesRegex(ValueError, 'link|anchor'):
                self.build()
        (self.root / 'wiki/content/second.md').write_text('## Continue\n\n[valid anchor](first.html#a-useful-question)')
        self.build()
        self.assertIn('first.html#a-useful-question', (self.out / 'wiki/articles/second.html').read_text())

    def test_rebuild_removes_only_previously_generated_stale_routes(self):
        self.build()
        keep = self.out / 'unrelated.txt'
        keep.write_text('Never delete unrelated output files')
        self.registry['articles'] = self.registry['articles'][:1]
        self.registry['articles'][0]['related'] = []
        self.registry['reading_paths'][0]['article_ids'] = ['first']
        (self.root / 'wiki/data/registry.json').write_text(json.dumps(self.registry))
        (self.root / 'wiki/content/second.md').unlink()
        (self.root / 'wiki/content/first.md').write_text('## Only remaining concept\n\nTest [cite:TEST0000001:c01].')
        self.build()
        self.assertEqual({p.stem for p in (self.out / 'wiki/articles').glob('*.html')}, {'first'})
        self.assertFalse((self.out / 'wiki/content/second.md').exists())
        self.assertTrue(keep.exists())

    def test_canonical_download_preserves_authored_bytes(self):
        authored = '## Continue\r\n\r\nUnicode café & punctuation.\r\n'.encode('utf-8')
        (self.root / 'wiki/content/second.md').write_bytes(authored)
        self.build()
        self.assertEqual((self.out / 'wiki/content/second.md').read_bytes(), authored)
        self.assertEqual((self.root / 'wiki/content/second.md').read_bytes(), authored)

    def test_consolidated_export_absolutizes_standard_markdown_links(self):
        (self.root / 'wiki/content/second.md').write_text('## Continue\n\n[Question](first.html#a-useful-question) and [this section](#continue).\n\n[reference][q]\n\n[q]: first.html#a-useful-question\n')
        self.build()
        full = (self.out / 'wiki/llms-full.md').read_text()
        self.assertIn('[Question](https://flaviusapop.github.io/ai-engineer-evals/wiki/articles/first.html#a-useful-question)', full)
        self.assertIn('[this section](https://flaviusapop.github.io/ai-engineer-evals/wiki/articles/second.html#continue)', full)
        self.assertIn('[q]: https://flaviusapop.github.io/ai-engineer-evals/wiki/articles/first.html#a-useful-question', full)

    def test_reading_path_neighbors_follow_path_order_not_taxonomy_order(self):
        self.registry['reading_paths'][0]['article_ids'] = ['second', 'first']
        (self.root / 'wiki/data/registry.json').write_text(json.dumps(self.registry))
        self.build()
        article = (self.out / 'wiki/articles/first.html').read_text()
        self.assertIn('aria-label="Reading path: Start here"', article)
        self.assertIn('Previous in path: <a href="second.html">Second concept</a>', article)
        second = (self.out / 'wiki/articles/second.html').read_text()
        self.assertIn('Next in path: <a href="first.html">First concept</a>', second)

    def test_machine_readable_exports_are_discoverable_from_the_guide(self):
        self.build()
        entry = (self.out / 'wiki/index.html').read_text()
        self.assertIn('href="llms-full.md"', entry)
        self.assertIn('href="../llms.txt"', entry)


class WikiBrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import functools
        from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
        import shutil
        import threading
        from playwright.sync_api import sync_playwright
        cls.temp = tempfile.TemporaryDirectory(prefix='wiki-browser-test-', dir=SCRATCH)
        cls.root = Path(cls.temp.name)
        fixture(cls.root)
        cls.out = cls.root / 'site'
        load_builder().build(cls.root, cls.out)
        # Clearly test-only report target: production report is never copied or read.
        (cls.out / 'report.html').write_text('<!doctype html><title>TEST ONLY source report</title><link rel="icon" href="wiki/assets/favicon.svg"><p id="video-TEST0000001">Synthetic report anchor</p>')
        class QuietHandler(SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                pass
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(cls.out)))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f'http://127.0.0.1:{cls.server.server_port}/'
        cls.pw = sync_playwright().start()
        cls.browser = cls.pw.chromium.launch(executable_path=shutil.which('google-chrome') or shutil.which('chromium'), headless=True, args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
        cls.temp.cleanup()

    def setUp(self):
        self.page = self.browser.new_page(viewport={'width': 1440, 'height': 900})
        self.errors = []
        self.page.on('pageerror', lambda error: self.errors.append(str(error)))
        self.page.on('console', lambda message: self.errors.append(message.text) if message.type == 'error' else None)

    def tearDown(self):
        self.page.close()
        self.assertEqual(self.errors, [], 'Browser runtime or console errors')

    def test_every_generated_local_url_anchor_and_external_attribute(self):
        from urllib.parse import urldefrag, urlsplit, unquote
        ids, local_urls = {}, set()
        routes = sorted(self.out.glob('wiki/**/*.html')) + [self.out / 'report.html']
        for route in routes:
            self.page.goto(self.url + str(route.relative_to(self.out)))
            ids[self.page.url] = set(self.page.locator('[id]').evaluate_all('(nodes) => nodes.map(n => n.id)'))
            for record in self.page.locator('[href], [src]').evaluate_all('(nodes) => nodes.map(n => ({url:n.href || n.src, tag:n.tagName, target:n.target, rel:n.rel}))'):
                if record['url'].startswith(self.url):
                    local_urls.add(record['url'])
                elif record['tag'] == 'A' and urlsplit(record['url']).scheme in ['https', 'http']:
                    self.assertEqual(record['target'], '_blank')
                    self.assertTrue({'noopener', 'noreferrer'} <= set(record['rel'].split()))
        for url in sorted(local_urls):
            base, fragment = urldefrag(url)
            response = self.page.request.get(base)
            self.assertEqual(response.status, 200, url)
            if fragment and base in ids:
                self.assertIn(unquote(fragment), ids[base], url)
        self.assertGreater(len(local_urls), 20)

    def test_keyboard_skip_link_and_no_javascript_fallback(self):
        self.page.goto(self.url + 'wiki/articles/first.html')
        self.page.keyboard.press('Tab')
        self.assertEqual(self.page.evaluate('document.activeElement.textContent'), 'Skip to content')
        self.page.keyboard.press('Enter')
        self.assertEqual(self.page.evaluate('document.activeElement.id'), 'main')
        context = self.browser.new_context(java_script_enabled=False, viewport={'width':320, 'height':900})
        try:
            page = context.new_page()
            page.goto(self.url + 'wiki/index.html')
            self.assertTrue(page.locator('main a[href="articles/first.html"]').is_visible())
            self.assertIn('Search needs JavaScript', page.locator('noscript').text_content())
            self.assertTrue(page.locator('#search-control').is_disabled())
            page.goto(self.url + 'wiki/articles/first.html')
            self.assertIn('heliotrope', page.locator('.prose').text_content())
            page.locator('.evidence summary').focus()
            page.keyboard.press('Enter')
            self.assertTrue(page.locator('#evidence-1').is_visible())
            page.goto(self.url + 'wiki/sources.html')
            details = page.locator('.source-entry')
            self.assertFalse(details.evaluate('(d) => d.open'))
            details.locator('summary').focus()
            page.keyboard.press('Enter')
            self.assertTrue(details.locator('a').first.is_visible())
        finally:
            context.close()

    def test_reading_layout_and_disclosures_at_all_four_widths(self):
        for width in [320, 390, 768, 1440]:
            with self.subTest(width=width):
                self.page.set_viewport_size({'width': width, 'height': 900})
                self.page.goto(self.url + 'wiki/articles/first.html')
                nav = self.page.locator('.section-nav')
                self.assertEqual(nav.evaluate('(d) => d.open'), width >= 1000)
                self.assertFalse(self.page.locator('.evidence').evaluate('(d) => d.open'))
                if os.environ.get('WIKI_TEST_ARTIFACTS'):
                    artifacts = Path(os.environ['WIKI_TEST_ARTIFACTS']).resolve()
                    self.assertTrue(artifacts.is_relative_to(SCRATCH.resolve()), 'Browser artifacts must stay in configured private scratch')
                    artifacts.mkdir(parents=True, exist_ok=True)
                    self.page.screenshot(path=str(artifacts / f'wiki-article-{width}.png'), full_page=True)
                self.page.locator('.citation').click()
                self.assertTrue(self.page.locator('.evidence').evaluate('(d) => d.open'))
                self.assertTrue(self.page.locator('#evidence-1').is_visible())
                self.assertEqual(self.page.evaluate('document.activeElement.id'), 'evidence-1')
                self.assertFalse(self.page.evaluate('document.documentElement.scrollWidth > innerWidth'))
                self.page.goto(self.url + 'wiki/articles/first.html#evidence-1')
                self.assertTrue(self.page.locator('.evidence').evaluate('(d) => d.open'))
                if width < 1000:
                    self.assertFalse(self.page.get_by_role('navigation', name='Section navigation').is_visible())
                    nav.locator('summary').focus()
                    self.page.keyboard.press('Enter')
                    self.assertTrue(self.page.get_by_role('navigation', name='Section navigation').is_visible())
                else:
                    prose = self.page.locator('.prose')
                    measure = prose.evaluate('(p) => {const s=getComputedStyle(p);const c=document.createElement("span");c.textContent="0";c.style.font=s.font;p.append(c);const w=c.getBoundingClientRect().width;c.remove();return p.getBoundingClientRect().width/w;}')
                    self.assertGreaterEqual(measure, 65)
                    self.assertLessEqual(measure, 75)
        for route in sorted(self.out.glob('wiki/**/*.html')):
            for width in [320, 390, 768, 1440]:
                self.page.set_viewport_size({'width': width, 'height': 900})
                self.page.goto(self.url + str(route.relative_to(self.out)))
                self.assertFalse(self.page.evaluate('document.documentElement.scrollWidth > innerWidth'), f'{route.name} at {width}')
                self.assertEqual(self.page.get_by_role('banner').count(), 1)
                self.assertEqual(self.page.get_by_role('main').count(), 1)
                self.assertEqual(self.page.locator('h1').count(), 1)

    def test_local_fulltext_search_uses_body_text_and_static_file_urls(self):
        for url in [self.url + 'wiki/index.html', (self.out / 'wiki/index.html').as_uri()]:
            with self.subTest(url=url):
                self.page.goto(url)
                search = self.page.get_by_role('searchbox', name='Search concepts')
                self.assertEqual(search.count(), 1, 'Missing full-text search control')
                search.fill('heliotrope')
                result = self.page.locator('#search-results a')
                self.assertEqual(result.count(), 1)
                self.assertEqual(result.first.text_content(), 'First concept')
                self.assertIn('heliotrope', self.page.locator('#search-results').text_content())
                self.assertTrue(result.first.get_attribute('href').endswith('articles/first.html'))
                search.fill('second')
                self.assertGreater(self.page.locator('#search-results a').count(), 0)
                search.fill('ZZZnotfound')
                self.assertIn('No concepts found', self.page.locator('#search-status').text_content())
                search.fill('<img src=x onerror=alert(1)>')
                self.assertEqual(self.page.locator('#search-results img').count(), 0)
                search.fill('')
                self.assertEqual(self.page.locator('#search-results a').count(), 0)


if __name__ == '__main__':
    unittest.main()
