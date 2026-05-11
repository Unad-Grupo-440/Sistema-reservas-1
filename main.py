
from servicio import *
from excepcion import *
import logging

def pruebas():

    print("===== INICIO DE PRUEBAS =====\n")

    # 1. Reserva válida
    try:
        r1 = ReservaSala(2, "vip")
        print(r1.descripcion())
        print("Costo:", r1.calcular_costo())
    except Exception as e:
        logging.error(e)
        print("Error:", e)

    # 2. Reserva inválida
    try:
        r2 = ReservaSala(-1, "vip")
    except Exception as e:
        logging.error(e)
        print("Error:", e)

    # 3. Equipo válido
    try:
        eq1 = AlquilerEquipo("video beam", 3)
        print(eq1.descripcion())
        print("Costo:", eq1.calcular_costo())
    except Exception as e:
        logging.error(e)
        print("Error:", e)

    # 4. Equipo inválido
    try:
        eq2 = AlquilerEquipo("equipo falso", 3)
    except Exception as e:
        logging.error(e)
        print("Error:", e)

    # 5. Asesoría válida
    try:
        a1 = Asesoria("intermedio", 2)
        print(a1.descripcion())
        print("Costo:", a1.calcular_costo())
    except Exception as e:
        logging.error(e)
        print("Error:", e)

    # 6. Asesoría inválida
    try:
        a2 = Asesoria("nivel falso", 2)
    except Exception as e:
        logging.error(e)
        print("Error:", e)

    print("\n===== FIN DE PRUEBAS =====")


if __name__ == "__main__":
    pruebas()
