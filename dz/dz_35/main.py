from os.path import exists

from sqlalchemy import and_, not_, or_

from create_db import create
from models.author import Author
from models.database import session, DATABASE_NAME

from models.book import Book
from models.user import User, user_book


if __name__ == '__main__':
    if not exists(DATABASE_NAME):
        create()

    # Запросы к БД

    print(session.query(User).all(), end=f'\n\n{"*" * 30}\n\n')

    print(session.query(Book).limit(3).all(), end=f'\n\n{"*" * 30}\n\n')

    print(session.query(Book).group_by(Book.author).count(), end=f'\n\n{"*" * 30}\n\n')

    print(session.query(User.name, User.surname, Book.title, Author.author).filter(and_(
        User.id == user_book.c.user_id,
        Book.id == user_book.c.book_id,
        Book.author == Author.id
    )).first(), end=f'\n\n{"*" * 30}\n\n')

    # for data in session.query(User.surname).filter(User.surname.like('%а%а%')):
    #     print(data)

    # for data in session.query(User).filter(User.data_of_birth.between('1990-01-01', '2010-01-01')).order_by(
    #         User.data_of_birth):
    #     print(data)

    # for data in session.query(Book.title, Author.author).join(Author.book).order_by(Book.author):
    #     print(data)

    # for data in session.query(User.name, User.surname, Author.author).filter(and_(
    #         user_book.c.user_id == User.id,
    #         user_book.c.book_id == Book.id,
    #         Book.author == Author.id,
    #         Author.author == 'Достоевский Ф.М.')
    # ):
    #     print(data)

    # for data in session.query(User.name, Book.title, Author.author).filter(and_(
    #         user_book.c.user_id == User.id,
    #         user_book.c.book_id == Book.id,
    #         Book.author == Author.id,
    #         Author.author == 'Булгаков М.А',
    #         not_(Book.title == 'Белая гвардия'))
    # ):
    #     print(data)

    # for data in session.query(User, Book.title).join(User.book).group_by(Book.title).having(or_(
    #         User.data_of_birth > '2000.01.01', User.surname.like('%а'))).all():
    #     print(data)






