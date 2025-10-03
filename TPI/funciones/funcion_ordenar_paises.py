from paises_info import *
from selecciones.ordenar_paises_nombre import *
from selecciones.ordenar_paises_poblacion import *
from selecciones.ordenar_paises_superficie import *
def ordenar_paises(seleccion): #Función que ordena los países según la selección del usuario
    match seleccion: #Se usa match para elegir la función según la selección del usuario
        case 1:
            ordenar_paises_nombre()
        case 2:
            ordenar_paises_poblacion()
        case 3:
            ordenar_paises_superficie()
        case _:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")