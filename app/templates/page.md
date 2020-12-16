---
title: "{{page.title}}"
date: "{{page.lastModified}}"
summary: "{{page.summary}}"
type: "{{page.kind}}"
{% if page.kind not in ["page_kind_summary"] %}
url: "/{{obj.slug()}}"
{% endif %}

{% if page.tags %}
tags: 
{% for tag in page.tags %}
- "{{tag}}"
{% endfor %}
{% endif %}

{% if page.categories %}
categories:
{% for category in page.categories %}
- "{{category}}"
{% endfor %}
{% endif %}

{% block header %}
{% endblock %}


{% if page.aliases%}
aliases:
{% for alias in page.aliases %}
- "/{{alias}}"
{% endfor %}
{% endif %}
---

{% block beforecontent %}
{% endblock %}

{% for section in content %}
## {{ section.title }}

{{ section.content }}

{% block aftercontent %}
{% endblock %}

{% endfor %}