"""
Solicitar al usuario/a los nombres de los clientes/as uno por uno y validar que cada nombre
no este vacio. Si se deja el campo vacio, mostrarle un mensaje de advertencia y volver a pedir
el nombre
Guardar cada nombre valido en una lista, asegurandote de agregarlo con el metodo append()
Permiti que la persona finalice la carga de nombres escribiendo la palabra "fin"
Una vez finalizada la carga, ordena alfabeticamente los nombres en la lista y
mostra la lista ordenada de nombres usando un bucle for
"""

#   Lista para almacenar los nombres
nombres = []
print("Bienvenido/a")
#   Bucle que hace todo
while True:
    print("Si no desea seguir cargando escriba fin")
    #   Pido el nombre
    nombre = input("Ingrese el nombre del cliente/a:  ").strip().lower()
    #   Reviso si ingresa fin y lo pongo en minuscula por si usa mayuscula
    if nombre.lower() == "fin":
        print(f"Gracias por usar el programa. ")
        #   Aca salgo si eso pasa
        break
    #   Si esta vacio me devuelve False, sino esta con datos y devuelve True
    if nombre:
        #   Lo agrego a la lista pero con la primer letra en mayuscula como un nombre
        nombres.append(nombre.title())
        print(f"Nombre ingresado {nombre}")
    else:
        #   Salto el bucle si no ingreso nada y  lo vuelvo a pedir
        print("No realizo ningun ingreso. Vuelva a intentarlo.  ")
        continue

#   Ordeno la lista
nombres.sort()
print("Listado")
#   Imprimo los elementos
for elemento in range(len(nombres)):
    print(f"Orden Alfabetico:{elemento+1}, Nombre: {nombres[elemento]}")
