import csv
from funciones.funcion_punto_cada_tres_cifras import *

def max_min_poblacion():
    poblacion = []
    nombre_paises = []
    # Leer el archivo CSV
    with open('paises.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            poblacion.append(int(row['poblacion']))
            nombre_paises.append(row['nombre'])
    # Ordenar por población
    for i in range(0, len(poblacion)-1):
        for j in range(i+1, len(poblacion)):
            if poblacion[i] > poblacion[j]:
                poblacion[i], poblacion[j] = poblacion[j], poblacion[i]
                nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
            else:
                poblacion[i], poblacion[j] = poblacion[j], poblacion[i]
                nombre_paises[j], nombre_paises[i]
    # Acomodar los paises por mayor y menor
    for i in range(len(poblacion)-1):
        for j in range(i+1, len(poblacion)):
            if poblacion[i] < poblacion[j]:  # Changed to < for descending order
                poblacion[i], poblacion[j] = poblacion[j], poblacion[i]
                nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
    # Print max and min with formatted numbers and index position
    # Hacer print del Max ymin con numero formateado
    print(f"\nEl país con más población es '{nombre_paises[0]}' y tiene {funcion_punto_cada_tres_cifras(poblacion[0],poblacion[0])} habitantes")
    print(f"El país con menor población es '{nombre_paises[-1]}' y tiene {funcion_punto_cada_tres_cifras(poblacion[-1],poblacion[-1])} habitantes")
    