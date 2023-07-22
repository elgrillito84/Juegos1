import pygame
import sys
import random



# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1920, 1080))


#Colores        
BLACK, DARK_BLUE, BLUE, DARK_GREEN, GREENISH_BLUE, LIGHT_TURQUOISE, GREEN, WATERY_GREEN, CYAN, RED, DARK_PINK,\
      PINK, ORANGE, RED_PINK, MAGENTA, YELLOW, LIGHT_YELLOW, WHITE, REDDISH_BROWN, PURPLE, MUSTARD, GREENISH_BROWN, GREY, TURQUOISE = \
    (0, 0, 0), (0, 0, 100), (0, 0, 255), (0, 100, 0), (0, 100, 100), (0, 100, 255), (0, 255, 0), (0, 255, 100), \
    (0, 255, 255), (255, 0, 0), (255, 0, 100), (255, 0, 255), (255, 100, 0), (255, 100, 100), (255, 100, 255), \
    (255, 255, 0), (255, 255, 100), (255, 255, 255), (100, 0, 0), (100, 0, 100), (100, 0, 255), (100, 100, 0), \
    (100, 100, 100), (100, 100, 255)
#Colores

"Agregar variables de la bola"
xc1,yc1,xc2,yc2,xc3,yc3,xc4,yc4,xc5,yc5=50,100,50,300,50,500,50,700,50,700

#Velocidad de la bola
speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = 3,3,3,3,3
clock = pygame.time.Clock()

while True:
    # Gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    xc1 += speed_xc1
    xc2 += speed_xc2
    xc3 += speed_xc3    
    xc4 += speed_xc4
    xc5 += speed_xc5
    #Que la bola rebote
    if xc1 > 1920 or xc1 < 0 or xc2 > 1920 or xc2 < 0 or xc3 > 1920 or xc3 < 0 or xc4 > 1920 or xc4 < 0 or xc5 > 1920 or xc5 < 0:
        speed_xc1 = -speed_xc1
        speed_xc2 = -speed_xc2
        speed_xc3 = -speed_xc3
        speed_xc4 = -speed_xc4
        speed_xc5 = -speed_xc5

    # Dibujar
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, 200), (1920,200), 5)
    pygame.draw.line(screen, WHITE, (0, 400), (1920,400), 5)
    pygame.draw.line(screen, WHITE, (0, 600), (1920,600), 5)
    pygame.draw.line(screen, WHITE, (0, 800), (1920,800), 5)
    pygame.draw.line(screen, WHITE, (0, 1000), (1920,1000), 5)
    pygame.draw.circle(screen, WHITE, (xc1, 100), 50, 0)
    pygame.draw.circle(screen, WHITE, (xc2, 300), 50, 0)
    pygame.draw.circle(screen, WHITE, (xc3, 500), 50, 0)
    pygame.draw.circle(screen, WHITE, (xc4, 700), 50, 0)
    pygame.draw.circle(screen, WHITE, (xc5, 900), 50, 0)
    



    # Actualizar
    pygame.display.flip()
    clock.tick(60)
    #I love amazon CodeWhisperer