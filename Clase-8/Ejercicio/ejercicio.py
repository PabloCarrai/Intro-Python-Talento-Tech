"""
Crear un diccionario llamado producto donde las claves sean los nombres
de los productos y los valores sean sus precios.
Permitir agregar productos y sus precios hasta que se decida vinalizar
Mostrar el contenido del diccionario despues de cada operacion
"""

listado_productos = []

while True:
    print("Bienvenido:  ")
    print("para salir enter")
    nombre_producto = input("Producto:   ")
    if nombre_producto == "":
        break
    precio_producto = int(input(f"Precio:   "))
    producto = {"nombre": nombre_producto, "precio": precio_producto}
    listado_productos.append(producto)
    for prod, precio in producto.items():
        print(f"Producto {prod.title()} Precio ${precio}")


print("\tListado completo: ")
for producto in listado_productos:
    print(
        f"\tProducto: {producto['nombre'].capitalize()}\t - Precio: ${producto['precio']}"
    )
