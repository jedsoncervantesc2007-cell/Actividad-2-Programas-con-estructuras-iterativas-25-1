"""
Programa 7: Vocales o consonantes
Solicita letras e indica si son vocales o consonantes. Termina cuando se ingresa un espacio.
"""

print("Ingresa letras (presiona espacio + Enter para terminar):")

while True:
    letra = input("Letra: ").strip()

    if letra == "" or letra == " ":
        print("Programa terminado.")
        break

    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa solo una letra.")
        continue

    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    if letra in vocales:
        print(f"'{letra}' es vocal")
    else:
        print(f"'{letra}' es consonante")
