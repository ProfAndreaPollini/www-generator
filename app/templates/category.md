{% extends "page.md" %}

{% block header %}


{% endblock %}

{% block beforecontent %}

Vedi tutte le [categorie di esercizi](/esercizi)

Ci sono {{obj.pages |length}} pagine 

{% for kind,pages in obj.pages_by_kind.items() %}
### {{kind}}

{% for p in pages%}
* [{{p.title}}](/{{p.slug()}})
{% endfor %}
{% endfor %}

{% endblock %}


