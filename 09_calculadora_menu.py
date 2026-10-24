"""
Programa 9: Calculadora básica con menú
Calculadora con operaciones de suma, resta, multiplicación y división.
"""

while True:
    print("\n=== Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == "5":
        print("¡Hasta luego!")
        break

    if opcion not in ("1", "2", "3", "4"):
        print("Opción inválida.")
        continue

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        print(f"Resultado: {a + b}")
    elif opcion == "2":
        print(f"Resultado: {a - b}")
    elif opcion == "3":
        print(f"Resultado: {a * b}")
    elif opcion == "4":
        if b == 0:
            print("Error: división por cero.")
        else:
            print(f"Resultado: {a / b}")
