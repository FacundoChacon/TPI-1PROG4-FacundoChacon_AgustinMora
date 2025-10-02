def funcion_buscar_pais(lista_paises, pais_a_buscar):
    pais = pais_a_buscar.lower()
    for i in range(0, len(lista_paises)):
        if pais in lista_paises[i]:
            return f"El país '{lista_paises[i].title()}' fue encontrado en la lista."
