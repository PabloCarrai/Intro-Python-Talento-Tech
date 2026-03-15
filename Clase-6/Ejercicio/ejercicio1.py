"""
1) Crear una lista con los nombres de los y las clientes que vamos a procesar.
Recorrer la lista y mostrar el nombre de cada cliente, clienta junto con su posicion
en la lista(por ejemplo Cliente 1, Cliente 2, etc
2) Recorrer la lista con un for y mostrar el nombre de cada
cliente junto con su posicion en la lista(por ejemplo: Cliente1 : Ana)
3) Si encuentras un nombre vacio, mostrar un mensaje de
alerta indicando que ese dato no es valido
"""

nombres = [
    "Juana",
    "romina",
    "Yesica",
    "cecilia",
    "paulo",
    "",
    "Ana",
    "",
    "Roberto",
    "Carla",
    "ernesto",
    "",
    "miguel"
]

for elemento in range(len(nombres)):
    if len(nombres[elemento]) == 0:
        print(f"Alerta Cliente/a {elemento+1}: Vacio")
    else:
        print(f"Cliente/a {elemento+1}: {nombres[elemento].capitalize()}")
