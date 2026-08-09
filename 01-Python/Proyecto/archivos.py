def cargar_usuarios():
    usuarios = []

    with open("01-Python/Proyecto/usuarios.txt", "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea == "":
                continue

            datos = linea.split(";")

            if len(datos) != 3:
                print("Una línea del archivo de usuarios no es válida.")
                continue

            usuario = {
                "nombre": datos[0],
                "contraseña": datos[1],
                "rol": datos[2]
            }
            usuarios.append(usuario)

    return usuarios

def guardar_usuarios(usuarios):
    with open("01-Python/Proyecto/usuarios.txt", "w") as archivo:

        for usuario in usuarios:
            linea = f"{usuario['nombre']};{usuario['contraseña']};{usuario['rol']}\n"
            archivo.write(linea)
