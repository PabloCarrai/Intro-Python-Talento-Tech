"""
Desafío - Limpiar y mostrar una lista de nombres
Queremos registrar el nombre de las personas que se anotan a un taller.
Pero a veces escriben mal o dejan el campo vacío.
Tu desafío es:
    Usar un bucle para cargar nombres (por ejemplo, 5)
    Ignorar los vacíos o espacios en blanco
    Guardar los nombres válidos usando .append()
    Ordenar la lista alfabéticamente con .sort()
    Mostrar solo los primeros 3 nombres válidos, usando slicing

🎯 Bonus: mostrar la cantidad total de nombres registrados correctamente.
"""

listado_nombres = []
nombres_correctos = 0

cantidad_nombres = 5
for numeros in range(5):
    nombre = input("Ingrese nombre de asistentes al taller:    ").strip().lower()
    #   Reviso si hay espacio entre las letras del nombre y hago un salto
    if " " in nombre:
        continue
    if nombre:
        nombres_correctos += 1
        #   Lo agrego a la lista pero con la primer letra en mayuscula como un nombre
        listado_nombres.append(nombre)
        print(f"Nombre ingresado {nombre}")


print(f"Lista Original {listado_nombres}")
listado_nombres.sort()
print(f"Lista Ordenada {listado_nombres}")
print("Primeros tres nombres validos")
porcion = listado_nombres[:3]
for elemento in range(len(porcion)):
    print(f"Elemento {elemento+1} Nombre: {porcion[elemento]}")
print(f"Cantidad de nombres total a cargar {cantidad_nombres}")
print(f"Cantidad de nombres cargados correctamente {nombres_correctos}")
