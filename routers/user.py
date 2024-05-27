from fastapi import APIRouter, Depends , Path
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User, LoginRequest
from typing import  List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from services.user import UserService
from fastapi.encoders import jsonable_encoder

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: LoginRequest):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    

@user_router.get('/users', tags=['users'], response_model=List[User], status_code=200, dependencies=[Depends(JWTBearer())])
def get_users() -> List[User]:
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/users/{id}', tags=['users'], response_model=User)
def get_user(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.post('/users', tags=['users'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario"})


@user_router.put('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def update_user(id: int, user: User)-> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el usuario"})


@user_router.delete('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def delete_user(id: int)-> dict:
    db = Session()
    result: User = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    
    UserService(db).delete_user(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el usuario"})