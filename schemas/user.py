from pydantic import BaseModel, Field
from typing import Optional 
from datetime import datetime

class LoginRequest(BaseModel):
    email: str = Field(..., max_length=50)
    password: Optional[str] = Field(None, max_length=50)

class Group(BaseModel):
    id: Optional[int] = None
    group_name: str = Field(..., max_length=50)
    details: Optional[str] = Field(None, max_length=250)
    is_active: Optional[bool] = Field(default=True)
    date_created: Optional[datetime] = Field(None)
    date_updated: Optional[datetime] = Field(None)
    # permissions = relationship('Permission', secondary='group_permissions', back_populates='groups')

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "group_name": "Administracion",
                    "details": "grupo de administradores de sistema",
                }
            ]
        }
    }


class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = Field(default=True)
    date_created: Optional[datetime] = Field(None)
    date_updated: Optional[datetime] = Field(None)
    group_id: Optional[int] = Field(None)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "guillermo",
                    "email": "guillermo@gmail.com",
                }
            ]
        },
    }


class UserCreate(BaseModel):
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)
    is_active: Optional[bool] = Field(default=True)
    group_id: Optional[int] = Field(None)

    class Config:
        orm_mode = True
        json_schema_extra = {
            "examples": [
                {
                    "username": "guillermo",
                    "email": "guillermo@gmail.com",
                }
            ]
        }