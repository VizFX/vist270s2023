---
layout: page
title: Material 

---

### Learning Material By Week
(Contact the instructor for details)






<ul>

{% assign titleSorted = site.posts  | sort: "title" %}
	  {% for post in titleSorted %}

	{% assign style = "color:#160329;" %}
	{% if post.title contains 'Summary' %}
		{% assign style = "color:#ff0000;font-size:x-large;margin-top:20px;" %}
	{% elsif  post.title contains 'Reading' %}
		{% assign style = "color:#0d0096;" %}
	{% elsif  post.title contains 'Lab' %}
		{% assign style = "color:#227839;" %}
	{% elsif  post.title contains 'Lecture' %}
		{% assign style = "color:#3f3e40;" %}
	{% elsif  post.title contains 'Homework' %}
		{% assign style = "color:#570c1c;" %}
	{%endif%}
	
	{% unless  post.title contains 'DRAFT' or  post.title contains '10' or post.title contains '11' or  post.title contains '12' or  post.title contains '13' or  post.title contains '14' %}
	<li style="{{style}}" >
	      <a href="{{ post.url | prepend:site.baseurl}}" style="{{style}}">{{ post.title }}</a>
	</li>
	{%endunless%}
  {% endfor %}
  
  
  

  
  
{% for post in titleSorted %}

  	{% assign style = "color:#160329;" %}
	{% if post.title contains 'Summary' %}
		{% assign style = "color:#ff0000;font-size:x-large;margin-top:20px;" %}
	{% elsif  post.title contains 'Reading' %}
		{% assign style = "color:#0d0096;" %}
	{% elsif  post.title contains 'Lab' %}
		{% assign style = "color:#227839;" %}
	{% elsif  post.title contains 'Lecture' %}
		{% assign style = "color:#3f3e40;" %}
	{% elsif  post.title contains 'Homework' %}
		{% assign style = "color:#570c1c;" %}
	{% endif %}
	{% unless post.title contains 'DRAFT'%}
	{% if post.title contains '10' or post.title contains '11' or  post.title contains '12' or  post.title contains '13' or  post.title contains '14' %}
	<li style="{{style}}" >
	      <a href="{{ post.url | prepend:site.baseurl}}" style="{{style}}">{{ post.title }}</a>
	</li>

	{%endif%}
	{% endunless %}

	
  {% endfor %}
  
  
</ul>

