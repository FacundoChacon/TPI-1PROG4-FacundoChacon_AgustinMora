from paises_info import *
poblacion = []
nombre_paises = []
def max_min_poblacion():
    for i in range(0,len(paises_info)):
                poblacion.append(paises_info[i].get("poblacion"))
                nombre_paises.append(paises_info[i].get("nombre"))
    for i in range(0,len(poblacion)-1):
        for j in range(i+1,len(poblacion)):
            if poblacion[i]>poblacion[j]:
                poblacion[i], poblacion[j] = poblacion[i], poblacion[j]
                nombre_paises[i], nombre_paises[j] = nombre_paises[i], nombre_paises[j]
            else:
                poblacion[i], poblacion[j] = poblacion[j], poblacion[i]
                nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
    print(f"\nEl pais con más poblacion es '{nombre_paises[0]}' y tiene {poblacion[0]}")
    print(f"El pais con menor poblacion es '{nombre_paises[len(nombre_paises)-1]}' y tiene {poblacion[len(poblacion)-1]}")