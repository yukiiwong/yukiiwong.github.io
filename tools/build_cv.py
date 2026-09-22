"""Build the three-page research CV from shared website data."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
profile = json.loads((ROOT / '_data/profile.json').read_text())
projects = json.loads((ROOT / '_data/research.json').read_text())
publications = json.loads((ROOT / '_data/publications.json').read_text())
submissions = json.loads((ROOT / '_data/submissions.json').read_text())
research_story = json.loads((ROOT / '_data/research_story.json').read_text())
project_by_id = {item['id']: item for item in projects}
OUT = ROOT / 'cv/Yukai_Wang_CV.pdf'
OUT.parent.mkdir(exist_ok=True)
INK, MUTED, ACCENT = colors.HexColor('#182b2a'), colors.HexColor('#546461'), colors.HexColor('#16745f')
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=25, leading=30, textColor=INK, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.3, leading=12.6, textColor=INK, spaceAfter=5),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.3, leading=11.3, textColor=MUTED, spaceAfter=5),
    'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=11.4, leading=15, textColor=ACCENT, spaceBefore=10, spaceAfter=6),
    'item': ParagraphStyle('item', fontName='Helvetica-Bold', fontSize=9.8, leading=13.1, textColor=INK, spaceAfter=3),
}

def plain(value):
    return escape(str(value).replace('\u2013', '-').replace('\u2014', '-').replace('\u2011', '-'))

def p(text, kind='body'):
    return Paragraph(text, styles[kind])

def heading(text):
    return p(plain(text).upper(), 'heading')

def project_item(item):
    return KeepTogether([
        p(plain(item['title']), 'item'),
        p(plain(item['status']), 'small'),
        p(plain(item['cv'])),
        Spacer(1, 4),
    ])

def submission_item(item):
    details = [
        p(plain(item['title']), 'item'),
        p('<b>' + plain(item['status']) + '</b> | ' + plain(item['venue']), 'body'),
    ]
    if item.get('authors'):
        details.append(p(plain(item['authors']).replace('Yukai Wang', '<b>Yukai Wang</b>'), 'small'))
    details += [p(plain(item['note']), 'small'), Spacer(1, 5)]
    return KeepTogether(details)

def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(colors.HexColor('#cedbd6'))
    canvas.line(46, 39, w-46, 39)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(46, 26, 'Yukai Wang | Curriculum vitae | ' + submissions['updated'])
    canvas.drawRightString(w-46, 26, str(doc.page))
    canvas.restoreState()

story = [
    p('YUKAI WANG', 'name'),
    p('PhD student | Cho Chun Shik Graduate School of Mobility | KAIST', 'body'),
    p('<link href="mailto:yukai@kaist.ac.kr" color="#16745f">yukai@kaist.ac.kr</link>  |  '
      '<link href="https://yukiiwong.github.io" color="#16745f">yukiiwong.github.io</link>  |  '
      '<link href="https://github.com/yukiiwong" color="#16745f">GitHub: yukiiwong</link>', 'small'),
    heading('Research profile'),
    p(plain(research_story['cv_profile'])),
    heading('Education'),
]
for e in profile['education']:
    story.append(KeepTogether([
        p(plain(e['degree']) + ' | ' + plain(e['dates']), 'item'),
        p(plain(e['institution']) + '<br/>' + plain(e['department']) +
          (' | Advisor: Prof. ' + plain(e['advisor']) if e.get('advisor') else ''), 'body'),
        Spacer(1, 3),
    ]))
story += [heading('Doctoral research | KAIST, 2023-present')]
for key in ['drone-world-models', 'rollout-diagnostics', 'missing-history', 'prosafeav']:
    story.append(project_item(project_by_id[key]))
story += [PageBreak(), p('YUKAI WANG | PUBLICATIONS AND CURRENT SUBMISSIONS', 'item')]
story.append(heading('Journal publication'))
for item in publications:
    if item['kind'] != 'journal':
        continue
    authors = plain(item['authors']).replace('Yukai Wang', '<b>Yukai Wang</b>')
    story.append(p(authors + ' (' + str(item['year']) + '). ' + plain(item['title']) + '. '
                   '<i>' + plain(item['venue']) + '</i>. '
                   '<link href="'+item['url']+'" color="#16745f">doi:10.1016/j.multra.2024.100137</link>'))
story.append(heading('Conference contributions'))
for item in publications:
    if item['kind'] != 'conference':
        continue
    authors = plain(item['authors']).replace('Yukai Wang', '<b>Yukai Wang</b>')
    story.append(KeepTogether([p(authors + '. ' + plain(item['title']) + '. '
        '<i>' + plain(item['venue']) + '</i>. '
        '<link href="'+escape(item['url'])+'" color="#16745f">[Record]</link>'), Spacer(1, 3)]))
story.append(heading('Manuscripts under review'))
story.append(p('Status as of ' + plain(submissions['updated']) + '. These manuscripts are not accepted publications.', 'small'))
for item in submissions['under_review']:
    story.append(submission_item(item))
story.append(p('Current submissions, earlier attempts, and working drafts are listed separately. '
               'The AAAI entries concern two distinct studies; the candidate-ranking manuscript '
               'remains ongoing work rather than a listed submission.', 'small'))

story += [PageBreak(), p('YUKAI WANG | RESEARCH DEVELOPMENT AND EXPERIENCE', 'item'),
          heading('Earlier submissions'),
          p('A record of earlier unsuccessful attempts, separate from publications and current review. '
            'NeurIPS was withdrawn after review, not formally rejected.', 'small')]
for item in submissions['previous']:
    story.append(submission_item(item))
story.append(heading('Additional ongoing research'))
for key in ['decision-utility', 'surrogate-safety', 'digital-twins']:
    item = project_by_id[key]
    story.append(KeepTogether([p(plain(item['title']), 'item'), p(plain(item['cv']), 'small'), Spacer(1, 3)]))
story.append(heading('Industry experience'))
i = profile['industry']
story.append(p('<b>'+plain(i['role'])+' | '+plain(i['company'])+'</b> | '+plain(i['dates'])+'<br/>'+plain(i['department'])))
story.append(heading('Selected awards'))
for a in profile['awards']:
    story.append(p('<b>'+str(a['year'])+' | '+plain(a['title'])+'</b>. '+plain(a['event'])+'.', 'small'))
story.append(heading('Methods and tools'))
story.append(p('Graph neural networks; recurrent state-space models; neural ODEs; autoregressive models; '
               'reinforcement learning; surrogate safety measures; extreme value theory; '
               'recording-disjoint evaluation and bootstrap diagnostics. Python, PyTorch / PyTorch Lightning, '
               'CARLA-based simulation, Git, and LaTeX.', 'small'))
story.append(Spacer(1, 5))
story.append(p('My research agenda extends world models from ego-vehicle control toward site-level traffic '
               'understanding, safety screening, and digital-twin evaluation. These are research goals, '
               'not claims of validated real-world intervention effects. Research story and figures: '
               '<link href="https://yukiiwong.github.io/research/" color="#16745f">yukiiwong.github.io/research/</link>.', 'small'))

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=46, leftMargin=46, topMargin=42,
                        bottomMargin=52, title='Yukai Wang - Curriculum Vitae', author='Yukai Wang')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
