from paises_info import *

def funcion_punto_cada_tres_cifras(i,dato):
    superficie = str(dato)
    contador = len(superficie)
    
    superficie_con_puntos = ""
    
    for i in range(0,len(superficie)):
        superficie_con_puntos += superficie[i]
        
        contador-=1
        if contador % 3 == 0:
            superficie_con_puntos+="."

    if superficie_con_puntos.endswith("."):
        return superficie_con_puntos[:-1]
    else:
        return superficie_con_puntos
