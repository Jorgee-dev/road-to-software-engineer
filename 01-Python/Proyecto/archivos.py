def cargar_usuarios():
    usuarios = []

    archivo = open("01-Python/Proyecto/usuarios.txt", "r")

    for linea in archivo:

        linea = linea.strip()

        if linea == "":
            continue

        datos = linea.split(";")

        usuario = {
            "nombre": datos[0],
            "contraseña": datos[1],
            "rol": datos[2]
        }

        usuarios.append(usuario)

    archivo.close()

    return usuarios

def guardar_usuarios(usuarios):
    archivo = open("01-Python/Proyecto/usuarios.txt", "w")

    for usuario in usuarios:
        linea = f"{usuario['nombre']};{usuario['contraseña']};{usuario['rol']}\n"
        archivo.write(linea)

    archivo.close()

