from paises_info import *
from selecciones.seleccion_filtrar_paises import *
def funcion_filtrar_paises(seleccion):

# Filtrar países por:
#           1) Continente
#           2) Rango de población
#           3) Rango de superficie
    if 1<= seleccion <=3:
        match seleccion:
            case 1:
                seleccion = int(input("\nElige una opción:\n1) África\n2) América\n3) Asia\n4) Europa\n5) Oceanía     |"))
                seleccion_filtrar_paises(seleccion)
                
            case 2:
                pass
            case 3:
                pass
        
    else:
        print("MAL")