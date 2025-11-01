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
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', '..', 'paises.csv')
    ruta_csv = os.path.abspath(ruta_csv)  # para obtener la ruta absoluta
    datos = []
    with open(ruta_csv, 'r', encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos

# Busca un país en la lista y devuelve su índice
def buscar_pais_index(pais, lista_paises):
    objetivo = quitar_tildes(pais)
    index = 0
    try:
        with open(lista_paises, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            # Skip header row if present
            next(reader, None)
            for fila in reader:
                if not fila:
                    continue
                if quitar_tildes(fila[0]) == objetivo:
                    return index
                index += 1
    except FileNotFoundError:
        # Si no existe el archivo, devolvemos -1 para indicar "no encontrado"
        return -1
    return -1
# Calcula el promedio de población por km2 para un país
def promedio(pais, lista_paises):
    idx = buscar_pais_index(pais, lista_paises)
    if idx == -1:
        print("Ingrese un país válido")
        return
    datos_paises = cargar_datos_csv()
    if idx < 0 or idx >= len(datos_paises):
        print("Ingrese un país válido")
        return
    info = datos_paises[idx]
    poblacion = info.get("poblacion")
    superficie = info.get("superficie")

    # Limpia cadenas numéricas (quita separadores de miles y espacios)
    def clean_num(s):
        if s is None:
            return None
        s = str(s).strip()
        if s == "":
            return None
        s = s.replace(",", "").replace(" ", "")
        return s

    poblacion_s = clean_num(poblacion)
    superficie_s = clean_num(superficie)

    try:
        poblacion_val = float(poblacion_s) if poblacion_s is not None else None
        superficie_val = float(superficie_s) if superficie_s is not None else None
        if poblacion_val is None or superficie_val is None:
            raise ValueError
    except (TypeError, ValueError):
        print(f"Datos incompletos o inválidos para '{pais}'.")
        return

    if superficie_val == 0:
        print(f"No se puede calcular el promedio para '{pais}' porque la superficie es 0.")
        return

    promedio_val = int(poblacion_val // superficie_val)
    print(f"El promedio de poblacion de '{pais}' es de {promedio_val} habitantes km²")
    