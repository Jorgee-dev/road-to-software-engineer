usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuario == "jorge" and contraseña == "asir2026":
    print("Acceso permitido.")
elif usuario == "admin":
    print("Acceso permitido.")
else:
    print("Acceso denegado.")