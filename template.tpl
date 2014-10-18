{# Template for using with IPython nbconvert #}
{# Example: ipython nbconvert --to html --template ./template.tpl testing_code_1.ipynb #}
{%- extends 'full.tpl' -%}
{% block input %}
{%- endblock input %} 
{% block in_prompt %}
{%- endblock in_prompt %} 

{# ipython nbconvert --to html --template template.tpl testing_code_1.ipynb #}