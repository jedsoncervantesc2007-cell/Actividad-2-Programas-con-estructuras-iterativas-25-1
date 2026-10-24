
"""
Programa 1: Factorial de un número
Calcula el factorial de un número ingresado por el usuario usando un ciclo for.
"""

n = int(input("Ingresa un número entero no negativo: "))

if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}")
