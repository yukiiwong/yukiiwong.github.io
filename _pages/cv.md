---
title: "CV"
layout: gridlay
permalink: /cv/
---
<p class="eyebrow">Curriculum vitae · September 2026</p>

# Yukai Wang

**{{ site.data.profile.role }} · KAIST**

<div class="cv-preview"><p>A two-page academic CV covering education, research interests and experience, publications, manuscripts under review, selected awards, and technical skills. Available in English and Chinese; paper titles and bibliographic details remain in English. Updated {{ site.data.submissions.updated }}.</p><div class="action-links"><a class="button-primary" href="{{ '/cv/Yukai_Wang_CV.pdf' | relative_url }}">English CV (PDF)</a><a class="button-secondary" href="{{ '/cv/Yukai_Wang_CV_CN.pdf' | relative_url }}" lang="zh-CN">中文简历（PDF）</a></div></div>

## Research profile

{{ site.data.research_story.cv_profile }}

## Education

{% for entry in site.data.profile.education %}
<div class="timeline-entry"><div class="timeline-date">{{ entry.dates }}</div><div><h3>{{ entry.degree }}</h3><p>{{ entry.institution }}<br/>{{ entry.department }}</p>{% if entry.advisor %}<p class="muted">Advisor: Prof. {{ entry.advisor }}</p>{% endif %}</div></div>
{% endfor %}

## Research and experience

- [Current research projects and visual demonstrations]({{ '/research/' | relative_url }})
- [Why I study drone data and traffic world models]({{ '/research/' | relative_url }}#research-story)
- [Journal article and conference contributions]({{ '/publications/' | relative_url }})
- [Manuscripts under review: AMAR, T-ITS, and AAAI 2027]({{ '/publications/' | relative_url }}#under-review)
- [Ongoing research]({{ '/publications/' | relative_url }}#ongoing-research)
- [Industry experience and selected awards]({{ '/about/' | relative_url }})

The PDF and website use the same research record, with published work, manuscripts under review, and ongoing projects clearly separated.

Contact: [yukai@kaist.ac.kr](mailto:yukai@kaist.ac.kr).
