import csv
from funciones.funcion_buscar_pais import *

def ordenar_paises_nombre(paises): #1
    for fila in paises:
        print(f"{fila.get("nombre")}")

def ordenar_paises_poblacion(paises): #2
    for fila in paises:
        print(f"El pais '{fila.get("nombre")}' tiene: {fila.get("poblacion")} habitantes")

def ordenar_paises_superficie(paises): #3
    seleccion = int(input("\nElige una opción:\n1) Mayor a menor (Descendente)\n2) menor a Mayor (Ascendente)\n| "))
    match seleccion:
        case 1:
            lista1=[]
            for fila in paises:
                try:
                    superficie1 = float(fila.get("superficie", 0))
                except (TypeError, ValueError):
                    superficie1 = 0.0
                nombre1 = fila.get("nombre","Desconocido")
                lista1.append((superficie1,nombre1))
                lista1_ordenada = sorted(lista1, reverse=True)
                
                for superficie1,nombre1 in lista1_ordenada:
                    print(f"El pais {nombre1} tiene: {superficie1}")
        case 2:
            contador=0
            lista1=[]
            for fila in paises:
                try:
                    superficie1 = float(fila.get("superficie", 0))
                except (TypeError, ValueError):
                    superficie1 = 0.0
                nombre1 = fila.get("nombre","Desconocido")
                lista1.append((superficie1,nombre1))
                lista1_ordenada = sorted(lista1)
                
                for superficie1,nombre1 in lista1_ordenada:
                    if contador<=1:
                        # print(nombre1)
                        print(f"El pais {nombre1} tiene: {superficie1}")
                        pass
                    if nombre1 == "Rusia":
                        # print("\nLOL\nLOL\nLOL\nLOL\nLOL")
                        contador+=1


def ingresar_editar_pais(paises): #4
    entrada = input("Ingrese el nombre del pais a modificar o un nombre nuevo si quiere agregar: ")
    nombres = []
    for i in range(len(paises)):
        nombres.append(normalize(paises[i].get("nombre")))
    # print(nombres)
    for i in range(0, len(paises)):
        if normalize(entrada) in normalize(paises[i].get("nombre")):
            entrada=normalize(paises[i].get("nombre"))
    
    if bool(funcion_buscar_pais(paises,entrada)):
        indice = nombres.index(entrada)
        nuevo_nombre = input("Ingrese el nuevo nombre del país: ")
        nueva_poblacion = input("Ingrese la nueva población del país: ")
        nueva_superficie = input("Ingrese la nueva superficie del país: ")
        nuevo_continente = input("Ingrese el nuevo continente del país: ")
        paises[indice]["nombre"] = nuevo_nombre.title()
        paises[indice]["poblacion"] = nueva_poblacion
        paises[indice]["superficie"] = nueva_superficie
        paises[indice]["continente"] = nuevo_continente
        print(f"El país '{entrada.title()}' ha sido modificado.")
        with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            if campos == "superficie":
                # Asegura que la superficie se guarde como float con dos decimales
                paises[indice]["superficie"] = float("{:.2f}".format(float(paises[indice]["superficie"])))
            escritor.writerows(paises)
    elif not bool(funcion_buscar_pais(paises,entrada)):
        nuevo_nombre = input("Ingrese el nombre del nuevo país: ")
        nueva_poblacion = input("Ingrese la población del nuevo país: ")
        nueva_superficie = input("Ingrese la superficie del nuevo país: ")
        nuevo_continente = input("Ingrese el continente del nuevo país: ")
        nuevo_pais = {
            "nombre": nuevo_nombre.title(),
            "poblacion": nueva_poblacion,
            "superficie": nueva_superficie,
            "continente": nuevo_continente
        }
        paises.append(nuevo_pais)
        print(f"El país '{nuevo_nombre.title()}' ha sido agregado.")
        with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            paises_copia = [pais.copy() for pais in paises]  # copia superficial de diccionarios
            for pais in paises_copia:
                # Asegura que la superficie se guarde como float con dos decimales
                pais["superficie"] = float("{:.2f}".format(float(pais["superficie"])))
            escritor.writerows(paises_copia)


def ordenar_paises(paises,seleccion): #Función que ordena los países según la selección del usuario
    match seleccion: #Se usa match para elegir la función según la selección del usuario
        case 1:
            ordenar_paises_nombre(paises)
        case 2:
            ordenar_paises_poblacion(paises)
        case 3:
            ordenar_paises_superficie(paises)
        case 4:
            ingresar_editar_pais(paises)
        case _:
            print("Opción no válida. Por favor, elija 1, 2, 3 o 4.")
