nombre = input("Introduce tu nombre: ").capitalize()
apellido = input("Introduce tu apellido: ").capitalize()
edad = int(input("Introduce tu edad: "))
ciudad = input("Introduce tu ciudad: ").capitalize()

correo = nombre[0].lower() + apellido.lower() + "@empresa.com"

print("======== TARJETA ========")
print(f"Nombre : {nombre} {apellido}")
print(f"Edad   : {edad} años")
print(f"Ciudad : {ciudad}")
print(f"Correo : {correo}")
print("=========================")