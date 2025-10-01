def funcion_buscar_pais(lista_paises, pais_a_buscar):
    pais = pais_a_buscar.lower()
    if pais in lista_paises:
        for i in range(0, len(lista_paises)):
            if lista_paises[i].startswith(pais):
                return f"El país '{lista_paises[i]}' fue encontrado en la lista."
    else:
        print(f"El país '{pais_a_buscar}' no fue encontrado en la lista.")