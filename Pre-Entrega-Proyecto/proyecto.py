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
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio: ${precios[elementos]}"
                )
        case "3":
            print("Elegistes 'Buscar productos'")
            for elementos in range(len(nombres)):
                print(
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio: ${precios[elementos]}"
                )
            nombre = input("Nombre del producto? ").strip().capitalize()
            if nombre:
                if nombre in nombres:
                    indice = nombres.index(nombre)
                    print(f"Informacion del producto {nombre}")
                    print(f"Categoria {categorias[indice]}")
                    print(f"Precio {precios[indice]}")
                else:
                    print("Elegiste un producto que no existe.")
                    continue
            else:
                print("Elegiste un producto que no existe.")
                break
        case "4":
            print("Elegistes 'Eliminar producto'")
            print("Estos son los productos existentes actualmente.")
            for elementos in range(len(nombres)):
                print(
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio: ${precios[elementos]}"
                )
            nombre = input("Nombre del producto a eliminar? ").strip().capitalize()
            if nombre:
                if nombre in nombres:
                    indice = nombres.index(nombre)
                    del nombres[indice]
                    del categorias[indice]
                    del precios[indice]
                    print("Producto eliminado  ")
                else:
                    print("Elegiste un producto que no existe.")
                    break
            else:
                print("Elegiste un producto que no existe.")
                break

        case "5":
            print("Elegistes 'Salir'")
            print("Hasta Luego")
            break
        case _:
            print("Elegistes cualquiera ")
            continue
