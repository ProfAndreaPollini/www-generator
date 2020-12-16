{% extends "page.md" %}

{% block header %}
{% if page.language %}
{% endif %}
{% endblock %}

{% block beforecontent %}
{% endblock %}

{% block aftercontent %}

{% for solution in obj.get_solutions() %}
*	[{{solution.title}}](/{{solution.slug()}})
{% endfor %}

### altri esercizi
{% for cat in obj.exercises_with_same_category() %}
#### [{{cat[0]}}](/category/{{cat[1]}})
{% for es in obj.exercises_with_same_category()[cat] %}
* [{{es.title}}](/{{es.slug()}})
{% endfor %}
{% endfor %}


{% endblock %}
