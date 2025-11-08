#filtro de paises por continente
def funcion_filtrar_continente(paises,seleccion):
    match seleccion:
                case 1: #Africa
                    print("")
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "África":
                            print(f"{paises[i].get("nombre")}")
                case 2: #America
                    print("")
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "América":
                            print(f"{paises[i].get("nombre")}")
                case 3: #Asia
                    print("")
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "Asia":
                            print(f"{paises[i].get("nombre")}")
                case 4: #Europa
                    print("")
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "Europa":
                            print(f"{paises[i].get("nombre")}")
                case 5: #Oceania
                    print("")
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "Oceanía":
                            print(f"{paises[i].get("nombre")}")

#Función que filtra los países según el rango de población ingresado por el usuario
def funcion_filtrar_poblacion(paises):
    min = int(input("Ingrese la cantidad mínima a filtrar: "))
    max = int(input("Ingrese la cantidad máxima a filtrar: "))
    print("")
    for fila in paises:
        if min < int(fila.get("poblacion")) and int(fila.get("poblacion")) < max:
            print(f"{fila.get("nombre")} tiene: {fila.get("poblacion")} habitantes")


'''def rango_superficie(paises):
    contador=0
    seleccion = int(input("\nElige una opción:\n1) Mayor a menor (Descendente)\n2) menor a Mayor (Ascendente)\n| "))
    match seleccion:
        case 1: #Mayor a menor
            lista1=[]
            for fila in paises:
                try:
                    superficie1 = float(fila.get("superficie", 0))
                except (TypeError, ValueError):
                    superficie1 = 0.0
                nombre1 = fila.get("nombre","Desconocido")
                lista1.append((superficie1,nombre1))
                lista1_ordenada = sorted(lista1,reverse=True)
                
                for superficie1,nombre1 in lista1_ordenada:
                    # print(nombre1)
                    if nombre1 == "Rusia":
                        # print("\nLOL\nLOL\nLOL\nLOL\nLOL")
                        contador+1
                    if contador<1:
                        print(f"El pais {nombre1} tiene: {superficie1}")
        case 2: #menor a Mayor
            lista1=[]
            for fila in paises:
                try:
                    superficie1 = float(fila.get("superficie", 0))
                except (TypeError, ValueError):
                    superficie1 = 0.0
                nombre1 = fila.get("nombre","Desconocido")
                lista1.append((superficie1,nombre1))
                lista1_ordenada = sorted(lista1)
                
                for superficie1,nombre1 in lista1_ordenada:
                    if contador<=1:
                        # print(nombre1)
                        print(f"El pais {nombre1} tiene: {superficie1}")
                        pass
                    if nombre1 == "Rusia":
                        # print("\nLOL\nLOL\nLOL\nLOL\nLOL")
                        contador+=1'''


def rango_superficie(paises): #3) Función que filtra los países según el rango de superficie ingresado por el usuario
    min = int(input("Ingrese la cantidad mínima a filtrar: "))
    max = int(input("Ingrese la cantidad máxima a filtrar: "))
    print("")
    for fila in paises:
        if min < float(fila.get("superficie")) and float(fila.get("superficie")) < max:
            print(f"{fila.get("nombre")} tiene: {fila.get("superficie")} km")



#Función principal que filtra los países según la selección del usuario
def funcion_filtrar_paises(paises, seleccion):
    match seleccion:
        case 1:
            seleccion = int(input("\nElige una opción:\n1) África\n2) América\n3) Asia\n4) Europa\n5) Oceanía \n| "))
            funcion_filtrar_continente(paises,seleccion)
        case 2:
            funcion_filtrar_poblacion(paises)
        case 3:
            rango_superficie(paises)