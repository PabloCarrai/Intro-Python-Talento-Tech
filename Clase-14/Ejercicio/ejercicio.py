"""
Validar los nombres de productos no esten vacios.
El precio sea un numero positivo antes de almacenarlo.
En la eliminacion de producto pedir una confirmacion antes
de proceder. Usar colorama para resaltar mensajes.
En rojo las advertencias en verde las confirmaciones
y en azul la informacion general
"""

from colorama import init, Fore, Back
import sqlite3
import os


directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(directorio_actual, "productos.db")
init(autoreset=True)


def verificar_db_existe(dbfile):
    try:
        if os.path.isfile(dbfile):
            print(f"El archivo {dbfile} existe, no nos toca hacer nada")
        else:
            print(f"El archivo {dbfile} no existe, ejecutar crear_db()")
            crear_db()
    except Exception as e:
        print(f"Error {e}")


def crear_db():
    #   accedemos a la db, si no esta la crea.
    conexion = sqlite3.connect(ruta_db)
    #   Creamos un cursor de la conexion
    cursor = conexion.cursor()
    #   Ejecutamos la sentencia que crea una tabla productos si esta no existe
    cursor.execute(
        "create table if not exists productos(id integer primary key autoincrement, nombre text not null, precio real not null)"
    )
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos la conexion
    conexion.close()
    print("Base de datos creada con su tabla productos")


def leer_datos(db):
    #   Abro la conexion
    conexion = sqlite3.connect(db)
    #   Genero un cursor
    cursor = conexion.cursor()
    #   La sentencia del select
    sentencia = "select * from productos"
    #   Corro dicha sentencia
    cursor.execute(sentencia)
    #   guardo el resultado en filas
    filas = cursor.fetchall()
    return filas
    conexion.close()


def mostrar_datos_db(datos):
    if datos is None:
        print("No hay datos")
    else:
        for dato in datos:
            print(f"Id: {dato[0]}, Nombre: {dato[1]} Precio: {dato[2]}")


def validar_datos(nombre, precio):
    if (
        isinstance(nombre, str)
        and bool(nombre.strip())
        and isinstance(precio, int)
        and precio > 0
    ):
        return True
    else:
        return False


def cargar_productos_db(db, nombre, precio):
    try:
        if validar_datos(nombre, precio):
            conexion = sqlite3.connect(db)
            #   Genero un cursor
            cursor = conexion.cursor()
            sentencia = "insert into productos(nombre,precio) values(?,?)"
            datos = (nombre, precio)
            conexion.execute(sentencia, datos)
            conexion.commit()
            conexion.close()
            print("Datos insertados")
        else:
            print("Error en alguno de los datos")
    except Exception as e:
        print(f"Error {e}")

        


def mostrar_menu():
    while True:
        print(f"{Back.GREEN}Bienvenido")
        print(f"{Back.RED}1) {Back.BLUE}Cargar Productos   ")
        print(f"{Back.RED}2) {Back.BLUE}Mostrar Producto   ")
        print(f"{Back.RED}3) {Back.BLUE}Editar Producto   ")
        print(f"{Back.RED}4) {Back.BLUE}Eliminar Producto   ")
        print(f"{Back.RED}5) {Back.BLUE}Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print(f"{Back.RED}Cargar Producto  ")
                while True:
                    nombre = input("Nombre?    ")
                    precio = input("Precio?    ")
                    cargar_productos_db(ruta_db, nombre, int(precio))
            case "2":
                print(f"{Back.RED}Mostrar Producto  ")
                mostrar_datos_db(leer_datos(ruta_db))
            case "3":
                print(f"{Back.RED}Editar Producto  ")
            case "4":
                print(f"{Back.RED}Eliminar Producto  ")
            case "5":
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


def main():
    #   Arranco el programa por mostrar el menu
    mostrar_menu()


if __name__ == "__main__":
    main()
