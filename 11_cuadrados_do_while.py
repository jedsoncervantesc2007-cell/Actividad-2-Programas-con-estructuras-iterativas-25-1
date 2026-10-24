"""
Programa 11: Generar secuencia de cuadrados (do-while simulado)
Muestra los cuadrados de los números desde 1 hasta el número ingresado usando do-while simulado.
"""

n = int(input("Ingresa un número entero positivo: "))

i = 1
while True:
    print(f"{i}² = {i ** 2}")
    i += 1
    if i > n:
        break
