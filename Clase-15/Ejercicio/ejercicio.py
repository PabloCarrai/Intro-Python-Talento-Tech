"""
Crear un programa para generar el
archivo .db y la tabla necesaria.
Para el TFI
"""

from colorama import init, Fore, Back
import sqlite3
import os


directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_db = os.path.join(directorio_actual, "estudiantes.db")
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
    #   Ejecutamos la sentencia que crea una tabla alumno si esta no existe
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,apellido TEXT NOT NULL,edad INTEGER CHECK (edad >= 5 AND edad <= 120),curso TEXT NOT NULL,email TEXT UNIQUE CHECK (email LIKE '%@%'))"
    )
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos la conexion
    conexion.close()
    print("Base de datos creada con su tabla estudiantes")


def main():
    verificar_db_existe(ruta_db)


if __name__ == "__main__":
    main()
