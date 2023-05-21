import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cursor = db.cursor()

    def add_book(self, title, url, author, publish, year, pages, price, img, description):
        try:
            self.__cursor.execute('SELECT COUNT(*) AS count FROM books WHERE url LIKE ?', (url, ))
            result = self.__cursor.fetchone()

            if result['count']:
                text = 'Книга с таким URL уже существует'
                return False, text

            self.__cursor.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
                title,
                url,
                author,
                publish,
                year,
                pages,
                price,
                img,
                description)
            )
            self.__db.commit()
            return True,

        except sqlite3.Error:
            return False,

    def get_books(self):
        try:
            self.__cursor.execute('SELECT title, url, author, price, image FROM books')
            result = self.__cursor.fetchall()

            if result:
                return result

        except sqlite3.Error as error:
            print(f'Ошибка получения книг из БД: {error}')

    def get_book(self, url):
        try:
            self.__cursor.execute('''SELECT title, url, author, publishing, year, pages, price, image, description
                                     FROM books WHERE url LIKE ?''', (url,))
            result = self.__cursor.fetchone()

            if result:
                return result

        except sqlite3.Error as error:
            print(f'Ошибка получения книги из БД: {error}')

    def get_menu(self):
        try:
            self.__cursor.execute('SELECT title, url FROM menu')
            result = self.__cursor.fetchall()

            if result:
                return result

        except sqlite3.Error as error:
            print(f'Ошибка получения меню из БД: {error}')