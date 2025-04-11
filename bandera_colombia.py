# importamos la libreria pygame
import pygame

# inicializamos los modulos de pygame
pygame.init()

# Establer titulo a la ventana
pygame.display.set_caption("Bandera de Colombia")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# definimos un color
amarillo = (255,255,0)
azul = (0,0,255)
rojo = (255,0,0)


# crear una superficie
amarillo_superficie = pygame.Surface((400,200))
azul_superficie = pygame.Surface((400, 100))
rojo_superficie = pygame.Surface((400,100))

# Rellenamos la superficie de azul
amarillo_superficie.fill(amarillo)
azul_superficie.fill(azul)
rojo_superficie.fill(rojo)

# Inserto o muevo la superficie en la ventana
ventana.blit(amarillo_superficie, (0,0))
ventana.blit(azul_superficie,(0,200))
ventana.blit(rojo_superficie, (0,300))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()