from paises_info import *
def funcion_buscar_pais(lista_paises, pais_a_buscar):
    contador = 0
    pais = pais_a_buscar.lower()
    if not pais_a_buscar.isalpha():
        return "\nIngresó un caracter no valido."
    if pais in lista_paises:
        indice = lista_paises.index(pais)
        if lista_paises[indice]:
            return f"El país '{lista_paises[indice].title()}' fue encontrado en la lista."
    for i in range(0, len(lista_paises)):
        if pais in lista_paises[i]:
            return f"El país '{lista_paises[i].title()}' fue encontrado en la lista."
        else:
            contador+=1
            if contador>=(len(paises_info)):
                return f'No se encontró "{pais_a_buscar}", por favor revise que haya introducido bien el texto.'