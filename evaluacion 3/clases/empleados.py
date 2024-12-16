from clases.usuario import Usuario
from datetime import datetime

class Empleado(Usuario):
    def __init__(self, nombre_usuario, contrasena_hash, nombre_completo, correo, telefono=None, puesto=None):
        super().__init__(nombre_usuario, contrasena_hash, tipo_usuario="Empleado")
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.telefono = telefono
        self.puesto = puesto
        self.fecha_registro = datetime.now()

    def __str__(self):
        return (f"Empleado: {self.nombre_completo}, Correo: {self.correo}, Puesto: {self.puesto}, "
                f"Registrado: {self.fecha_registro}")
