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
            print(f"Id: {dato[0]}, Nombre: {dato[1]} Precio: ${dato[2]}")


def validar_datos():
    while True:
        try:
            nombre = input("Nombre?   ").strip().capitalize()
            precio = int(input("Precio?    "))
            if not nombre or precio <= 0:
                continue
            else:
                return nombre, precio
                break
        except ValueError:
            print("Error en los datos cargados")


def insertar_datos(db, nombre, precio):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        datos = (nombre, precio)
        cursor.execute("insert into productos(nombre,precio) values(?,?)", datos)
        conexion.commit()
        print("Registro insertado")
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"Error detectado, haciendo rollback: {e}")


def validar_id_existente_db(db, id):
    #   Abro la conexion
    conexion = sqlite3.connect(db)
    #   Genero un cursor
    cursor = conexion.cursor()
    #   La sentencia del select
    sentencia = "select id from productos where id=?"
    datos = (id,)
    #   Corro dicha sentencia
    cursor.execute(sentencia, datos)
    #   guardo el resultado en filas
    filas = cursor.fetchone()
    return filas
    conexion.close()


def editar_valores_db(db, nombre, precio, id):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION;")
        sentencia = "update productos set nombre=?, precio=? where id=?"
        datos = (nombre, precio, id)
        cursor.execute(sentencia, datos)
        cursor.execute("COMMIT;")
        print("Transaccion comiteada como el vecino manda.")
    except sqlite3.Error as e:
        print(f"Ocurrio un error: {e}")
        cursor.execute("ROLLBACK;")
        print("Se hizo un rollback")
    finally:
        conexion.close()


def validar_id(db):
    while True:
        try:
            id_existente = int(input("Id?"))
            if (
                id_existente <= 0
                or validar_id_existente_db(ruta_db, id_existente) == None
            ):
                continue
            else:
                return id_existente
                break
        except ValueError:
            print(f"Error con el id")


def eliminar_dato_db(db, id):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        sentencia = "delete from productos where id=?"
        datos = (id,)
        cursor.execute(sentencia, datos)
        conexion.commit()
        print("Registro eliminado como el vecino manda. ")
    except sqlite3.Error as e:
        conexion.rollback()
        print("Ocurrio un error: {e}")
    finally:
        conexion.close()


def validar_desicion_usuario(db, id):
    respuesta = (
        input(f"{Back.RED}Esta seguro que quiere eliminar el producto?    ").lower().strip()
    )
    match respuesta:
        case "si" | "s":
            print(f"{Back.RED}Eliminando producto")
            eliminar_dato_db(db, id)
        case "no" | "n":
            print(f"{Back.BLUE}No eliminamos nada")
        case _:
            print(f"{Back.GREEN}Respuesta no reconocida....")


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
                nombre, precio = validar_datos()
                insertar_datos(ruta_db, nombre, precio)
                print(f"{nombre}{precio}")
            case "2":
                print(f"{Back.RED}Mostrar Producto  ")
                mostrar_datos_db(leer_datos(ruta_db))
            case "3":
                print(f"{Back.RED}Editar Producto  ")
                mostrar_datos_db(leer_datos(ruta_db))
                id = validar_id(ruta_db)
                nombre, precio = validar_datos()
                editar_valores_db(ruta_db, nombre, precio, id)
            case "4":
                print(f"{Back.RED}Eliminar Producto  ")
                mostrar_datos_db(leer_datos(ruta_db))
                id = validar_id(ruta_db)

                validar_desicion_usuario(ruta_db, id)
            case "5":
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


def main():
    #   verificar_db_existe(ruta_db)
    #   Arranco el programa por mostrar el menu
    mostrar_menu()


if __name__ == "__main__":
    main()
