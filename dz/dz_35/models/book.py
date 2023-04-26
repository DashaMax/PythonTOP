from sqlalchemy import Table, Integer, String, Column, ForeignKey, Text
from sqlalchemy.orm import relationship

from .database import Base


user_book = Table(
                    'user_book', Base.metadata,
                    Column('user_id', Integer(), ForeignKey('users.id')),
                    Column('book_id', Integer(), ForeignKey('books.id'))
                 )


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String(200), nullable=False)
    author = Column(String(50))
    description = Column(Text())
    user = relationship('User', secondary=user_book, backref="books")

    def __init__(self, title, author, description=None):
        self.title = title
        self.author = author
        self.description = description

    def __repr__(self):
        return f'Title: {self.title},' \
               f'Author: {self.author},' \
               f'Description: {self.description}'

