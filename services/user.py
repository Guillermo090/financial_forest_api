from models.user import User as UserModel, Group as GroupModel
from schemas.user import User, Group, UserCreate
from sqlalchemy.orm import joinedload
from utils.bcrypt_pwd import check_password, hash_password

class UserService():
    
    def __init__(self, db) -> None:
        self.db = db


    def get_users(self):
        # result = self.db.query(UserModel).all()
        result = self.db.query(UserModel).options(joinedload(UserModel.group)).all()
        filtered_result = [
            {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_active': user.is_active,
                'date_created': user.date_created,
                'date_updated': user.date_updated,
                'group_id': user.group_id,
                'group_name': user.group.group_name if user.group else None
            }
            for user in result
        ]
        return filtered_result


    def get_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).options(joinedload(UserModel.group)).first()
        filtered_result = { 
            'id': result.id,
            'username': result.username,
            'email': result.email,
            'is_active': result.is_active,
            'date_created': result.date_created,
            'date_updated': result.date_updated,
            'group_id': result.group_id,
            'group_name': result.group.group_name if result.group else None
        }
        return filtered_result


    def create_user(self, user: UserCreate):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return


    def update_user(self, id: int, data: User):
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        user.username = data.username if data.username else user.username
        user.email = data.email if data.email else user.email
        # user.password = data.password
        user.is_active = data.is_active if data.is_active else user.is_active
        user.group_id = data.group_id if data.group_id else user.group_id
        self.db.commit()
        return


    def delete_user(self, id: int):
       self.db.query(UserModel).filter(UserModel.id == id).delete()
       self.db.commit()
       return
    

    def get_groups(self):
        result = self.db.query(GroupModel).all()
        return result
    

    def get_group(self, id):
        result = self.db.query(GroupModel).filter(GroupModel.id == id).first()
        return result
    

    def create_group(self, group: Group):
        new_group = GroupModel(**group.model_dump())
        self.db.add(new_group)
        self.db.commit()
        return

    
    def update_group(self, id: int, data: Group):
        group = self.db.query(GroupModel).filter(GroupModel.id == id).first()
        group.group_name = data.group_name
        group.details = data.details
        group.is_active = data.is_active
        self.db.commit()
        return


    def delete_group(self, id: int):
       self.db.query(GroupModel).filter(GroupModel.id == id).delete()
       self.db.commit()
       return
    

    def user_group_asociation(self, user_id: int, group_id: int):
       
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        # Actualizar el group_id del usuario
        user.group_id = group_id
        self.db.commit()
        return user


    def auth_user_data(self, email:str, password:str):

        user = self.db.query(
            UserModel.email, UserModel.password
        ).filter(UserModel.email == email).first()
        if not user:
            return

        password_validated = check_password(password, user.password)
        if not password_validated:
            return False

        return user
    

    def get_user_by_email(self, email:str):

        user = self.db.query(UserModel).first()
        if not user:
            return False
        return user
    

    def update_password(self, email:str, password:str):

        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            return False
        
        user.password = hash_password(password)
        self.db.commit()
        return user