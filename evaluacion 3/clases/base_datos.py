class BaseDatos:
    def __init__(self):
        self.usuarios = []
        self.empleados = []
        self.indicadores = []
        self.registros = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_indicador(self, indicador):
        self.indicadores.append(indicador)

    def agregar_registro(self, registro):
        self.registros.append(registro)
