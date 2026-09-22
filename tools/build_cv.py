"""Build the two-page CV from the same verified data used by the website."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
profile = json.loads((ROOT / '_data/profile.json').read_text())
projects = json.loads((ROOT / '_data/research.json').read_text())
publications = json.loads((ROOT / '_data/publications.json').read_text())
OUT = ROOT / 'cv/Yukai_Wang_CV.pdf'
OUT.parent.mkdir(exist_ok=True)
INK, MUTED, ACCENT = colors.HexColor('#182b2a'), colors.HexColor('#546461'), colors.HexColor('#16745f')
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=25, leading=30, textColor=INK, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, leading=13.1, textColor=INK, spaceAfter=5),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.3, leading=11.3, textColor=MUTED, spaceAfter=5),
    'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=11.4, leading=15, textColor=ACCENT, spaceBefore=13, spaceAfter=7),
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

def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(colors.HexColor('#cedbd6'))
    canvas.line(46, 39, w-46, 39)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(46, 26, 'Yukai Wang | Curriculum vitae | September 2026')
    canvas.drawRightString(w-46, 26, str(doc.page))
    canvas.restoreState()

story = [
    p('YUKAI WANG', 'name'),
    p('PhD student | Cho Chun Shik Graduate School of Mobility | KAIST', 'body'),
    p('<link href="mailto:yukai@kaist.ac.kr" color="#16745f">yukai@kaist.ac.kr</link>  |  '
      '<link href="https://yukiiwong.github.io" color="#16745f">yukiiwong.github.io</link>  |  '
      '<link href="https://github.com/yukiiwong" color="#16745f">GitHub: yukiiwong</link>', 'small'),
    heading('Research profile'),
    p('Traffic world models, multi-agent trajectory learning, and safety assessment. '
      'My research uses drone-recorded trajectories to study interaction dynamics, '
      'self-conditioned rollout, and the relationship between predictive accuracy and decision usefulness.'),
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
for item in projects[:4]:
    story.append(project_item(item))
story += [PageBreak(), p('YUKAI WANG', 'item'), heading('Additional ongoing research')]
for item in projects[4:]:
    story.append(project_item(item))
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
story.append(Spacer(1, 8))
story.append(p('Working manuscripts and ongoing studies are listed as research experience, separately from '
               'published articles and conference records. Project figures and current descriptions: '
               '<link href="https://yukiiwong.github.io/research/" color="#16745f">yukiiwong.github.io/research/</link>.', 'small'))

doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=46, leftMargin=46, topMargin=42,
                        bottomMargin=52, title='Yukai Wang - Curriculum Vitae', author='Yukai Wang')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
