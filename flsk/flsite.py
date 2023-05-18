import os
import sqlite3

from flask import (Flask, render_template, url_for, request, \
    flash, session, redirect, g, abort)

from FDataBase import FDataBase


DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'dhg478gyger684grefg3467rgwgi'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    connect = sqlite3.connect(app.config['DATABASE'])
    connect.row_factory = sqlite3.Row
    return connect


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as file:
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
    return render_template('index.html', title='Главная', menu=dbase.get_menu(), posts=dbase.get_posts())


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['title']) > 4 and len(request.form['description']) > 10:
            result = dbase.add_post(request.form['title'], request.form['url'], request.form['description'])

            if not result:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')

        else:
            flash('Ошибка добавления статьи', category='error')

    return render_template('add_post.html', title='Добавить статью', menu=dbase.get_menu())


@app.route('/post/<slug>')
def show_post(slug):
    db = get_db()
    dbase = FDataBase(db)
    title, description = dbase.get_post(slug)

    if not title:
        abort(404)

    return render_template('post.html', title=f'Статья {title}', description=description, menu=dbase.get_menu())


# @app.route('/about')
# def about():
#     return render_template('about.html', title='About')


# @app.route('/profile/<username>')
# def profile(username):
#     return render_template('profile.html', title='LK', username=username)


# @app.route('/contacts', methods=['POST', 'GET'])
# def contacts():
#     if request.method == 'POST':
#         if len(request.form['username']) > 2:
#             context = {
#                 'username': request.form['username'],
#                 'email': request.form['email'],
#                 'message': request.form['message']
#             }
#             flash('Message success!', category='success')
#             return render_template('contact.html', title='Contacts', **context)
#         else:
#             flash('Message error!', category='error')
#     return render_template('contact.html', title='Contacts')


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template('page404.html', title='Страница не найдена', menu=dbase.get_menu())


# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if 'userLogged' in session and session['userLogged'] == 'dasha':
#         return redirect(url_for('profile', username=session['userLogged']))
#     return render_template('login.html', title='Login')


@app.teardown_appcontext
def close_db(db):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)