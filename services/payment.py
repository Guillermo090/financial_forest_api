from models.payment import Payment as PaymentModel, Person as PersonModel
from schemas.payment import Payment, Person
from sqlalchemy.orm import joinedload

class PaymentService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_payments(self):
        result = self.db.query(PaymentModel).all()
        return result
    
    def get_persons(self):
        result = self.db.query(PersonModel).all()
        return result