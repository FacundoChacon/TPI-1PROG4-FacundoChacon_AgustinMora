from paises_info import *
from funciones.funcion_punto_cada_tres_cifras import *

def promedio_superficie():
    superficie = 0
    for i in range(0,len(paises_info)):
        pais = paises_info[i].get("nombre")
        if pais != "Rusia" or pais != "Turquía":
            superficie+=paises_info[i].get("superficie")
        elif pais == "Rusia":
            indice=paises_info.index[i]
            superficie+=paises_info[indice].get("superficie")
        elif pais == "Turqía":
            indice=paises_info.index[i]
            superficie+=paises_info[indice].get("superficie")

    dividir = superficie / (len(paises_info))
    dividir = str(f"{dividir:.2f}")

    nuevo_dividir = dividir[:3] + "." + dividir[3:6] + "," + dividir[7:]
    superficie = str(superficie)
    nuevo_superficie = superficie[:3] + "." + superficie[3:6] + "." + superficie[6:9] + "," + superficie[10:]
    print(f"La suma de todas las superficies del mundo es: {nuevo_superficie}")
    print(f"El promedio de la superficie de todos los paises del mundo es: {nuevo_dividir}")