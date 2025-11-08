
#Filtro del maximo y minimo de la poblacion del mundo
def max_min_poblacion(paises):
    lista_poblacion = []
    for fila in paises:
        poblacion = fila.get("poblacion")
        lista_poblacion.append(int(poblacion))
    poblacion_max = max(lista_poblacion)
    poblacion_min = min(lista_poblacion)
    for fila in paises:
        if str(poblacion_max) == fila.get("poblacion"):
            print(f"El pais con mayor poblacion es '{fila.get("nombre")}' con {poblacion_max}")
        if str(poblacion_min) == fila.get("poblacion"):
            print(f"El pais con menor poblacion es '{fila.get("nombre")}' con {poblacion_min}")

#Calcula el promedio de la poblacion del mundo
def promedio_poblacion(paises):
    suma = 0
    cantidad_paises = 0
    for fila in paises:
        suma += int(fila.get("poblacion"))
        cantidad_paises += 1
    promedio = suma//(cantidad_paises-2)
    print(f"El promedio de la poblacion de todo el mundo es de: {promedio}")

#Calcula el promedio de la superficie del mundo
def promedio_superficie(paises):
    suma = 0
    cantidad_paises = 0
    for fila in paises:
        suma += int(float(fila.get("superficie")))
        cantidad_paises += 1
    promedio = suma//(cantidad_paises-2)
    print(f"El promedio de la superficie de todo el mundo es de: {promedio}")


#Calcula la cantidad de paises por continente
def paises_por_continente(paises,seleccion):
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
                        print(f"El continente de América tiene: {america} paises")
                    case 3: #Asia
                        asia  = 0
                        for i in range (len(paises)):
                            if paises[i].get("continente") == "Asia":
                                asia +=1
                        print(f"El continente de Asia tiene: {asia} paises")
                    case 4: #Europa
                        Europa  = 0
                        for i in range (len(paises)):
                            if paises[i].get("continente") == "Europa":
                                Europa +=1
                        print(f"El continente de Europa tiene: {Europa} paises")
                    case 5: #Oceania
                        oceania  = 0
                        for i in range (len(paises)):
                            if paises[i].get("continente") == "Oceanía":
                                oceania +=1
                        print(f"El continente de Oceanía tiene: {oceania} paises")

#Opciones que hay para calcular las estadisticas de lo que desee el usuario
def estadisticas(lista_paises):
    print("Mostrar estadísticas:" \
    "\n1) País con mayor y menor población" \
    "\n2) Promedio de población" \
    "\n3) Promedio de superficie" \
    "\n4) Cantidad de países por continente")
    seleccion = int(input("Ingrese una opción: "))
    match seleccion:
        case 1:
            max_min_poblacion(lista_paises)
        case 2:
            promedio_poblacion(lista_paises)
        case 3:
            promedio_superficie(lista_paises)
        case 4:
            seleccion = int(input("\nElige una opción:\n1) África\n2) América\n3) Asia\n4) Europa\n5) Oceanía \n| "))
            paises_por_continente(lista_paises,seleccion)
        case _:
            print("Se esperaba una de las opciones indicadas, intentelo de nuevo")