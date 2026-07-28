def iniciar_sesion(usuarios):
    nombre_usuario = input("Nombre de usuario: ")
    if nombre_usuario in usuarios:
        print(f"Bienvenido, {nombre_usuario}")
    else:
        print("Ese usuario no está registrado.")