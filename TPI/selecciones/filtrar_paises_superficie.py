import csv
from funciones.funcion_punto_cada_tres_cifras import *

def filtrar_paises_superficie(seleccion):
    # Leer el archivo CSV y almacenar los países en una lista
    paises = []
    with open('paises.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        paises = list(reader)  # Convertir el lector a una lista
    # Filtrar países según la superficie y la opción seleccionada
    match seleccion:
        case 1:
            print("")  # Espacio en blanco para mejor legibilidad
            for pais in paises:
                # Mostrar países con superficie menor a 1000 km²
                if float(pais['superficie']) < 1000:
                    print(f"{pais['nombre']}: tiene {pais['superficie']} km.")
        case 2:
            print("")
            for i, pais in enumerate(paises):
                superficie = float(pais['superficie'])
                # Mostrar países con superficie entre 1000 y 50000 km²
                if 1000 <= superficie < 50000:
                    superficie_formateada = funcion_punto_cada_tres_cifras(i, superficie)
                    print(f"{pais['nombre']}: tiene {superficie_formateada} km")
        case 3:
            print("")
            for i, pais in enumerate(paises):
                superficie = float(pais['superficie'])
                # Mostrar países con superficie entre 50000 y 500000 km²
                if 50000 <= superficie < 500000:
                    superficie_formateada = funcion_punto_cada_tres_cifras(i, superficie)
                    print(f"{pais['nombre']}: tiene {superficie_formateada} km")
        case 4:
            print("")
            for i, pais in enumerate(paises):
                superficie = float(pais['superficie'])
                # Mostrar países con superficie entre 500000 y 1000000 km²
                if 500000 <= superficie < 1000000:
                    superficie_formateada = funcion_punto_cada_tres_cifras(i, superficie)
                    print(f"{pais['nombre']}: tiene {superficie_formateada} km")
        case 5:
            print("")
            for i, pais in enumerate(paises):
                superficie = float(pais['superficie'])
                # Mostrar países con superficie mayor o igual a 1000000 km²
                if 1000000 <= superficie:
                    superficie_formateada = funcion_punto_cada_tres_cifras(i, superficie)
                    print(f"{pais['nombre']}: tiene {superficie_formateada} km")
        case _:
            # Mensaje de error para opción no válida
            print("Incorrecto, ingrese una opción valida.")