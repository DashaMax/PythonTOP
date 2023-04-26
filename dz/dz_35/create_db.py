from faker import Faker
from datetime import datetime

from models.book import Book
from models.user import User
from models.database import create_db, session


def create():
    create_db()
    _load_fake_data()


def _load_fake_data():
    faker = Faker(locale='ru_RU')

    for i in range(10):
        name = faker.first_name()
        surname = faker.last_name()
        address = faker.address()
        data = datetime.strptime(faker.date(), "%Y-%m-%d")
        user = User(name, surname, data, address)
        session.add(user)

        title = f'book{i + 1}'
        author = faker.last_name()
        description = faker.text()
        book = Book(title, author, description)
        session.add(book)

    session.commit()
    # print(session.query(User).all())
    # print(session.query(Book).all())
    session.close()