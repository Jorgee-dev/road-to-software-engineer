from menu import mostrar_menu
from informacion import mostrar_informacion
from usuarios import crear_usuario, ver_usuarios, eliminar_usuario
from login import iniciar_sesion

usuarios = []
opcion = ""

while opcion != "6":

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        iniciar_sesion(usuarios)

    elif opcion == "2":
        crear_usuario(usuarios)

    elif opcion == "3":
        ver_usuarios(usuarios)

    elif opcion == "4":
        eliminar_usuario(usuarios)

    elif opcion == "5":
        mostrar_informacion()

    elif opcion == "6":
        print("Saliendo del programa...")