import sqlite3
import os

#   Directorio actual del proyecto
directorio_actual = os.path.dirname(os.path.abspath(__file__))
#   Path absoluto del archivo inventario.db
ruta_db = os.path.join(directorio_actual, "inventario.db")


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
        "CREATE TABLE productos (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,descripcion TEXT,cantidad INTEGER NOT NULL CHECK (cantidad >= 0),precio REAL NOT NULL CHECK (precio > 0.0),categoria TEXT)"
    )
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos la conexion
    conexion.close()
    print("Base de datos creada con su tabla productos")


def eliminar_db():
    if os.path.exists(ruta_db):
        os.remove(ruta_db)
        print("Archivo Eliminado")
    else:
        print("No hay archivo a Eliminar")


"""
CREATE TABLE productos (id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
descripcion TEXT,
cantidad INTEGER NOT NULL CHECK (cantidad >= 0),
precio REAL NOT NULL CHECK (precio > 0.0),
categoria TEXT)"
"""


def insertar_datos_db(db, nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        consulta = "insert into productos(nombre, descripcion, cantidad, precio, categoria) values(?,?,?,?,?)"
        datos = (nombre, descripcion, cantidad, precio, categoria)
        cursor.execute(consulta, datos)
        conexion.commit()
        print(f"Registro ingresado {datos}")
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        conexion.close()


def listar_datos_producto_db(db):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION")
        consulta = "select nombre, descripcion, cantidad, precio, categoria from productos order by nombre"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        conexion.close()
