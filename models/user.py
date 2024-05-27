from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, func

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
