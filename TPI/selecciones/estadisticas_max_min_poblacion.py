import csv
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
                nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
    print(f"\nEl pais con más poblacion es '{nombre_paises[0]}' y tiene {poblacion[0]}")
    print(f"El pais con menor poblacion es '{nombre_paises[len(nombre_paises)-1]}' y tiene {poblacion[len(poblacion)-1]}")