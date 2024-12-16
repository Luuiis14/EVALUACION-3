# main.py
from negocio.encriptacion import encriptar, desencriptar
from negocio.procesamientos import procesar_y_guardar
from datos.crud import obtener_publicaciones
from auxiliares.constantes import URL_API


def menu():
    while True:
        print("\nMenú Principal")
        print("1. Encriptar contraseña")
        print("2. Obtener y guardar datos de la API")
        print("3. Mostrar publicaciones guardadas")
        print("4. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            pwd = input("Ingrese la contraseña: ")
            encriptado = encriptar(pwd)
            print("Encriptado:", encriptado)
            print("Desencriptado:", desencriptar(encriptado))
        elif opcion == "2":
            procesar_y_guardar("posts")
            print("Datos guardados exitosamente.")
        elif opcion == "3":
            publicaciones = obtener_publicaciones()
            for pub in publicaciones:
                print(f"{pub.id}: {pub.title}")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
