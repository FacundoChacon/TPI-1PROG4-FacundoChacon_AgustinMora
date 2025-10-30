from paises_info import *
from funciones.funcion_punto_cada_tres_cifras import *
def filtrar_paises_superficie(seleccion):
#1) <1.000
#2) 1.000< x 50.000
#3) 50.000< x 500.000
#4) 500.000< x <1.000.000
#5) 1.000.000 < x
    match seleccion:
        case 1:
            print("")
            for i in range(0,len(paises_info)):
                if paises_info[i].get("superficie") <1000: #si el pais tiene menos de 1.000km entra en el if
                    print(f"{paises_info[i].get("nombre")}: tiene {paises_info[i].get("superficie")} km.")
        case 2:
            print("")
            for i in range(0,len(paises_info)):
                if 1000 <=  paises_info[i].get("superficie") <50000: #Si el país tiene entre 1.000 y 50.000km entra en el if
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
        case 3:
            print("")
            for i in range(0,len(paises_info)):
                if 50000 <=  paises_info[i].get("superficie") <500000: #Si el país tiene entre 5.000 y 500.000km entra en el if
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
        case 4:
            print("")
            for i in range(0,len(paises_info)):
                if 500000 <=  paises_info[i].get("superficie") <1000000:
                    #Si el país tiene entre 500.000 y 1.000.000km entra en el if
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
        case 5:
            print("")
            for i in range(0,len(paises_info)):
                if 1000000 <=  paises_info[i].get("superficie"): #Si el país es mayor que 1.000.000 entra en el if
                    funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                    print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
        case _:
            print("Incorrecto, ingrese una opción valida.")
            