from servicio import Servicio
from excepciones import (
    ServicioNoDisponible,
    DatosInvalidos
)

# =========================
# SERVICIO 1 - RESERVA DE SALAS
# =========================

class ReservaSala(Servicio):

    tipos_sala = ["normal", "vip", "auditorio"]

    def __init__(
        self,
        horas,
        tipo_sala="normal",
        disponible=True,
        aire_acondicionado=False,
        internet=False,
        videobeam=False
    ):
        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise DatosInvalidos(
                "Las horas deben ser mayores a 0"
            )

        if tipo_sala.lower() not in self.tipos_sala:
            raise ServicioNoDisponible(
                "Tipo de sala no disponible"
            )

        self.horas = horas
        self.tipo_sala = tipo_sala.lower()

        self.disponible = disponible
        self.aire_acondicionado = aire_acondicionado
        self.internet = internet
        self.videobeam = videobeam

    def validar_disponibilidad(self):

        if not self.disponible:
            raise ServicioNoDisponible(
                "Sala no disponible"
            )

    def calcular_costo(self, descuento=0):

        if self.tipo_sala == "vip":
            costo = self.horas * 12000

        elif self.tipo_sala == "auditorio":
            costo = self.horas * 20000

        else:
            costo = self.horas * 7000

        total = costo - descuento

        if total < 0:
            raise DatosInvalidos(
                "El descuento no puede ser mayor al costo"
            )

        return total

    def descripcion(self):

        return (
            f"Servicio: {self.nombre} | "
            f"Tipo de sala: {self.tipo_sala} | "
            f"Horas: {self.horas} | "
            f"Disponible: {self.disponible} | "
            f"Aire acondicionado: {self.aire_acondicionado} | "
            f"Internet: {self.internet} | "
            f"Videobeam: {self.videobeam}"
        )


# =========================
# SERVICIO 2 - ALQUILER DE EQUIPOS
# =========================

class AlquilerEquipo(Servicio):

    equipos_disponibles = [

        # AUDIOVISUALES
        "video beam",
        "pantalla de proyeccion",
        "telon",
        "sistema de sonido",
        "microfono inalambrico",
        "microfono de solapa",

        # MOBILIARIO
        "sillas auditorio",
        "sillas banquete",
        "mesa redonda",
        "mesa rectangular",
        "mesa coctel",
        "sillones",

        # GESTION Y CONECTIVIDAD
        "pantalla tactil",
        "software de eventos",
        "wifi empresarial",

        # AMBIENTE
        "aire acondicionado",
        "calefaccion",
        "iluminacion regulable"
    ]

    def __init__(self, equipo, dias):
        super().__init__("Alquiler de Equipos")

        if dias <= 0:
            raise DatosInvalidos(
                "Los días deben ser mayores a 0"
            )

        if equipo.lower() not in self.equipos_disponibles:
            raise ServicioNoDisponible(
                f"El equipo '{equipo}' no está disponible"
            )

        self.equipo = equipo.lower()
        self.dias = dias

    def validar_disponibilidad(self):
        pass

    def calcular_costo(self, impuesto=0):

        precios = {
            "video beam": 20000,
            "pantalla de proyeccion": 15000,
            "telon": 10000,
            "sistema de sonido": 70000,
            "microfono inalambrico": 15000,
            "microfono de solapa": 18000,
            "sillas auditorio": 5000,
            "sillas banquete": 7000,
            "mesa redonda": 10000,
            "mesa rectangular": 9000,
            "mesa coctel": 12000,
            "sillones": 15000,
            "pantalla tactil": 40000,
            "software de eventos": 60000,
            "wifi empresarial": 25000,
            "aire acondicionado": 35000,
            "calefaccion": 30000,
            "iluminacion regulable": 28000
        }

        costo_base = precios[self.equipo] * self.dias

        total = costo_base + impuesto

        return total

    def descripcion(self):

        return (
            f"Servicio: {self.nombre} | "
            f"Equipo: {self.equipo} | "
            f"Días: {self.dias}"
        )


# =========================
# SERVICIO 3 - ASESORIAS ESPECIALIZADAS
# =========================

class Asesoria(Servicio):

    niveles_validos = [
        "basico",
        "intermedio",
        "avanzado"
    ]

    def __init__(
        self,
        nivel,
        horas,
        experto_certificado=True
    ):
        super().__init__("Asesoría Especializada")

        if nivel.lower() not in self.niveles_validos:
            raise ServicioNoDisponible(
                "Nivel de asesoría inválido"
            )

        if horas <= 0:
            raise DatosInvalidos(
                "Las horas deben ser mayores a 0"
            )

        self.nivel = nivel.lower()
        self.horas = horas
        self.experto_certificado = experto_certificado

    def validar_disponibilidad(self):

        if not self.experto_certificado:
            raise ServicioNoDisponible(
                "Asesor no certificado"
            )

    def calcular_costo(
        self,
        descuento=0,
        impuesto=0
    ):

        if self.nivel == "basico":
            valor_hora = 20000

        elif self.nivel == "intermedio":
            valor_hora = 35000

        else:
            valor_hora = 50000

        subtotal = valor_hora * self.horas

        total = subtotal - descuento + impuesto

        if total < 0:
            raise DatosInvalidos(
                "El total no puede ser negativo"
            )

        return total

    def descripcion(self):

        return (
            f"Servicio: {self.nombre} | "
            f"Nivel: {self.nivel} | "
            f"Horas: {self.horas} | "
            f"Experto certificado: {self.experto_certificado}"
        )


# =========================
# SERVICIO 4 - SERVICIOS COMPLEMENTARIOS
# =========================

class ServicioComplementario(Servicio):

    servicios_disponibles = [
        "parqueadero",
        "zona de registro",
        "soporte tecnico"
    ]

    def __init__(self, servicio, cantidad_horas):
        super().__init__("Servicio Complementario")

        if servicio.lower() not in self.servicios_disponibles:
            raise ServicioNoDisponible(
                "Servicio complementario no disponible"
            )

        if cantidad_horas <= 0:
            raise DatosInvalidos(
                "Las horas deben ser mayores a 0"
            )

        self.servicio = servicio.lower()
        self.cantidad_horas = cantidad_horas

    def calcular_costo(self):

        costos = {
            "parqueadero": 7500,
            "zona de registro": 15000,
            "soporte tecnico": 40000
        }

        return (
            costos[self.servicio]
            * self.cantidad_horas
        )

    def descripcion(self):

        return (
            f"Servicio: {self.servicio} | "
            f"Horas: {self.cantidad_horas}"
        )