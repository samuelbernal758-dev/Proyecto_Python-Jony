from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Factura, FacturaCrear
from app.database import list_facturas

router = APIRouter(prefix="/facturas", tags=["Facturas"])

@router.get("")  
def lista_facturas():
    return {"facturas": list_facturas}

@router.post("", response_model=Factura)
def create_factura(data_factura: FacturaCrear):
    factura_val = Factura(
        id=len(list_facturas) + 1,
        fecha=data_factura.fecha,
        cliente=data_factura.cliente,
        valor_total=data_factura.valortotal
    )
    list_facturas.append(factura_val)
    return factura_val

@router.put("/{id}", response_model=Factura)
def update_factura(id: int, data_factura: FacturaCrear):
    for factura_item in list_facturas:
        if factura_item.id == id:
            factura_item.fecha = data_factura.fecha
            factura_item.cliente = data_factura.cliente
            factura_item.valor_total = data_factura.valortotal
            return factura_item
    raise HTTPException(status_code=404, detail="factura not found")

@router.delete("/{id}", response_model=Factura)
def delete_factura(id: int):
    for factura_item in list_facturas:
        if factura_item.id == id:
            list_facturas.remove(factura_item)
            return factura_item
    raise HTTPException(status_code=404, detail="factura not found")
