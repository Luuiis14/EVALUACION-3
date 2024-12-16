from datetime import datetime

class RegistroIndicador:
    def __init__(self, indicador, usuario):
        self.indicador = indicador
        self.usuario = usuario
        self.fecha_registro = datetime.now()

    def __str__(self):
        return (f"Registro de Indicador: {self.indicador.nombre_indicador}, Usuario: {self.usuario.nombre_usuario}, "
                f"Fecha Registro: {self.fecha_registro}")
