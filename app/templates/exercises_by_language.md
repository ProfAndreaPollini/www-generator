{% extends "page.md" %}

{% block header %}
url: "/esercizi-{{obj.page_language}}"
{% endblock %}

{% block beforecontent %}

## Elenco esercizi in {{obj.page_language}} 

{%for cat,pages in obj.pages_by_category.items() %}
{% if not cat == "" %}
* [{{cat}}](/category/{{obj.category_slugs[cat] }}) ({{pages | length }})
{% else %}

{% endif %}

{% endfor %}

{%for cat,pages in obj.pages_by_category.items() %}
{% if not cat == "" %}
### {{cat}}
{% else %}

{% endif %}
{% for p in pages%}
[{{p.title}}](/{{p.slug()}})
{%endfor%}
{% endfor %}


{% endblock %}
