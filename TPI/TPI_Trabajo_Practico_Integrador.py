from funciones.funcion_buscar_pais import *
menu=True
mundi1 = [
    "Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda",
    "Arabia Saudita", "Argelia", "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán",
    "Bahamas", "Bangladés", "Barbados", "Baréin", "Bélgica", "Belice", "Benín", "Bielorrusia", 
    "Birmania", "Bolivia", "Bosnia y Herzegovina", "Botsuana", "Brasil", "Brunéi", "Bulgaria", 
    "Burkina Faso", "Burundi", "Bután","Cabo Verde", "Camboya", "Camerún", "Canadá", "Catar", 
    "Chad", "Chile", "China", "Chipre", "Colombia", "Comoras", "Corea del Norte", "Corea del Sur", 
    "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", 
    "Egipto", "El Salvador", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", 
    "España", "Estados Unidos", "Estonia", "Esuatini", "Etiopía","Filipinas", "Finlandia", 
    "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", 
    "Guinea", "Guinea Ecuatorial", "Guinea-Bisáu", "Guyana", "Haití", "Honduras", "Hungría",
    "India", "Indonesia", "Irak", "Irán", "Irlanda", "Islandia", "Islas Marshall", "Islas Salomón",
    "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", 
    "Kiribati", "Kuwait", "Laos", "Lesoto", "Letonia", "Líbano", "Liberia", "Libia", 
    "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Madagascar", "Malasia", 
    "Malaui", "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", "México", 
    "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montenegro", "Mozambique", "Namibia", "Nauru", 
    "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega", "Nueva Zelanda", "Omán", "Países Bajos", 
    "Pakistán", "Palaos", "Palestina", "Panamá", "Papúa Nueva Guinea", "Paraguay", "Perú", "Polonia", "Portugal", "Puerto Rico",
    "Qatar", "Reino Unido", "República Centroafricana", "República Checa", 
    "República Democrática del Congo", "República Dominicana", "Ruanda", "Rumania", "Rusia", 
    "Samoa", "San Cristóbal y Nieves", "San Marino", "San Vicente y las Granadinas", "Santa Lucía",
    "Santo Tomé y Príncipe", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria",
    "Somalia", "Sri Lanka", "Sudáfrica", "Sudán", "Sudán del Sur", "Suecia", "Suiza", "Surinam",
    "Tailandia", "Tanzania", "Tayikistán", "Timor Oriental", "Togo", "Tonga", "Trinidad y Tobago",
    "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán",
    "Vanuatu", "Vaticano", "Venezuela", "Vietnam", "Yemen", "Yibuti", "Zambia", "Zimbabue"
]

for i in range(0,len(mundi1)):
    mundi1[i]=mundi1[i].lower()

while menu:
    print("---MENU---")
    print("1) Buscar un país por nombre")
    print("2) Filtrar países")
    print("3) Ordenar países")
    print("4) Mostrar estadísticas de países")
    print("5) Ingrese 0 (cero) para salir")
    opcion = int(input("\nIngresar la opcion deseada: "))
    if opcion <= 5 or opcion > 0:
        match opcion:
            case 1:
                seleccion = input("Ingrese un país: ").lower()
                print(funcion_buscar_pais(mundi1, seleccion))
            case 2:
                pass
            case 3:
                print("Ordenar países por: \n1) Nombre\n2) Población\n3) Superficie")
                seleccion = input("\nIngrese una opción: ")
                if not seleccion.isdigit():
                    print("\nSolo se permiten ingresar números!!\n")
                    continue
                seleccion = int(seleccion)
                match seleccion:
                    case 1:
                        #COMPLETAR!_!_!_!_!_!_!_!_
                        mundi1.sort
                        for i in range(0,len(mundi1)):
                            print(mundi1[i])
                pass
            case 4:
                pass
            case 0:
                print("Saliendo...")
                break
    else:
        print("\nOpción incorrecta. Ingrese un número del 1 al 5\n")
        continue
