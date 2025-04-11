# importamos la libreria pygame
import pygame

# inicializamos los modulos de pygame
pygame.init()

# Establer titulo a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# definimos un color
azul = (0,0,255)

# crear una superficie
azul_superficie = pygame.Surface((400,400))

# Rellenamos la superficie de azul
azul_superficie.fill(azul)

# Inserto o muevo la superficie en la ventana
ventana.blit(azul_superficie, (0,0))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()