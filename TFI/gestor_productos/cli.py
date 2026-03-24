#   Del modulo db nos trameos funciones que afectan la db
from db import (
    eliminar_db,
    ruta_db,
    verificar_db_existe,
    insertar_datos_db,
    listar_datos_producto_db,
    validar_id_existente_db,
    actualizar_datos_por_id,
    eliminar_producto_por_id,
)

#   Funciones_extras son funciones a parte de las usadas por la db.
from funciones_extras import (
    verificar_si_no,
    ingresar_datos,
    mostrar_datos_productos,
    validar_ingreso_id_valido,
)

#   Importamos colorama para el menu
from colorama import init, Fore, Back

init(autoreset=True)


def inicializaciones_base_dato():
    #   Esta funcion es un menu para la gestion de la db
    while True:
        print(f"{Back.GREEN}Menu Base de Datos")
        print(f"{Back.RED}1) {Back.BLUE}Inicializar Base De Datos   ")
        print(f"{Back.RED}2) {Back.BLUE}Eliminar Base De Datos   ")
        print(f"{Back.RED}3) {Back.BLUE}Salir   ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                #   Aca inicializamos la db, por si no existe
                print(f"{Back.RED}Inicializar Base De Datos   ")
                verificar_db_existe(ruta_db)
            case "2":
                #   En algunos casos es necesario eliminar la db
                print(f"{Back.RED}Eliminar Base De Datos   ")
                verificar_si_no(eliminar_db, "Estas seguro de querer eliminar la db?")
            case "3":
                print(f"{Back.RED}Salir   ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


def mostrar_menu_secundario():
    #   Este es el menu de busquedas
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
    #   Este es el menu principal
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
                #   Aca validamos la correcta carga de los datos necesarios
                nombre, descripcion, cantidad, precio, categoria = ingresar_datos()
                #   Insertamos los mismos en la db
                insertar_datos_db(
                    ruta_db, nombre, descripcion, cantidad, precio, categoria
                )
            case "2":
                print(f"{Back.RED}Listar Producto   ")
                #   guardamos la consulta en resultado
                resultado = listar_datos_producto_db(ruta_db)
                #   Y los mostramos
                mostrar_datos_productos(resultado)
            case "3":
                print(f"{Back.RED}Actualizar Producto(por Id)   ")
                #   guardamos la consulta en resultado
                resultado = listar_datos_producto_db(ruta_db)
                #   Y los mostramos
                mostrar_datos_productos(resultado)
                #   Validamos el id como dato valido
                id = validar_ingreso_id_valido()
                #   Validamos que exista en la db
                resultado = validar_id_existente_db(ruta_db, id)
                #   Si resultado es none indicamos el error, que no hay datos
                if resultado == None:
                    print("No hay datos para ese id.")
                    continue
                else:
                    #   validamos todos los datos
                    nombre, descripcion, cantidad, precio, categoria = ingresar_datos()
                    #   con esos datos actualizamos el registro por el id
                    actualizar_datos_por_id(
                        ruta_db, nombre, descripcion, cantidad, precio, categoria, id
                    )
                    print("Registro actualizado")
            case "4":
                print(f"{Back.RED}Buscar Producto    ")
                #   Accedemos a otro menu secundario
                mostrar_menu_secundario()
            case "5":
                print(f"{Back.RED}Eliminar Producto(por Id)   ")
                #   mostramos los productos
                resultado = listar_datos_producto_db(ruta_db)
                mostrar_datos_productos(resultado)
                #   Validamos el id
                id = validar_ingreso_id_valido()
                #   que el id exista en la db
                resultado = validar_id_existente_db(ruta_db, id)
                if resultado == None:
                    print("No hay datos para ese id.")
                    continue
                else:
                    #   Eliminamos el producto por el id
                    eliminar_producto_por_id(ruta_db, id)
            case "6":
                print(f"{Back.RED}Inicializaciones Base Datos(Peligroso)")
                #   Accedemos a otro menu
                inicializaciones_base_dato()
            case "7":
                #   Salimos
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")
