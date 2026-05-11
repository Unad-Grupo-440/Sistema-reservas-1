from excepcion import DatosInvalidos


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def confirmar(self):
        if self.estado != "pendiente":
            raise DatosInvalidos("La reserva ya fue procesada")

        self.estado = "confirmada"

    def cancelar(self):
        if self.estado == "cancelada":
            raise DatosInvalidos("Ya está cancelada")

        self.estado = "cancelada"

    def descripcion(self):
        return f"Reserva de {self.cliente} - Estado: {self.estado}"
        
        # Corrección de operadores y validaciones
