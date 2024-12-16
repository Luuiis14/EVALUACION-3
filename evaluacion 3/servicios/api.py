# servicios/api.py
import requests
from auxiliares.constantes import URL_API

def obtener_datos(tipo):
    response = requests.get(f"{URL_API}/{tipo}")
    return response.json()

def enviar_datos(tipo, datos):
    response = requests.post(f"{URL_API}/{tipo}", json=datos)
    return response.status_code
