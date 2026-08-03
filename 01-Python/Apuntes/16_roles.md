# Día 16 - Roles y sistema de permisos

## 🎯 Objetivo del día

Hoy hemos añadido uno de los conceptos más importantes de cualquier aplicación real: **los roles de usuario**.

Hasta ahora todos los usuarios podían realizar exactamente las mismas acciones. A partir de hoy cada usuario tendrá un rol que determinará los permisos que posee dentro del programa.

---

# ¿Qué es un rol?

Un rol es una característica del usuario que indica qué acciones puede realizar.

Ejemplos de roles:

- Administrador
- Usuario

El rol forma parte de la información del usuario, igual que el nombre o la contraseña.

---

# El usuario sigue siendo un diccionario

Hasta ahora un usuario almacenaba:

- Nombre
- Contraseña

Ahora también almacena:

- Rol

Esto demuestra que un diccionario puede crecer añadiendo nuevas claves sin necesidad de crear nuevas variables.

---

# Guardar el rol en el archivo

Como el usuario tiene un dato nuevo, también debemos almacenarlo en el archivo de texto.

Antes cada línea del archivo contenía:

- Nombre
- Contraseña

Ahora contiene:

- Nombre
- Contraseña
- Rol

La estructura del archivo siempre debe coincidir con la estructura de los datos que utiliza el programa.

---

# Compatibilidad de datos

Al añadir el campo **rol** apareció un problema.

Los usuarios que ya estaban guardados en el archivo no tenían ese dato.

Como consecuencia, el programa intentaba leer información que no existía y producía un error.

La solución fue actualizar el archivo para que todos los usuarios tuvieran también su rol.

Este tipo de problemas ocurre constantemente en aplicaciones reales y se conoce como **migración de datos**.

---

# Login y autorización

Hoy hemos aprendido que son conceptos diferentes.

## Login

Responde a la pregunta:

> ¿Quién eres?

Comprueba que el nombre de usuario y la contraseña sean correctos.

---

## Autorización

Responde a la pregunta:

> ¿Qué puedes hacer?

Depende del rol del usuario.

Dos usuarios pueden iniciar sesión correctamente y, aun así, tener permisos completamente distintos.

---

# El menú no controla los permisos

Ocultar una opción del menú **no significa** impedir que alguien la utilice.

El menú únicamente muestra información al usuario.

Quien realmente decide si una acción puede ejecutarse es el `main.py`.

Por eso los permisos siempre deben comprobarse en la lógica del programa.

---

# Sistema de permisos

Actualmente existen dos roles.

## Administrador

Puede:

- Crear usuarios.
- Ver usuarios.
- Eliminar usuarios.
- Ver información.
- Cerrar sesión.

---

## Usuario

Puede:

- Ver información.
- Cerrar sesión.

Si intenta acceder a una acción restringida, el programa mostrará un mensaje indicando que no tiene permisos.

---

# Repetición de código

Durante la sesión apareció la misma comprobación varias veces.

Aprendimos una regla muy importante:

> Si el mismo código se repite muchas veces, probablemente debería convertirse en una función.

Todavía no lo hemos hecho porque seguimos otra regla aún más importante.

---

# Regla del día

> **Primero haz que funcione.**
>
> **Después haz que sea bonito.**

Es mejor tener un programa funcionando aunque repita algunas líneas que intentar optimizar demasiado pronto y terminar rompiendo el proyecto.

Cuando todo funcione correctamente, ya habrá tiempo para mejorar el código.

Este proceso de mejorar el código sin cambiar su funcionamiento se conoce como **refactorización**.

---

# Conceptos nuevos

## Rol

Información que determina los permisos de un usuario.

---

## Autorización

Proceso mediante el cual el programa decide si un usuario puede realizar una determinada acción.

---

## Migración de datos

Actualización de los datos antiguos cuando cambia la estructura del programa.

---

## Refactorización

Modificar el código para hacerlo más limpio o mantenible sin cambiar su funcionamiento.

---

