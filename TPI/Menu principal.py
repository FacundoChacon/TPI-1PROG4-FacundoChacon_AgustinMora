import csv
import os
from paises_info import * #Se importa la lista completa de los países, más su información (continente, habitantes,etc)
from funciones.funcion_buscar_pais import * #Se importa de la carpeta "funciones" la funcion para la opción 1)
from funciones.funcion_filtrar_paises import * #Se importa de la carpeta "funciones" la funcion para la opción 2)
from funciones.funcion_ordenar_paises import * #Se importa de la carpeta "funciones" la funcion para la opción 3)
from funciones.funcion_estadisticas_paises import * #Se importa de la carpeta "funciones" la funcion para la opción 4)

def armador_csv():#Se llama a la función que crea el archivo csv con la información de los países
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

def llenar_lista_local(paises):#Se llena una lista con diccionarios desde el archivo csv
    with open("paises.csv", "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append(fila)
    for i in range(0, len(paises)):
        print(paises[i].get("nombre"))

paises = []
if not os.path.exists("paises.csv"):
    armador_csv()
    llenar_lista_local(paises)
else:
    llenar_lista_local(paises)


menu=True
while menu:
    print("\n---MENU---")
    print("1) Buscar un país por nombre")
    print("2) Filtrar países")
    print("3) Ordenar países")
    print("4) Mostrar estadísticas de países")
    print("• Ingrese cualquier otro numero para salir")
    try:
        opcion = int(input("| ")) #Se le pide al usuario que ingrese una opción del menú
        match opcion: #Se evalúa la opción ingresada por el usuario
            case 1:
                seleccion = input("Ingrese un país: ").lower()
                funcion_buscar_pais(paises, seleccion)
            case 2:
                seleccion = int(input("\nFiltrar países por:\n1) Continente\n2) Rango de población\n3) Rango de superficie \n| "))
                #funcion_filtrar_paises(paises, seleccion)
            case 3:
                print("Ordenar países por:\n1) Nombre\n2) Población\n3) Superficie\n4) Agregar o editar un pais")
                seleccion = int(input("Ingrese una opción: "))
                #ordenar_paises(paises, seleccion)
            case 4:
                print("Mostrar estadísticas:\n1) País con mayor y menor población\n2) Promedio de población\n3) Promedio de superficie\n4) Cantidad de países por continente")
                seleccion = int(input("Ingrese una opción: "))
                #estadisticas(seleccion, paises)
            case _: #Cualquier otra opción ingresada por el usuario
                print("Saliendo del programa...")
                menu = False
                break
    except ValueError: print("\nSolo se permiten números enteros!","\nVolviendo al menú principal...") 