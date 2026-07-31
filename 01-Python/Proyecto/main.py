from menu import mostrar_menu
from informacion import mostrar_informacion
from usuarios import crear_usuario, ver_usuarios
from login import iniciar_sesion
from utilidades import limpiar_pantalla, pausar
from archivos import cargar_usuarios
from archivos import eliminar_usuario

usuarios = cargar_usuarios()
opcion = ""

while opcion != "6":

    limpiar_pantalla()
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        if iniciar_sesion(usuarios):
            print("Acceso concedido.")
            pausar()
        else:
            print("Acceso denegado.")
            pausar()

    elif opcion == "2":
        crear_usuario(usuarios)
        pausar()

    elif opcion == "3":
        ver_usuarios(usuarios)
        pausar()

    elif opcion == "4":
        eliminar_usuario(usuarios)
        pausar()

    elif opcion == "5":
        mostrar_informacion()
        pausar()

    elif opcion == "6":
        print("Saliendo del programa...")