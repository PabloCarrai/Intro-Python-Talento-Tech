"""
Pagina 17
Modificar el programa de la clase 10 para usar una mejora de
la misma usando el modulo Colorama. Y agregar la fecha y hora de la compra.
"""

from colorama import init, Fore, Back
from datetime import datetime

init(autoreset=True)

#   Las listas en donde guardo los datos
nombres = []
precios = []
fechas = []


#   Funcion para mostrar los productos
def mostrar_producto():
    if nombres:
        for elemento in range(len(nombres)):
            print(
                f"{elemento+1}-  {nombres[elemento]}-  ${precios[elemento]} ({fechas[elemento]})"
            )
    else:
        print("No hay nada")


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
                del fechas[indice]
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
            ahora = datetime.now()
            ahora_arreglado = ahora.strftime("%d/%m/%y - %H:%M")
            nombres.append(nombre)
            precios.append(precio)
            fechas.append(ahora_arreglado)
            return nombre, precio
            break
        else:
            print("No ingreso alguno de los datos. Vuelva a intentarlo")
            continue


#   Funcion para mostrar el menu y acceder a las otras funciones.
def mostrar_menu():
    while True:
        print(f"{Back.GREEN}Bienvenido")
        print(f"{Back.RED}1) {Back.BLUE}Mostrar productos   ")
        print(f"{Back.RED}2) {Back.BLUE}Cargar producto   ")
        print(f"{Back.RED}3) {Back.BLUE}Eliminar producto   ")
        print(f"{Back.RED}4) {Back.BLUE}Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print(f"{Back.RED}Mostrar producto  ")
                mostrar_producto()
            case "2":
                print(f"{Back.RED}Cargar producto  ")
                fruta, precio = cargar_producto()
                print(f"Fruta: {fruta}  ${precio}")
            case "3":
                print(f"{Back.RED}Eliminar producto  ")
                resultado = eliminar_producto()
                print(resultado)
            case "4":
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


#   Arranco el programa por mostrar el menu
mostrar_menu()
