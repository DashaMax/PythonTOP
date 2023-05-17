from flask import Flask, render_template, url_for


app = Flask(__name__)

menu = [
    {'title': 'Главная', 'url': '/'},
    {'title': 'О нас', 'url': '/about'},
    {'title': 'Услуги', 'url': '/services'},
    {'title': 'Доставка', 'url': '/delivery'},
    {'title': 'Контакты', 'url': '/contacts'}
]


@app.route('/')
def index():
    context = {
        'title': menu[0]['title'],
        'text': 'Текст главной страницы'
    }
    return render_template('index.html', menu=menu, **context)


@app.route('/about')
def about():
    context = {
        'title': menu[1]['title'],
        'text': 'Текст о нас'
    }
    return render_template('about.html', menu=menu, **context)


@app.route('/services')
def services():
    context = {
        'title': menu[2]['title'],
        'text': 'Текст про услуги'
    }
    return render_template('services.html', menu=menu, **context)


@app.route('/delivery')
def delivery():
    context = {
        'title': menu[3]['title'],
        'text': 'Текст доставки'
    }
    return render_template('delivery.html', menu=menu, **context)


@app.route('/contacts')
def contacts():
    context = {
        'title': menu[4]['title'],
        'text': 'Текст контактов'
    }
    return render_template('contacts.html', menu=menu, **context)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', menu=menu, title='404 Страница не найдена')


if __name__ == '__main__':
    app.run(debug=True)