from faker import Faker
from datetime import datetime

from models.book import Book
from models.user import User
from models.author import Author
from models.database import create_db, session


def create():
    create_db()
    _load_fake_data()


def _load_fake_data():
    faker = Faker(locale='ru_RU')

    authors = [
        Author('Булгаков М.А'),
        Author('Достоевский Ф.М.'),
        Author('Толстой Л.Н.'),
        Author('Тургенев И.С.')
    ]
    session.add_all(authors)
    session.commit()

    books = [
        Book('Мастер и Маргарита', authors[0].id, faker.text()),
        Book('Преступление и наказание', authors[1].id, faker.text()),
        Book('Война и мир', authors[2].id, faker.text()),
        Book('Белая гвардия', authors[0].id, faker.text()),
        Book('Отцы и дети', authors[3].id, faker.text()),
        Book('Собачье сердце', authors[0].id, faker.text()),
        Book('Анна Каренина', authors[2].id, faker.text()),
    ]
    session.add_all(books)
    session.commit()

    for i in range(20):
        name = faker.first_name()
        surname = faker.last_name()
        address = faker.address()
        data = datetime.strptime(faker.date(), "%Y-%m-%d")
        user = User(name, surname, data, address)
        user.book.append(faker.random.choice(books))
        session.add(user)

    session.commit()
    session.close()