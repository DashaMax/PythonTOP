from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_NAME = 'library'

engine = create_engine(f'sqlite:///{DATABASE_NAME}.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


