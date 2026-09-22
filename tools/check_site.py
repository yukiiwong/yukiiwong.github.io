"""Check the public portfolio entry points before Pages deployment (stdlib only)."""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
pages = ['index.html', 'research/index.html', 'about/index.html',
         'publications/index.html', 'cv/index.html', 'blogs/index.html']

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.images = [], set(), []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('img', 'script') and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.images.append(attrs)

failures = []
for rel in pages:
    path = root / rel
    if not path.is_file():
        failures.append(f'Missing page: {rel}')
        continue
    text = path.read_text()
    parser = Page()
    parser.feed(text)
    for placeholder in ['Preprints111', 'articles222', 'proceedings333', 'Example news here', 'Example Research', 'Feynman lectures', '&lt;/nav&gt;', '&lt;/article&gt;', '&lt;figcaption&gt;']:
        if placeholder in text:
            failures.append(f'{rel}: template placeholder {placeholder}')
    for img in parser.images:
        if 'alt' not in img:
            failures.append(f'{rel}: image has no alt attribute')
    if rel == 'research/index.html' and len(parser.images) < 7:
        failures.append('Research figures did not render as images')
    if rel in ('index.html', 'research/index.html'):
        for retired in ('rollout-protocol.png', 'ranking-protocol.png'):
            if retired in text:
                failures.append(f'{rel}: retired protocol illustration {retired}')
    if rel == 'research/index.html':
        sources = {img.get('src', '') for img in parser.images}
        for figure in ('rollout-error-propagation.png', 'rollout-placement-scenes.png',
                       'prediction-utility-transfer.png', 'selector-tradeoff.png'):
            if not any(src.endswith('/' + figure) for src in sources):
                failures.append(f'Research result figure missing: {figure}')
    for link in parser.links:
        u = urlsplit(link)
        if u.scheme not in ('', 'http', 'https') or u.netloc not in ('', 'yukiiwong.github.io', '127.0.0.1:4173'):
            continue
        decoded = unquote(u.path)
        target = (root / decoded.lstrip('/')) if decoded.startswith('/') else path.parent / decoded
        if not decoded:
            target = path
        elif target.is_dir():
            target = target / 'index.html'
        if not target.is_file():
            failures.append(f'{rel}: broken local link {link}')
            continue
        if u.fragment and target.suffix == '.html':
            dest = Page()
            dest.feed(target.read_text())
            if unquote(u.fragment) not in dest.ids:
                failures.append(f'{rel}: missing anchor {link}')
pdf = root / 'cv/Yukai_Wang_CV.pdf'
if not pdf.is_file() or not pdf.read_bytes().startswith(b'%PDF-'):
    failures.append('CV PDF missing or invalid')
if failures:
    print('\n'.join(failures))
    sys.exit(1)
print(f'PASS: {len(pages)} portfolio pages, local links, figure references, anchors, placeholders, and CV PDF.')
