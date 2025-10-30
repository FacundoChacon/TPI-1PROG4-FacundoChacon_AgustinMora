from paises_info import *
def ordenar_paises_superficie(): #Ordena los países por superficie de Mayor a menor, mostrando su nombre y cantidad de Km²
    superficie_paises = []
    nombre_paises = []
    eleccion = int(input("Ingrese '1' para ordenar de Mayor a menor o '2' para ordenar de menor a Mayor: "))
    match eleccion:
        case 1: #Caso '1' Mayor a menor
            print("")
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
        case 2: #Caso '2' menor a Mayor
            print("")
            for i in range(0,len(paises_info)):
                superficie_paises.append(paises_info[i].get("superficie"))
                nombre_paises.append(paises_info[i].get("nombre"))
            for i in range(0,len(superficie_paises)-1):
                for j in range(i+1,len(superficie_paises)):
                    if superficie_paises[i]>superficie_paises[j]:
                        superficie_paises[i], superficie_paises[j] = superficie_paises[j], superficie_paises[i]
                        nombre_paises[i], nombre_paises[j] = nombre_paises[j], nombre_paises[i]
                    else:
                        superficie_paises[i], superficie_paises[j] = superficie_paises[i], superficie_paises[j]
                        nombre_paises[i], nombre_paises[j] = nombre_paises[i], nombre_paises[j]
            for i in range(0,len(superficie_paises)):
                print(f"El país {nombre_paises[i]} tiene {superficie_paises[i]} Km² de superficie")
        case _:
            print("Incorrecto, ingrese una opción valida.")