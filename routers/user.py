from fastapi import APIRouter, Depends , Path, status
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User, LoginRequest, Group, UserCreate
from typing import  List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from services.user import UserService
from fastapi.encoders import jsonable_encoder

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: LoginRequest):
    db = Session()
    result = UserService(db).auth_user_data(user.email, user.password)
    if not result:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, 
            content={'message': "No Autorizado"})

    token: str = create_token(user.model_dump())
    return JSONResponse(status_code=200, content=token)


@user_router.post('/update_password', tags=['auth'])
def update_password(user: LoginRequest):
    db = Session()
    result = UserService(db).get_user_by_email(user.email)
    if not result:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={'message': "Error al realizar la solicitud"})

    
    UserService(db).update_password(user.email, user.password)
    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': "ok"})


@user_router.get('/users', tags=['users'], response_model=List[User], 
    status_code=200, dependencies=[Depends(JWTBearer())])
def get_users() -> List[User]:
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@user_router.get('/users/{id}', tags=['users'], response_model=User, 
    dependencies=[Depends(JWTBearer())] )
def get_user(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, 
            content={'message': "No encontrado"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@user_router.post('/users', tags=['users'], response_model=dict, 
    status_code=201, dependencies=[Depends(JWTBearer())])
def create_user(user: UserCreate) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, 
        content={"message": "Se ha registrado el usuario"})


@user_router.put('/users/{id}', tags=['users'], response_model=dict, 
    status_code=200, dependencies=[Depends(JWTBearer())])
def update_user(id: int, user: User)-> dict:
    db = Session()
    result = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, 
            content={'message': "No encontrado"})
    
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=status.HTTP_200_OK, 
        content={"message": "Se ha modificado el usuario"})


@user_router.delete('/users/{id}', tags=['users'], response_model=dict, 
    status_code=200, dependencies=[Depends(JWTBearer())])
def delete_user(id: int)-> dict:
    db = Session()
    result: User = UserService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No se encontró"})
    
    UserService(db).delete_user(id)
    return JSONResponse(status_code=status.HTTP_200_OK, 
        content={"message": "Se ha eliminado el usuario"})


@user_router.get('/groups', tags=['groups'], response_model=List[Group], status_code=200, dependencies=[Depends(JWTBearer())])
def get_groups() -> List[Group]:
    db = Session()
    result = UserService(db).get_groups()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@user_router.get('/groups/{id}', tags=['groups'], response_model=Group)
def get_group(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = UserService(db).get_group(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "No encontrado"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@user_router.post('/groups', tags=['groups'], response_model=dict, status_code=201)
def create_group(group: Group) -> dict:
    db = Session()
    UserService(db).create_group(group)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Se ha registrado el grupo"})


@user_router.put('/groups/{id}', tags=['groups'], response_model=dict, status_code=200)
def update_group(id: int, group: Group)-> dict:
    db = Session()
    result = UserService(db).get_group(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': "No encontrado"})
    
    UserService(db).update_group(id, group)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha modificado el grupo"})


@user_router.delete('/groups/{id}', tags=['groups'], response_model=dict, status_code=200)
def delete_group(id: int)-> dict:
    db = Session()
    result: User = UserService(db).get_group(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "No se encontró"})
    
    UserService(db).delete_group(id)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Se ha eliminado el grupo"})
