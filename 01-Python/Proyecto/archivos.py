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
            "contraseña": datos[1]
        }

        usuarios.append(usuario)

    archivo.close()
    
    return usuarios