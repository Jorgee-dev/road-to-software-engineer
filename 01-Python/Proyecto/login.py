from utilidades import normalizar_nombre

def iniciar_sesion(usuarios):
    nombre_usuario = normalizar_nombre(input("Nombre de usuario: "))
    contraseña_usuario = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["nombre"] == nombre_usuario and usuario["contraseña"] == contraseña_usuario:
            return usuario

    return None


def cerrar_sesion():
    print("Sesión cerrada correctamente.")
    return None