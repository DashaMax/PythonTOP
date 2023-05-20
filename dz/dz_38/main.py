import os
import sqlite3

from flask import Flask, render_template, url_for, g, request, flash

from FDataBase import FDataBase


DATABASE = '/tmp/.db'
DEBUG = True
SECRET_KEY = 'dhg478gyger684grefg3467rgwgi689'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'space.db')))


def connect_db():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect


def create_db():
    db = connect_db()
    with app.open_resource('script.sql', mode='r') as file:
        db.cursor().executescript(file.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


menu = [
    {'title': 'Главная', 'url': '/'},
    {'title': 'О нас', 'url': '/about'},
    {'title': 'Добавить', 'url': '/add'},
    {'title': 'Доставка', 'url': '/delivery'},
    {'title': 'Контакты', 'url': '/contacts'}
]


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)

    context = {
        'title': menu[0]['title'],
        'books': dbase.get_books()
    }

    return render_template('index.html', menu=menu, **context)


@app.route('/book/<url>')
def book(url):
    db = get_db()
    dbase = FDataBase(db)
    book_ = dbase.get_book(url)

    context = {
        'title': book_['title'],
        'book': book_
    }

    return render_template('book.html', menu=menu, **context)


@app.route('/about')
def about():
    context = {
        'title': menu[1]['title'],
        'text': 'Текст о нас'
    }
    return render_template('about.html', menu=menu, **context)


@app.route('/add', methods=['GET', 'POST'])
def add():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['title']) > 1 and len(request.form['author']) > 2:
            desc = request.form['description'] if request.form['description'] else None
            result = dbase.add_book(request.form['title'], request.form['url'], request.form['author'], desc)

            if len(result) == 2:
                flash(result[1], category='error')
            else:
                flash('Книга успешно добавлена', category='success')

        else:
            flash('Ошибка добавления книги', category='error')

    context = {
        'title': menu[2]['title']
    }

    return render_template('add.html', menu=menu, **context)


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