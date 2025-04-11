# Estructura de un juego en Pygame

## Inicialización

- Como en todo programa en Python, se debe importar los módulos o librerías a utilizar
`import pygame`

- Inicializar pygame usando la función init().  Inicializa todos los módulos de pygame importados.
`pygame.init()`

## Visualización de la ventana

`ventana = pygame.display.set_mode((600, 400))`

- set_mode() es la función encargada de definir el tamaño de la ventana. En el ejemplo, se está definiendo una ventana de 600 px de ancho, por 400 px de alto.

`pygame.display.set_caption("Mi ventana")`

- set_caption() es la función que añade un título a la ventana.

### función set_mode()

`set_mode(size =(0,0), flags = 0, depth = 0, display = 0)`

- size = (600,400) : define el tamaño de la ventana.

- flags: define uno o mas comportamientos para la ventana.
    - Valores:
        - pygame.FULLSCREEN
        - pygame.RESIZABLE
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE: pantalla completa, dimensiones modificables.

## Bucle del juego - game loop
- Bucle infinito que se interrumpirá el cumplir ciertos criterios.
- Reloj interno del juego
- En cada iteración del bucle del juego podemos mover a un personaje, o tener en cuenta que un obejto a alcanzado a otro, o que se ha cruzado la linea de llegada, lo que quiere decir que la partida ha terminado.
- Cada iteración es una oportunidad para actualizar todos los datos relacionados con el estado actual de la partida.
- En cada iteración se realizan las siguientes tareas:
    1. Compropar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteración actual.
    3. Obtener las entradas del sistema, o de interacción con el jugador.
    4. Actualizar todas las entidades que caracterizan el juego.
    5. Refrescar la pantalla.

    ## Superficies pygame
    - Superficie:
        - Elemento geométrico.
        - Linea, polígono, imagen, texto que se muestra en la pantalla.
        - El polígono se puede o no rellenar de color.
        -  Las superficies se crean de diferente manera dependiendo del tipo:
            - imagen: image.load()
            - texto: font.render()
            - Superficie genérica: pygame.Surface()
            - Ventana del juego: pygamen.display.set_mode()

## Bandera Colombia

## Gestión del tiempo y los eventos

### Módulo time

- Ofrece varias funciones que permiten cronometrar la sesión actual (desde el init()) o pausar, la ejecución, por ejemplo.
- Funciones:
    - pygame.time.get_ticks
    - pygame.time.waitpygame.time.delay

- Objeto Clock
    - La función tick permite actualizar el reloj asociado con el juego actual.
    - Se llama cada vez que se actualiza la pantalla del juego.
    - Permite especificar el número máximo de fotogramas que se muestran por segundo, y por tanto, limitar y controlar la velocidad de ejecución del juego.
    - Si insertamos en un bucle de juego la siguiente linea, garantizamos que nunca se irá mas rápido de 50 fotogramas por segundo: `Clock.tick(50)`

### Gestión de eventos
- Hay diferentes formas para que el programa sepa que se ha desencadenado un evento.
- Es esencial que los programas puedan conocer inmediantamente las acciones del jugador a través del teclado, el mouse, el joystick o cualqiuer otro periferico.

#### Función pygame.event.get
- Permite obtener todos los eventos en espera de ser procesados y que están disponibles en una cola.
- Si no hay ninguno, se obtiene una colección vacía.

```Python
# Usamos un bucle for para recorrer todos los eventos de la colección obtenida al llamar a la función get.
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            PARAR_JUEGO = True
```
#### Función pygame.event.wait
- Esta función espera a que ocurra un evento, y en cuanto sucede, está disponible.

```Python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
```

#### Función pygame.event.poll
- Devuelve solo uno de los eventos que están en la cola de espera