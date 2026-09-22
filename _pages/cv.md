---
title: "CV"
layout: gridlay
permalink: /cv/
---
<p class="eyebrow">Curriculum vitae · September 2026</p>

# Yukai Wang

<div class="cv-preview"><p>A concise overview of my education, research experience, published and conference work, industry experience, and selected awards.</p><a class="button-primary" href="{{ '/cv/Yukai_Wang_CV.pdf' | relative_url }}">Download CV (PDF)</a></div>

## Research profile

PhD student at KAIST studying traffic world models, multi-agent trajectory learning, reinforcement learning, and traffic safety. My recent work explores how models learned from drone trajectories behave in self-conditioned rollout, and whether their predictions support useful decisions.

## Education

{% for entry in site.data.profile.education %}
<div class="timeline-entry"><div class="timeline-date">{{ entry.dates }}</div><div><h3>{{ entry.degree }}</h3><p>{{ entry.institution }}<br/>{{ entry.department }}</p>{% if entry.advisor %}<p class="muted">Advisor: Prof. {{ entry.advisor }}</p>{% endif %}</div></div>
{% endfor %}

## Research and experience

- [Current research projects and visual demonstrations]({{ '/research/' | relative_url }})
- [Journal article and conference contributions]({{ '/publications/' | relative_url }})
- [Industry experience and selected awards]({{ '/about/' | relative_url }})

Working manuscripts and ongoing studies are distinguished from published articles and conference records throughout the CV.

Contact: [yukai@kaist.ac.kr](mailto:yukai@kaist.ac.kr).
