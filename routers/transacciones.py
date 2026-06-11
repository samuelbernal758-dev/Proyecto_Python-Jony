from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Transaccion, TransaccionCrear
from app.database import list_transacciones

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

@router.get("")  
def listar_transacciones():
    return {"transacciones": list_transacciones}

@router.post("", response_model=Transaccion)
def create_transaccion(data_transaccion: TransaccionCrear):
    transaccion_val = Transaccion(
        id=len(list_transacciones) + 1,
        descripcion=data_transaccion.descripcion,
        factura=data_transaccion.factura
    )
    list_transacciones.append(transaccion_val)
    return transaccion_val

@router.put("/{id}", response_model=Transaccion)
def update_transaccion(id: int, data_transaccion: TransaccionCrear):
    for transaccion_val in list_transacciones:
        if transaccion_val.id == id:
            transaccion_val.descripcion = data_transaccion.descripcion
            transaccion_val.factura = data_transaccion.factura
            return transaccion_val
    raise HTTPException(status_code=404, detail="transaccion not found")

@router.delete("/{id}", response_model=Transaccion)
def delete_transaccion(id: int):
    for transaccion_val in list_transacciones:
        if transaccion_val.id == id:
            list_transacciones.remove(transaccion_val)
            return transaccion_val
    raise HTTPException(status_code=404, detail="transaccion not found")
