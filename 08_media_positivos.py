"""
Programa 8: Calcular la media de números positivos
Permite ingresar números positivos hasta que se ingresa uno negativo y calcula la media.
"""

suma = 0
contador = 0

print("Ingresa números positivos. Un número negativo finaliza el programa.")

while True:
    num = float(input("Número: "))
    if num < 0:
        break
    suma += num
    contador += 1

if contador == 0:
    print("No se ingresaron números positivos.")
else:
    media = suma / contador
    print(f"Media de los {contador} números positivos: {media:.2f}")
