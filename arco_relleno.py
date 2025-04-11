import pygame

pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arco Relleno")

# Color del fondo y del arco
fondo = (255, 255, 255)  # Blanco
color_arco = (255, 0, 0)  # Rojo

# Rectángulo para el arco
rect_arco = (100, 100, 200, 150)  # (x, y, ancho, alto)

# Extensión del arco (ejemplo: 180 grados = semicírculo)
extension_arco = 180

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(fondo)

    # Dibujar el arco relleno
    pygame.draw.ellipse(screen, color_arco, rect_arco, 0)  # 0 rellena el círculo completo
    pygame.draw.ellipse(screen, color_arco, rect_arco, 2)  # 2 define el borde del círculo (ancho 2)
    pygame.draw.arc(screen, color_arco, rect_arco, 0, extension_arco, 2)  # 2 define el borde del arco (ancho 2)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()