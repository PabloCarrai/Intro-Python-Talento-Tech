def verificar_si_no(funcion, pregunta):
    #   Esta funcion usa una pregunta, y espera una confirmacion a esa pregunta
    respuesta = input(pregunta).lower().strip()
    #   De acuerdo a la pregunta lanzamos una funcion
    match respuesta:
        case "si" | "s":
            print("Genial, avanzamos nomas...")
            funcion()
        case "no" | "n":
            print("Ok no hacemos nada... ")
        case _:
            print("Respondistes cualquiera. Ubicate...")


def ingresar_datos():
    #   Aca pedimos los datos y lo validamos
    while True:
        try:
            nombre = input("Nombre?   ").capitalize()
            descripcion = input("Descripcion?   ").capitalize()
            cantidad = int(input("Cantidad?  "))
            precio = int(input("Precio?   "))
            categoria = input("Categoria?   ").capitalize()
            #   Primero validamos que no esten vacios
            if not nombre or not descripcion or not categoria:
                print("Estas Cargando Mal los Valores")
            else:
                #   Despues validamos los valores
                if precio <= 0 or cantidad <= 0:
                    print("Estas Cargando Mal los Valores")
                    continue
                else:
                    #   Recien ahi devolvemos los mismos
                    return (nombre, descripcion, int(cantidad), int(precio), categoria)
        except Exception as e:
            print(f"Error Estas Cargando Mal los Valores. {e}")


def mostrar_datos_productos(resultado):
    #   Validamos que resultado no este vacio
    if not resultado:
        print("No hay registros cargados")
    else:
        #   Mostramos todos los datos
        for dato in resultado:
            print(
                f"Id: {dato[0]} Nombre: {dato[1]} Descripcion: {dato[2]} Cantidad: {dato[3]} Precio: ${dato[4]} Categoria: {dato[5]}"
            )


def validar_ingreso_id_valido():
    #   Validamos un id valido
    while True:
        try:
            id = int(input("Id?   "))
            if id <= 0:
                print("El id esta mal cargado...")
                continue
            else:
                return id
                break
        except ValueError:
            print("El id esta mal cargado...")
