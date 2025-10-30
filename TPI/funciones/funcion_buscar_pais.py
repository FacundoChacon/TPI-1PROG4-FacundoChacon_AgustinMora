from paises_info import *
def funcion_buscar_pais(lista_paises, pais_a_buscar):
    def sin_tildes(s):
        reemplazar_tildes = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
        for a, b in reemplazar_tildes:
            s = s.replace(a, b)
        return s
    paises_sin_tildes = []
    for i in range(0, len(lista_paises)):
        paises_sin_tildes.append(sin_tildes(lista_paises[i]))
    contador = 0
    pais = pais_a_buscar.lower()
    if pais == "":
        return "\nIngresó un caracter no valido."
    if pais in paises_sin_tildes:
        indice = paises_sin_tildes.index(pais)
        if lista_paises[indice]:
            return f"El país '{lista_paises[indice].title()}' fue encontrado en la lista."
    for i in range(0, len(lista_paises)):
        if pais in paises_sin_tildes[i].lower():
            return f"El país '{lista_paises[i].title()}' fue encontrado en la lista."
        else:
            contador+=1
            if contador>=(len(paises_info)):
                return f'No se encontró "{pais_a_buscar}", por favor revise que haya introducido bien el texto.'