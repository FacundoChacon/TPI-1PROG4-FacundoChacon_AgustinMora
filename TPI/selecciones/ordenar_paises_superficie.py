from paises_info import *
def ordenar_paises_superficie():
    superficie_paises = []
    nombre_paises = []
    for i in range(0,len(paises_info)):
        superficie_paises.append(paises_info[i].get("superficie"))
        nombre_paises.append(paises_info[i].get("nombre"))
    for i in range(0,len(superficie_paises)-1):
        for j in range(i+1,len(superficie_paises)):
            if superficie_paises[i]>superficie_paises[j]:
                superficie_paises[i], superficie_paises[j] = superficie_paises[i], superficie_paises[j]
                nombre_paises[i], nombre_paises[j] = nombre_paises[i], nombre_paises[j]
            else:
                superficie_paises[i], superficie_paises[j] = superficie_paises[j], superficie_paises[i]
                nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
    for i in range(0,len(superficie_paises)):
        print(f"El país {nombre_paises[i]} tiene {superficie_paises[i]} Km² de superficie")