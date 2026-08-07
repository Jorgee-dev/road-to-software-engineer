from utilidades import tiene_permiso

def mostrar_menu_inicio():

    print("================ MENÚ ================")
    print("1. Iniciar sesión")
    print("5. Información")
    print("6. Salir")
    print("======================================")

def mostrar_menu_admin(usuario_actual):

    print("======================================")
    print(f"Usuario actual:\n{usuario_actual['nombre']}")
    print("======================================")
    print("================ MENÚ ================")
    print("1. Cerrar sesión")
    print("2. Crear usuario")
    print("3. Ver usuarios")
    print("4. Eliminar usuario")
    print("5. Información")
    print("6. Salir")
    print("======================================")

def mostrar_menu_usuario(usuario_actual):

    print("======================================")
    print(f"Usuario actual:\n{usuario_actual['nombre']}")
    print("======================================")
    print("================ MENÚ ================")
    print("1. Cerrar sesión")

    if tiene_permiso(usuario_actual, "ver_usuarios"):
        print("3. Ver usuarios")

    print("5. Información")
    print("6. Salir")
    print("======================================")