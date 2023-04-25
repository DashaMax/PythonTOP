from sqlalchemy import Column, ForeignKey, Integer, String
from models.database import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    surname = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    patronymic = Column(String(50))
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name, age, id_group):
        self.surname, self.name, self.patronymic = full_name
        self.age = age
        self.group = id_group

    def __repr__(self):
        return f'Student: {self.surname}, {self.name}, {self.patronymic}\nAge: {self.age}\nGroup: {self.group}'