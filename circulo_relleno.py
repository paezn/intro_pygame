import pygame

# Inicializar Pygame
pygame.init()

# Establecer la pantalla
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Círculo Relleno")

# Definir colores
white = (255, 255, 255)
red = (255, 0, 0)

# Definir el centro del círculo y su radio
center_x = width // 2
center_y = height // 2
radius = 100

# Bucle principal del juego
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar el círculo relleno
    pygame.draw.circle(screen, red, (center_x, center_y), radius)

    

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()