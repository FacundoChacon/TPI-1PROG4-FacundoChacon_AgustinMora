import csv
from pathlib import Path
def ordenar_paises_nombre(csv_path='paises.csv'):
    """
    Lee el archivo CSV (espera una columna 'nombre' o similar) y imprime
    los países ordenados por nombre.
    """
    path = Path(csv_path)
    if not path.exists():
        print(f"Archivo no encontrado: {path}")
        return
    with path.open(encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        # Buscar la columna que corresponde a "nombre" (sin importar mayúsculas)
        nombre_key = next((h for h in fieldnames if h.lower() == 'nombre'), None)
        if nombre_key is None and fieldnames:
            # Si no hay columna 'nombre', usar la primera columna disponible
            nombre_key = fieldnames[0]
        paises = [row for row in reader]
    paises.sort(key=lambda r: (r.get(nombre_key) or '').lower())
    for p in paises:
        print(p.get(nombre_key, ''))
        