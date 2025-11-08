
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

#Calcula la cantidad de paises que detectados en el mundo
def paises_por_continente(paises):
    cantidad_paises = 0
    for fila in paises:
        cantidad_paises += 1
    cantidad_paises = cantidad_paises-2
    print(f"La cantidad de paises que hay en el mundo son: {cantidad_paises}")


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
            paises_por_continente(lista_paises)
        case _:
            print("Se esperaba una de las opciones indicadas, intentelo de nuevo")