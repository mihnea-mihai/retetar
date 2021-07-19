---
---

# Rețete

{% for recipe in site.retete %}
  * [{{ recipe.title }}]({{ recipe.url }})
{% endfor %}