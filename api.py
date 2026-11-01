from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Compra(BaseModel):
    precio: float
    descuento: float

@app.post("/compra")
def procesar_compra(compra: Compra):
    if compra.precio < 0:
        raise HTTPException(400, "Precio invalido")
    if not 0 <= compra.descuento <= 100:
        raise HTTPException(400, "Descuento invalido")
    subtotal = compra.precio * (
        1 - compra.descuento / 100
    )
    total = round(subtotal * 1.16, 2)
    return {"total": total}