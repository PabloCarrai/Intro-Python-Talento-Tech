from db import (
    eliminar_db,
    ruta_db,
    verificar_db_existe,
    insertar_datos_db,
    listar_datos_producto_db,
)
from funciones_extras import verificar_si_no, ingresar_datos, mostrar_datos_productos
from colorama import init, Fore, Back

init(autoreset=True)


def inicializaciones_base_dato():
    while True:
        print(f"{Back.GREEN}Menu Base de Datos")
        print(f"{Back.RED}1) {Back.BLUE}Inicializar Base De Datos   ")
        print(f"{Back.RED}2) {Back.BLUE}Eliminar Base De Datos   ")
        print(f"{Back.RED}3) {Back.BLUE}Salir   ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print(f"{Back.RED}Inicializar Base De Datos   ")
                verificar_db_existe(ruta_db)
            case "2":
                print(f"{Back.RED}Eliminar Base De Datos   ")
                verificar_si_no(eliminar_db, "Estas seguro de querer eliminar la db?")
            case "3":
                print(f"{Back.RED}Salir   ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


def mostrar_menu_secundario():
    while True:
        print(f"{Back.GREEN}Menu Busqueda")
        print(f"{Back.RED}1) {Back.BLUE}Buscar por Id)   ")
        print(f"{Back.RED}2) {Back.BLUE}Buscar por Nombre)   ")
        print(f"{Back.RED}3) {Back.BLUE}Buscar por Categoria)   ")
        print(f"{Back.RED}4) {Back.BLUE}Buscar por Cantidad)   ")
        print(f"{Back.RED}5) {Back.BLUE}Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print(f"{Back.RED}Buscar Producto(por Id)   ")
            case "2":
                print(f"{Back.RED}Buscar Producto(por nombre)   ")
            case "3":
                print(f"{Back.RED}Buscar Producto(por categoria)   ")
            case "4":
                print(f"{Back.RED}Buscar Producto(por cantidad)   ")
            case "5":
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


def mostrar_menu():
    while True:
        print(f"{Back.GREEN}Bienvenido")
        print(f"{Back.RED}1) {Back.BLUE}Nuevo Producto   ")
        print(f"{Back.RED}2) {Back.BLUE}Listar Producto   ")
        print(f"{Back.RED}3) {Back.BLUE}Actualizar Producto(por Id)   ")
        print(f"{Back.RED}4) {Back.BLUE}Buscar Producto    ")
        print(f"{Back.RED}5) {Back.BLUE}Eliminar Producto(por Id)   ")
        print(f"{Back.RED}6) {Back.BLUE}Inicializaciones Base Datos(Peligroso)   ")
        print(f"{Back.RED}7) {Back.BLUE}Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print(f"{Back.RED}Nuevo Producto   ")
                nombre, descripcion, cantidad, precio, categoria = ingresar_datos()
                insertar_datos_db(
                    ruta_db, nombre, descripcion, cantidad, precio, categoria
                )
            case "2":
                print(f"{Back.RED}Listar Producto   ")
                resultado = listar_datos_producto_db(ruta_db)
                mostrar_datos_productos(resultado)
            case "3":
                print(f"{Back.RED}Actualizar Producto(por Id)   ")
            case "4":
                print(f"{Back.RED}Buscar Producto    ")
                mostrar_menu_secundario()
            case "5":
                print(f"{Back.RED}Eliminar Producto(por Id)   ")
            case "6":
                print(f"{Back.RED}Inicializaciones Base Datos(Peligroso)")
                inicializaciones_base_dato()
            case "7":
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")
