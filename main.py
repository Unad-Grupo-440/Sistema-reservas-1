from servicios import ReservaSala, AlquilerEquipo, Asesoria, ServicioComplementario

def pruebas():
    print("=== PRUEBAS DEL SISTEMA ===\n")

    try:
        # PRUEBA RESERVA SALA
        reserva = ReservaSala(2, "vip")
        print(reserva.descripcion())
        print("Costo:", reserva.calcular_costo())
        print("\n-----------------\n")

        # PRUEBA ALQUILER EQUIPO
        equipo = AlquilerEquipo("video beam", 3)
        print(equipo.descripcion())
        print("Costo:", equipo.calcular_costo())
        print("\n-----------------\n")

        # PRUEBA ASESORIA
        asesoria = Asesoria("intermedio", 2)
        print(asesoria.descripcion())
        print("Costo:", asesoria.calcular_costo())
        print("\n-----------------\n")

        # PRUEBA SERVICIO COMPLEMENTARIO
        servicio = ServicioComplementario("parqueadero", 5)
        print(servicio.descripcion())
        print("Costo:", servicio.calcular_costo())

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    pruebas()
# Corrección de operadores y validaciones.

