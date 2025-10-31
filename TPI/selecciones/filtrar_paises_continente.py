import csv

def filtrar_paises_continente(seleccion):
    # Verifica que la selección sea válida (entre 1 y 5)
    if 1 <= seleccion <= 5:
        # Diccionario que mapea números a nombres de continentes
        continentes = {
            1: "África",
            2: "América",
            3: "Asia",
            4: "Europa",
            5: "Oceanía"
        }
        # Imprime el encabezado con el continente seleccionado
        print(f"\nPaíses en {continentes[seleccion]}:")
        print("-" * 30)
        # Abre y lee el archivo CSV con la información de los países
        with open('paises.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            encontrado = False
            # Itera sobre cada país en el archivo
            for pais in lector:
                # Si el país pertenece al continente seleccionado, lo imprime
                if pais['continente'] == continentes[seleccion]:
                    print(pais['nombre'])
                    encontrado = True
        # Si no se encontraron países, muestra un mensaje
        if not encontrado:
            print(f"No se encontraron países en {continentes[seleccion]}")
        print("-" * 30)
    else:
        print("Opción inválida.")
