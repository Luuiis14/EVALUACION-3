# datos/crud.py
from modelos.publicaciones import Base, Publicacion
from datos.conexión import engine, session

Base.metadata.create_all(engine)

def insertar_publicacion(publicacion):
    session.add(publicacion)
    session.commit()

def obtener_publicaciones():
    return session.query(Publicacion).all()
