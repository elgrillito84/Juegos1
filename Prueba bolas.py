import pygame
import sys
import random



# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1920, 1080))
BLACK					=			(  0,   0,   0)
DARK_BLUE				=			(  0,   0, 100)
BLUE					=			(  0,   0, 255)
DARK_GREEN			=			(  0, 100,   0)
GREENISH_BLUE			=			(  0, 100, 100)
LIGHT_TURQUOISE		=			(  0, 100, 255)
GREEN					=			(  0, 255,   0)
WATERY_GREEN			=			(  0, 255, 100)
CYAN					=			(  0, 255, 255)

RED						=			(255,   0,   0)
DARK_PINK				=			(255,   0, 100)
PINK					=			(255,   0, 255)
ORANGE				=			(255, 100,   0)
RED_PINK				=			(255, 100, 100)
MAGENT				=			(255, 100, 255)
YELLOW					=			(255, 255,   0)
LIGHT_YELLOW			=			(255, 255, 100)
WHITE					=			(255, 255, 255)

REDDISH_BROWN		=			(100,   0,   0)
PURPLE					=			(100,   0, 100)
MUSTARD				=			(100,   0, 255)
GREENISH_BROWN		=			(100, 100,   0)
GREY					=			(100, 100, 100)
TURQUOISE				=			(100, 100, 255)

while True:
    # Gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Dibujar
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, 200), (1920,200), 5)
    pygame.draw.line(screen, WHITE, (0, 400), (1920,400), 5)
    pygame.draw.line(screen, WHITE, (0, 600), (1920,600), 5)
    pygame.draw.line(screen, WHITE, (0, 800), (1920,800), 5)
    pygame.draw.line(screen, WHITE, (0, 1000), (1920,1000), 5)



    # Actualizar
    pygame.display.flip()