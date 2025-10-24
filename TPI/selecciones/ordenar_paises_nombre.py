from paises_info import *
def ordenar_paises_nombre(): #Ordena los países por nombre (ya estaba ordenada la lista original)
    for i in range(0,len(paises_info)):
        print(paises_info[i].get("nombre"))