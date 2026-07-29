# ¿Qué es un diccionario?

Un diccionario es una estructura de datos que guarda información mediante pares de clave y valor.

Ejemplo:

usuario = {
    "nombre": "Jorge",
    "edad": 20
}

---

# ¿Qué es una clave?

Es el nombre con el que identificamos un dato.

Ejemplos:

"nombre"
"edad"
"contraseña"

---

# ¿Qué es un valor?

Es la información asociada a una clave.

Ejemplos:

"Jorge"
20
"asir2026"

---

# ¿Cómo acceder a un valor?

usuario["nombre"]

---

# ¿Cómo modificar un valor?

usuario["edad"] = 21

---

# ¿Cómo añadir un nuevo dato?

usuario["correo"] = "jorge@empresa.com"

---

# Diferencia entre una lista y un diccionario

Lista:
- Guarda elementos ordenados.
- Se accede mediante posiciones (índices).

Ejemplo:

usuarios = ["Jorge", "Carlos"]

Diccionario:
- Guarda información mediante claves y valores.
- Se accede mediante la clave.

Ejemplo:

usuario = {
    "nombre": "Jorge",
    "edad": 20
}

---

# ¿Cuándo usar un diccionario?

Cuando un mismo elemento necesita guardar varios datos relacionados.

Ejemplo:
- Nombre
- Contraseña
- Edad
- Correo
- Ciudad