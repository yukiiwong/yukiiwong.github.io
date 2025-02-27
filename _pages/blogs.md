---
title: "Blog"
layout: page
sitemap: false
permalink: /blogs/
---

<h3 id="research">🔬 Research</h3>
<ul>
  {% for post in site.posts %}
    {% if post.categories contains "research" %}
      <li>{{ post.date | date_to_string }}: 
        <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>

<h3 id="course">📖 Course</h3>
<ul>
  {% for post in site.posts %}
    {% if post.categories contains "course" %}
      <li>{{ post.date | date_to_string }}: 
        <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>

<h3 id="selflearning">🚀 Self Learning</h3>
<ul>
  {% for post in site.posts %}
    {% if post.categories contains "selflearning" %}
      <li>{{ post.date | date_to_string }}: 
        <a href="{{ site.url }}{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>