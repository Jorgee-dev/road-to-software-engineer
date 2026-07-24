nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")

nombre = nombre.lower()
apellido = apellido.lower()

usuario = nombre[0] + apellido
correo = usuario + "@empresa.com"

print(f"Usuario generado: {usuario}")
print(f"Correo generado: {correo}")
print(f"Longitud del usuario: {len(usuario)}")