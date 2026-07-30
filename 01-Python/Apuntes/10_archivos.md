# Archivos

## Abrir un archivo

```python
archivo = open("usuarios.txt", "r")

#Modos de apertura
"r" → Leer
"w" → Escribir (borra el contenido anterior)
"a" → Añadir al final

#Escribir 
archivo.write("Hola\n")

Leer línea por línea
for linea in archivo:
    print(linea)

# Cerrar
archivo.close()

#strip()
texto = texto.strip()

#split()
datos = linea.split(";")

#Persistencia
Guardar información para que siga existiendo aunque el programa se cierre.

