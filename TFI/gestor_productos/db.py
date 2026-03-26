#   Importo el modulo sqlite3 y os
import sqlite3
import os

#   Directorio actual del proyecto
directorio_actual = os.path.dirname(os.path.abspath(__file__))
#   Path absoluto del archivo inventario.db
ruta_db = os.path.join(directorio_actual, "inventario.db")


def verificar_db_existe(dbfile):
    """
    Esta funcion chequea si el archivo inventario.db existe, sino ejecuta crear_db()
    """
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
    """
    Chequeo con el path absoluto si el archivo de la db existe y en ese caso lo elimino.
    Caso contrario no hago nada.
    """
    if os.path.exists(ruta_db):
        os.remove(ruta_db)
        print("Archivo Eliminado")
    else:
        print("No hay archivo a Eliminar")


def insertar_datos_db(db, nombre, descripcion, cantidad, precio, categoria):
    #   Creo la conexion a la db
    conexion = sqlite3.connect(db)
    #   Creo el cursor
    cursor = conexion.cursor()
    #   Uso un try para evitar errore
    try:
        #   Esta consulta hace un insert de todos los datos
        consulta = "insert into productos(nombre, descripcion, cantidad, precio, categoria) values(?,?,?,?,?)"
        #   Genero una variable tipo tupla con todos los datos
        datos = (nombre, descripcion, cantidad, precio, categoria)
        #   Corro la consulta con todos los datos
        cursor.execute(consulta, datos)
        #   Hago efectivo el cambio
        conexion.commit()
        print(f"Registro ingresado {datos}")
    except sqlite3.Error as e:
        #   En caso de un error hago un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()


def listar_datos_producto_db(db):
    #   Inicio la conexion a la db
    conexion = sqlite3.connect(db)
    #   Genero un cursor
    cursor = conexion.cursor()
    #   Uso un try por las dudas
    try:
        #   Arrango la transaccion
        cursor.execute("BEGIN TRANSACTION")
        #   Genero la consulta
        consulta = "select id,nombre, descripcion, cantidad, precio, categoria from productos order by nombre"
        #   Corro dicha consulta
        cursor.execute(consulta)
        #   Me traigo los resultados
        resultado = cursor.fetchall()
        #   Los devuelvo
        return resultado
    except sqlite3.Error as e:
        #   En caso de error hago un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()


def validar_id_existente_db(db, id):
    #   Abro la conexion a la db
    conexion = sqlite3.connect(db)
    #   genero un cursor
    cursor = conexion.cursor()
    #   Arranco un try
    try:
        #   Arranco la transaccion
        conexion.execute("BEGIN TRANSACTION;")
        #   Genero una tupla para la consulta
        datos = (id,)
        #   Genero la consulta del select necesario
        secuencia = "select id from productos where id=?"
        #   Ejecuto la consulta pasandoles los datos
        cursor.execute(secuencia, datos)
        #   Solo necesito el primer registro
        resultado = cursor.fetchone()
        #   Devuelvo el mismo
        return resultado
        #   Hago efectivo el cambio
        conexion.commit()
    except sqlite3.Error as e:
        #   En caso de error vamos con un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()


def actualizar_datos_por_id(db, nombre, descripcion, cantidad, precio, categoria, id):
    #   Inicio la conexio
    conexion = sqlite3.connect(db)
    #   Genero un cursor
    cursor = conexion.cursor()
    #   Uso un try por las dudas
    try:
        #   La consulta del update
        consulta = "update productos set nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? where id=?"
        #   La tupla con los nuevos datos
        datos = (nombre, descripcion, cantidad, precio, categoria, id)
        #   Ejecuto el update con los datos
        cursor.execute(consulta, datos)
        #   Genero el cambio
        conexion.commit()
        print("Cambios realizados")
    except sqlite3.Error as e:
        #   Si algo sale mal hago un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()


def eliminar_producto_por_id(db, id):
    #   Me conecto a la db
    conexion = sqlite3.connect(db)
    #   Genero el cursor
    cursor = conexion.cursor()
    #   Uso un try por las dudas
    try:
        #   Arranco la transaccion
        cursor.execute("BEGIN TRANSACTION;")
        #   La consulta del delete
        consulta = "delete from productos where id=?"
        #   La tupla con los datos del id
        datos = (id,)
        #   Ejecuto la consulta con los datos del id
        cursor.execute(consulta, datos)
        #   Hago efectivo el cambio
        conexion.commit()
        print("Registro eliminado")
    except sqlite3.Error as e:
        #   Si algo sale mal hago un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()


def buscar_producto_por_id(db, id):
    #   Me conecto a la db
    conexion = sqlite3.connect(db)
    #   Genero el cursor
    cursor = conexion.cursor()
    #   Uso un try por las dudas
    try:
        #   Arranco la transaccion
        cursor.execute("BEGIN TRANSACTION;")
        #   La consulta del delete
        consulta = "select * from productos where id=?"
        #   Ejecuto la consulta con los datos del id
        cursor.execute(consulta, id)
        #   Solo necesito el primer registro
        resultado = cursor.fetchall()
        #   Devuelvo el mismo
        return resultado
    except sqlite3.Error as e:
        #   Si algo sale mal hago un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()


def buscar_producto_por(db, tipo_busqueda, elemento_a_buscar,operador="="):
    #   Me conecto a la db
    conexion = sqlite3.connect(db)
    #   Genero el cursor
    cursor = conexion.cursor()
    #   Uso un try por las dudas
    try:
        #   Arranco la transaccion
        cursor.execute("BEGIN TRANSACTION;")
        #   La consulta del select
        consulta = f"select * from productos where {tipo_busqueda}{operador}?"
        #   Necesito una tupla para el dato a buscar
        dato = (elemento_a_buscar,)
        #   Ejecuto la consulta con los datos del id
        cursor.execute(consulta, dato)
        #   Solo necesito el primer registro
        resultado = cursor.fetchall()
        #   Devuelvo el mismo
        return resultado
    except sqlite3.Error as e:
        #   Si algo sale mal hago un rollback
        conexion.rollback()
        print(f"Ocurrio un error: {e}")
    finally:
        #   Cierro la conexion
        conexion.close()