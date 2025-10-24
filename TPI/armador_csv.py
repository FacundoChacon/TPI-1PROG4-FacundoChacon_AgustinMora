from paises_info import *
import csv

def armador_csv():
    paises_copia = [pais.copy() for pais in paises_info]  # copia superficial de diccionarios
    for pais in paises_copia:
        # Asegura que la superficie se guarde como float con dos decimales
        pais["superficie"] = float("{:.2f}".format(pais["superficie"]))
    
    with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises_copia)
    
    paises_copia = [pais.copy() for pais in paises_info]  # copia superficial de diccionarios

    for pais in paises_copia:
        # Asegura que la superficie se guarde como float con dos decimales
        pais["superficie"] = float("{:.2f}".format(pais["superficie"]))
    with open("paises.csv", mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises_copia)