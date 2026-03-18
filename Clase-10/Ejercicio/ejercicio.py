"""
Pagina 15
Agregar Producto: Cada producto debe tener uun nombre y precio.
Consultar Productos: Muestra todos los productos en la lista junto con sus precios
Eliminar productos: A partir de su nombre
Menu interactivo: Debe ofrecer un menu para que se pueda elegir la accion a realizar.
(Incorporar funciones que devuelvan un valor)
"""

#   Las listas en donde guardo los datos
nombres = []
precios = []


#   Funcion para mostrar los productos
def mostrar_producto():
    if nombres:
        return nombres
    else:
        return []
        


#   Funcion para eliminar producto
def eliminar_producto():
    while True:
        resultado = mostrar_producto()
        if resultado:
            for i, fruta in enumerate(nombres, start=1):
                print(f"{i}.{fruta}")
            else:
                print("Lista Vacia")
        nombre = (
            input("Ingrese el nombre del producto a eliminar   ").strip().capitalize()
        )
        if nombre:
            if nombre in nombres:
                indice = nombres.index(nombre)
                del nombres[indice]
                del precios[indice]
                return nombre
                break
            else:
                return "El nombre no es valido"
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
            return nombre, precio
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
                resultado = mostrar_producto()
                if resultado:
                    for i, fruta in enumerate(nombres, start=1):
                        print(f"{i}.{fruta}")
                else:
                    print("Lista Vacia")
            case "2":
                print("Cargar producto  ")
                fruta, precio = cargar_producto()
                print(f"Fruta: {fruta}  ${precio}")
            case "3":
                print("Eliminar producto  ")
                resultado = eliminar_producto()
                print(resultado)
            case "4":
                print("Salir  ")
                break
            case _:
                print("Elegistes Cualquiera. ")


#   Arranco el programa por mostrar el menu
mostrar_menu()
