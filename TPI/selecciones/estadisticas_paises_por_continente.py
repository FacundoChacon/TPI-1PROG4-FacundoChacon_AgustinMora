from paises_info import *
def paises_continente():
    africa = 0
    america = 0
    asia = 0
    europa = 0
    oceania = 0
    for i in range(0,len(paises_info)):
        if paises_info[i].get("continente") == "África":
            africa+=1
    for i in range(0,len(paises_info)):
        if paises_info[i].get("continente") == "América":
            america+=1
    for i in range(0,len(paises_info)):
        if paises_info[i].get("continente") == "Asia":
            asia+=1
    for i in range(0,len(paises_info)):
        if paises_info[i].get("continente") == "Europa":
            europa+=1
    for i in range(0,len(paises_info)):
        if paises_info[i].get("continente") == "Oceanía":
            oceania+=1
    print(f"África tiene {africa} paises")
    print(f"América tiene {america} paises")
    print(f"Asia tiene {asia} paises")
    print(f"Europa tiene {europa} paises")
    print(f"Oceanía tiene {oceania} paises")