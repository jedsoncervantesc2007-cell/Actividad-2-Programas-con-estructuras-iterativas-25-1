"""
Programa 3: Contar letras 'a' en una palabra
Cuenta cuántas veces aparece la letra 'a' (mayúscula o minúscula) en la palabra ingresada.
"""

palabra = input("Ingresa una palabra: ")
contador = 0

for letra in palabra:
    if letra.lower() == "a":
        contador += 1

print(f"La letra 'a' aparece {contador} veces.")
