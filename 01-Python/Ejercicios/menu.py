opcion = ""

while opcion != "3":

    print("===== MENÚ =====")
    print("1. Saludar")
    print("2. Decir adiós")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola!")

    elif opcion == "2":
        print("¡Adiós!")

    elif opcion == "3":
        print("Saliendo del programa...")

    else:
        print("❌ Opción no disponible.")

print("Programa finalizado.")