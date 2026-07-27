print("===================================")
print(" SISTEMA DE GESTIÓN DE USUARIOS ")
print("===================================")

opcion = ""

usuarios = []

while opcion != "5":

    print()
    print("================ MENÚ ================")
    print("1. Iniciar sesión")
    print("2. Crear usuario")
    print("3. Ver usuarios")
    print("4. Información")
    print("5. Salir")
    print("======================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Inicio de sesión próximamente...")

    elif opcion == "2":
        nombre = input("Nombre del usuario: ")
        usuarios.append(nombre)
        print("Usuario creado correctamente.")

    elif opcion == "3":

        print("======== USUARIOS ========")

        if len(usuarios) == 0:
         print("No hay usuarios registrados.")
        else:
            for usuario in usuarios:
                print("-", usuario)
                
        print("==========================")

    elif opcion == "4":
        print("======== INFORMACIÓN ========")
        print("Versión: 1.0")
        print("Autor: Jorge")
        print("Curso: Road to Software Engineer")
        print("============================")

    elif opcion == "5":
        print("Hasta pronto.")

    else:
        print("Opción no válida.")