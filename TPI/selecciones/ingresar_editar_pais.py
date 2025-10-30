from paises_info import *
def ingresar_editar_pais():
    cantidad = int(input("Ingrese la cantidad de países que desea agregar o editar: "))
    for numero_pais in range(cantidad):
        nombre_pais = input(f"Ingrese el nombre del país {numero_pais + 1}: ")
        pais_existente = next((pais for pais in paises_info if pais["nombre"].lower() == nombre_pais.lower()), None)
        
        if pais_existente:
            print(f"El país '{nombre_pais}' ya existe. Puede editar su información.")
            poblacion = int(input("Ingrese la nueva población: "))
            superficie = float(input("Ingrese la nueva superficie: "))
            continente = input("Ingrese el nuevo continente: ")
            
            pais_existente["poblacion"] = poblacion
            pais_existente["superficie"] = superficie
            pais_existente["continente"] = continente
            print(f"Información del país '{nombre_pais}' actualizada.")
        else:
            print(f"El país '{nombre_pais}' no existe. Se agregará como un nuevo país.")
            poblacion = int(input("Ingrese la población: "))
            superficie = float(input("Ingrese la superficie: "))
            continente = input("Ingrese el continente: ")
            
            nuevo_pais = {
                "nombre": nombre_pais,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            }
            # print(f"País '{nombre_pais}' agregado exitosamente.")
            # with open("paises_info.py", "a") as archivo:
            #     archivo.writelines(nuevo_pais)