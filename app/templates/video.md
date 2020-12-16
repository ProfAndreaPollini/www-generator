{% extends "page.md" %}

{% block header %}
video_id: "{{obj.video_url}}"
{% endblock %}

{% block beforecontent %}

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/{{obj.video_url}}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
{% endblock %}

{% block aftercontent %}


{% endblock %}
