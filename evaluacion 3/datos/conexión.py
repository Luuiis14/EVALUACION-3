# datos/conexion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mi_base.db")
Session = sessionmaker(bind=engine)
session = Session()

def obtener_datos_api():
    print("\nSeleccione tipo de datos:")
    print("1. Posts")
    print("2. Comentarios")
    print("3. Álbumes")
    print("4. Fotos")
    print("5. Tareas")
    print("6. Usuarios")
    
    opcion = input("Elija una opción: ")
    
    datos_api = {
        '1': JSONPlaceholderService.obtener_posts,
        '2': JSONPlaceholderService.obtener_comentarios,
        '3': JSONPlaceholderService.obtener_albums,
        '4': JSONPlaceholderService.obtener_fotos,
        '5': JSONPlaceholderService.obtener_tareas,
        '6': JSONPlaceholderService.obtener_usuarios
    }
    
    if opcion in datos_api:
        datos = datos_api[opcion]()
        print(f"Se obtuvieron {len(datos)} registros")
    else:
        print("Opción inválida")

def enviar_datos_api():
    nuevo_post = {
        'title': input("Ingrese título del post: "),
        'body': input("Ingrese contenido del post: "),
        'userId': int(input("Ingrese ID de usuario: "))
    }
    
    respuesta = JSONPlaceholderService.crear_post(nuevo_post)
    print("Respuesta de la API:", respuesta)
