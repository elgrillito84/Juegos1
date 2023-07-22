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

clock = pygame.time.Clock()
screen.fill(WHITE)
dvd=pygame.image.load("dvd.png")
nuevo_ancho = int(dvd.get_width() * 0.10)
nuevo_alto = int(dvd.get_height() * 0.10)
dvd_escalada = pygame.transform.scale(dvd, (nuevo_ancho, nuevo_alto))
xc1=random.randint(0,1920)

yc2=random.randint(0,1080)
speed_x=5
speed_y=5



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    xc1=xc1+speed_x
    yc2=yc2+speed_y
    if xc1>1700 or xc1<0:
      speed_x=speed_x*-1
    if yc2>900 or yc2<-75:
        speed_y=speed_y*-1
        
    # Dibujar
    screen.fill(WHITE)
    screen.blit(dvd_escalada, (xc1,yc2),)

























    # Actualizar
    pygame.display.flip()
    clock.tick(60)
    #I love amazon CodeWhisperer