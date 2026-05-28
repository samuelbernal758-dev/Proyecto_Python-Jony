from fastapi import FastAPI
from app.modelos.cliente import (
    Cliente, ClienteCrear,
    Factura, FacturaCrear,
    Transaccion, TransaccionCrear
)

app = FastAPI()

list_clients: list[Cliente] = []
list_facturas: list[Factura] = []
list_transacciones: list[Transaccion] = []


@app.get("/")
def home():
    return {"message": "Welcome to the Clientes API!"}


@app.get("/clientes")
def listar_clientes():
    return {"clients": list_clients}


@app.post("/clientes", response_model=Cliente)
def create_clients(date_client: ClienteCrear):
    cliente = Cliente(
        id=len(list_clients) + 1,
        name=date_client.name,
        age=date_client.age,
        description=date_client.description
    )
    list_clients.append(cliente)
    return cliente


@app.get("/clientes/{id}", response_model=Cliente)
def get_client(id: int):
    for client_item in list_clients:
        if client_item.id == id:
            return client_item
    return {"message": "client not found"}  


@app.put("/clientes/{id}", response_model=Cliente)  
def update_client(id: int, date_client: ClienteCrear):
    for client_item in list_clients:
        if client_item.id == id:
            client_item.name = date_client.name
            client_item.age = date_client.age
            client_item.description = date_client.description
            return client_item
    return {"message": "client not found"}  


@app.delete("/clientes/{id}", response_model=Cliente)  
def delete_client(id: int):
    for client_item in list_clients:
        if client_item.id == id:
            list_clients.remove(client_item)
            return client_item
    return {"message": "client not found"}  


@app.get("/facturas")  
def lista_facturas():
    return {"facturas": list_facturas}


@app.post("/facturas", response_model=Factura)
def create_factura(data_factura: FacturaCrear):
    factura_val = Factura(
        id=len(list_facturas) + 1,
        fecha=data_factura.fecha,
        cliente=data_factura.cliente,
        valor_total=data_factura.valortotal
    )
    list_facturas.append(factura_val)
    return factura_val


@app.get("/transacciones")  
def listar_transacciones():
    return {"transacciones": list_transacciones}


@app.post("/transacciones", response_model=Transaccion)
def create_transaccion(data_transaccion: TransaccionCrear):
    transaccion_val = Transaccion(
        id=len(list_transacciones) + 1,
        descripcion=data_transaccion.descripcion,
        factura=data_transaccion.factura
    )
    list_transacciones.append(transaccion_val)
    return transaccion_val