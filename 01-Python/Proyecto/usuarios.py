def crear_usuario(usuarios):
    nombre = input("Nombre: ")
    contraseña = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Ese usuario ya está registrado.")
            return
    usuario = {
    "nombre": nombre,
    "contraseña": contraseña
}
    archivo = open("01-Python/Proyecto/usuarios.txt", "a")
    usuarios.append(usuario)
    archivo.write(f"{usuario['nombre']};{usuario['contraseña']}\n")
    archivo.close()

    print("Usuario creado correctamente.")
    
def ver_usuarios(usuarios):

    print("======== USUARIOS ========")

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for i in range(len(usuarios)):
            print(f"{i + 1} - {usuarios[i]['nombre']}")

    print("==========================")
    
def eliminar_usuario(usuarios):
    nombre = input("Nombre del usuario a eliminar: ")
    contraseña = input("Contraseña del usuario a eliminar: ")
    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            usuarios.remove(usuario)
            print("Usuario eliminado correctamente.")
            return
    print("Ese usuario no existe.")