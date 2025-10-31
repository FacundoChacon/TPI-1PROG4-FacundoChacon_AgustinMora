import csv
import os
# Función para normalizar texto quitando tildes y ñ
def quitar_tildes(s):
    if not s:
        return ""
    s = s.strip().lower()
    tabla = str.maketrans("áéíóúüñ", "aeiouun") 
    return s.translate(tabla)
# Carga los datos del archivo CSV de países
def cargar_datos_csv():
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'archivos', 'paises.csv')
    datos = []
    with open(ruta_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos
# Busca un país en la lista y devuelve su índice
def buscar_pais_index(pais, lista_paises):
    objetivo = quitar_tildes(pais)
    for i, nombre in enumerate(lista_paises):
        if quitar_tildes(nombre) == objetivo:
            return i
    return -1
# Calcula el promedio de población por km2 para un país
def promedio(pais, lista_paises):
    idx = buscar_pais_index(pais, lista_paises)
    if idx == -1:
        print("Ingrese un país válido")
        return
    datos_paises = cargar_datos_csv()
    info = datos_paises[idx]
    poblacion = info.get("Population")
    superficie = info.get("Area")
    try:
        poblacion = int(poblacion)
        superficie = float(superficie)
    except (TypeError, ValueError):
        print(f"Datos incompletos o inválidos para '{pais}'.")
        return
    if superficie == 0:
        print(f"No se puede calcular el promedio para '{pais}' porque la superficie es 0.")
        return
    promedio_val = int(poblacion // superficie)
    print(f"El promedio de poblacion de '{pais}' es de {promedio_val} habitantes km²")





'''
from funciones.funcion_buscar_pais import *
import unicodedata

def promedio(pais,lista_paises):
    def sin_tildes(s):
        s = (s or "").strip().lower()
        normalizado = unicodedata.normalize('NFKD', s)
        return ''.join(c for c in normalizado if not unicodedata.combining(c))
    paises_sin_tildes = []
    for i in range(0, len(lista_paises)):
        paises_sin_tildes.append(sin_tildes(lista_paises[i]))
    pais_encontrado = False
    buscado = sin_tildes(pais)
    for i in range(0,len((paises_sin_tildes))):
        if buscado == (paises_sin_tildes[i]):
            poblacion = paises_info[i].get("poblacion")
            superficie = paises_info[i].get("superficie")
            try:
                poblacion = int(poblacion)
                superficie = int(superficie)
                if superficie == 0:
                    print(f"No se puede calcular el promedio para '{pais}' porque la superficie es 0.")
                else:
                    promedio_val = poblacion // superficie
                    print(f"El promedio de poblacion de '{pais}' es de {promedio_val} habitantes km²")
            except (TypeError, ValueError):
                print(f"Datos incompletos o inválidos para '{pais}'.")
            pais_encontrado = True
            break
    if not pais_encontrado:
        print("Ingrese un país válido")
'''