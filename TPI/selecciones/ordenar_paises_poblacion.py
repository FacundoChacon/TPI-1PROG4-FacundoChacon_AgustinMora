import csv
from pathlib import Path
def ordenar_paises_poblacion(csv_path='paises.csv'):
    """
    Lee países desde un archivo CSV y los imprime ordenados por población (mayor a menor).
    Se espera que el CSV tenga columnas 'nombre' y 'poblacion' (se intenta detectar variantes como 'población' o 'population').
    """
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró {csv_path}")
    paises = []
    with path.open(newline='', encoding='utf-8') as f:
        # Intentar leer como DictReader (con cabecera). Si no hay cabecera válida, caerá al reader por filas.
        reader = csv.DictReader(f)
        if reader.fieldnames and any(h.lower() in ('nombre', 'pais', 'pais_nombre') for h in reader.fieldnames):
            for row in reader:
                # Buscar claves posibles para nombre y población
                nombre = next((row.get(k) for k in ('nombre', 'Nombre', 'pais', 'Pais') if row.get(k)), None)
                pobl = next((row.get(k) for k in ('poblacion', 'población', 'population', 'Population') if row.get(k)), None)
                if not nombre or not pobl:
                    continue
                try:
                    pobl_val = int(str(pobl).replace('.', '').replace(',', ''))
                except:
                    try:
                        pobl_val = int(float(pobl))
                    except:
                        continue
                paises.append((nombre, pobl_val))
        else:
            # Sin cabecera: asumir formato nombre,poblacion por fila
            f.seek(0)
            reader2 = csv.reader(f)
            for row in reader2:
                if not row:
                    continue
                nombre = row[0]
                pobl = row[1] if len(row) > 1 else ''
                try:
                    pobl_val = int(str(pobl).replace('.', '').replace(',', ''))
                except:
                    try:
                        pobl_val = int(float(pobl))
                    except:
                        continue
                paises.append((nombre, pobl_val))
    # Ordenar de mayor a menor por población
    paises.sort(key=lambda x: x[1], reverse=True)
    for nombre, pobl in paises:
        print(f"El país {nombre} tiene {pobl} habitantes")