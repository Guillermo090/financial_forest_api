from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

 
# Tablas de asociación para las relaciones many-to-many
group_permissions = Table('group_permissions', Base.metadata,
    Column('group_id', Integer, ForeignKey('group.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True)
)

user_permissions = Table('user_permissions', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True)
)


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    permission_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    groups = relationship('Group', secondary='group_permissions', back_populates='permissions')
    users = relationship('User', secondary='user_permissions', back_populates='permissions')


class Group(Base):
    __tablename__ = 'group'
    
    id = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)
    details = Column(String)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    permissions = relationship('Permission', secondary='group_permissions', back_populates='groups')
    users = relationship('User', back_populates='group')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship('Group', back_populates='users')
    permissions = relationship('Permission', secondary='user_permissions', back_populates='users')