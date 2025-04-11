import pygame
import math

pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Porción de Elipse Rellena")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Rectángulo para la elipse
rect_width = 200
rect_height = 100
rect_x = 300
rect_y = 250
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Porción de elipse a dibujar (ejemplo: un cuarto de la elipse)
angle_start = 0
angle_end = math.pi/2  # 90 grados

# Función para calcular los puntos de la elipse
def get_ellipse_points(rect, angle_start, angle_end, num_points=360):
    points = []
    for i in range(num_points):
        angle = angle_start + (angle_end - angle_start) * i / (num_points - 1)
        x = rect.center[0] + rect.width / 2 * math.cos(angle)
        y = rect.center[1] + rect.height / 2 * math.sin(angle)
        points.append((int(x), int(y)))
    return points

# Dibujando
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar la elipse rellena
    pygame.draw.ellipse(screen, BLUE, rect, 0)

    # Obtener los puntos de la porción de elipse
    ellipse_points = get_ellipse_points(rect, angle_start, angle_end)

    # Dibujar la porción de elipse
    pygame.draw.polygon(screen, BLACK, ellipse_points, 1)  # Línea de borde

    pygame.display.flip()

pygame.quit()