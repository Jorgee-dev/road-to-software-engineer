from archivos import guardar_usuarios
from utilidades import normalizar_nombre

def crear_usuario(usuarios):
    nombre = normalizar_nombre(input("Nombre: "))
    

    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    
    contraseña = input("Contraseña: ")

    if contraseña == "":
        print("La contraseña no puede estar vacía.")
        return

    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Ese usuario ya está registrado.")
            return

    usuario = {
        "nombre": nombre,
        "contraseña": contraseña,
        "rol": "usuario"
}

    usuarios.append(usuario)
    guardar_usuarios(usuarios)

    print("Usuario creado correctamente.")

def eliminar_usuario(usuarios, usuario_actual):

    nombre = normalizar_nombre(input("Nombre del usuario a eliminar: "))
    if usuario_actual["nombre"] == nombre:
        print("No puedes eliminar tu propio usuario mientras tienes la sesión iniciada.")
        return

    contraseña = input("Contraseña del usuario a eliminar: ")
    
    for usuario in usuarios:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            print("Usuario eliminado correctamente.")
            return
    print("Ese usuario no existe.")

def ver_usuarios(usuarios):

    print("======== USUARIOS ========")

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for i in range(len(usuarios)):
            print(f"{i + 1} - {usuarios[i]['nombre']}")

    print("==========================")
    
