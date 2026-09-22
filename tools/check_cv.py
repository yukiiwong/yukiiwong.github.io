"""Validate the two-page academic CV; visual review is still required.

Run after build_cv.py. Requires pypdf and pdfplumber.
"""
import argparse
import json
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--lang', choices=('en', 'zh'), default='en')
args = parser.parse_args()
CHINESE = args.lang == 'zh'
path = ROOT / ('cv/Yukai_Wang_CV_CN.pdf' if CHINESE else 'cv/Yukai_Wang_CV.pdf')
reader = PdfReader(path)
assert len(reader.pages) == 2, 'CV must remain two pages'


def normalized(text):
    return ' '.join(text.replace('\u2013', '-').replace('\u2014', '-').split())


text = normalized(' '.join(page.extract_text() for page in reader.pages))
expected_headings = ('王于凯', '博士候选人', '教育背景', '研究经历', '学术成果与投稿',
                    '已发表期刊论文', '会议成果', '在投论文', '荣誉与奖励', '专业技能') if CHINESE else ('PhD Candidate', 'Research Experience', 'Publications and Manuscripts',
                 'Journal Article', 'Conference Contributions', 'Manuscripts Under Review',
                 'Selected Honors and Awards', 'Technical Skills')
for expected in expected_headings:
    assert expected in text, f'Missing expected heading or identity: {expected}'
for outdated in ('PhD student', 'ICML', 'NeurIPS', 'Rejected', 'Withdrawn', 'unsuccessful'):
    assert outdated not in text, f'Outdated public status: {outdated}'
assert text.count('进行中' if CHINESE else 'Ongoing') == 2, 'Ongoing work must be consolidated into two research themes'
for theme in (('交通世界模型与数字孪生', '决策效用与安全评估') if CHINESE else ('Traffic world models and digital twins', 'Decision utility and safety assessment')):
    assert theme in text, f'Missing consolidated research theme: {theme}'
cv = json.loads((ROOT / ('_data/cv_zh.json' if CHINESE else '_data/cv.json')).read_text())
research = json.loads((ROOT / '_data/research.json').read_text())
covered_projects = []
for group in cv['research_groups']:
    for item in group['items']:
        covered_projects.extend([item['project']] + item.get('related_projects', []))
assert sorted(covered_projects) == sorted(item['id'] for item in research), 'Research coverage must be preserved without duplication'
assert text.count('Under review') == (4 if CHINESE else 7), 'Current submission statuses must be retained'
if CHINESE:
    assert text.count('在投，') == 3, 'Three related research entries must retain their review status'
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
    expected_fonts = ('STSongti-SC-Regular-6', 'STSongti-SC-Bold-1', 'LiberationSerif', 'LiberationSerif-Bold', 'LiberationSerif-Italic') if CHINESE else ('LiberationSerif', 'LiberationSerif-Bold', 'LiberationSerif-Italic', 'LiberationSerif-BoldItalic')
    for face in expected_fonts:
        assert any(name.endswith(face) for name in used_fonts), f'Missing font face: {face}'

for page in reader.pages:
    for font in page['/Resources']['/Font'].values():
        font = font.get_object()
        if any(name in font['/BaseFont'] for name in ('LiberationSerif', 'STSongti')):
            assert '/FontFile2' in font['/FontDescriptor'], 'Serif font must be embedded'

print('PASS: two pages, content/status preservation, nested headings, embedded typefaces, and page bounds.')
