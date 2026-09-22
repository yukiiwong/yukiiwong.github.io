"""Validate the two-page academic CV; visual review is still required.

Run after build_cv.py. Requires pypdf and pdfplumber.
"""
import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'cv/Yukai_Wang_CV.pdf'
reader = PdfReader(path)
assert len(reader.pages) == 2, 'CV must remain two pages'


def normalized(text):
    return ' '.join(text.replace('\u2013', '-').replace('\u2014', '-').split())


text = normalized(' '.join(page.extract_text() for page in reader.pages))
for expected in ('PhD Candidate', 'Research Experience', 'Publications and Manuscripts',
                 'Journal Article', 'Conference Contributions', 'Manuscripts Under Review',
                 'Selected Honors and Awards', 'Technical Skills'):
    assert expected in text, f'Missing expected heading or identity: {expected}'
for outdated in ('PhD student', 'ICML', 'NeurIPS', 'Rejected', 'Withdrawn', 'unsuccessful'):
    assert outdated not in text, f'Outdated public status: {outdated}'
assert text.count('Ongoing') == 2, 'Ongoing work must be consolidated into two research themes'
for theme in ('Traffic world models and digital twins', 'Decision utility and safety assessment'):
    assert theme in text, f'Missing consolidated research theme: {theme}'
cv = json.loads((ROOT / '_data/cv.json').read_text())
research = json.loads((ROOT / '_data/research.json').read_text())
covered_projects = []
for group in cv['research_groups']:
    for item in group['items']:
        covered_projects.extend([item['project']] + item.get('related_projects', []))
assert sorted(covered_projects) == sorted(item['id'] for item in research), 'Research coverage must be preserved without duplication'
assert text.count('Under review') == 7, 'Four submissions plus three related research entries expected'
assert '..' not in text, 'Duplicate punctuation in bibliographic entries'
publications = json.loads((ROOT / '_data/publications.json').read_text())
submissions = json.loads((ROOT / '_data/submissions.json').read_text())
for entry in publications + submissions['under_review']:
    assert normalized(entry['title']) in text, f'Missing title: {entry["title"]}'
assert any(isinstance(item, list) for item in reader.outline), 'Nested section bookmarks missing'

with pdfplumber.open(path) as pdf:
    used_fonts = set()
    for number, page in enumerate(pdf.pages, 1):
        assert page.width == 612 and page.height == 792
        used_fonts.update(char['fontname'] for char in page.chars)
        for char in page.chars:
            assert char['x0'] >= 49.5 and char['x1'] <= 562.5, f'Page {number}: horizontal overflow'
            assert char['top'] >= 35 and char['bottom'] <= 769, f'Page {number}: vertical overflow'
        assert len(page.lines) >= 3, f'Page {number}: section rules missing'
    for face in ('LiberationSerif', 'LiberationSerif-Bold', 'LiberationSerif-Italic', 'LiberationSerif-BoldItalic'):
        assert any(name.endswith(face) for name in used_fonts), f'Missing font face: {face}'

for page in reader.pages:
    for font in page['/Resources']['/Font'].values():
        font = font.get_object()
        if 'LiberationSerif' in font['/BaseFont']:
            assert '/FontFile2' in font['/FontDescriptor'], 'Serif font must be embedded'

print('PASS: two pages, content/status preservation, nested headings, embedded typefaces, and page bounds.')
