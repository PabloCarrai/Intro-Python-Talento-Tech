"""
1) Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle
while para solicitar el ingreso de cada mes. Validar que los ingresos sean numeros
positivos. Si se ingresa un valor negativo, mostrar un mensaje indicando que el
valor no es valido y volve a pedir el dato.
2) Calcular el total acumulado durante los 6 meses y el promedio mensual. Mostrar el
resultado al final del programa.
"""

ingresos = 0
meses = 0
nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

while meses < 6:
    gasto_mes = int(input(f"Gasto de: {nombre_mes[meses]}?  $"))
    if gasto_mes <= 0:
        print("Valor no valido. Vuelve a ingresarlo")
        continue
    ingresos += gasto_mes
    meses += 1

print(f"Total Gastado en los 6 meses \t${ingresos}")
print(f"El promedio es \t${ingresos/len(nombre_mes)}")
