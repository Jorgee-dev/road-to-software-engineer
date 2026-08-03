def mostrar_menu(usuario_actual):

    print("================ MENÚ ================")

    if usuario_actual:

        print("======================================")
        print(f"Usuario actual: {usuario_actual['nombre']}")
        print(f"Rol: {usuario_actual['rol']}")
        print("======================================")

        print("1. Cerrar sesión")

        if usuario_actual["rol"] == "admin":
            print("2. Crear usuario")
            print("3. Ver usuarios")
            print("4. Eliminar usuario")

        print("5. Información")
        print("6. Salir")

    else:

        print("1. Iniciar sesión")
        print("2. Crear usuario")
        print("3. Ver usuarios")
        print("4. Eliminar usuario")
        print("5. Información")
        print("6. Salir")

    print("======================================")