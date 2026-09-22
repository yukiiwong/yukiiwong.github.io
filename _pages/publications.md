---
title: "Publications"
layout: gridlay
permalink: /publications/
---
<p class="eyebrow">Publications, submissions &amp; research development</p>

# Research record

Published work, manuscripts under review, and ongoing projects are listed separately below. Current research status is updated as of **{{ site.data.submissions.updated }}**.

## Journal article

{% for item in site.data.publications %}{% if item.kind == 'journal' %}
<article class="publication-entry"><span class="publication-year">{{ item.year }}</span><h3>{{ item.title }}</h3><p>{{ item.authors | replace: 'Yukai Wang', '<strong>Yukai Wang</strong>' }}<br/><em>{{ item.venue }}</em></p><a href="{{ item.url }}">DOI / article</a> · <a href="{{ item.source }}">Open-access record</a></article>
{% endif %}{% endfor %}

## Conference contributions

{% for item in site.data.publications %}{% if item.kind == 'conference' %}
<article class="publication-entry"><span class="publication-year">{{ item.year }}</span><h3>{{ item.title }}</h3><p>{{ item.authors | replace: 'Yukai Wang', '<strong>Yukai Wang</strong>' }}<br/><em>{{ item.venue }}</em></p><a href="{{ item.url }}">Laboratory conference record</a></article>
{% endif %}{% endfor %}

<h2 id="under-review">Manuscripts under review</h2>

{% include submission-records.html items=site.data.submissions.under_review %}

<h2 id="ongoing-research">Ongoing research</h2>

These active projects form part of my broader research programme. They are listed separately from the manuscripts currently under review.

{% for project in site.data.research %}{% if project.status == 'Ongoing' %}
<article class="submission-entry"><p class="submission-meta"><span class="submission-status">{{ project.status }}</span></p><h3><a href="{{ '/research/' | relative_url }}#{{ project.id }}">{{ project.title }}</a></h3><p>{{ project.cv }}</p></article>
{% endif %}{% endfor %}

For bibliographic updates, see [Google Scholar](https://scholar.google.com/citations?hl=en&user=86WFIcAAAAAJ).
