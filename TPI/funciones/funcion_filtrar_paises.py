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