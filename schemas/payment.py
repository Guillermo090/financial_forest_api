from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Person(BaseModel):
    id: Optional[int] = Field(None)
    rut: str = Field(..., max_length=15)
    name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=100)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "name": "guillermo",
                    "last_name": "Royo Rivera",
                }
            ]
        }


class Payment(BaseModel):
    id: Optional[int] = Field(None)
    date_payment: Optional[datetime] = Field(None)
    creditor_id: int = Field(...)
    debtor_id: int = Field(...)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "date_payment": "2024-01-01T01:12:15",
                    "creditor_id": 1,
                    "debtor_id": 2,
                }
            ]
        }