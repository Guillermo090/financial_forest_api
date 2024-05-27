from pydantic import BaseModel, Field
from typing import Optional 
from datetime import datetime

class LoginRequest(BaseModel):
    email: str = Field(..., max_length=50)
    password: Optional[str] = Field(None, max_length=50)

class User(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = Field(None, max_length=50)
    email: str = Field(..., max_length=50)
    password: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = Field(default=True)
    date_created: Optional[datetime] = Field(None)
    date_updated: Optional[datetime] = Field(None)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "guillermo",
                    "email": "guillermo@gmail.com",
                }
            ]
        }
    }