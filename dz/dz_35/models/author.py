from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

from .database import Base


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    author = Column(String(50), nullable=False)
    book = relationship('Book')

    def __init__(self, author):
        self.author = author

    def __repr__(self):
        return f'Автор: {self.author}'