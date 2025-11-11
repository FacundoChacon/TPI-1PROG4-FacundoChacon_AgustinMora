import csv
from funciones.funcion_buscar_pais import *

def ingresar_editar_pais(paises): 
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
        return
    else:
        nuevo_nombre = entrada
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