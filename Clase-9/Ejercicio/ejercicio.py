"""
Pagina 20
Crear un programa que haga lo siguiente(usando funciones).
Agregar productos: permite a la usuarios/as agregar producto a una lista.
Cada producto debe tener un nombre y un precio.
Consultar productos: Muestra todos los productos en la lista junto con
sus precios.
Eliminar productos: Elimina un prodcto de la lista a partir de su nombre
menu interactivo. El programa debe ofrecer un menu ara el usuario/a
"""

#   Las listas en donde guardo los datos
nombres = []
precios = []


#   Funcion para mostrar los productos
def mostrar_producto():
    print("Bienvenido")
    print("Productos disponibles ")
    if len(nombres) == 0:
        print("No hay productos cargados")
    else:
        for elemento in range(len(nombres)):
            print(f"Productos: {nombres[elemento]}, Precio: {precios[elemento]}")


#   Funcion para eliminar producto
def eliminar_producto():
    while True:
        mostrar_producto()
        nombre = (
            input("Ingrese el nombre del producto a eliminar   ").strip().capitalize()
        )
        if nombre:
            if nombre in nombres:
                indice = nombres.index(nombre)
                del nombres[indice]
                del precios[indice]
                print("Producto eliminado")
                break
            else:
                print("El nombre no es valido")
                continue
        else:
            print("El nombre no es valido")
            continue


#   Funcion para cargar producto
def cargar_producto():
    while True:
        print("Bienvenido a la carga de productos  ")
        nombre = input("Nombre del Producto?   ").strip().capitalize()
        precio = input("Precio del Producto?  ")
        if nombre and precio:
            nombres.append(nombre)
            precios.append(precio)
            print("Producto ingresado")
            break
        else:
            print("No ingreso alguno de los datos. Vuelva a intentarlo")
            continue


#   Funcion para mostrar el menu y acceder a las otras funciones.
def mostrar_menu():
    while True:
        print("Bienvenido")
        print("1. Mostrar productos   ")
        print("2. Cargar producto   ")
        print("3. Eliminar producto   ")
        print("4. Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print("Mostrar producto  ")
                mostrar_producto()
            case "2":
                print("Cargar producto  ")
                cargar_producto()
            case "3":
                print("Eliminar producto  ")
                eliminar_producto()
            case "4":
                print("Salir  ")
                break
            case _:
                print("Elegistes Cualquiera. ")


#   Arranco el programa por mostrar el menu
mostrar_menu()
