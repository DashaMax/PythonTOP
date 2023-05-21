import os
import sqlite3

from flask import Flask, render_template, url_for, g, request, flash, abort

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


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)

    context = {
        'title': dbase.get_menu()[0]['title'],
        'menu': dbase.get_menu(),
        'books': dbase.get_books()
    }

    return render_template('index.html', **context)


@app.route('/book/<url>')
def book(url):
    db = get_db()
    dbase = FDataBase(db)
    book_ = dbase.get_book(url)

    if not book_:
        abort(404)

    context = {
        'title': book_['title'],
        'menu': dbase.get_menu(),
        'book': book_
    }

    return render_template('book.html', **context)


@app.route('/about')
def about():
    db = get_db()
    dbase = FDataBase(db)

    context = {
        'title': dbase.get_menu()[1]['title'],
        'menu': dbase.get_menu(),
        'text': 'Текст о нас'
    }
    return render_template('about.html', **context)


@app.route('/add', methods=['GET', 'POST'])
def add():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['author']) > 4 and len(request.form['publish']) > 2 and \
                request.form['url'] and request.form['year'] and request.form['pages'] and request.form['price']:
            desc = request.form['description'] if request.form['description'] else None
            img = 'img/' + request.form['image'] if request.form['image'] else None

            result = dbase.add_book(
                request.form['title'],
                request.form['url'],
                request.form['author'],
                request.form['publish'],
                request.form['year'],
                request.form['pages'],
                request.form['price'],
                img,
                desc
            )

            if len(result) == 2:
                flash(result[1], category='error')
            else:
                flash('Книга успешно добавлена', category='success')

        else:
            flash('Ошибка добавления книги', category='error')

    context = {
        'title': dbase.get_menu()[2]['title'],
        'menu': dbase.get_menu()
    }

    return render_template('add.html', **context)


@app.route('/delivery')
def delivery():
    db = get_db()
    dbase = FDataBase(db)

    context = {
        'title': dbase.get_menu()[3]['title'],
        'menu': dbase.get_menu(),
        'text': 'Текст доставки'
    }
    return render_template('delivery.html', **context)


@app.route('/contacts')
def contacts():
    db = get_db()
    dbase = FDataBase(db)

    context = {
        'title': dbase.get_menu()[4]['title'],
        'menu': dbase.get_menu(),
        'text': 'Текст контактов'
    }
    return render_template('contacts.html', **context)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    menu = dbase.get_menu()
    return render_template('page404.html', menu=menu, title='404 Страница не найдена')


if __name__ == '__main__':
    app.run(debug=True)