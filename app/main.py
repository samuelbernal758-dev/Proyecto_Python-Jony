from fastapi import FastAPI
from routers import cliente, facturas, transacciones

app = FastAPI()

# Registrar los enrutadores modulares
app.include_router(cliente.router)
app.include_router(facturas.router)
app.include_router(transacciones.router)

@app.get("/")
def home():
 return {"message": "Welcome to the Clientes API!"}
