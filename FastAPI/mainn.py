import zoneinfo

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

ciudades = {
    "AR": "America/Argentina/Buenos_Aires",
    "GT": "America/Guatemala",
    "MX": "America/Mexico_City",
    "CO": "America/Bogota",
    "ES": "España",
    "CL": "Chile"
}

@app.get("/hora/{iso_code}")
def hora(iso_code):
    clave = iso_code.upper() #upper = mayuscula
    zona_ciudad = ciudades.get(clave)
    tiempo_zona = zoneinfo.ZoneInfo(zona_ciudad)
    return {"Hora": datetime.now(tiempo_zona)}


'''
pip install uv
uv init
uv add 'fastapi[standard]'
uv run fastapi dev main.py
fastapi dev main.py
'''