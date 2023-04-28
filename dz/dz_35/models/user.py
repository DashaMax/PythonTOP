from sqlalchemy import Integer, String, Column, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


user_book = Table(
                    'user_book', Base.metadata,
                    Column('user_id', Integer(), ForeignKey('users.id')),
                    Column('book_id', Integer(), ForeignKey('books.id'))
                 )


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    data_of_birth = Column(Date(), nullable=False)
    address = Column(String(150))
    book = relationship('Book', secondary=user_book, backref="users")

    def __init__(self, name, surname, data, address):
        self.name = name
        self.surname = surname
        self.data_of_birth = data
        self.address = address

    def __repr__(self):
        return f'Имя: {self.name}, ' \
               f'Фамилия: {self.surname}, ' \
               f'Дата рождения: {self.data_of_birth}, ' \
               f'Адресс: {self.address}'