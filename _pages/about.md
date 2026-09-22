---
title: "About"
layout: gridlay
permalink: /about/
---
<p class="eyebrow">Background &amp; experience</p>

# About me

I am **Yukai Wang (王于凯)**, a PhD student at KAIST's Cho Chun Shik Graduate School of Mobility. My research combines traffic modeling, machine learning, and safety analysis, with a current focus on learning and evaluating multi-agent traffic world models from drone trajectory data.

I am advised by [Prof. Tiantian Chen](https://sites.google.com/view/chentiantian/home) and work in the [Human Factors Centered Transport Safety Laboratory](https://human-facts.kaist.ac.kr/). My earlier work at Southeast University, advised by Prof. Zhiyuan Liu, focused on transportation and learning-based decision methods.

## Education

{% for entry in site.data.profile.education %}
<div class="timeline-entry"><div class="timeline-date">{{ entry.dates }}</div><div><h3>{{ entry.degree }} · {{ entry.institution }}</h3><p>{{ entry.department }}</p>{% if entry.advisor %}<p class="muted">Advisor: Prof. {{ entry.advisor }}</p>{% endif %}{% if entry.note %}<p class="muted">{{ entry.note }}</p>{% endif %}</div></div>
{% endfor %}

## Research experience

**Doctoral research, KAIST · 2023–present.** Multi-agent trajectory learning and traffic world models; closed-loop evaluation and rollout diagnostics; world-model reinforcement learning; traffic-conflict and extreme-value methods. See [Research]({{ '/research/' | relative_url }}) for project descriptions, figures, and current status.

**Graduate research, Southeast University · 2020–2023.** Transportation research with Prof. Zhiyuan Liu. Related collaborative work on deep reinforcement learning for joint travel-mode and departure-time choice appeared in *Multimodal Transportation* in 2024.

## Industry experience

<div class="timeline-entry"><div class="timeline-date">{{ site.data.profile.industry.dates }}</div><div><h3>{{ site.data.profile.industry.role }} · {{ site.data.profile.industry.company }}</h3><p>{{ site.data.profile.industry.department }}</p></div></div>

## Selected awards

{% for award in site.data.profile.awards %}
<div class="timeline-entry"><div class="timeline-date">{{ award.year }}</div><div><h3>{{ award.title }}</h3><p>{{ award.event }}</p></div></div>
{% endfor %}

## Research methods and tools

Graph neural networks; recurrent state-space models; neural ODEs; autoregressive trajectory models; reinforcement learning; surrogate safety measures; extreme value theory; recording-disjoint evaluation and bootstrap diagnostics. Implementation experience includes Python, PyTorch / PyTorch Lightning, CARLA-based simulation, Git, and LaTeX.

<div class="action-links"><a class="button-primary" href="{{ '/cv/Yukai_Wang_CV.pdf' | relative_url }}">Download CV</a><a class="button-secondary" href="mailto:yukai@kaist.ac.kr">Get in touch</a></div>
