from pydantic import BaseModel



class ClienteCrear(BaseModel):
    name: str
    age: int
    description: str

class Cliente(ClienteCrear):
    id: int


class FacturaCrear(BaseModel):
    fecha: str
    cliente: int
    valortotal: float

class Factura(FacturaCrear):
    id: int
    valor_total: float


class TransaccionCrear(BaseModel):
    descripcion: str
    factura: int

class Transaccion(TransaccionCrear):
    id: int