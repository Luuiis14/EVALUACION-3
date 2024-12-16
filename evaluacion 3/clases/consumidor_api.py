from clases.indicador_economico import IndicadorEconomico

class ConsumidorAPI:
    @staticmethod
    def consultar_indicador(nombre_indicador, fecha_inicio, fecha_fin):
        try:
            # Simulación del consumo de API
            print(f"Consultando {nombre_indicador} desde {fecha_inicio} hasta {fecha_fin}...")
            return [
                IndicadorEconomico(nombre_indicador, fecha_inicio, 100.5, "FuenteSimulada"),
                IndicadorEconomico(nombre_indicador, fecha_fin, 101.2, "FuenteSimulada")
            ]
        except Exception as e:
            print(f"Error al consultar API: {e}")
            return []
