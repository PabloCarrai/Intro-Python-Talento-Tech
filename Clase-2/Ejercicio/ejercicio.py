"""
Pagina 19:
Solicite al cliente su nombre, apellido, edad y correo electronico.
Almacene estos datos en variables.
Mostrar organizados en Forma de tarjeta de presentacion en la pantalla
"""

print("\t###########################################")
print("\tBienvenido a Gestion de datos personales: ")
print("\t###########################################")
nombre = input("Ingrese su nombre: ")
apellido = input(nombre + " Su apellido: ")
edad = input(nombre + " Edad: ")
correo_electronico = input(nombre + " Correo: ")
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
