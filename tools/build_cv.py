"""Build a two-page academic CV with a reference-inspired typographic hierarchy.

Requires reportlab and Liberation Serif. Set CV_FONT_DIR if the font family is
not in one of the standard Linux or Codex runtime locations below.
"""
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


def data(name):
    return json.loads((ROOT / f'_data/{name}.json').read_text())


profile = data('profile')
projects = {item['id']: item for item in data('research')}
publications = data('publications')
submissions = data('submissions')
cv = data('cv')
OUT = ROOT / 'cv/Yukai_Wang_CV.pdf'
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

INK = colors.HexColor('#111111')
MUTED = colors.HexColor('#555555')
PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN = 50
CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN
body = ParagraphStyle('body', fontName='CVSerif', fontSize=10.6, leading=12.7,
                      textColor=INK, spaceAfter=3, allowWidows=0, allowOrphans=0)
styles = {
    'body': body,
    'name': ParagraphStyle('name', parent=body, fontName='CVSerif-Bold', fontSize=27,
                           leading=31, alignment=TA_CENTER, spaceAfter=4),
    'contact': ParagraphStyle('contact', parent=body, alignment=TA_CENTER,
                              fontSize=10.1, leading=12.2, spaceAfter=2),
    'section': ParagraphStyle('section', parent=body, fontName='CVSerif-Bold',
                              fontSize=14, leading=17, spaceBefore=10, spaceAfter=8,
                              keepWithNext=True),
    'subsection': ParagraphStyle('subsection', parent=body, fontName='CVSerif-Bold',
                                 fontSize=11.6, leading=14, spaceBefore=5, spaceAfter=4,
                                 keepWithNext=True),
    'theme': ParagraphStyle('theme', parent=body, fontName='CVSerif-BoldItalic',
                            fontSize=10.8, leading=13, spaceBefore=4, spaceAfter=3,
                            keepWithNext=True),
    'date': ParagraphStyle('date', parent=body, alignment=TA_RIGHT),
    'bullet': ParagraphStyle('bullet', parent=body, leftIndent=10, firstLineIndent=0,
                             bulletIndent=0, bulletFontName='CVSerif', bulletFontSize=9,
                             spaceAfter=2.5),
    'reference': ParagraphStyle('reference', parent=body, leftIndent=16,
                                firstLineIndent=0, bulletIndent=0, bulletFontName='CVSerif',
                                bulletFontSize=10.6, spaceAfter=5),
    'note': ParagraphStyle('note', parent=body, fontSize=9.5, leading=11.5,
                           textColor=MUTED, spaceAfter=3),
}


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
    canvas.setFont('CVSerif', 8.5)
    canvas.drawString(MARGIN, 27, 'Yukai Wang | Curriculum Vitae | ' + submissions['updated'])
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 27, str(doc.page))
    canvas.restoreState()


story = [
    p(plain(profile['name']), 'name'),
    p(plain(profile['role']) + ' | KAIST', 'contact'),
    p('<link href="mailto:' + profile['email'] + '">' + plain(profile['email']) + '</link> | '
      '<link href="' + profile['website'] + '">yukiiwong.github.io</link> | '
      '<link href="' + profile['github'] + '">GitHub</link>', 'contact'),
    Spacer(1, 3), heading('Education'),
]
for entry in profile['education']:
    institution = 'KAIST' if 'KAIST' in entry['institution'] else entry['institution']
    details = [dated_row('<b>' + plain(institution) + '</b>, ' + plain(entry['degree']), entry['dates']),
               bullet(plain(entry['department']) +
                      ('; <b>Advisor:</b> Prof. ' + plain(entry['advisor']) if entry.get('advisor') else ''))]
    if entry.get('note'):
        details.append(bullet(plain(entry['note'])))
    story += [KeepTogether(details), Spacer(1, 3)]

story += [heading('Research Interests'), p(plain(cv['research_interests'])),
          heading('Research Experience'),
          dated_row('<b>Doctoral Research, KAIST</b>', profile['education'][0]['dates'])]
for group in cv['research_groups']:
    story.append(p(plain(group['heading']), 'theme'))
    for item in group['items']:
        project = projects[item['project']]
        for related in item.get('related_projects', []):
            if projects[related]['status'] != project['status']:
                raise ValueError('Split grouped CV research when project statuses differ: ' + item['label'])
        status = project['status'].split(' · Earlier')[0].replace(' · ', ', ')
        story.append(bullet('<b>' + plain(item['label']) + '.</b> ' + plain(item['text']) +
                            ' <i>(' + plain(status) + ')</i>'))
story += [Spacer(1, 5),
          KeepTogether([
              dated_row('<b>Graduate Research, Southeast University</b>', profile['education'][1]['dates']),
              bullet(plain(cv['graduate_research'])),
          ]),
          heading('Industry Experience'),
          KeepTogether([
              dated_row('<b>' + plain(profile['industry']['role']) + ', ' + plain(profile['industry']['company']) +
                        '</b>', profile['industry']['dates'], date_width=115),
              bullet(plain(profile['industry']['department'])),
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
for award in profile['awards']:
    story += [dated_row('<b>' + plain(award['title']) + '</b>, ' + plain(award['event']) + '.',
                        str(award['year']), date_width=40), Spacer(1, 3)]
story.append(heading('Technical Skills'))
for item in cv['skills']:
    story.append(p('<b>' + plain(item['label']) + ':</b> ' + plain(item['text'])))

doc = CVDocument(str(OUT), pagesize=letter, rightMargin=MARGIN - 6, leftMargin=MARGIN - 6,
                 topMargin=42, bottomMargin=43, title='Yukai Wang - Curriculum Vitae',
                 author=profile['name'], subject='Academic CV: education, research, publications, and experience')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
