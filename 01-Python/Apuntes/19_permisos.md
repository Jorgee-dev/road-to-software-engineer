# Día 19 — Sistema de permisos y roles

##  Objetivo del día

Mejorar el sistema de usuarios para que las acciones disponibles no dependan únicamente de comprobar si el usuario es administrador.

La idea es separar:

- Los roles de los usuarios.
- Los permisos que tiene cada rol.
- Las opciones que aparecen en el menú.
- Las acciones que realmente puede ejecutar el usuario.

---

##  Roles

Un rol identifica el tipo de usuario que está conectado.

Los roles que tenemos actualmente son:

- Admin
- Usuario
- Moderador

Un mismo rol puede tener varios permisos.

Por ejemplo:

- Admin → puede crear, ver y eliminar usuarios.
- Moderador → puede ver usuarios.
- Usuario → no puede gestionar usuarios.

---

##  Permisos

Los permisos representan acciones concretas que puede realizar un usuario.

Actualmente tenemos:

- Crear usuario.
- Ver usuarios.
- Eliminar usuario.

Los permisos se almacenan en `permisos.py`.

Esto permite separar los permisos de la lógica principal del programa.

---

##  Diccionarios anidados

Para organizar los permisos utilizamos diccionarios dentro de otro diccionario.

El primer nivel representa el rol.

El segundo nivel representa los permisos de ese rol.

De esta forma podemos consultar qué puede hacer un usuario dependiendo de su rol.

---

##  Función `tiene_permiso()`

Creamos una función encargada de comprobar si un usuario tiene un permiso concreto.

La función recibe:

- El usuario actual.
- El permiso que queremos comprobar.

Primero comprueba si existe un usuario conectado.

Después obtiene su rol y comprueba que ese rol exista dentro del sistema de permisos.

Finalmente comprueba que el permiso exista para ese rol y devuelve su valor.

---

##  Sistema seguro de permisos

Si el usuario no está conectado, la función devuelve `False`.

Si el rol no existe, devuelve `False`.

Si el permiso no existe, devuelve `False`.

Esto evita que un error en los permisos provoque que el programa se cierre.

Además, es más seguro negar el acceso cuando no conocemos los permisos de un usuario.

---

##  Menús según el usuario

El programa tiene diferentes menús dependiendo del estado del usuario.

### Sin sesión

Puede:

- Iniciar sesión.
- Ver información.
- Salir.

### Usuario normal

Puede:

- Cerrar sesión.
- Ver información.
- Salir.

### Moderador

Puede:

- Cerrar sesión.
- Ver usuarios.
- Ver información.
- Salir.

### Administrador

Puede:

- Cerrar sesión.
- Crear usuarios.
- Ver usuarios.
- Eliminar usuarios.
- Ver información.
- Salir.

---

##  Menú vs permisos

Una idea importante aprendida hoy:

Ocultar una opción del menú NO proporciona seguridad.

El menú solamente controla lo que el usuario puede ver.

La seguridad real se encuentra en la comprobación de permisos antes de ejecutar una acción.

Por ejemplo, aunque un usuario escriba manualmente una opción que no aparece en su menú, `tiene_permiso()` debe impedir que pueda realizarla.

---

##  Separación de responsabilidades

El proyecto queda dividido en diferentes responsabilidades:

- `main.py` → controla el flujo principal del programa.
- `menu.py` → muestra los diferentes menús.
- `usuarios.py` → gestiona las operaciones relacionadas con usuarios.
- `login.py` → gestiona el inicio y cierre de sesión.
- `archivos.py` → guarda y carga los usuarios.
- `utilidades.py` → contiene funciones auxiliares y comprobaciones.
- `permisos.py` → define los roles y permisos.

Esta separación hace que el proyecto sea más fácil de mantener y ampliar.

---

## Escalabilidad

El sistema ahora permite añadir nuevos roles sin tener que modificar todas las funciones del programa.

Por ejemplo, se podría añadir un nuevo rol y asignarle diferentes permisos.

Esto es mejor que comprobar constantemente si el usuario pertenece a un rol concreto dentro del `main.py`.

---

## Concepto clave 

Un rol no debería determinar directamente todo lo que puede hacer un usuario.

El rol representa un conjunto de permisos.

Esto permite crear sistemas más flexibles y fáciles de ampliar.