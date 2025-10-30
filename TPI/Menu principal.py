from paises_info import * #Se importa la lista completa de los países, más su información (continente, habitantes,etc)
from funciones.funcion_buscar_pais import * #Se importa de la carpeta "funciones" la funcion para la opción 1)
from funciones.funcion_filtrar_paises import * #Se importa de la carpeta "funciones" la funcion para la opción 2)
from funciones.funcion_ordenar_paises import * #Se importa de la carpeta "funciones" la funcion para la opción 3)
from funciones.funcion_estadisticas_paises import * #Se importa de la carpeta "funciones" la funcion para la opción 4)
from armador_csv import * #Se importa la función que crea el archivo csv

armador_csv() #Se llama a la función que crea el archivo csv con la información de los países
paises_info_minusculas=[]
for i in range(0,len(paises_info)):
    paises_info_minusculas.append(paises_info[i]["nombre"].lower())

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
            case 1: #Buscar un país por nombre
                seleccion = input("Ingrese un país: ").lower()
                print(funcion_buscar_pais(paises_info_minusculas, seleccion))
            case 2: #Filtrar países
                seleccion = int(input("\nFiltrar países por:\n1) Continente\n2) Rango de población\n3) Rango de superficie \n| "))
                funcion_filtrar_paises(seleccion)
                
            case 3: #Ordenar países
                print("Ordenar países por:\n1) Nombre\n2) Población\n3) Superficie\n4) Agregar o editar un pais")
                seleccion = int(input("Ingrese una opción: "))
                ordenar_paises(seleccion)
            case 4: #Mostrar estadísticas de países
                print("Mostrar estadísticas:\n1) País con mayor y menor población\n2) Promedio de población\n3) Promedio de superficie\n4) Cantidad de países por continente")
                seleccion = int(input("Ingrese una opción: "))
                estadisticas(seleccion,paises_info_minusculas)
            case _: #Cualquier otra opción ingresada por el usuario
                print("Saliendo del programa...")
                menu = False
                break
                #Se cambia el valor de la variable "menu" a False para que el bucle termine y el programa finalice
                #Se utiliza "break" para salir del bucle inmediatamente
    except ValueError: print("\nSolo se permiten números enteros!","\nVolviendo al menú principal...") 