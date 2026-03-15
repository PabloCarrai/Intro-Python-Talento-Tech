"""
Necesitamos crear una lista con los nombres de los clientes que vamos a
procesar. Ademas, es necesario detectar si alguno de los nombres esta
en blanco y mostrar una alerta en esos casos. Luego, para los nombres
validos, nos aseguraremos que uno comience con una letra mayuscula, y el
resto en minusculas
"""

lista_nombres = []
lista_nombres_validos = []
cantidad_nombres = int(input("Cuantos nombres vas a cargar?   "))
for numero in range(cantidad_nombres):
    nombre = input("Ingrese un nombre  ")
    lista_nombres.append(nombre)


for n in range(len(lista_nombres)):
    if len(lista_nombres[n]) == 0:
        print(f"El nombre esta Vacio")
    else:
        lista_nombres_validos.append(lista_nombres[n])

for n in range(len(lista_nombres_validos)):
    print(lista_nombres_validos[n].title())
