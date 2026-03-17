#   Las tres listas que uso para guardar los nombres, categorias y precios de productos
nombres = []
categorias = []
precios = []

#   Con el bucle hago casi toda la operacion.
while True:
    #   El menu que se muestra
    print("Bienvenido:   ")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Eliminar producto")
    print("5. Salir")
    #   Obtengo la eleccion del cliente
    opcion = input("Ingrese una opcion: ")
    #   El match es perfecto para darle el funcionamiento al menu
    match opcion:
        #   El caso de agregar el producto
        case "1":
            print("Elegistes 'Agrega producto'")
            producto = input("Nombre del producto?    ")
            categoria = input("Categoria del producto?    ")
            precio = input("Precio?    ")
            #   Reviso que el usuario/a haya ingresado algo en las tres variables
            if producto and categoria and precio:
                #   Al nombre y a la categoria le quito los espacios y hago la primer letra mayuscula
                nombres.append(producto.strip().capitalize())
                categorias.append(categoria.strip().capitalize())
                precios.append(precio)
                print(
                    f"Producto agregado Nombre: {producto} Categoria: {categoria} Precio: ${precio}"
                )
            #   En el caso de que alguna variable este vacio hago un continue
            else:
                print("Te olvidaste de ingresar algo, vuelva a intentarlo  ")
                continue
        #   Caso 2 mostrar los productos
        case "2":
            print("Elegistes 'Mostrar productos'")
            #   Recorro usando un indice las tres listas para mostrar los productos deacuerdo al indice
            for elementos in range(len(nombres)):
                print(
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio: ${precios[elementos]}"
                )
        #   El caso de buscar el producto por el nombre
        case "3":
            print("Elegistes 'Buscar productos'")
            for elementos in range(len(nombres)):
                print(
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio: ${precios[elementos]}"
                )
            #   El nombre lo tomo del mismo modo que lo agrego a las listas
            nombre = input("Nombre del producto? ").strip().capitalize()
            #   Reviso si la variable no esta vacia
            if nombre:
                #   Reviso si lo que ingreso esta en la lista de productos
                if nombre in nombres:
                    #   Guardo el indice del elemento
                    indice = nombres.index(nombre)
                    print(f"Informacion del producto {nombre}")
                    #   Y con el indice consigo los otros datos
                    print(f"Categoria {categorias[indice]}")
                    print(f"Precio {precios[indice]}")
                else:
                    print("Elegiste un producto que no existe.")
                    continue
            else:
                print("Elegiste un producto que no existe.")
                break
        #   El caso de eliminar el producto por el nombre
        case "4":
            #   Primero muestro los existentes
            print("Elegistes 'Eliminar producto'")
            print("Estos son los productos existentes actualmente.")
            for elementos in range(len(nombres)):
                print(
                    f"Producto: {nombres[elementos]} Categoria: {categorias[elementos]}, Precio: ${precios[elementos]}"
                )
            nombre = input("Nombre del producto a eliminar? ").strip().capitalize()
            #   Si la variable no esta vacio
            if nombre:
                #   Y existe en la lista
                if nombre in nombres:
                    #   Obtengo el indice
                    indice = nombres.index(nombre)
                    #   Elimino todos sus elementos
                    del nombres[indice]
                    del categorias[indice]
                    del precios[indice]
                    print("Producto eliminado  ")
                else:
                    print("Elegiste un producto que no existe.")
                    continue
            else:
                print("Elegiste un producto que no existe.")
                break

        case "5":
            #   Salgo de la aplicacion
            print("Elegistes 'Salir'")
            print("Hasta Luego")
            break
        case _:
            #   Me aseguro que no elija una opcio no valida
            print("Elegistes cualquiera ")
            continue
