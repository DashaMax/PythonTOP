import math
import re
import sqlite3
import time

from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cursor = db.cursor()

    def get_menu(self):
        sql = 'SELECT * FROM mainmenu'
        try:
            self.__cursor.execute(sql)
            result = self.__cursor.fetchall()
            if result:
                return result
        except IOError:
            print('Ошибка чтения из БД')
        return []

    def add_post(self, title, url, description):
        try:
            self.__cursor.execute('SELECT COUNT(*) AS count FROM posts WHERE url LIKE ?', (url, ))
            result = self.__cursor.fetchone()

            if result['count'] > 0:
                print('Статья с таким URL уже существует')
                return False

            # base = url_for('static', filename='images')
            # text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>", r"\g<tag>" + base + r"/\g<url>>", text)

            tm = math.floor(time.time())
            self.__cursor.execute('INSERT INTO posts VALUES (NULL, ?, ?, ?, ?)', (title, url, description, tm))
            self.__db.commit()
            return True

        except sqlite3.Error as error:
            print(f'Ошибка добавления статьи в БД: {error}')
            return False

    def get_post(self, slug):
        try:
            self.__cursor.execute('SELECT title, description FROM posts WHERE url LIKE ?', (slug,))
            result = self.__cursor.fetchone()

            if result:
                return result

        except sqlite3.Error as error:
            print(f'Ошибка получения статьи из БД: {error}')

        return False, False

    def get_posts(self):
        try:
            self.__cursor.execute('SELECT url, title, description FROM posts ORDER BY time DESC')
            result = self.__cursor.fetchall()

            if result:
                return result

        except sqlite3.Error as error:
            print(f'Ошибка получения статей из БД: {error}')

        return []

