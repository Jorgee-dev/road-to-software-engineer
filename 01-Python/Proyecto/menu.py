def mostrar_menu(usuario_actual):
    if usuario_actual:
        print("======================================")
        print(f"Usuario actual:\n{usuario_actual['nombre']}")
        print("======================================")
    
    print("================ MENÚ ================")
    print("1. Iniciar sesión")
    print("2. Crear usuario")
    print("3. Ver usuarios")
    print("4. Eliminar usuario")
    print("5. Información")
    print("6. Salir")
    print("======================================")

