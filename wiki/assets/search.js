'use strict';
(() => {
  const input = document.querySelector('#search-control');
  if (!input || !Array.isArray(window.WIKI_SEARCH)) return;
  const results = document.querySelector('#search-results');
  const status = document.querySelector('#search-status');
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  // Walk code points once, counting normalized UTF-16 units while retaining original offsets.
  const originalOffset = (text, target) => {
    let original = 0, normalized = 0;
    for (const character of text) {
      const length = normalize(character).length;
      if (normalized + length > target) break;
      normalized += length;
      original += character.length;
    }
    return original;
  };
  const records = window.WIKI_SEARCH.map(record => ({...record,
    titleKey: normalize(record.title), summaryKey: normalize(record.summary), textKey: normalize(record.text)}));
  input.disabled = false;
  input.addEventListener('input', () => {
    const query = normalize(input.value.trim());
    results.replaceChildren();
    if (!query) { status.textContent = 'Search titles, summaries and article text.'; return; }
    const terms = query.split(/\s+/);
    const matches = records.filter(r => terms.every(t => `${r.titleKey} ${r.summaryKey} ${r.textKey}`.includes(t)))
      .map(r => ({...r, score: terms.reduce((n, t) => n + (r.titleKey.includes(t) ? 10 : 0) + (r.summaryKey.includes(t) ? 3 : 0), 0)}))
      .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title));
    status.textContent = matches.length ? `${matches.length} concept${matches.length === 1 ? '' : 's'} found.` : 'No concepts found. Try a broader term.';
    for (const record of matches) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = record.url; link.textContent = record.title;
      const snippet = document.createElement('p');
      const phraseLocation = record.textKey.indexOf(query);
      const location = phraseLocation >= 0 ? phraseLocation : record.textKey.indexOf(terms[0]);
      let start = location >= 0 ? Math.max(0, originalOffset(record.text, location) - 65) : 0;
      if (start && /[\uDC00-\uDFFF]/.test(record.text[start]) && /[\uD800-\uDBFF]/.test(record.text[start - 1])) start--;
      let end = start + 200;
      if (end < record.text.length && /[\uDC00-\uDFFF]/.test(record.text[end]) && /[\uD800-\uDBFF]/.test(record.text[end - 1])) end++;
      snippet.textContent = location >= 0 ? `${start ? '…' : ''}${record.text.slice(start, end)}${record.text.length > end ? '…' : ''}` : record.summary;
      item.append(link, snippet); results.append(item);
    }
  });
})();
