from config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

class Person(Base):

    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    rut = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
    
    payments_as_debtor  = relationship('Payment', foreign_keys='Payment.debtor_id', back_populates='debtor')
    payments_as_creditor  = relationship('Payment', foreign_keys='Payment.creditor_id', back_populates='creditor')


class Payment(Base):
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    date_payment = Column(DateTime)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    creditor_id = Column(Integer, ForeignKey('person.id'))
    debtor_id = Column(Integer, ForeignKey('person.id'))

    creditor = relationship('Person', foreign_keys=[creditor_id], back_populates='payments_as_creditor')
    debtor = relationship('Person', foreign_keys=[debtor_id], back_populates='payments_as_debtor')