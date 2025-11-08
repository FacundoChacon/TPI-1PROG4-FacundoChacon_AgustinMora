#filtro de paises por continente
def funcion_filtrar_continente(paises,seleccion):
    match seleccion:
                case 1: #Africa
                    africa  = 0
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "África":
                            africa +=1
                    print(f"El continente de África tiene: {africa} paises")
                case 2: #America
                    america  = 0
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "América":
                            america +=1
                    print(f"El continente de África tiene: {america} paises")
                case 3: #Asia
                    asia  = 0
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "Asia":
                            asia +=1
                    print(f"El continente de África tiene: {asia} paises")
                case 4: #Europa
                    Europa  = 0
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "Europa":
                            Europa +=1
                    print(f"El continente de África tiene: {Europa} paises")
                case 5: #Oceania
                    oceania  = 0
                    for i in range (len(paises)):
                        if paises[i].get("continente") == "Oceanía":
                            oceania +=1
                    print(f"El continente de África tiene: {oceania} paises")

#Función que filtra los países según el rango de población ingresado por el usuario
def funcion_filtrar_poblacion(paises):
    min = int(input("Ingrese la cantidad mínima a filtrar: "))
    max = int(input("Ingrese la cantidad máxima a filtrar: "))
    for fila in paises:
        if min < int(fila.get("poblacion")) and int(fila.get("poblacion")) < max:
            print(f"{fila.get("nombre")} tiene: {fila.get("poblacion")} habitantes")

#Función que filtra los países según el rango de superficie ingresado por el usuario
def rango_superficie(paises):
    seleccion = int(input("\nElige una opción:\n1) Mayor a menor (Descendente)\n2) menor a Mayor (Ascendente)\n| "))
    match seleccion:
        case 1:
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
                    print(f"El pais {nombre1} tiene: {superficie1}")
        case 2:
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
                    print(f"El pais {nombre1} tiene: {superficie1}")

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