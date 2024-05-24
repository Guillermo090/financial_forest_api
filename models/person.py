from config.db import Base
from sqlalchemy import Column, Integer, String, DateTime

class Person(Base):

    __tablename__ = 'persona'

    id = Column(Integer, primary_key=True)
    rut = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)
    