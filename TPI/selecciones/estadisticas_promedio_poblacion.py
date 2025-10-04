from paises_info import *
def promedio(pais):
    for i in range(0,len(paises_info)):
        if pais == paises_info[i].get("nombre"):
            poblacion = paises_info[i].get("poblacion")
            superficie = paises_info[i].get("superficie")
            promedio = poblacion // superficie
            print(f"El promedio de poblacion de '{pais}' es de {promedio} habitantes km²")