{% extends "page.md" %}

{% block header %}
{% if page.language %}
{% endif %}
{% endblock %}

{% block beforecontent %}
soluzione di [{{page.exercise.title}}](/{{page.exercise.slug()}}):

{% for section in page.exercise.get_content()%}
{{section.content}}
{% endfor %}
### soluzione
{% endblock %}

{% block aftercontent %}

### soluzioni in altri linguaggi

{% for solution in obj.exercise.get_solutions() %}
{% if not solution == obj %}
*	[{{solution.title}}](/{{solution.slug()}})
{% endif %}
{% endfor %}


{% for cat in page.exercise.exercises_with_same_category().keys() %}
### altri [{{cat[0]}}](/category/{{cat[1]}})
{% for es in page.exercise.exercises_with_same_category()[cat] %}
* [{{es.title}}](/{{es.slug()}})
{% endfor %}
{% endfor %}
{% endblock %}
