from paises_info import *
def ordenar_paises_nombre():
    for i in range(0,len(paises_info)):
        print(paises_info[i].get("nombre"))