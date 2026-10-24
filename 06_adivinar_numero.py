"""
Programa 6: Adivinar el número
Genera un número aleatorio entre 1 y 100 y el usuario debe adivinarlo.
"""

import random

secreto = random.randint(1, 100)
intentos = 0

print("Adivina el número entre 1 y 1003" \
"")

while True:
    intento = int(input("Di un numero: "))
    intentos += 1

    if intento < secreto:
        print("Demasiado bajo")
    elif intento > secreto:
        print("Demasiado alto")
    else:
        print(f"Correcto Lo adivinaste en {intentos} intentos.")
        break
