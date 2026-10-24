"""
Programa 10: Contador de números impares (do-while simulado)
Muestra todos los números impares desde 1 hasta el número ingresado usando do-while simulado.
"""

n = int(input("Ingresa un número entero positivo: "))

i = 1
while True:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
    if i > n:
        break
print()
