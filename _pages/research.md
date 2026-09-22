---
title: "Research"
layout: gridlay
permalink: /research/
---
<p class="eyebrow">Research overview · September 2026</p>

# World models for traffic, beyond a single vehicle

{{ site.data.research_story.thesis }} My work connects **drone trajectory data**, **multi-agent world models**, and **traffic safety**, with a site-centric perspective complementary to ego-vehicle driving models.

<section class="research-story" id="research-story" aria-label="Research story">
{% for part in site.data.research_story.paragraphs %}<div class="story-part"><h2>{{ part.heading }}</h2><p>{{ part.text }}</p></div>{% endfor %}
<p class="intro-note">{{ site.data.research_story.development_note }} <a href="{{ '/publications/' | relative_url }}#submission-history">Submission history &rarr;</a></p>
</section>

## Research projects

<nav class="project-index" aria-label="Research projects">{% for project in site.data.research %}<a href="#{{ project.id }}">{{ forloop.index | prepend: '0' }} · {{ project.title }}</a>{% endfor %}</nav>

<p class="intro-note">Status updated {{ site.data.submissions.updated }}. Under-review manuscripts, working drafts, and earlier submissions are distinguished in the <a href="{{ '/publications/' | relative_url }}#under-review">research record</a>; none of these labels implies acceptance.</p>

{% for project in site.data.research %}
<article class="research-detail" id="{{ project.id }}">
  <p class="project-status">{{ project.status }}</p>
  <h2>{{ project.title }}</h2>
  <p class="project-tags">{{ project.tags | join: ' · ' }}</p>
  <p>{{ project.description }}</p>
  <p><strong>Research focus.</strong> {{ project.contribution }}</p>
  {% if project.image %}
  <figure class="project-figure {{ project.figure_class }} {% if project.id == 'drone-world-models' %}trajectory-figure{% endif %}">
    <a href="{{ '/images/research/' | append: project.image | relative_url }}" aria-label="Open full-size figure for {{ project.title | escape }}"><img src="{{ '/images/research/' | append: project.image | relative_url }}" alt="{{ project.alt | escape }}" width="{{ project.image_width }}" height="{{ project.image_height }}" loading="lazy" /></a>
    <figcaption>{{ project.caption }}{% if project.id == 'drone-world-models' %} <a href="https://levelxdata.com/ind-dataset/">Dataset information</a>.{% endif %} Click the figure to view it at full size.</figcaption>
  </figure>
  {% endif %}
  {% if project.secondary_image %}
  <details class="framework-detail"><summary>{{ project.secondary_summary | default: 'View the model architecture' }}</summary><figure class="project-figure {{ project.figure_class }}"><a href="{{ '/images/research/' | append: project.secondary_image | relative_url }}" aria-label="Open supporting figure for {{ project.title | escape }}"><img src="{{ '/images/research/' | append: project.secondary_image | relative_url }}" alt="{{ project.secondary_alt | escape }}" width="{{ project.secondary_width }}" height="{{ project.secondary_height }}" loading="lazy" /></a><figcaption>{{ project.secondary_caption }} Click the figure to view it at full size.</figcaption></figure></details>
  {% endif %}
  <p class="scope-note"><strong>Scope.</strong> {{ project.scope }}</p>
  {% if project.record_url %}<a href="{{ project.record_url }}">Conference record &rarr;</a>{% endif %}
</article>
{% endfor %}

## Related public code

[Traffic World Model](https://github.com/yukiiwong/traffic_wm) is a separate public prototype for multi-site drone trajectory modeling with a Transformer, teacher-forced training, and open-loop rollout visualization. It is not the implementation for every project listed above. Additional public work is available on [my GitHub profile](https://github.com/yukiiwong).

<p class="small muted">Figures are drawn from my research manuscript and experiment materials. Dataset imagery remains attributable to its original provider; no raw trajectory dataset is distributed through this website.</p>
