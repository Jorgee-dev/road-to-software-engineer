edad = int(input("¿Cuántos años tienes?: "))
if edad >= 18:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == "asir2026":
        print("Contraseña correcta.")
        print("Acceso permitido.") 
    else: 
        print("Contraseña incorrecta.")
        print("Acceso denegado.")
else:
    print("Acceso denegado.")
