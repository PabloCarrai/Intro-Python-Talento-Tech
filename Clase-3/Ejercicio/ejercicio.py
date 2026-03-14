"""
Pagina 15:  (parece una boludes, pero me costo un felpudo)
Necesito que desarrolles un pequeño programa en python que
haga exactamente lo siguiente:
    Solicite al cliente nombre, apellido, edad y correo electronico
    Compruebe que el nombre, el apellido y el correo no esten en blanco
    y que la edad sea mayor de 18 años
    Muestre los datos por la terminal, en el orden que se ingresaron.
    Si alguno de los datos ingresados no cumple con los requisitos
    solo mostrar el texto "ERROR!"

"""

print("\t###########################################")
print("\tBienvenido a Gestion de datos personales: ")
print("\t###########################################")
nombre = input("Ingrese su nombre: ")
apellido = input(nombre + " Su apellido: ")
edad = input(nombre + " Edad: ")
correo_electronico = input(nombre + " Correo: ")

#   si la variable esta vacia devuelve false
if nombre and apellido and correo_electronico and int(edad) > 18:
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
    print("ERROR!")
