from fastapi import APIRouter, HTTPException
from app.modelos.cliente import Cliente, ClienteCrear
from app.database import list_clients

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("")
def listar_clientes():
    return {"clients": list_clients}

@router.post("", response_model=Cliente)
def create_clients(date_client: ClienteCrear):
    cliente = Cliente(
        id=len(list_clients) + 1,
        name=date_client.name,
        age=date_client.age,
        description=date_client.description
    )
    list_clients.append(cliente)
    return cliente

@router.get("/{id}", response_model=Cliente)
def get_client(id: int):
    for client_item in list_clients:
        if client_item.id == id:
            return client_item
    raise HTTPException(status_code=404, detail="client not found")

@router.put("/{id}", response_model=Cliente)  
def update_client(id: int, date_client: ClienteCrear):
    for client_item in list_clients:
        if client_item.id == id:
            client_item.name = date_client.name
            client_item.age = date_client.age
            client_item.description = date_client.description
            return client_item
    raise HTTPException(status_code=404, detail="client not found")

@router.delete("/{id}", response_model=Cliente)  
def delete_client(id: int):
    for client_item in list_clients:
        if client_item.id == id:
            list_clients.remove(client_item)
            return client_item
    raise HTTPException(status_code=404, detail="client not found")
