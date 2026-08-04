from menu import mostrar_menu
from informacion import mostrar_informacion
from usuarios import crear_usuario, ver_usuarios, eliminar_usuario
from login import iniciar_sesion, cerrar_sesion
from utilidades import limpiar_pantalla, pausar, es_admin
from archivos import cargar_usuarios

usuarios = cargar_usuarios()
usuario_actual = None
opcion = ""

while opcion != "6":

    limpiar_pantalla()
    mostrar_menu(usuario_actual)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if usuario_actual is None:

            usuario_actual = iniciar_sesion(usuarios)

            if usuario_actual:
                print(f"Bienvenido, {usuario_actual['nombre']}")
            else:
                print("Usuario o contraseña incorrectos.")
        else:

            usuario_actual = cerrar_sesion()
        pausar()

    elif opcion == "2":

        if es_admin(usuario_actual):
            crear_usuario(usuarios)
        else:
            print("No tienes permisos para realizar esta acción.")
        pausar()

    elif opcion == "3":
        if es_admin(usuario_actual):
            ver_usuarios(usuarios)
        else:
            print("No tienes permisos para realizar esta acción.")
        pausar()

    elif opcion == "4":
        if es_admin(usuario_actual):
            eliminar_usuario(usuarios)
        else:
            print("No tienes permisos para realizar esta acción.")
        pausar()

    elif opcion == "5":
        mostrar_informacion()
        pausar()

    elif opcion == "6":
        print("Saliendo del programa...")