"""
Programa 2: Conteo de números
Solicita una cantidad de números y cuenta cuántos son mayores, menores o iguales a 0.
"""

cantidad = int(input("¿Cuántos números vas a ingresar? "))

mayores = 0
menores = 0
iguales = 0

for i in range(cantidad):
    num = float(input(f"Ingresa el número {i + 1}: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print(f"Mayores que 0: {mayores}")
print(f"Menores que 0: {menores}")
print(f"Iguales a 0: {iguales}")
