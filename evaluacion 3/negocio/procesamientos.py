# negocio/procesamiento.py
from servicios.api import obtener_datos
from datos.crud import insertar_publicacion
from modelos.publicaciones import Publicacion

def procesar_y_guardar(tipo):
    datos = obtener_datos(tipo)
    for item in datos:
        pub = Publicacion(id=item['id'], userId=item['userId'], title=item['title'], body=item['body'])
        insertar_publicacion(pub)
