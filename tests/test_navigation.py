"""Navigation contracts for the public field guide."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
GUIDE = 'https://flaviusapop.github.io/ai-engineer-evals/wiki/'


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.links = []
        self.active = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('header', 'nav'):
            self.stack.append(tag)
        if tag == 'a':
            self.active = [attrs, tuple(self.stack), '']

    def handle_data(self, data):
        if self.active is not None:
            self.active[2] += data

    def handle_endtag(self, tag):
        if tag == 'a' and self.active is not None:
            self.links.append(self.active)
            self.active = None
        if tag in ('header', 'nav') and self.stack and self.stack[-1] == tag:
            self.stack.pop()


def guide_link(path, landmark):
    parser = LinkParser()
    parser.feed(path.read_text())
    links = [link for link in parser.links if link[0].get('href') == GUIDE and landmark in link[1]]
    return links


class NavigationTests(unittest.TestCase):
    def test_homepage_links_to_field_guide_in_navigation(self):
        links = guide_link(ROOT / 'index.html', 'nav')
        self.assertEqual(len(links), 1, 'homepage navigation must link to the public field guide')
        self.assertIn('field guide', links[0][2].lower())
        if links[0][0].get('target') == '_blank':
            self.assertTrue({'noopener', 'noreferrer'} <= set(links[0][0].get('rel', '').split()))

    def test_report_header_links_to_field_guide(self):
        links = guide_link(ROOT / 'templates/report.html', 'header')
        self.assertEqual(len(links), 1, 'report header must link to the public field guide')
        self.assertIn('field guide', links[0][2].lower())
        if links[0][0].get('target') == '_blank':
            self.assertTrue({'noopener', 'noreferrer'} <= set(links[0][0].get('rel', '').split()))

    def test_readme_header_links_to_field_guide(self):
        header = (ROOT / 'README.md').read_text().split('##', 1)[0]
        self.assertIn(f'[Field guide]({GUIDE})', header, 'README header must link to the public field guide')


if __name__ == '__main__':
    unittest.main()
