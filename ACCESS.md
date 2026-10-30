# Public collection: sources, building and verification

## Browse

- Library: https://flaviusapop.github.io/ai-engineer-evals/
- Report: https://flaviusapop.github.io/ai-engineer-evals/report.html#collection
- Source repository: https://github.com/flaviusapop/ai-engineer-evals

This is a public GitHub Pages site. No login, VPN or Tailscale connection is required. The report defaults to **Newest first**, with **Oldest first** and **Topic grouping** options. Sorting works with search and topic/scope filters, and preserves open transcripts.

## Sources of truth

- `videos.json` owns the 313 per-video records: titles, dates, summaries, takeaways and original-video/transcript links.
- `transcripts/` preserves the extracted captions. `manifest.json` associates each transcript with its original-video URL and SHA-256 hash.
- `templates/report.html` owns layout, synthesis and browser controls. The report's video content is generated from the records and transcript files.
- `report.html` is the self-contained distribution, including embedded transcripts; it also works offline.
- `README.md` is the Markdown report; `videos.csv` is the spreadsheet index.
- Screening audits and date-boundary evidence document the inclusion process. Local-machine evidence paths have been removed from this public export; original-video and publisher citations are retained.
- `collection.zip` contains the portable report, captions, data, audits, template, generator and tests.

## Rebuild

```bash
python scripts/build.py
python scripts/build.py --check
uv run --with playwright python tests/test_report.py -v
```

Tests use a system Google Chrome/Chromium when available, otherwise Playwright's installed Chromium. If needed, install it with `uv run --with playwright playwright install chromium`.

To test the deployed page:

```bash
uv run --with playwright python tests/test_report.py --url https://flaviusapop.github.io/ai-engineer-evals/report.html -v
```

The builder verifies transcript hashes before rendering. If intentionally correcting a transcript, explicitly update its manifest hash and document the correction. The template is a dated snapshot: membership changes also require updating counts, window/coverage statements and the synthesis.

## Deployment and attribution

GitHub Pages serves the `main` branch at the repository root. `.nojekyll` preserves the static files and caption downloads without Jekyll processing. Only this collection is published.

Original talks and caption content are attributable to their respective presenters and publishers, linked throughout the collection. This repository does not claim ownership of that material or apply a blanket software license to third-party transcripts. Caption transcription errors may remain; one transcript has a specifically flagged source-language problem.
