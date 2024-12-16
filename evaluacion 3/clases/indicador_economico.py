class IndicadorEconomico:
    def __init__(self, nombre_indicador, fecha_consulta, valor, fuente):
        self.nombre_indicador = nombre_indicador
        self.fecha_consulta = fecha_consulta
        self.valor = valor
        self.fuente = fuente

    def __str__(self):
        return (f"Indicador: {self.nombre_indicador}, Fecha: {self.fecha_consulta}, Valor: {self.valor}, "
                f"Fuente: {self.fuente}")
