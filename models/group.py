from sqlalchemy import Column, Integer, String
from models.database import Base
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)
    student = relationship('Student')

    def __repr__(self):
        return self.group_name