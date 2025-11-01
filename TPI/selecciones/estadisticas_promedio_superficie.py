import csv
from funciones.funcion_punto_cada_tres_cifras import *

def promedio_superficie():
    # Inicializar variables para suma de superficies y contador de países
    superficie = 0
    pais_count = 0
    # Leer archivo CSV con datos de países
    with open('paises.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            pais = row.get("nombre")
            # Procesar todos los países (la condición if/elif es redundante)
            if pais != "Rusia" and pais != "Turquía":
                superficie += float(row.get("superficie", 0))
                pais_count += 1
            elif pais == "Rusia" or pais == "Turquía":
                superficie += float(row.get("superficie", 0))
                pais_count += 1
    if pais_count > 0:# Calcular promedio si hay países
        dividir = superficie / pais_count
    else:
        dividir = 0
    # Formatear números con separadores de miles y decimales
    dividir = str(f"{dividir:.2f}")
    nuevo_dividir = dividir[:3] + "." + dividir[3:6] + "," + dividir[7:]
    superficie = str(superficie)
    nuevo_superficie = superficie[:3] + "." + superficie[3:6] + "." + superficie[6:9] + "," + superficie[10:]
    # Mostrar resultados
    print(f"La suma de todas las superficies del mundo es: {nuevo_superficie}")
    print(f"El promedio de la superficie de todos los paises del mundo es: {nuevo_dividir}")