"""
Desafío - Funciones que devuelven resultados
Esta vez, cada función tiene que devolver un valor con return, sin modificar listas directamente desde adentro.
Tu programa debe:
    Definir una función que devuelva una nueva lista con un producto agregado.
    Otra función que devuelva una copia sin un producto (si existe).
    Otra función que devuelva la lista ordenada (sin afectar la original).
    El menú principal debe llamar a estas funciones y actualizar la lista principal según los resultados.

🎯 Bonus: mostrar la lista antes y después de cada acción para observar los cambios.
"""


def agregar(lista, producto):
    #   Reviso si producto viene vacio, y retorno la misma lista
    if producto:
        #   Si tiene un valor hago una lista de copia y agrego el valor, retornando esta lista
        copia = lista.copy()
        copia.append(producto)
        return copia
    else:
        print("No se puede agregar un producto vacio")
        return lista


def mostrar(lista):
    if not lista:
        print("No hay nada para mostrar")
    else:
        for elemento in range(len(lista)):
            print(f"Elemento: {elemento+1}, Producto: {lista[elemento]}")


def eliminar(lista, producto):
    copia = lista.copy()
    if producto:
        if producto in copia:
            copia.remove(producto)
            return copia
        else:
            print("No existe dicho producto  ")
    else:
        print("No ingresaste nada para eliminar")


def mostrar_ordenados(lista):
    if not lista:
        print("No hay nada para mostrar")
    else:
        copia = sorted(lista)
        return copia


#   Funcion para mostrar el menu y acceder a las otras funciones.
def mostrar_menu():
    productos = []
    while True:
        print("Bienvenido")
        print("1. Mostrar productos   ")
        print("2. Cargar producto   ")
        print("3. Eliminar producto   ")
        print("4. Mostrar productos ordenados   ")
        print("5. Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print("Mostrar producto  ")
                mostrar(productos)
            case "2":
                print("Cargar producto  ")
                producto = input("Ingrese un producto   ").strip()
                productos = agregar(productos, producto)
            case "3":
                print("Eliminar producto  ")
                producto = input("Producto a eliminar?  ")
                productos = eliminar(productos, producto)
            case "4":
                print("Mostrar productos ordenados  ")
                productos = mostrar_ordenados(productos)
                mostrar(productos)
            case "5":
                print("Salir  ")
                break
            case _:
                print("Elegistes Cualquiera. ")


#   Arranco el programa por mostrar el menu
mostrar_menu()
