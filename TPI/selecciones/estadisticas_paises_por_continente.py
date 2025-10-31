import csv
def paises_continente():
    africa = 0
    america = 0
    asia = 0
    europa = 0
    oceania = 0
    with open('paises.csv', 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for pais in lector:
            if pais["continente"] == "África":
                africa += 1
            elif pais["continente"] == "América":
                america += 1
            elif pais["continente"] == "Asia":
                asia += 1
            elif pais["continente"] == "Europa":
                europa += 1
            elif pais["continente"] == "Oceanía":
                oceania += 1
    print(f"África tiene {africa} paises")
    print(f"América tiene {america} paises")
    print(f"Asia tiene {asia} paises")
    print(f"Europa tiene {europa} paises")
    print(f"Oceanía tiene {oceania} paises")