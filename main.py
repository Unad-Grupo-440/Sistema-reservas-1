
from servicio import *
from excepcion import *
import logging


def pruebas():

    print("==== INICIO PRUEBAS ====\n")

    # 1
    try:
        s = ReservaSala(2, "vip")
        print(s.descripcion())
        print(s.calcular_costo())
    except Exception as e:
        logging.error(e)

    # 2
    try:
        ReservaSala(-1, "vip")
    except Exception as e:
        logging.error(e)

    # 3
    try:
        e = AlquilerEquipo("video beam", 2)
        print(e.descripcion())
        print(e.calcular_costo())
    except Exception as e:
        logging.error(e)

    # 4
    try:
        AlquilerEquipo("fake", 2)
    except Exception as e:
        logging.error(e)

    # 5
    try:
        a = Asesoria("intermedio", 3)
        print(a.descripcion())
        print(a.calcular_costo())
    except Exception as e:
        logging.error(e)

    # 6
    try:
        Asesoria("malo", 3)
    except Exception as e:
        logging.error(e)

    print("\n==== FIN PRUEBAS ====")


if __name__ == "__main__":
    pruebas()

