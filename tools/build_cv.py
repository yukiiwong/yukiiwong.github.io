"""Build a two-page academic CV with a reference-inspired typographic hierarchy.

Requires reportlab and Liberation Serif. Set CV_FONT_DIR if the font family is
not in one of the standard Linux or Codex runtime locations below.
"""
import argparse
import json
import os
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--lang', choices=('en', 'zh'), default='en')
args = parser.parse_args()
CHINESE = args.lang == 'zh'


def data(name):
    return json.loads((ROOT / f'_data/{name}.json').read_text())


profile = data('profile')
projects = {item['id']: item for item in data('research')}
publications = data('publications')
submissions = data('submissions')
cv = data('cv_zh' if CHINESE else 'cv')
OUT = ROOT / ('cv/Yukai_Wang_CV_CN.pdf' if CHINESE else 'cv/Yukai_Wang_CV.pdf')
OUT.parent.mkdir(exist_ok=True)

font_dirs = [
    Path(os.environ['CV_FONT_DIR']) if os.environ.get('CV_FONT_DIR') else None,
    Path('/usr/share/fonts/truetype/liberation2'),
    Path('/usr/share/fonts/truetype/liberation'),
    Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/'
    'libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype',
]
font_dir = next((p for p in font_dirs if p and (p / 'LiberationSerif-Regular.ttf').is_file()), None)
if font_dir is None:
    raise RuntimeError('Liberation Serif not found. Set CV_FONT_DIR to its font directory.')
for suffix, filename in (
    ('', 'Regular'), ('-Bold', 'Bold'), ('-Italic', 'Italic'), ('-BoldItalic', 'BoldItalic'),
):
    pdfmetrics.registerFont(TTFont('CVSerif' + suffix, str(font_dir / f'LiberationSerif-{filename}.ttf')))
pdfmetrics.registerFontFamily('CVSerif', normal='CVSerif', bold='CVSerif-Bold',
                            italic='CVSerif-Italic', boldItalic='CVSerif-BoldItalic')

TEXT_FONT = 'CVSerif'
if CHINESE:
    chinese_font = Path(os.environ.get('CV_CJK_FONT', '/System/Library/Fonts/Supplemental/Songti.ttc'))
    if not chinese_font.is_file():
        raise RuntimeError('Songti font collection not found. Set CV_CJK_FONT to Songti.ttc.')
    pdfmetrics.registerFont(TTFont('CVSong', str(chinese_font), subfontIndex=6))
    pdfmetrics.registerFont(TTFont('CVSong-Bold', str(chinese_font), subfontIndex=1))
    pdfmetrics.registerFontFamily('CVSong', normal='CVSong', bold='CVSong-Bold',
                                 italic='CVSong', boldItalic='CVSong-Bold')
    TEXT_FONT = 'CVSong'

ZH_HEADINGS = {
    'Education': '教育背景', 'Research Interests': '研究方向',
    'Research Experience': '研究经历', 'Industry Experience': '实习经历',
    'Publications and Manuscripts': '学术成果与投稿', 'Journal Article': '已发表期刊论文',
    'Conference Contributions': '会议成果', 'Manuscripts Under Review': '在投论文',
    'Selected Honors and Awards': '荣誉与奖励', 'Technical Skills': '专业技能',
}


def localized_heading(text):
    return ZH_HEADINGS.get(text, text) if CHINESE else text

INK = colors.HexColor('#111111')
MUTED = colors.HexColor('#555555')
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 50
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
body = ParagraphStyle('body', fontName=TEXT_FONT, fontSize=10.6, leading=16 if CHINESE else 12.7,
                      textColor=INK, spaceAfter=3, allowWidows=0, allowOrphans=0,
                      wordWrap='CJK' if CHINESE else None)
styles = {
    'body': body,
    'name': ParagraphStyle('name', parent=body, fontName=TEXT_FONT + '-Bold', fontSize=27,
                           leading=31, alignment=TA_CENTER, spaceAfter=4),
    'contact': ParagraphStyle('contact', parent=body, alignment=TA_CENTER,
                              fontSize=10.1, leading=12.2, spaceAfter=2),
    'section': ParagraphStyle('section', parent=body, fontName=TEXT_FONT + '-Bold',
                              fontSize=14, leading=17, spaceBefore=10, spaceAfter=8,
                              keepWithNext=True),
    'subsection': ParagraphStyle('subsection', parent=body, fontName=TEXT_FONT + '-Bold',
                                 fontSize=11.6, leading=14, spaceBefore=5, spaceAfter=4,
                                 keepWithNext=True),
    'theme': ParagraphStyle('theme', parent=body, fontName='CVSong-Bold' if CHINESE else 'CVSerif-BoldItalic',
                            fontSize=11.2 if CHINESE else 10.8, leading=15 if CHINESE else 13, spaceBefore=4, spaceAfter=3,
                            keepWithNext=True),
    'date': ParagraphStyle('date', parent=body, alignment=TA_RIGHT),
    'bullet': ParagraphStyle('bullet', parent=body, leftIndent=10, firstLineIndent=0,
                             bulletIndent=0, bulletFontName='CVSerif', bulletFontSize=9,
                             spaceAfter=2.5),
    'reference': ParagraphStyle('reference', parent=body, fontName='CVSerif', leading=12.7, wordWrap=None, leftIndent=16,
                                firstLineIndent=0, bulletIndent=0, bulletFontName='CVSerif',
                                bulletFontSize=10.6, spaceAfter=5),
    'note': ParagraphStyle('note', parent=body, fontSize=9.5, leading=11.5,
                           textColor=MUTED, spaceAfter=3),
}
if CHINESE:
    # Reserve one em for CJK closing punctuation, which ReportLab may hang.
    styles['body'].rightIndent = body.fontSize
    styles['bullet'].rightIndent = body.fontSize


def plain(value):
    return escape(str(value).replace('\u2013', '-').replace('\u2014', '-')
                  .replace('\u2011', '-').replace('\u00a0', ' '))


def p(text, kind='body', **kwargs):
    return Paragraph(text, styles[kind], **kwargs)


class RuledHeading(Paragraph):
    """A primary heading with a thin black rule, following the supplied reference."""
    def draw(self):
        super().draw()
        self.canv.setStrokeColor(INK)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, -3, self.width, -3)


def heading(text, level=0):
    text = localized_heading(text)
    result = RuledHeading(plain(text), styles['section']) if level == 0 else p(plain(text), 'subsection')
    result.outline_title = text
    result.outline_level = level
    return result


def dated_row(text, dates, *, date_width=104):
    row = Table([[p(text), p(plain(dates), 'date')]],
                colWidths=[CONTENT_WIDTH - date_width, date_width], hAlign='LEFT')
    row.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (0, -1), 8),
        ('RIGHTPADDING', (1, 0), (1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    return row


def bullet(text):
    return p(text, 'bullet', bulletText='\u2022')


def author_list(text):
    """Abbreviate only the verified author names, preserving their order."""
    names = text.replace(', and ', ', ').split(', ')
    result = []
    for name in names:
        parts = name.split()
        formatted = plain(parts[-1] + ', ' + ' '.join(part[0] + '.' for part in parts[:-1]))
        result.append('<b>' + formatted + '</b>' if name == profile['name'] else formatted)
    return ', '.join(result[:-1]) + ', &amp; ' + result[-1] if len(result) > 1 else result[0]


def reference(item, number, *, submitted=False):
    text = author_list(item['authors']) + ' ' if item.get('authors') else ''
    if item.get('year'):
        text += '(' + str(item['year']) + '). '
    text += plain(item['title']) + '. <i>' + plain(item['venue']) + '</i>.'
    if submitted:
        text += ' <b>(' + plain(item['status']) + ')</b>.'
    elif item['kind'] == 'journal':
        text += '<br/><link href="' + escape(item['url']) + '">' + plain(item['url']) + '</link>'
    else:
        text += ' <link href="' + escape(item['url']) + '">[Record]</link>'
    return p(text, 'reference', bulletText=f'{number}.')


class CVDocument(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, 'outline_title'):
            key = 'heading-' + str(self.seq.nextf('outline'))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.outline_title, key, level=flowable.outline_level)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(MUTED)
    canvas.setFont(TEXT_FONT, 8.5)
    footer_text = (cv['name'] + ' | 个人简历 | ' + cv['updated']) if CHINESE else ('Yukai Wang | Curriculum Vitae | ' + submissions['updated'])
    canvas.drawString(MARGIN, 27, footer_text)
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 27, str(doc.page))
    canvas.restoreState()


story = [
    p(plain(cv['name'] if CHINESE else profile['name']), 'name'),
    p(plain(cv['role'] + ' | ' + cv['institution'] if CHINESE else profile['role'] + ' | KAIST'), 'contact'),
    p('<link href="mailto:' + profile['email'] + '">' + plain(profile['email']) + '</link> | '
      '<link href="' + profile['website'] + '">yukiiwong.github.io</link> | '
      '<link href="' + profile['github'] + '">GitHub</link>', 'contact'),
    Spacer(1, 3), heading('Education'),
]
for index, original_entry in enumerate(profile['education']):
    entry = {**original_entry, **cv['education'][index]} if CHINESE else original_entry
    institution = 'KAIST' if 'KAIST' in entry['institution'] else entry['institution']
    if CHINESE:
        institution = entry['institution']
    details = [dated_row('<b>' + plain(institution) + '</b>' + ('，' if CHINESE else ', ') + plain(entry['degree']), entry['dates'].replace('present', '至今') if CHINESE else entry['dates']),
               bullet(plain(entry['department']) +
                      (('；<b>导师：</b>' + plain(entry['advisor']) + ' 教授' if CHINESE else '; <b>Advisor:</b> Prof. ' + plain(entry['advisor'])) if entry.get('advisor') else ''))]
    if entry.get('note'):
        details.append(bullet(plain(entry['note'])))
    story += [KeepTogether(details), Spacer(1, 3)]

story += [heading('Research Interests'), p(plain(cv['research_interests'])),
          heading('Research Experience'),
          dated_row('<b>' + ('博士阶段研究，KAIST' if CHINESE else 'Doctoral Research, KAIST') + '</b>', profile['education'][0]['dates'].replace('present', '至今') if CHINESE else profile['education'][0]['dates'])]
for group in cv['research_groups']:
    story.append(p(plain(group['heading']), 'theme'))
    for item in group['items']:
        project = projects[item['project']]
        for related in item.get('related_projects', []):
            if projects[related]['status'] != project['status']:
                raise ValueError('Split grouped CV research when project statuses differ: ' + item['label'])
        status = project['status'].split(' · Earlier')[0].replace(' · ', ', ')
        if CHINESE:
            status = status.replace('Ongoing', '进行中').replace('Under review, ', '在投，')
        story.append(bullet('<b>' + plain(item['label']) + ('。</b>' if CHINESE else '.</b> ') + plain(item['text']) +
                            ('（' + plain(status) + '）' if CHINESE else ' <i>(' + plain(status) + ')</i>')))
industry = cv['industry'] if CHINESE else profile['industry']
story += [Spacer(1, 5),
          KeepTogether([
              dated_row('<b>' + ('硕士阶段研究，东南大学' if CHINESE else 'Graduate Research, Southeast University') + '</b>', profile['education'][1]['dates']),
              bullet(plain(cv['graduate_research'])),
          ]),
          heading('Industry Experience'),
          KeepTogether([
              dated_row('<b>' + plain(industry['role']) + ('，' if CHINESE else ', ') + plain(industry['company']) +
                        '</b>', industry['dates'], date_width=115),
              bullet(plain(industry['department'])),
          ]),
          PageBreak(), heading('Publications and Manuscripts'),
          heading('Journal Article', 1)]
for number, item in enumerate((p for p in publications if p['kind'] == 'journal'), 1):
    story.append(reference(item, number))
story.append(heading('Conference Contributions', 1))
for number, item in enumerate((p for p in publications if p['kind'] == 'conference'), 1):
    story.append(reference(item, number))
story.append(heading('Manuscripts Under Review', 1))
for number, item in enumerate(submissions['under_review'], 1):
    story.append(reference(item, number, submitted=True))
story.append(heading('Selected Honors and Awards'))
for index, original_award in enumerate(profile['awards']):
    award = {**original_award, **cv['awards'][index]} if CHINESE else original_award
    story += [dated_row('<b>' + plain(award['title']) + '</b>' + ('，' if CHINESE else ', ') + plain(award['event']) + ('。' if CHINESE else '.'),
                        str(award['year']), date_width=40), Spacer(1, 3)]
story.append(heading('Technical Skills'))
for item in cv['skills']:
    story.append(p('<b>' + plain(item['label']) + ('：</b>' if CHINESE else ':</b> ') + plain(item['text'])))

doc = CVDocument(str(OUT), pagesize=letter, rightMargin=MARGIN - 6, leftMargin=MARGIN - 6,
                 topMargin=42, bottomMargin=43, title='王于凯 - 中文个人简历' if CHINESE else 'Yukai Wang - Curriculum Vitae',
                 author=profile['name'], subject='Academic CV: education, research, publications, and experience')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
