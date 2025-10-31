from paises_info import *
import csv, os, unicodedata, difflib
def funcion_buscar_pais(lista_paises, pais_a_buscar):
    def normalize(s):
        if s is None:
            return ""
        s = str(s).strip().lower()
        # elimina tildes y diacríticos de forma robusta
        s = unicodedata.normalize("NFKD", s)
        s = "".join(c for c in s if not unicodedata.combining(c))
        return s
    # cargar lista desde CSV si se pasó una ruta
    paises = []
    if isinstance(lista_paises, str) and os.path.exists(lista_paises):
        with open(lista_paises, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # asume que el nombre del país está en la primera columna
                paises.append(row[0].strip())
    else:
        # si se pasó una lista/iterable de nombres
        if isinstance(lista_paises, (list, tuple)) or hasattr(lista_paises, "__iter__"):
            for item in lista_paises:
                if item is None:
                    continue
                s = str(item).strip()
                if s:
                    paises.append(s)
        else:
            raise ValueError("lista_paises debe ser una ruta al CSV o un iterable de nombres de país")
    if not pais_a_buscar or not str(pais_a_buscar).strip():
        return "Ingresó un caracter no valido."
    consulta_norm = normalize(pais_a_buscar)
    paises_norm = [normalize(p) for p in paises]
    # coincidencia exacta (sin tildes y case-insensitive)
    if consulta_norm in paises_norm:
        idx = paises_norm.index(consulta_norm)
        return f"El país '{paises[idx].title()}' fue encontrado en la lista."
    # coincidencia por subcadena (p. ej. ingresan parte del nombre)
    for i, pn in enumerate(paises_norm):
        if consulta_norm in pn or pn in consulta_norm:
            return f"El país '{paises[i].title()}' fue encontrado en la lista."
    # coincidencia aproximada (correcciones ortográficas)
    aproximadas = difflib.get_close_matches(consulta_norm, paises_norm, n=1, cutoff=0.7)
    if aproximadas:
        idx = paises_norm.index(aproximadas[0])
        return f"Coincidencia aproximada: '{paises[idx].title()}' (revisar ortografía)."
    return f'No se encontró "{pais_a_buscar}", por favor revise que haya introducido bien el texto.'