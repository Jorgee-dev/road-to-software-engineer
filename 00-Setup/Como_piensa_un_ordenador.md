# Cómo piensa un ordenador

## Idea más importante

Un ordenador no piensa.

Solo entiende dos estados:

- 0
- 1

Todo lo que hacemos termina convirtiéndose en unos y ceros.

## ¿Qué ocurre al encender el ordenador?

1. Pulso el botón de encendido.
2. La placa base recibe electricidad.
3. La CPU comienza a ejecutar instrucciones.
4. La BIOS/UEFI comprueba el hardware.
5. Busca un sistema operativo.
6. Carga Windows en la memoria RAM.
7. Windows toma el control y aparece el escritorio.

# Prguntas

- ¿Por qué crees que Windows no puede arrancar directamente sin pasar antes por la BIOS/UEFI?
La BIOS/UEFI es el primer software que se ejecuta. Comprueba que el hardware funciona correctamente y localiza el sistema operativo para poder cargarlo. Sin ese paso, el ordenador no sabría qué hacer al encenderse.
- Si la CPU solo ejecuta instrucciones, ¿dónde crees que se guardan tus fotos, juegos y documentos?
En la SSD o HDD

## ¿Qué es la RAM?

Explica con tus palabras:

- ¿Para qué sirve?
Guardar temporalmente los programas y datos que la CPU necesita utilizar en ese momento.
- ¿Por qué no ejecuta la CPU los programas directamente desde el SSD?
Porque el SSD es mucho mas lento a comparación con la RAM
- ¿Qué ocurre cuando la RAM se llena?
El ordenador empieza a usar el SSD como RAM y genera una lentitud ya que este va mas lento.

# Prguntas

- Si apagas el ordenador, ¿la RAM conserva la información? ¿Por qué crees que sí o que no?
Si lo apagas bien, creo que dejaría de conservar la información ya que si su función es guardar información temporalmente cuando apagas se acabó ese tiempo.
- Si tienes un ordenador con un SSD enorme (2 TB) pero solo 4 GB de RAM, ¿crees que podrá tener muchos programas abiertos al mismo tiempo? Explica por qué.
No, aunque tengas muchísimo espacio para guardar archivos, la RAM es la que limita cuántos programas puedes tener trabajando cómodamente al mismo tiempo.
- Si yo tengo un ordenador con un SSD de 2 TB y otro con un SSD de 256 GB, pero ambos tienen 16 GB de RAM y la misma CPU, ¿cuál será más rápido al abrir programas? ¿Por qué?
Irán prácticamente igual de rápido

## ¿Cómo ejecuta un programa la CPU?

Explica paso a paso qué ocurre desde que haces doble clic en VS Code hasta que aparece la ventana.

Desde el momento que la persona abre el programa, se buscará el programa en la SSD, se hace una copia en la RAM, entra en juego la CPU que lee el programa y lo ejecuta, windows dibuja la interfaz y lo que vemos después es la cración de todo ese proceso.

# Prguntas

- ¿Por qué la CPU no puede entender directamente un programa escrito en Python?
La CPU entiende su idioma (lenguaje maquina) que son instrucciones en binario
- ¿Para qué sirve el intérprete de Python?
Python traducirá lo que nosotros escribamos en el lenguaje de la CPU para que lo entienda
- ¿Qué ocurriría si elimináramos Python de tu ordenador y luego intentaras ejecutar un archivo .py?
El ordenador no tendrá ese "traductor" y no podrá ejecutarlo

## Lo que he entendido hoy

- Todo el hardware trabaja en conjunto, pero cada uno se centra en agilizar proceso de otro componente que se le pueda atascar.
- Los interpretes son traductores entre humanos y maquinas para crear progrmas a base de instrucciones
- El proceso de encendido del ordenador tiene muchos mas procesos de los que pensamos al igual que el proceso de abrir un programa oculta muchas tareas.
- Hay que valorar el rendimiento del ordenador para poder diagnositacar posbiles fallos o malwares
- La RAM pierde toda la información cuando deja de recibir electricidad.