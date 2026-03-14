"""
Formate correctamente los textos ingresados en apellido y nombre,
convirtiendo las primeras letras de cada palabra a mayuscula y
el resto en minustulas. asegurarse que el correo electronico no
tenga espacios y contenga solo una @. Que clasifique a sus clientes
por rango etario basandose en su edad
(Niño/a para los y las menores de 15 años
adolescente de 15 a 18 y adulto/a para personas mayores a 18 años)
"""

apellido = input("Ingrese su Apellido:  ").title()
nombre = input("Ingrese su Nombre:   ").title()
edad = int(input("Ingrese su edad:  "))
correo_electronico = input("Ingrese su correo: ").lower().strip()


#   Evaluar que los datos no vengan vacios
errores_varios = ""
if not nombre:
    errores_varios = errores_varios + "Falto ingresar el nombre\n"
if not apellido:
    errores_varios = errores_varios + "Falto ingresar el apellido\n"
if not edad:
    errores_varios = (
        errores_varios + "Falto ingresar La edad o no ingresaste un valor valido\n"
    )
else:
    evaluacion_edad = ""
    if 1 <= edad < 15:
        evaluacion_edad = "Niños/a"
    elif 15 <= edad < 18:
        evaluacion_edad = "Adolescente"
    elif edad >= 18:
        evaluacion_edad = "Adulto/a"

if not correo_electronico:
    errores_varios = errores_varios + "Falto ingresar el correo\n"

if len(errores_varios) >= 1:
    print(f"Hubo Errores {errores_varios}")

#   No tengo una forma sencilla con lo que vimos de evitar el @@
if correo_electronico.find("@") != -1:
    print(f"Bienvenido {apellido} {nombre}")
    print(f"{apellido} {nombre}. Debido a su edad usted es {evaluacion_edad}")
    print(f"Su correo es {correo_electronico}")

