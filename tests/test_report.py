"""Browser acceptance tests. Run: uv run --with playwright python tests/test_report.py -v"""
import argparse
import pathlib
import shutil
import unittest
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--url', default=(ROOT / 'report.html').as_uri())
options, remaining = parser.parse_known_args()

class ReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pw = sync_playwright().start()
        executable = shutil.which('google-chrome') or shutil.which('chromium')
        cls.browser = cls.pw.chromium.launch(executable_path=executable, headless=True, args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()

    def setUp(self):
        self.page = self.browser.new_page(viewport={'width': 1440, 'height': 900})
        self.errors = []
        self.page.on('pageerror', lambda error: self.errors.append(str(error)))
        self.page.goto(options.url, wait_until='load')

    def tearDown(self):
        self.page.close()
        self.assertEqual(self.errors, [], 'Browser runtime errors')

    def visible_dates(self):
        return self.page.locator('.video:not([hidden]) time').all_text_contents()

    def test_generated_report_is_reproducible(self):
        import subprocess
        import sys
        builder = ROOT / 'scripts' / 'build.py'
        self.assertTrue(builder.is_file(), 'Portable report builder is missing')
        result = subprocess.run([sys.executable, str(builder), '--check'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_topic_grouping_restores_original_record_order(self):
        import json
        expected = json.loads((ROOT / 'videos.json').read_text())
        self.page.locator('#sort').select_option('topic')
        actual = self.page.locator('.video').evaluate_all('(cards) => cards.map(c => c.dataset.id)')
        self.assertEqual(actual, [r['id'] for r in expected])

    def test_sorting_preserves_search_and_scope_filters(self):
        self.page.locator('#scope').select_option('core')
        self.assertEqual(len(self.visible_dates()), 190)
        self.page.locator('#search').fill('judge')
        visible = self.page.locator('.video:not([hidden])')
        ids = visible.evaluate_all('(cards) => cards.map(c => c.dataset.id)')
        self.assertGreater(len(ids), 0)
        for mode, reverse in [('oldest', False), ('newest', True)]:
            self.page.locator('#sort').select_option(mode)
            self.assertEqual(set(visible.evaluate_all('(cards) => cards.map(c => c.dataset.id)')), set(ids))
            dates = self.visible_dates()
            self.assertEqual(dates, sorted(dates, reverse=reverse))
            self.assertTrue(visible.evaluate_all('(cards) => cards.every(c => c.dataset.scope === "core")'))

    def test_transcript_stays_open_when_card_moves(self):
        first = self.page.locator('.video').first
        video_id = first.get_attribute('data-id')
        first.locator('.transcript-jump').click()
        transcript = self.page.locator(f'#transcript-{video_id}')
        self.assertTrue(transcript.evaluate('(d) => d.open'))
        text = transcript.locator('pre').text_content()
        self.page.locator('#sort').select_option('oldest')
        self.assertTrue(transcript.evaluate('(d) => d.open'))
        self.assertEqual(transcript.locator('pre').text_content(), text)

    def test_every_rendered_record_matches_its_source_data(self):
        import json
        expected = {r['id']: r for r in json.loads((ROOT / 'videos.json').read_text())}
        actual = self.page.locator('.video').evaluate_all('''(cards) => cards.map(c => ({id:c.dataset.id, title:c.querySelector('h2').textContent, summary:c.querySelector('.digest').textContent, url:c.querySelector('.meta a').href, transcript:c.querySelector('pre').textContent}))''')
        self.assertEqual({r['id'] for r in actual}, set(expected))
        for record in actual:
            source = expected[record['id']]
            self.assertEqual(record['title'], source['title'])
            self.assertEqual(record['summary'], source['summary'])
            self.assertEqual(record['url'], source['url'])
            transcript = (ROOT / source['transcript']).read_text().split('## Transcript', 1)[1].strip()
            self.assertEqual(record['transcript'], transcript)

    def test_mobile_and_desktop_have_no_horizontal_overflow(self):
        for width in [320, 390, 768, 1440]:
            with self.subTest(width=width):
                self.page.set_viewport_size({'width': width, 'height': 900})
                self.assertFalse(self.page.evaluate('document.documentElement.scrollWidth > innerWidth'))

    def test_oldest_first_control_reverses_chronology(self):
        control = self.page.locator('#sort')
        self.assertEqual(control.count(), 1, 'Sort control is missing')
        control.select_option('oldest')
        dates = self.visible_dates()
        self.assertEqual(dates, sorted(dates))
        control.select_option('newest')
        self.assertEqual(self.visible_dates(), sorted(dates, reverse=True))

    def test_initial_video_order_is_newest_first(self):
        dates = self.visible_dates()
        self.assertEqual(len(dates), 313)
        self.assertEqual(dates, sorted(dates, reverse=True))

if __name__ == '__main__':
    unittest.main(argv=['test_report.py', *remaining])
