import csv
def cargar_paises_info():
    paises_info = []
    with open('paises.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            paises_info.append(row)
    return paises_info
def ordenar_paises_superficie():
    paises_info = cargar_paises_info()
    superficie_paises = []
    nombre_paises = []
    eleccion = int(input("Ingrese '1' para ordenar de Mayor a menor o '2' para ordenar de menor a Mayor: "))
    match eleccion:
        case 1: # Caso '1' Mayor a menor
            print("")
            for pais in paises_info:
                superficie_paises.append(float(pais.get("superficie")))
                nombre_paises.append(pais.get("nombre"))
            for i in range(len(superficie_paises)-1):
                for j in range(i+1, len(superficie_paises)):
                    if superficie_paises[i] < superficie_paises[j]:
                        superficie_paises[i], superficie_paises[j] = superficie_paises[j], superficie_paises[i]
                        nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
            for i in range(len(superficie_paises)):
                print(f"El país {nombre_paises[i]} tiene {superficie_paises[i]} Km² de superficie")
        case 2: # Caso '2' menor a Mayor
            print("")
            for pais in paises_info:
                superficie_paises.append(float(pais.get("superficie")))
                nombre_paises.append(pais.get("nombre"))
            for i in range(len(superficie_paises)-1):
                for j in range(i+1, len(superficie_paises)):
                    if superficie_paises[i] > superficie_paises[j]:
                        superficie_paises[i], superficie_paises[j] = superficie_paises[j], superficie_paises[i]
                        nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
            for i in range(len(superficie_paises)):
                print(f"El país {nombre_paises[i]} tiene {superficie_paises[i]} Km² de superficie")
        case _:
            print("Incorrecto, ingrese una opción valida.")
            