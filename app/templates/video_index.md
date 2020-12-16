{% extends "page.md" %}

{% block header %}
url: "/{{obj.section}}"
{% endblock %}

{% block beforecontent %}

## Elenco Video!!

{%for cat,pages in obj.pages_by_category.items() %}
{% if not cat == "" %}
### [{{cat}}](/category/{{obj.category_slugs[cat] }}) ({{pages | length }})
{% else %}

{% endif %}
{% for p in pages%}
[{{p.title}}](/{{p.slug()}})
{%endfor%}
{% endfor %}


{% endblock %}
