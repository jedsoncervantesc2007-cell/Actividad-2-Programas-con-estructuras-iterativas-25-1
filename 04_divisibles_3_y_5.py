"""
Programa 4: Imprimir números divisibles por 3 y 5
Imprime todos los números entre 1 y 100 que sean divisibles tanto por 3 como por 5.
"""

print("Números divisibles por 3 y por 5 entre 1 y 100:")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print()
