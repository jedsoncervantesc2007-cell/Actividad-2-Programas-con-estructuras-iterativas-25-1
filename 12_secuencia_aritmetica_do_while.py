"""
Programa 12: Generar una secuencia aritmética (do-while simulado)
Genera una secuencia aritmética hasta un número máximo usando do-while simulado.
"""

primer = int(input("Primer número: "))
diferencia = int(input("Diferencia: "))
maximo = int(input("Número máximo: "))

actual = primer
print("Secuencia:", end=" ")

while True:
    print(actual, end=" ")
    actual += diferencia
    if actual > maximo:
        break
print()
