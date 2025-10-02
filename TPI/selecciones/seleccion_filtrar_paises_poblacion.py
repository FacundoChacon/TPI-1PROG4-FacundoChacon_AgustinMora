from paises_info import *
def seleccion_filtrar_paises_poblacion(seleccion):
#1) Menos de 1 Millón
#2) Entre 1-10 Millones
#3) Más de 10 Millones
        if 1<= seleccion <=3:
            print("")
            match seleccion:
                case 1:
                    for i in range(0,len(paises_info)):
                        if paises_info[i].get("poblacion") < 1000000:
                            print(f"{paises_info[i].get("nombre")}: tiene {paises_info[i].get("poblacion")} habitantes.")
                case 2:
                    for i in range(0,len(paises_info)):
                        if 1000000 < paises_info[i].get("poblacion") < 10000000:
                            print(f"{paises_info[i].get("nombre")}: tiene {paises_info[i].get("poblacion")} habitantes.")
                case 3:
                    for i in range(0,len(paises_info)):
                        if 10000000 < paises_info[i].get("poblacion"):
                            print(f"{paises_info[i].get("nombre")}: tiene {paises_info[i].get("poblacion")} habitantes.")