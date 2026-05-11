from excepcion import DatosInvalidos


class Cliente:

    def __init__(self, nombre):
        if not nombre:
            raise DatosInvalidos("Nombre inválido")

        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if not nombre:
            raise DatosInvalidos("Nombre inválido")

        self._nombre = nombre

# Corrección de operadores y validaciones
