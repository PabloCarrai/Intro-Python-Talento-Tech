"""
Desafío - Registro de notas con validación
Vas crear un pequeño sistema para gestionar productos, pero esta vez usando una base de datos real con SQLite.
🔧 ¿Qué tiene que hacer tu programa?
    Mostrar un menú con 4 opciones:
        Agregar un nuevo producto
        Listar todos los productos
        Cambiar el precio de un producto
        Eliminar un producto
    Usar input() para pedir los datos al usuario (nombre, precio, id, etc.)
    Validar los valores ingresados (por ejemplo, que el precio sea un número válido)
    Mostrar mensajes claros de éxito o error en cada operación
💡 Algunas sugerencias:
    Usá INSERT, SELECT, UPDATE y DELETE desde Python con sqlite3
    Usá try-except si querés prevenir errores inesperados
    Probá ejecutar varias operaciones seguidas y consultá al final para ver los resultados
"""

import sqlite3
import os


directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(directorio_actual, "productos-1.db")

#   Definir una tabla llamada productos con
#   los campos id(clave primaria autoincremental),
#   nombre(texto no nulo) y precio(real,no nulo)


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


def insertar_registro(db, producto, precio):
    conexion = sqlite3.connect(db)
    #   Creamos un cursor de la conexion
    cursor = conexion.cursor()
    datos = (producto, precio)
    sentencia = "insert into productos(nombre,precio) values(?,?)"
    #   Ejecutamos la sentencia que crea una tabla productos si esta no existe
    cursor.execute(sentencia, datos)
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos el cursor
    cursor.close()
    #   Cerramos la conexion
    conexion.close()
    print(f"Dato Ingresado, {datos}")


def mostrar_registros(db):
    conexion = sqlite3.connect(db)
    #   Creamos un cursor de la conexion
    cursor = conexion.cursor()
    sentencia = "select * from productos"
    #   Ejecutamos la sentencia
    cursor.execute(sentencia)
    #   Obtengo los registros de la consulta
    filas = cursor.fetchall()
    #   Muestro los datos
    for fila in filas:
        print(f"Id: {fila[0]} Producto: {fila[1].capitalize()}, Precio: $ {fila[2]}")
    #   Cerramos el cursor
    cursor.close()
    #   Cerramos la conexion
    conexion.close()


def modificar_registro(db, producto, precio, id):
    conexion = sqlite3.connect(db)
    #   Creamos un cursor de la conexion
    cursor = conexion.cursor()
    datos = (producto, precio, id)
    sentencia = "update productos set nombre=?, precio=? where id=?"
    #   Ejecutamos la sentencia que crea una tabla productos si esta no existe
    cursor.execute(sentencia, datos)
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos el cursor
    cursor.close()
    #   Cerramos la conexion
    conexion.close()
    print(f"Dato modificado, {datos}")


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


def validar_id_exista_db(db, id):
    conexion = sqlite3.connect(db)
    #   Creamos un cursor de la conexion
    cursor = conexion.cursor()
    sentencia = "select id from productos where id=?"
    #   Ejecutamos la sentencia
    cursor.execute(sentencia, (id,))
    #   Obtengo los registros de la consulta
    filas = cursor.fetchone()
    #   Revuelvo el registro existente
    return filas
    #   Cerramos el cursor
    cursor.close()
    #   Cerramos la conexion
    conexion.close()


def eliminar_registro(db, id):
    conexion = sqlite3.connect(db)
    #   Creamos un cursor de la conexion
    cursor = conexion.cursor()
    sentencia = "delete from productos where id=?"
    #   Ejecutamos la sentencia que crea una tabla productos si esta no existe
    cursor.execute(sentencia, (id,))
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos el cursor
    cursor.close()
    #   Cerramos la conexion
    conexion.close()
    print("Dato eliminado")


def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Cargar Producto")
        print("2) Mostrar Productos")
        print("3) Modificar Productos")
        print("4) Eliminar Productos")
        print("5) Salir")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                while True:
                    nombre = input("Nombre?   ")
                    precio = input("Precio?   ")
                    try:
                        precio = int(precio)
                    except ValueError:
                        print(f"El precio esta mal ingresado")
                    if validar_datos(nombre, precio):
                        insertar_registro(ruta_db, nombre, precio)
                        break
                    else:
                        print("Hay un problema con los datos ingresados")
                        continue
            case "2":
                mostrar_registros(ruta_db)
            case "3":
                mostrar_registros(ruta_db)
                id = input("Ingrese el id del producto a modificar   ")
                if id:
                    print("Es un id no vacio")
                    try:
                        resultado = validar_id_exista_db(ruta_db, id)
                        if resultado == None:
                            print("No hay datos")
                        else:
                            nombre = input("Nombre?   ")
                            precio = input("Precio? ")
                            try:
                                precio = int(precio)
                            except ValueError:
                                print("Problema con el precio")
                            if validar_datos(nombre, precio):
                                modificar_registro(ruta_db, nombre, precio, id)
                            else:
                                print("Problema con los datos. ")
                    except Exception as e:
                        print(f"Error {e}")
                else:
                    print("Id vacio")
            case "4":
                mostrar_registros(ruta_db)
                id = input("Ingrese el id del producto a eliminar   ")
                if id:
                    print("Es un id no vacio")
                    try:
                        resultado = validar_id_exista_db(ruta_db, id)
                        if resultado == None:
                            print("No hay datos")
                        else:
                            eliminar_registro(ruta_db, id)
                            print("Eliminar registro")
                            pass
                    except Exception as e:
                        print(f"Error {e}")
                else:
                    print("Id vacio")
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")


def main():
    mostrar_menu()


if __name__ == "__main__":
    main()
