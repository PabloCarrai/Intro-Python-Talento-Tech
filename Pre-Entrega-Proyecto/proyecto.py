nombres = []
categorias = []
precios = []

while True:
    print("Bienvenido:   ")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")
    match opcion:
        case "1":
            print("Elegistes 'Agrega producto'")
            producto = input("Nombre del producto?    ")
            categoria = input("Categoria del producto?    ")
            precio = input("Precio?    ")

            if producto and categoria and precio:
                nombres.append(producto.strip().capitalize())
                categorias.append(categoria.strip().capitalize())
                precios.append(precio)
                print(
                    f"Producto agregado Nombre: {producto} Categoria: {categoria} Precio: ${precio}"
                )
            else:
                print("Te olvidaste de ingresar algo, vuelva a intentarlo  ")
                continue
        case "2":
            print("Elegistes 'Mostrar productos'")
            for elementos in range(len(nombres)):
                print(
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio:{precios[elementos]}"
                )
        case "3":
            print("Elegistes 'Buscar productos'")
        case "4":
            print("Elegistes 'Eliminar producto'")
        case "5":
            print("Elegistes 'Salir'")
            print("Hasta Luego")
            break
        case _:
            print("Elegistes cualquiera ")
            continue
