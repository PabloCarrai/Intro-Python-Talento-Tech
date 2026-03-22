"""
1). Crear una base de datos SQlite llamada productos.db
2). Definir una tabla llamada productos con los campos id(clave primaria autoincremental),nombre(texto no nulo) y precio(real,no nulo)
3). Diseñar un programa que permita:
    Registrar un producto ingresando su nombre y precio.
    Mostrar todos los productos almacenados en la base de datos

El nombre no puede estar vacio.
El precio debe ser un numero mayor que cero.
"""

import sqlite3
import os


directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(directorio_actual, "productos.db")

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
        " create table if not exists productos(id integer primary key autoincrement, nombre text not null, precio real not null)"
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


def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Cargar Producto")
        print("2) Mostrar Productos")
        print("3) Salir")

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
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")


def main():
    mostrar_menu()


if __name__ == "__main__":
    main()
