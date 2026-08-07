from permisos import permisos
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

def tiene_permiso(usuario_actual, permiso):

    if usuario_actual is None:
        return False

    rol = usuario_actual["rol"]

    if rol not in permisos:
        return False

    if permiso not in permisos[rol]:
        return False

    return permisos[rol][permiso]

