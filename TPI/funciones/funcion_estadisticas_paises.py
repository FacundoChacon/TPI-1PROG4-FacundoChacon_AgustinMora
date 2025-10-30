from paises_info import *
from selecciones.estadisticas_max_min_poblacion import *
from selecciones.estadisticas_paises_por_continente import *
from selecciones.estadisticas_promedio_poblacion import *
from selecciones.estadisticas_promedio_superficie import *
def estadisticas(seleccion,lista_paises):
    match seleccion:
        case 1:
            max_min_poblacion()
        case 2:
            pais = input("Ingrese el pais que desee buscar: \n").title()
            promedio(pais,lista_paises)
        case 3:
            promedio_superficie()
        case 4:
            paises_continente()
        case _:
            print("Se esperaba una de las opciones indicadas, intentelo de nuevo")