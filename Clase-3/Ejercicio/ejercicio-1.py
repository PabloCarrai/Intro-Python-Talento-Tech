"""
Colab
En lugar de mostrar "ERROR!".
Comentar cual es el problema:
    Si uno de los campos estan vacios
    o si es menor de edad
"""

print("\t###########################################")
print("\tBienvenido a Gestion de datos personales: ")
print("\t###########################################")
nombre = input("Ingrese su nombre: ")
apellido = input(nombre + " Su apellido: ")
edad = input(nombre + " Edad: ")
correo_electronico = input(nombre + " Correo: ")

resultados_erroneos = ""

if not nombre:
    resultados_erroneos = resultados_erroneos + "Nombre esta vacio\n"
if not apellido:
    resultados_erroneos = resultados_erroneos + "Apellido esta vacio\n"
if not correo_electronico:
    resultados_erroneos = resultados_erroneos + "Correo Electronico esta vacio\n"
#   Si esta vacio no tengo forma de probar la edad
if not edad:
    resultados_erroneos = resultados_erroneos + "Edad esta vacio\n"
else:
    if int(edad) < 18:
        resultados_erroneos = resultados_erroneos + "Es menor de 18\n"

if not resultados_erroneos:
    print("\t###########################################")
    print("\t\t\tResumiendo: ")
    print("\t###########################################")
    print("\tNombre: \t", nombre)
    print("\tApellido: \t", apellido)
    print("\tEdad: \t\t", str(edad) + " años.")
    print("\tCorreo: \t", correo_electronico)
    print("\t###########################################")
    print("\t\tGracias por usar este programa. ")
    print("\t###########################################")
else:
    print("Hubo errores ")
    print(resultados_erroneos)
