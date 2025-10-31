import csv

def ingresar_editar_pais():
    # Primero leemos el archivo CSV existente
    paises_info = []
    try:
        with open('paises.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            paises_info = list(lector)
    except FileNotFoundError:
        # Si el archivo no existe, comenzamos con una lista vacía
        paises_info = []
    cantidad = int(input("Ingrese la cantidad de países que desea agregar o editar: "))
    for numero_pais in range(cantidad):
        nombre_pais = input(f"Ingrese el nombre del país {numero_pais + 1}: ")
        pais_existente = next((pais for pais in paises_info if pais["nombre"].lower() == nombre_pais.lower()), None)
        if pais_existente:
            print(f"El país '{nombre_pais}' ya existe. Puede editar su información.")
            poblacion = int(input("Ingrese la nueva población: "))
            superficie = float(input("Ingrese la nueva superficie: "))
            continente = input("Ingrese el nuevo continente: ")
            pais_existente["poblacion"] = str(poblacion)
            pais_existente["superficie"] = str(superficie)
            pais_existente["continente"] = continente
            print(f"Información del país '{nombre_pais}' actualizada.")
        else:
            print(f"El país '{nombre_pais}' no existe. Se agregará como un nuevo país.")
            poblacion = int(input("Ingrese la población: "))
            superficie = float(input("Ingrese la superficie: "))
            continente = input("Ingrese el continente: ")
            nuevo_pais = {
                "nombre": nombre_pais,
                "poblacion": str(poblacion),
                "superficie": str(superficie),
                "continente": continente
            }
            paises_info.append(nuevo_pais)
            print(f"País '{nombre_pais}' agregado exitosamente.")
    # Guardamos todos los cambios en el archivo CSV
    with open('paises.csv', 'w', newline='', encoding='utf-8') as archivo:
        campos = ['nombre', 'poblacion', 'superficie', 'continente']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises_info)