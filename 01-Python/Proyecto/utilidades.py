import os

def limpiar_pantalla():
    os.system("cls")

def pausar():
    input("\nPulsa ENTER para continuar...")

def es_admin(usuario_actual):

    if usuario_actual is None:
        return False

    if usuario_actual["rol"] == "admin":
        return True

    return False