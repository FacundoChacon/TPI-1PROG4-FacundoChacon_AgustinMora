from paises_info import *
from funciones.funcion_punto_cada_tres_cifras import *
def filtrar_paises_superficie(seleccion):
#1)      <500
#2) 500< x <1.000
#3) 1.000< x <10.000
#4) 10.000< x <50.000
#5) 50.000< x <100.000
#6) 100.000< x <200.000
#7) 200.000< x <500.000
#8) 500.000< x <1.000.000
#9) 1.000.000< x <3.000.000
#10) 3.000.000 < x
    if 1<= seleccion <=10:
        print("")
        match seleccion:
            case 1:
                for i in range(0,len(paises_info)):
                    if paises_info[i].get("superficie") <500:
                        #si el pais tiene menos de 500km entra en el if
                        print(f"{paises_info[i].get("nombre")}: tiene {paises_info[i].get("superficie")} km.")
            case 2:
                for i in range(0,len(paises_info)):

                    if 500 <=  paises_info[i].get("superficie") <1000:
                        #Si el país tiene entre 500 y 1.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 3:
                for i in range(0,len(paises_info)):
                    if 1000 <=  paises_info[i].get("superficie") <10000:
                        #Si el país tiene entre 1.000 y 10.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 4:
                for i in range(0,len(paises_info)):
                    if 10000 <=  paises_info[i].get("superficie") <50000:
                        #Si el país tiene entre 10.000 y 50.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 5:
                for i in range(0,len(paises_info)):
                    if 50000 <=  paises_info[i].get("superficie") <100000:
                        #Si el país tiene entre 50.000 y 100.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 6:
                for i in range(0,len(paises_info)):
                    if 100000 <=  paises_info[i].get("superficie") <200000:
                        #Si el país tiene entre 100.000 y 200.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 7:
                for i in range(0,len(paises_info)):
                    if 200000 <=  paises_info[i].get("superficie") <500000:
                        #Si el país tiene entre 200.000 y 500.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 8:
                for i in range(0,len(paises_info)):
                    if 500000 <=  paises_info[i].get("superficie") <1000000:
                        #Si el país tiene entre 500.000 y 1.000.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 9:
                for i in range(0,len(paises_info)):
                    if 1000000 <=  paises_info[i].get("superficie") <3000000:
                        #Si el país tiene entre 1.000.000 y 3.000.000km entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")
            case 10:
                for i in range(0,len(paises_info)):
                    if 3000000 <=  paises_info[i].get("superficie"):
                        #Si el país tiene más de 3.000.000 entra en el if
                        funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie")) #Se le pasa la superficie a la función
                        print(f"{paises_info[i].get("nombre")}: tiene {funcion_punto_cada_tres_cifras(i,paises_info[i].get("superficie"))} km")