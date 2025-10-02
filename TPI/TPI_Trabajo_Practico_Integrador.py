from paises_info import * #Se importa la lista completa de los países, más su información (continente, habitantes,etc)
from funciones.funcion_buscar_pais import * #Se importa de la carpeta "funciones" la funcion para la opción 1)
from funciones.funcion_filtrar_paises import *

menu=True
paises_info_minusculas=[]

for i in range(0,len(paises_info)):
    paises_info_minusculas.append(paises_info[i]["nombre"].lower())

while menu:
    print("\n---MENU---")
    print("1) Buscar un país por nombre")
    print("2) Filtrar países")
    print("3) Ordenar países")
    print("4) Mostrar estadísticas de países")
    print("0) Ingrese 0 (cero) para salir")
    # opcion = int(input("\nIngresar la opcion deseada: "))
    opcion = int(input("| "))
    if opcion <= 5 or opcion > 0:
        match opcion:
            case 1:
                seleccion = input("Ingrese un país: ").lower()
                print(funcion_buscar_pais(paises_info_minusculas, seleccion))
            case 2:
                seleccion = int(input("\nFiltrar países por:\n1) Continente\n2) Rango de población\n3) Rango de superficie    |"))
                funcion_filtrar_paises(seleccion)
                
            case 3:
                print("Ordenar países por:\n1) Nombre\n2) Población\n3) Superficie")
                seleccion = int(input("Ingrese una opción: "))
                if 1<= seleccion <=3:
                    print("BIEN")
                else:
                    print("MAL")
                    continue
            case 4:
                print("Mostrar estadísticas:\n1) País con mayor y menor población\n2) Promedio de población\n3) Promedio de superficie\n4) Cantidad de países por continente")
                seleccion = int(input("Ingrese una opción: "))
                if 1<= seleccion <=4:
                    print("BIEN")
                else:
                    print("MAL")
                    continue
            case 0:
                print("Saliendo...")
                break
    else:
        print("\nOpción incorrecta. Ingrese un número del 1 al 5\n")
        continue