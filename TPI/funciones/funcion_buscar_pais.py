import unicodedata

def normalize(s):
        if s is None:
            return ""
        s = str(s).strip().lower()
        # elimina tildes y diacríticos de forma robusta
        s = unicodedata.normalize("NFKD", s)
        s = "".join(c for c in s if not unicodedata.combining(c))
        return s

def funcion_buscar_pais(lista_paises, pais_a_buscar):
    for i in range(0, len(lista_paises)):
        if normalize(pais_a_buscar) in normalize(lista_paises[i].get("nombre")):
            print(f"El pais {lista_paises[i].get("nombre").title()} fue encontrado en la lista")
            return
    print(f"No se encontro el pais {pais_a_buscar}")