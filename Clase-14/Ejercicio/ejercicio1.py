"""
Desafío - Sistema seguro de gestión de alumnos
Te propongo un desafío integral: crear un programa que permita gestionar una base de datos de alumnos con todas las buenas prácticas que aprendiste.
🔧 ¿Qué tiene que hacer el programa?
    Mostrar un menú con las siguientes opciones:
        Agregar un nuevo alumno
        Listar todos los alumnos
        Modificar el email de un alumno
        Eliminar un alumno (con confirmación)
        Salir
    Usar consultas SQL seguras con parámetros (?)
    Validar entradas (por ejemplo, que el ID sea un número válido)
    Mostrar mensajes claros de éxito o advertencia
    Cuidar la integridad de los datos (usando commit() y validaciones)
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
    #   Ejecutamos la sentencia que crea una tabla productos si esta no existe
    cursor.execute(
        "create table if not exists estudiantes(id integer primary key autoincrement, nombre text not null, apellido text not null,correo text not null)"
    )
    #   Hacemos efectivos los cambios
    conexion.commit()
    #   Cerramos la conexion
    conexion.close()
    print("Base de datos creada con su tabla estudiantes")


def leer_datos(db):
    #   Abro la conexion
    conexion = sqlite3.connect(db)
    #   Genero un cursor
    cursor = conexion.cursor()
    #   La sentencia del select
    sentencia = "select * from estudiantes"
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
            print(
                f"Id: {dato[0]}, Nombre: {dato[1]} Apellido: {dato[2]} Correo: {dato[3]}"
            )


def validar_datos():
    while True:
        try:
            nombre = input("Nombre?   ").strip().capitalize()
            apellido = input("Apellido?   ").strip().capitalize()
            correo = input("Correo?    ")
            if not nombre or not apellido or not correo:
                continue
            else:
                return nombre, apellido, correo
                break
        except ValueError:
            print("Error en los datos cargados")


def insertar_datos(db, nombre, apellido, correo):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        datos = (nombre, apellido, correo)
        cursor.execute(
            "insert into estudiantes(nombre, apellido,correo) values(?,?,?)", datos
        )
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
    sentencia = "select id from estudiantes where id=?"
    datos = (id,)
    #   Corro dicha sentencia
    cursor.execute(sentencia, datos)
    #   guardo el resultado en filas
    filas = cursor.fetchone()
    return filas
    conexion.close()


def editar_valores_db(db, correo, id):
    conexion = sqlite3.connect(db)
    cursor = conexion.cursor()
    try:
        cursor.execute("BEGIN TRANSACTION;")
        sentencia = "update estudiantes set correo=? where id=?"
        datos = (correo, id)
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
        sentencia = "delete from estudiantes where id=?"
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
        input(f"{Back.RED}Esta seguro que quiere eliminar el estudiante?    ")
        .lower()
        .strip()
    )
    match respuesta:
        case "si" | "s":
            print(f"{Back.RED}Eliminando estudiante")
            eliminar_dato_db(db, id)
        case "no" | "n":
            print(f"{Back.BLUE}No eliminamos nada")
        case _:
            print(f"{Back.GREEN}Respuesta no reconocida....")


def validar_correo():
    while True:
        try:
            correo = input("Correo?    ")
            if not correo:
                continue
            else:
                return correo
                break
        except ValueError:
            print("Error en los datos cargados")


def mostrar_menu():
    while True:
        print(f"{Back.GREEN}Bienvenido")
        print(f"{Back.RED}1) {Back.BLUE}Nuevo Alumno   ")
        print(f"{Back.RED}2) {Back.BLUE}Listar Alumnos   ")
        print(f"{Back.RED}3) {Back.BLUE}Modificar Correo   ")
        print(f"{Back.RED}4) {Back.BLUE}Eliminar Alumno   ")
        print(f"{Back.RED}5) {Back.BLUE}Salir    ")
        opcion = input("Ingrese una opcion  ")
        match opcion:
            case "1":
                print(f"{Back.RED}Nuevo Alumno  ")
                nombre, apellido, correo = validar_datos()
                insertar_datos(ruta_db, nombre, apellido, correo)
                print(f"{nombre} {apellido}")
            case "2":
                print(f"{Back.RED}Listar Alumnos  ")
                mostrar_datos_db(leer_datos(ruta_db))
            case "3":
                print(f"{Back.RED}Modificar Correo  ")
                mostrar_datos_db(leer_datos(ruta_db))
                id = validar_id(ruta_db)
                correo = validar_correo()
                editar_valores_db(ruta_db, correo, id)
            case "4":
                print(f"{Back.RED}Eliminar Alumno  ")
                mostrar_datos_db(leer_datos(ruta_db))
                id = validar_id(ruta_db)
                validar_desicion_usuario(ruta_db, id)
            case "5":
                print(f"{Back.RED}Salir  ")
                break
            case _:
                print(f"{Back.RED}Elegistes Cualquiera. ")


def main():
    # verificar_db_existe(ruta_db)
    #   Arranco el programa por mostrar el menu
    mostrar_menu()


if __name__ == "__main__":
    main()
