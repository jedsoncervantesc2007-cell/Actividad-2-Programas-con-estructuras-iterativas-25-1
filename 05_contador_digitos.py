"""
Programa 5: Contador de dígitos
Solicita un número entero y determina cuántos dígitos tiene.
"""

numero = int(input("Ingresa un número entero: "))
numero_abs = abs(numero)

if numero_abs == 0:
    digitos = 1
else:
    digitos = 0
    while numero_abs > 0:
        numero_abs //= 10
        digitos += 1

print(f"El número tiene {digitos} dígito(s).")
