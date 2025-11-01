import csv
from funciones.funcion_punto_cada_tres_cifras import funcion_punto_cada_tres_cifras

def filtrar_paises_poblacion(seleccion, csv_path='paises.csv'):
    # Lee el CSV y lo convierte en lista de diccionarios
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Convertimos el lector a una lista de diccionarios para poder iterar varias veces
        rows = list(reader)
        # Selecciona el filtro según la opción recibida
    match seleccion:
        case 1:
            # OPción 1: países con menos de 1.000.000 de habitantes
            print("")
            for i, row in enumerate(rows):
                try:
                    # Intentamos convertir el campo 'poblacion' a entero; si falla, saltamos la fila
                    pobl = int(row.get('poblacion', '0'))
                except ValueError:
                    continue
                if pobl < 1_000_000:
                    # Imprimimos el nombre y la población formateada.
                    # Se pasa 'i' (índice) y 'pobl' a la función de formateo (sgún implementación existente).
                    print(f"{row.get('nombre')}: tiene {funcion_punto_cada_tres_cifras(i, pobl)} habitantes.")
        case 2:
            # Opción 2: países con población entre 1.000.000 y 10.000.000
            print("")
            for i, row in enumerate(rows):
                try:
                    pobl = int(row.get('poblacion', '0'))
                except ValueError:
                    continue
                # Nótese que la condición excluye exactamente 1.000.000 y 10.000.000; ajustar si se quiere inclusve
                if 1_000_000 < pobl < 10_000_000:
                    print(f"{row.get('nombre')}: tiene {funcion_punto_cada_tres_cifras(i, pobl)} habitantes.")
        case 3:
            # Opción 3: países con más de 10.000.000 de habitantes
            print("")
            for i, row in enumerate(rows):
                try:
                    pobl = int(row.get('poblacion', '0'))
                except ValueError:
                    continue
                if pobl > 10_000_000:
                    print(f"{row.get('nombre')}: tiene {funcion_punto_cada_tres_cifras(i, pobl)} habitantes.")
        case _:
            # Opción inválida: instrucción al usuario
            print("Incorrecto, ingrese una opción valida.")