from abc import ABC, abstractmethod
from excepcion import DatosInvalidos, ServicioNoDisponible


class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# =======================
# RESERVA DE SALAS
# =======================

class ReservaSala(Servicio):

    def __init__(self, horas, tipo_sala="normal"):
        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise DatosInvalidos("Las horas deben ser mayores a 0")

        if tipo_sala.lower() not in ["normal", "vip"]:
            raise ServicioNoDisponible("Tipo de sala no disponible")

        self.horas = horas
        self.tipo_sala = tipo_sala.lower()

    def calcular_costo(self):
        precios = {"normal": 7000, "vip": 12000}
        return precios[self.tipo_sala] * self.horas

    def descripcion(self):
        return f"{self.nombre} - {self.tipo_sala} por {self.horas} horas"


# =======================
# ALQUILER DE EQUIPOS
# =======================

class AlquilerEquipo(Servicio):

    def __init__(self, equipo, dias):
        super().__init__("Alquiler de Equipos")

        equipos = ["video beam", "pantalla", "sonido"]

        if equipo.lower() not in equipos:
            raise ServicioNoDisponible("Equipo no disponible")

        if dias <= 0:
            raise DatosInvalidos("Días inválidos")

        self.equipo = equipo.lower()
        self.dias = dias

    def calcular_costo(self):
        precios = {"video beam": 20000, "pantalla": 15000, "sonido": 50000}
        return precios[self.equipo] * self.dias

    def descripcion(self):
        return f"{self.nombre} - {self.equipo} por {self.dias} días"


# =======================
# ASESORÍA
# =======================

class Asesoria(Servicio):

    def __init__(self, nivel, horas):
        super().__init__("Asesoría")

        niveles = ["basico", "intermedio", "avanzado"]

        if nivel.lower() not in niveles:
            raise ServicioNoDisponible("Nivel no válido")

        if horas <= 0:
            raise DatosInvalidos("Horas inválidas")

        self.nivel = nivel.lower()
        self.horas = horas

    def calcular_costo(self):
        tarifas = {"basico": 20000, "intermedio": 35000, "avanzado": 50000}
        return tarifas[self.nivel] * self.horas

    def descripcion(self):
        return f"{self.nombre} - {self.nivel} por {self.horas} horas"

        # Corrección de operadores y validaciones
