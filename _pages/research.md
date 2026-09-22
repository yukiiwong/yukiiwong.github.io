---
title: "Research"
layout: gridlay
permalink: /research/
---
<p class="eyebrow">Research overview · September 2026</p>

# Learning traffic dynamics, evaluating their usefulness

My work connects **drone trajectory data**, **multi-agent world models**, and **traffic safety**. I am interested in both building predictive models and understanding what their predictions justify: a plausible trajectory, a stable rollout, a useful action ranking, or a defensible safety diagnostic.

<nav class="project-index" aria-label="Research projects">{% for project in site.data.research %}<a href="#{{ project.id }}">{{ forloop.index | prepend: '0' }} · {{ project.title }}</a>{% endfor %}</nav>

<p class="intro-note">Projects below include ongoing work and working manuscripts. Their labels describe research status; they do not imply journal acceptance.</p>

{% for project in site.data.research %}
<article class="research-detail" id="{{ project.id }}">
  <p class="project-status">{{ project.status }}</p>
  <h2>{{ project.title }}</h2>
  <p class="project-tags">{{ project.tags | join: ' · ' }}</p>
  <p>{{ project.description }}</p>
  <p><strong>Research focus.</strong> {{ project.contribution }}</p>
  {% if project.image %}
  <figure class="project-figure {{ project.figure_class }} {% if project.id == 'drone-world-models' %}trajectory-figure{% endif %}">
    <a href="{{ '/images/research/' | append: project.image | relative_url }}" aria-label="Open full-size figure for {{ project.title | escape }}"><img src="{{ '/images/research/' | append: project.image | relative_url }}" alt="{{ project.alt | escape }}" loading="lazy" /></a>
    <figcaption>{{ project.caption }}{% if project.id == 'drone-world-models' %} <a href="https://levelxdata.com/ind-dataset/">Dataset information</a>.{% endif %} Click the figure to view it at full size.</figcaption>
  </figure>
  {% endif %}
  {% if project.secondary_image %}
  <details class="framework-detail"><summary>{{ project.secondary_summary | default: 'View the model architecture' }}</summary><figure class="project-figure {{ project.figure_class }}"><a href="{{ '/images/research/' | append: project.secondary_image | relative_url }}" aria-label="Open supporting figure for {{ project.title | escape }}"><img src="{{ '/images/research/' | append: project.secondary_image | relative_url }}" alt="{{ project.secondary_alt | escape }}" loading="lazy" /></a><figcaption>{{ project.secondary_caption }} Click the figure to view it at full size.</figcaption></figure></details>
  {% endif %}
  <p class="scope-note"><strong>Scope.</strong> {{ project.scope }}</p>
  {% if project.record_url %}<a href="{{ project.record_url }}">Conference record &rarr;</a>{% endif %}
</article>
{% endfor %}

## Related public code

[Traffic World Model](https://github.com/yukiiwong/traffic_wm) is a separate public prototype for multi-site drone trajectory modeling with a Transformer, teacher-forced training, and open-loop rollout visualization. It is not the implementation for every project listed above. Additional public work is available on [my GitHub profile](https://github.com/yukiiwong).

<p class="small muted">Figures are drawn from my research manuscript and experiment materials. Dataset imagery remains attributable to its original provider; no raw trajectory dataset is distributed through this website.</p>
