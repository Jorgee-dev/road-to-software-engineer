from menu import mostrar_menu
from informacion import mostrar_informacion
from usuarios import crear_usuario, ver_usuarios, eliminar_usuario
from login import iniciar_sesion
from utilidades import limpiar_pantalla, pausar
from archivos import cargar_usuarios

usuarios = cargar_usuarios()
usuario_actual = None
opcion = ""

while opcion != "6":

    limpiar_pantalla()
    mostrar_menu(usuario_actual)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        usuario_actual = iniciar_sesion(usuarios)
        if usuario_actual:
            print(f"Bienvenido, {usuario_actual['nombre']}")
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