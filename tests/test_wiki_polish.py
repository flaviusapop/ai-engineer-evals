import unittest
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


class WikiPolishTests(unittest.TestCase):
    def test_header_search_stays_on_one_line_without_overflow(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--allow-file-access-from-files'])
            try:
                for path in ('wiki/index.html', 'wiki/articles/choosing-and-designing-agent-benchmarks.html'):
                    page = browser.new_page()
                    errors = []
                    page.on('pageerror', lambda error: errors.append(str(error)))
                    page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
                    for width in (320, 390, 768, 1440):
                        with self.subTest(path=path, width=width):
                            page.set_viewport_size({'width': width, 'height': 900})
                            page.goto((ROOT / path).as_uri(), wait_until='load')
                            metrics = page.locator('.site-header a').last.evaluate('''link => {
                                const range = document.createRange();
                                range.selectNodeContents(link);
                                return {text: link.textContent, rects: [...range.getClientRects()].map(r => ({top: r.top, width: r.width})),
                                  scroll: document.documentElement.scrollWidth, viewport: document.documentElement.clientWidth};
                            }''')
                            self.assertEqual((metrics['text'], len(metrics['rects'])), ('Search', 1), metrics)
                            self.assertLessEqual(metrics['scroll'], metrics['viewport'], metrics)
                    self.assertEqual(errors, [])
                    page.close()
            finally:
                browser.close()


    def test_unicode_normalization_keeps_late_phrase_in_snippet(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
            try:
                page = browser.new_page()
                page.set_content('<input id="search-control" disabled><p id="search-status"></p><ul id="search-results"></ul>')
                page.evaluate('''() => { window.WIKI_SEARCH = [
                    {title: 'Ligatures', summary: 'Summary', url: 'ligatures.html',
                     text: 'reward ' + 'ﬃ'.repeat(110) + '😀 reward hacking is here'},
                    {title: 'Combining', summary: 'Summary', url: 'combining.html',
                     text: 'reward ' + 'e\\u0301'.repeat(250) + '😀 reward hacking is here'}
                ]; }''')
                page.add_script_tag(path=str(ROOT / 'wiki/assets/search.js'))
                page.locator('#search-control').fill('reward hacking')
                for title in ('Ligatures', 'Combining'):
                    with self.subTest(title=title):
                        result = page.locator('#search-results li').filter(has=page.get_by_role('link', name=title))
                        self.assertEqual(result.count(), 1)
                        self.assertIn('reward hacking', result.locator('p').inner_text())
            finally:
                browser.close()

    def test_phrase_snippet_and_search_behaviors(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
            try:
                page = browser.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
                page.set_content('<input id="search-control" disabled><p id="search-status"></p><ul id="search-results"></ul>')
                page.evaluate('''() => { window.WIKI_SEARCH = [
                    {title: 'Owner', summary: 'A summary', url: 'owner.html', text: 'reward ' + 'filler '.repeat(45) + 'reward hacking is here'},
                    {title: 'Accent', summary: 'Another summary', url: 'accent.html', text: 'café habits'},
                    {title: 'Fallback', summary: 'Fallback summary', url: 'fallback.html', text: 'alpha ' + 'filler '.repeat(45) + 'beta'}
                ]; }''')
                page.add_script_tag(path=str(ROOT / 'wiki/assets/search.js'))
                control = page.locator('#search-control')
                control.fill('reward hacking')
                owner = page.locator('#search-results li').filter(has=page.get_by_role('link', name='Owner'))
                self.assertEqual(owner.count(), 1)
                self.assertIn('reward hacking', owner.locator('p').inner_text())
                control.fill('')
                self.assertEqual(page.locator('#search-results li').count(), 0)
                self.assertIn('Search titles', page.locator('#search-status').inner_text())
                control.fill('no-such-concept')
                self.assertIn('No concepts found', page.locator('#search-status').inner_text())
                control.fill('cafe')
                self.assertEqual(page.locator('#search-results a').inner_text(), 'Accent')
                control.fill('alpha beta')
                self.assertIn('alpha', page.locator('#search-results li p').inner_text())
                self.assertEqual(errors, [])
            finally:
                browser.close()


if __name__ == '__main__':
    unittest.main()
