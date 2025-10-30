from paises_info import *
from funciones.funcion_punto_cada_tres_cifras import *

def filtrar_paises_poblacion(seleccion):
#1) Menos de 1 Millón
#2) Entre 1-10 Millones
#3) Más de 10 Millones
    # print("")
    match seleccion:
        case 1:
            print("")
            for i in range(0,len(paises_info)):
                if paises_info[i].get("poblacion") < 1000000:
                    #Si hay menos de 1.000.000 de habitantes entra en el if
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("poblacion"))
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("poblacion"))} habitantes.")
        case 2:
            print("")
            for i in range(0,len(paises_info)):
                if 1000000 < paises_info[i].get("poblacion") < 10000000:
                    #Si hay 1.000.000 y 10.000.000 de habitantes entra en el if
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("poblacion"))
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("poblacion"))} habitantes.")
        case 3:
            print("")
            for i in range(0,len(paises_info)):
                #Si hay más de 10.000.000 de habitantes entra en el if
                if 10000000 < paises_info[i].get("poblacion"):
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("poblacion"))
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("poblacion"))} habitantes.")
        case _:
            print("Incorrecto, ingrese una opción valida.")
            