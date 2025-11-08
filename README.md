# TPI-1PROG4-FacundoChacon_AgustinMora
→
- Descripcion general del programa y sus usos:
  Este programa crea y gestiona una base de datos de países usando un archivo CSV.
  Si no existe el archivo paises.csv, lo genera con datos de cada país (nombre, población, superficie y continente) y
  carga esa información en una lista de diccionarios. 
  Luego se muestra un menú interactivo que permite:
  - Buscar un país por nombre
  - filtrar países por continente, población o superficie
  - Ordenar países según distintos criterios
  - Mostrar estadísticas generales.
  El usuario elige una opción y el programa ejecuta la función correspondiente.
  En resumidas cuentas, es una aplicación de consola que organiza y analiza información de países mediante archivos CSV y funciones modulares.
- Ejemplos de entradas y slidas:
  Es un programa que funciona mayormente con opciones numericas, en el caso de que el usuario ingrese un numero que este fuera de los casos indicados simplemente
  va al caso default que le solicita ingresar uno de las opciones mostradas. Si es que el usuario no ingrese un caracter de tipo entero (ya sea un string o flotante)
  el error que retorna se lo captura con try except y le indica al usuario ingresar un numero de tipo entero. Para las demas funciones ya hay validaciones que evitan cualquier
  descuido o tipo de error.
  Si el usuario ingresa lo esperado, el programa va a devolver lo esperado, sino se le va a indicar al usuario volver intentarlo y continuando con el programa sin
  que se detenga
→
Trabajo Practico Integrador de Facundo Chacon y Agustin Mora. Comision: 1PROG4
