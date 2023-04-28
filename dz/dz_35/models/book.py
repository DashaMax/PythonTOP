from sqlalchemy import Integer, String, Column, Text, ForeignKey

from .database import Base


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    title = Column(String(200), nullable=False)

    # По-хорошему, у таблиц books и authors должна быть связь многие ко многим - будем считать,
    # что в нашей библиотеки нет книг, написанных несколькими авторами
    author = Column(Integer(), ForeignKey('authors.id'))
    description = Column(Text())

    def __init__(self, title, author, description=None):
        self.title = title
        self.author = author
        self.description = description

    def __repr__(self):
        return f'Название: {self.title}, ' \
               f'Автор: {self.author}'

