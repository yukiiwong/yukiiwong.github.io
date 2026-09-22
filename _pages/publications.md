---
title: "Publications"
layout: gridlay
permalink: /publications/
---
<p class="eyebrow">Publications &amp; conference work</p>

# Research record

## Journal article

{% for item in site.data.publications %}{% if item.kind == 'journal' %}
<article class="publication-entry"><span class="publication-year">{{ item.year }}</span><h3>{{ item.title }}</h3><p>{{ item.authors | replace: 'Yukai Wang', '<strong>Yukai Wang</strong>' }}<br/><em>{{ item.venue }}</em></p><a href="{{ item.url }}">DOI / article</a> · <a href="{{ item.source }}">Open-access record</a></article>
{% endif %}{% endfor %}

## Conference contributions

{% for item in site.data.publications %}{% if item.kind == 'conference' %}
<article class="publication-entry"><span class="publication-year">{{ item.year }}</span><h3>{{ item.title }}</h3><p>{{ item.authors | replace: 'Yukai Wang', '<strong>Yukai Wang</strong>' }}<br/><em>{{ item.venue }}</em></p><a href="{{ item.url }}">Laboratory conference record</a></article>
{% endif %}{% endfor %}

## Ongoing manuscripts and projects

Recent work covers trajectory world models from drone data, closed-loop rollout diagnostics, future-free candidate ranking, and surrogate safety assessment. These projects are presented with figures and clearly labeled research status on the [Research page]({{ '/research/' | relative_url }}).

<p class="scope-note">Conference records and working manuscripts are listed separately from published journal articles. The ongoing PhD world-model studies are not presented as accepted journal publications.</p>

For bibliographic updates, see [Google Scholar](https://scholar.google.com/citations?hl=en&user=86WFIcAAAAAJ).
