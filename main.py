
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()
app.title = 'Financial Forest'


class Payment(BaseModel):
    id: int
    name: str



payments = [{'id':1,'name':'pepe'}, {'id':2,'name':'felo'}]
@app.get("/payments", tags=['pagos'])
def get_payments():
    return payments

@app.get("/payments/{id}", tags=['pagos'])
def get_payment(id:int):
    # Filtrar por id
    payments_filtered = filter(lambda payment: payment["id"] == id, payments)
    # Obtener el primer registro que coincida
    primer_registro = next(payments_filtered, None)
    print(primer_registro)
    return primer_registro

@app.post("/payments", tags=['pagos'])
def create_payment(id :int = Body(), name :str = Body()):
    new = {'id':id, 'name':name}
    payments.append(new)
    return new 
