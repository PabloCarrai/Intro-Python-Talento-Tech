"""
# Desafío - Limpiar y mostrar una lista de nombres
Tenemos una lista con nombres de personas que se anotaron a una capacitación.
Pero algunos tienen problemas:
- Algunos están vacíos o con espacios solamente
- Otros tienen mayúsculas y minúsculas mal combinadas
Tu tarea es:
1. Recorrer la lista con un `for`
2. Ignorar los valores vacíos o incorrectos usando `continue`
3. Mostrar solo los nombres válidos, **bien formateados** (con `.strip()` y `.title()`)
🔧 Bonus: al final, mostrar cuántos nombres válidos se encontraron.
(Intenta resolverlo antes de mirar la posible solución que aparece más abajo!)

"""

nombres = [
    "Juana",
    "romina",
    "Yesica",
    "cecilia",
    "paUlO",
    "",
    "Ana",
    "",
    "RobeRto",
    "Carla",
    "ernesto",
    "",
    "miguel",
    "  ",
    "Dante",
    "lAuTaro",
]

contador_palabras_ok = 0
contador_palabras_nok = 0

for elemento in range(len(nombres)):
    if len(nombres[elemento]) == 0 or nombres[elemento] == "  ":
        contador_palabras_nok += 1
        continue
    else:
        contador_palabras_ok += 1
        print(f"Indice {elemento+1}, valor {nombres[elemento].strip().title()}")

print(f"Cantidad de palabras {len(nombres)}")
print(f"Cantidad de palabras Ok {contador_palabras_ok}")
print(f"Cantidad de palabras No Ok {contador_palabras_nok}")
