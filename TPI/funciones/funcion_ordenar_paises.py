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





def ordenar_paises(paises,seleccion): #Función que ordena los países según la selección del usuario
    match seleccion: #Se usa match para elegir la función según la selección del usuario
        case 1:
            ordenar_paises_nombre(paises)
        case 2:
            ordenar_paises_poblacion(paises)
        case 3:
            ordenar_paises_superficie(paises)
        case _:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")
