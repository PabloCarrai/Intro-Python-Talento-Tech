def verificar_si_no(funcion, pregunta):
    respuesta = input(pregunta).lower().strip()
    match respuesta:
        case "si" | "s":
            print("Genial, avanzamos nomas...")
            funcion()
        case "no" | "n":
            print("Ok no hacemos nada... ")
        case _:
            print("Respondistes cualquiera. Ubicate...")


def ingresar_datos():
    while True:
        try:
            nombre = input("Nombre?   ").capitalize()
            descripcion = input("Descripcion?   ").capitalize()
            cantidad = int(input("Cantidad?  "))
            precio = int(input("Precio?   "))
            categoria = input("Categoria?   ").capitalize()
            if not nombre or not descripcion or not categoria:
                print("Estas Cargando Mal los Valores")
            else:
                return (nombre, descripcion, int(cantidad), int(precio), categoria)
        except Exception as e:
            print(f"Error Estas Cargando Mal los Valores. {e}")


def mostrar_datos_productos(resultado):
    if not resultado:
        print("No hay registros cargados")
    else:
        for dato in resultado:
            print(
                f"Nombre: {dato[0]} Descripcion: {dato[1]} Cantidad: {dato[2]} Precio: {dato[3]} Categoria: {dato[4]}"
            )
