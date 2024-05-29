from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_token
from utils.bcrypt_pwd import hash_password, check_password
from services.user import UserService
from config.database import Session

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if not auth.credentials:
            raise HTTPException(status_code=403, detail="Credenciales son requeridas")
      
        token = auth.credentials
        data = validate_token(token)
        if data is None:
            raise HTTPException(status_code=403, detail="Token inválido o expirado")
        return data
