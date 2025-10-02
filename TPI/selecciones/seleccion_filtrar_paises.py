from paises_info import *

def seleccion_filtrar_paises(seleccion):
    if 1<= seleccion <=5:
        print("")
        match seleccion:
            case 1:
                for i in range(0,len(paises_info)):
                    if paises_info[i].get("continente") == "África":
                        print (paises_info[i].get("nombre"))
            case 2:
                for i in range(0,len(paises_info)):
                    if paises_info[i].get("continente") == "América":
                        print (paises_info[i].get("nombre"))
            case 3:
                for i in range(0,len(paises_info)):
                    if paises_info[i].get("continente") == "Asia":
                        print (paises_info[i].get("nombre"))
            case 4:
                for i in range(0,len(paises_info)):
                    if paises_info[i].get("continente") == "Europa":
                        print (paises_info[i].get("nombre"))
            case 5:
                for i in range(0,len(paises_info)):
                    if paises_info[i].get("continente") == "Oceanía":
                        print (paises_info[i].get("nombre"))
    else:
        print("MALLLLALALAMLALMALM")