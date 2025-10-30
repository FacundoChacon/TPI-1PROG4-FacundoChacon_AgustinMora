from paises_info import *
from selecciones.filtrar_paises_continente import *
from selecciones.filtrar_paises_poblacion import *
from selecciones.filtrar_paises_superficie import *
def funcion_filtrar_paises(seleccion):

# Filtrar países por:
#           1) Continente
#           2) Rango de población
#           3) Rango de superficie
    match seleccion:
        case 1:
            seleccion = int(input("\nElige una opción:\n1) África\n2) América\n3) Asia\n4) Europa\n5) Oceanía \n| "))
            filtrar_paises_continente(seleccion)
        case 2:
            seleccion = int(input("\nElige una opción:\n1) Menos de 1 Millón\n2) Entre 1-10 Millones\n3) Más de 10 Millones \n| "))
            filtrar_paises_poblacion(seleccion)
        case 3:
            seleccion = int(input("\nElige una opción:\n \
1) Menos de 1.000km \n \
2) Entre 1.000-50.000km\n \
3) Entre 50.000-500.000km\n \
4) Entre 500.000-1.000.000km\n \
5) Más de 1.000.000km \n| "))
            filtrar_paises_superficie(seleccion)
        case _:
            print("Opción inválida, vuelva a intentarlo.")
            return
        