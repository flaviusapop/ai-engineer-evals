"""Rebuild the portable report and ZIP from this collection's canonical files.

Run `python scripts/build.py`, or `python scripts/build.py --check` for a dry check.
The template owns presentation; videos.json and transcripts own per-video content.
"""
import argparse
import hashlib
import html
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
records = json.loads((ROOT / 'videos.json').read_text())
manifest = json.loads((ROOT / 'manifest.json').read_text())
assert len(records) == 313 and len({r['id'] for r in records}) == 313
assert {r['id'] for r in records} == set(manifest)
cards = []
for r in records:
    source = ROOT / r['transcript']
    assert source.resolve().is_relative_to((ROOT / 'transcripts').resolve())
    raw = source.read_text()
    assert hashlib.sha256(source.read_bytes()).hexdigest() == manifest[r['id']]['sha256']
    assert r['url'] in raw and r['url'] == manifest[r['id']]['url']
    body = raw.split('## Transcript', 1)[1].strip()
    assert len(body) > 300 and '[TRUNCATED]' not in body
    e = lambda value: html.escape(str(value), quote=True)
    takes = ''.join('<li>' + e(t) + '</li>' for t in r.get('takeaways', []))
    if r.get('transcript_note'):
        takes += '<li class="caption-note">' + e(r['transcript_note']) + '</li>'
    cards.append(
        f'<article class="video" id="video-{r["id"]}" data-id="{r["id"]}" data-scope="{e(r["scope"])}" data-category="{e(r["category"])}">'
        f'<div class="eyebrow">{r["number"]:02d} / {e(r["scope"])} / {e(r["category"])}</div>'
        f'<h2>{e(r["title"])}</h2><p class="meta"><time>{e(r["date"])}</time> · '
        f'<a href="{e(r["url"])}" target="_blank" rel="noopener noreferrer">Watch on YouTube ↗</a> · '
        f'<a class="transcript-jump" href="#transcript-{r["id"]}">Transcript ↓</a></p>'
        f'<p class="digest">{e(r["summary"])}</p><ul>{takes}</ul>'
        f'<details class="transcript" id="transcript-{r["id"]}"><summary>Read full transcript <span>+</span></summary>'
        '<p class="caption-note">Extracted captions; original timestamp availability varies. Transcription errors may remain.</p>'
        f'<button type="button" class="download" data-video="{r["id"]}">Download transcript (.txt)</button>'
        f'<pre>{e(body)}</pre></details></article>'
    )
template = (ROOT / 'templates/report.html').read_text()
assert template.count('<!-- VIDEO_CARDS -->') == 1
page = template.replace('<!-- VIDEO_CARDS -->', ''.join(cards))
if args.check:
    assert (ROOT / 'report.html').read_text() == page, 'Report is stale: run python scripts/build.py'
    print('PASS: report is reproducible; all 313 source links and transcript hashes verified.')
else:
    (ROOT / 'report.html').write_text(page)
    allow = [
        '.nojekyll', '.gitignore', 'index.html', 'report.html', 'README.md', 'ACCESS.md', 'videos.json', 'videos.csv',
        'manifest.json', 'channel-inventory.json', 'screening-audit.json',
        'publisher-screening-1.json', 'publisher-screening-2.json',
        'date-boundary-evidence.json', 'supplemental-resolution.json',
        'templates/report.html', 'scripts/build.py', 'tests/test_report.py',
    ] + [r['transcript'] for r in records]
    assert len(allow) == len(set(allow))
    with zipfile.ZipFile(ROOT / 'collection.zip', 'w') as archive:
        for name in sorted(allow):
            info = zipfile.ZipInfo('ai-engineer-evals/' + name, date_time=(2026, 10, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (ROOT / name).read_bytes())
    print(f'Built report.html and collection.zip: {len(records)} videos, {len(allow)} archive entries.')
