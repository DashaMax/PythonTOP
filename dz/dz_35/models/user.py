from sqlalchemy import Integer, String, Column, Date

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    data_of_birth = Column(Date(), nullable=False)
    address = Column(String(150))

    def __init__(self, name, surname, data, address):
        self.name = name
        self.surname = surname
        self.data_of_birth = data
        self.address = address

    def __repr__(self):
        return f'Name: {self.name},' \
               f'Surname: {self.surname},' \
               f'Data_of_birth: {self.data_of_birth},' \
               f'Address: {self.address}'