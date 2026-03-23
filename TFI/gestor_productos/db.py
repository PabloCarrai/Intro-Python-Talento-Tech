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