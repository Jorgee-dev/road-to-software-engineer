def crear_usuario(usuarios):
    nombre = input("Nombre del usuario: ")
    usuarios.append(nombre)
    print("Usuario creado correctamente.")
    
def ver_usuarios(usuarios):

    print("======== USUARIOS ========")

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for i in range(len(usuarios)):
            print(f"{i + 1} - {usuarios[i]}")

    print("==========================")
    
def eliminar_usuario(usuarios):
    nombre = input("Nombre del usuario a eliminar: ")
    if nombre in usuarios:
        usuarios.remove(nombre)
        print("Usuario eliminado correctamente.")
    else:
        print("Ese usuario no existe.")