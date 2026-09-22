---
title: "Publications"
layout: gridlay
permalink: /publications/
---
<p class="eyebrow">Publications, submissions &amp; research development</p>

# Research record

This page records both completed work and the submission process. Current review status is updated as of **{{ site.data.submissions.updated }}**. Under-review and earlier unsuccessful submissions are not accepted publications.

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

<h2 id="submission-history">Earlier submissions and research development</h2>

{{ site.data.research_story.development_note }}

{% include submission-records.html items=site.data.submissions.previous history=true %}

## Other working manuscripts and projects

Future-free candidate ranking, forecast-driven surrogate safety assessment, and digital-twin validity remain ongoing research. They are not included in the under-review list above. Project descriptions and original experiment figures are on the [Research page]({{ '/research/' | relative_url }}).

<p class="scope-note">Rejected and withdrawn are different outcomes. The NeurIPS entry records a withdrawal after review, not a formal rejection. Review correspondence and anonymous reviewer details are not reproduced here.</p>

For bibliographic updates, see [Google Scholar](https://scholar.google.com/citations?hl=en&user=86WFIcAAAAAJ).
