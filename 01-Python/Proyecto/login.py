def iniciar_sesion(usuarios):
    nombre_usuario = input("Nombre de usuario: ").strip().title()
    contraseña_usuario = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["nombre"] == nombre_usuario and usuario["contraseña"] == contraseña_usuario:
            return usuario

    return None
