from models.user import User as UserModel
from schemas.user import User


class UserService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def create_user(self, user: User):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_user(self, id: int, data: User):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        user.username = data.username
        user.email = data.email
        user.password = data.password
        user.is_active = data.is_active
        user.date_created = data.date_created
        user.date_updated = data.date_updated
        self.db.commit()
        return

    def delete_user(self, id: int):
       self.db.query(UserModel).filter(UserModel.id == id).delete()
       self.db.commit()
       return