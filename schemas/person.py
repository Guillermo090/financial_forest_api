from pydantic import BaseModel, Field
from typing import Optional

class Person(BaseModel):
    id: Optional[int]
    rut: str = Field(min_length=10, max_length=15) 
    nombres: str = Field(max_length=50)
    apellidos: str = Field(max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 13,
                "rut": "17585654-3",
                "nombres": "Fernando",
                "apellidos": "Cepeda",
            }
        }