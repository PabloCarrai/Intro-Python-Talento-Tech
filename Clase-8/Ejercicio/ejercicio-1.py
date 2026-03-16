"""
Desafío - Registro de productos con precios
Tenés que construir un pequeño sistema para registrar productos que una persona va comprando.
Tu programa debe:
    Usar un diccionario vacío al comenzar.
    Pedir al usuario que cargue 3 productos con su precio.
    Validar que el precio ingresado sea un número mayor a 0.
    Guardar el producto como clave y el precio como valor.
    Mostrar el contenido completo del diccionario.
    Mostrar el total gastado, sumando todos los precios.
🎯 Bonus: mostrar los productos en orden alfabético (orden de claves).
"""

listado_productos = []
compra_total = 0

for i in range(3):
    print("Bienvenido   ")
    producto = input("Nombre del Producto: ?   ")
    precio = input("Precio del Producto?   ")
    if int(precio) <= 0:
        print("El precio no es valido")
        break
    if producto and precio:
        listado_productos.append({"nombre": producto.capitalize(), "precio": precio})
        compra_total += int(precio)
    print("Carga exitosa")


#   Esto se supone ordena la lista por la llaves de cada diccionario
lista_ordenada = sorted(listado_productos, key=lambda x: x["nombre"])

for elemento in lista_ordenada:
    print(f"Producto: {elemento['nombre']}, {elemento['precio']}")
print(f"Total Gastado: {compra_total}")
