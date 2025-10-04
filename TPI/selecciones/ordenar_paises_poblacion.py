from paises_info import *
def ordenar_paises_poblacion(): #Ordena los países por población de mayor a menor, mostrando su nombre y cantidad de habitantes
    habitantes_paises = []
    nombre_paises = []
    for i in range(0,len(paises_info)):
        habitantes_paises.append(paises_info[i].get("poblacion"))
        nombre_paises.append(paises_info[i].get("nombre"))
    for i in range(0,len(habitantes_paises)-1):
        for j in range(i+1,len(habitantes_paises)):
            if habitantes_paises[i]>habitantes_paises[j]:
                habitantes_paises[i], habitantes_paises[j] = habitantes_paises[i], habitantes_paises[j]
                nombre_paises[i], nombre_paises[j] = nombre_paises[i], nombre_paises[j]
            else:
                habitantes_paises[i], habitantes_paises[j] = habitantes_paises[j], habitantes_paises[i]
                nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
    for i in range(0,len(habitantes_paises)):
        print(f"El país {nombre_paises[i]} tiene {habitantes_paises[i]} habitantes")