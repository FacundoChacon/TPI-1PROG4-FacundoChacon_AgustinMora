from paises_info import *
from selecciones.filtrar_paises_continente import *
from selecciones.filtrar_paises_poblacion import *
from selecciones.filtrar_paises_superficie import *
def funcion_filtrar_paises(seleccion):

# Filtrar países por:
#           1) Continente
#           2) Rango de población
#           3) Rango de superficie
    if 1<= seleccion <=3:
        match seleccion:
            case 1:
                seleccion = int(input("\nElige una opción:\n1) África\n2) América\n3) Asia\n4) Europa\n5) Oceanía \n| "))
                filtrar_paises_continente(seleccion)
            case 2:
                seleccion = int(input("Eliga una opción:\n1) Menos de 1 Millón\n2) Entre 1-10 Millones\n3) Más de 10 Millones \n| "))
                filtrar_paises_poblacion(seleccion)
            case 3:
                seleccion = int(input("\nEliga una opción:\n1) Menos de 500km\n2) Entre 500-1.000km\n3) Entre 1.000-10.000km\n4) Entre 10.000-50.000km\n5) Entre 50.000-100.000km\n6) Entre 100.000-200.000km\n7) Entre 200.000-500.000km\n8) Entre 500.000-1.000.000km\n9) Entre 1.000.000-3.000.000km\n10) Más de 3.000.000km \n| "))
                filtrar_paises_superficie(seleccion)
        
    else:
        print("MAL")