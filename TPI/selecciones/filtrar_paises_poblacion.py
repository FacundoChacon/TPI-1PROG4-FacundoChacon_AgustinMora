import csv
from funciones.funcion_punto_cada_tres_cifras import funcion_punto_cada_tres_cifras

def filtrar_paises_poblacion(seleccion, csv_path='paises.csv'):
    # Lee el CSV y lo convierte en lista de diccionarios
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    match seleccion:
        case 1:
            print("")
            for i, row in enumerate(rows):
                try:
                    pobl = int(row.get('poblacion', '0'))
                except ValueError:
                    continue
                if pobl < 1_000_000:
                    print(f"{row.get('nombre')}: tiene {funcion_punto_cada_tres_cifras(i, pobl)} habitantes.")
        case 2:
            print("")
            for i, row in enumerate(rows):
                try:
                    pobl = int(row.get('poblacion', '0'))
                except ValueError:
                    continue
                if 1_000_000 < pobl < 10_000_000:
                    print(f"{row.get('nombre')}: tiene {funcion_punto_cada_tres_cifras(i, pobl)} habitantes.")
        case 3:
            print("")
            for i, row in enumerate(rows):
                try:
                    pobl = int(row.get('poblacion', '0'))
                except ValueError:
                    continue
                if pobl > 10_000_000:
                    print(f"{row.get('nombre')}: tiene {funcion_punto_cada_tres_cifras(i, pobl)} habitantes.")
        case _:
            print("Incorrecto, ingrese una opción valida.")