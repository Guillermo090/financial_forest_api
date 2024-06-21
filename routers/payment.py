from fastapi import APIRouter, Depends , Path, status
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.payment import Payment, Person
from typing import  List
from middlewares.jwt_bearer import JWTBearer
from config.database import Session
from services.payment import PaymentService
from fastapi.encoders import jsonable_encoder


payment_router = APIRouter()

@payment_router.get('/payment_persons', tags=['payment_persons'], response_model=List[Person], 
    status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_payment_persons() -> List[Person]:
    db = Session()
    result = PaymentService(db).get_persons()
    return JSONResponse(status_code=status.HTTP_200_OK, 
        content=jsonable_encoder(result))

@payment_router.get('/payments', tags=['payments'], response_model=List[Payment], 
    status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())])
def get_payments() -> List[Payment]:
    db = Session()
    result = PaymentService(db).get_payments()
    return JSONResponse(status_code=status.HTTP_200_OK, 
        content=jsonable_encoder(result))