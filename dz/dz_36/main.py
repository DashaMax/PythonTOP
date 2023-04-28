from jinja2 import Template


data = [
    {'link': 'index', 'title': 'Главная'},
    {'link': 'news', 'title': 'Новости'},
    {'link': 'about', 'title': 'О компании'},
    {'link': 'shop', 'title': 'Магазин'},
    {'link': 'contacts', 'title': 'Контакты'}
]

link = '''<ul>
{% for d in data -%}
    <li><a href="/{{ d.link }}"{% if d.title == "Главная" %} class="active"{% endif %}>{{ d.title }}</a></li>
{% endfor -%}
</ul>'''

tm = Template(link)
msg = tm.render(data=data)
print(msg)