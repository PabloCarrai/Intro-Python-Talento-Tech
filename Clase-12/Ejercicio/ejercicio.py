import os

# Obtiene la carpeta donde está guardado este script .py
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Une esa carpeta con el nombre del archivo
ruta_archivo = os.path.join(directorio_actual, "datos.txt")

clientes = []


def mostrar_datos(lista):
    if not lista:
        print("\n[!] La lista está vacía.")
        return
    print("\n--- Lista de Clientes ---")
    for elemento in lista:
        print(
            f"Nombre: {elemento[0]} \tApellido: {elemento[1]} \tCorreo: {elemento[2]}"
        )


def pedir_datos():
    nombre = input("Nombre?   ").strip()
    apellido = input("Apellido?   ").strip()
    correo = input("Correo?   ").strip()
    if nombre and apellido and correo:
        if "@" in correo:
            print("Validamos")
            return nombre, apellido, correo
    return None  # Cambiado a None para mejor manejo de errores


def cargar_cliente(lista, nombre, apellido, correo):
    lista.append([nombre, apellido, correo])
    print("Datos Cargados a la lista")


def eliminar_dato(lista, nombre):
    encontrado = False
    # Recorremos de atrás hacia adelante para no saltar índices al borrar
    for elemento in range(len(lista) - 1, -1, -1):
        if nombre.lower() == lista[elemento][0].lower():
            del lista[elemento]
            encontrado = True

    if encontrado:
        print(f"Cliente '{nombre}' eliminado correctamente.")
    else:
        print(f"El nombre '{nombre}' no existe en los datos.")


def leer_datos_archivos(archivo):
    try:
        with open(archivo, "r") as f:
            contenido = f.read()
            if not contenido:
                return []
            return eval(contenido)
    except (FileNotFoundError, SyntaxError):
        print("Error: No se pudo leer el archivo o no existe.")
        return None


def guardar_datos_archivos(lista, archivo):
    try:
        with open(archivo, "w") as f:
            f.write(str(lista))
            print("Datos guardados en", archivo)
    except Exception as e:
        print(f"Error al guardar: {e}")


def mostrar_menu():
    global clientes  # Permite modificar la lista clientes definida fuera de la función
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) Mostrar clientes")
        print("2) Cargar cliente")
        print("3) Eliminar cliente")
        print("4) Guardar a Archivo")
        print("5) Leer desde Archivo")
        print("6) Salir")

        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                mostrar_datos(clientes)
            case "2":
                resultado = pedir_datos()
                if resultado:
                    nombre, apellido, correo = resultado
                    cargar_cliente(clientes, nombre, apellido, correo)
                else:
                    print("Error: Datos incompletos o correo sin @.")
            case "3":
                if not clientes:
                    print("No hay clientes para eliminar.")
                    continue
                nombre = input("Nombre del cliente a eliminar? ")
                eliminar_dato(clientes, nombre)
            case "4":
                guardar_datos_archivos(clientes, ruta_archivo)
            case "5":
                nuevos_datos = leer_datos_archivos(ruta_archivo)
                if nuevos_datos is not None:
                    clientes = nuevos_datos
                    print("Datos cargados correctamente desde el archivo.")
            case "6":
                guardar_datos_archivos(clientes, ruta_archivo)
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")


def main():
    mostrar_menu()


if __name__ == "__main__":
    main()
