import pygame
import sys
import random
import time



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
speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = [random.uniform(1.5, 2.0) for _ in range(5)]
clock = pygame.time.Clock()
#Que gane una bola
numero=random.randint(1,5)
if numero == 1:
    speed_xc1 = 2.5
elif numero == 2:
    speed_xc2 = 2.5
elif numero == 3:
    speed_xc3 = 2.5
elif numero == 4:
    speed_xc4 = 2.5
elif numero == 5:
    speed_xc5 = 2.5
running=True

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
    #Que la bola rebote (No se va ha hacer)
    #actualizar la velocidad de la bola si ha ganado:
    if xc1 >=random.randint(700,1000) and speed_xc1 == 2.5:
        speed_xc1 = 1
    if xc2 >=random.randint(700,1000) and speed_xc2 == 2.5:
        speed_xc2 = 1
    if xc3 >=random.randint(700,1000) and speed_xc3 == 2.5:
        speed_xc3 = 1
    if xc4 >=random.randint(700,1000)  and speed_xc4 == 2.5:
        speed_xc4 = 1
    if xc5 >=random.randint(700,1000)  and speed_xc5 == 2.5:
        speed_xc5 = 1
    if xc1 >=random.randint(1050,1200) and speed_xc1 == 1:
        speed_xc1 = 3
    if xc2 >=random.randint(1050,1200)  and speed_xc2 == 1:
        speed_xc2 = 3
    if xc3 >=random.randint(1050,1200)   and speed_xc3 == 1:
        speed_xc3 = 3
    if xc4 >=random.randint(1050,1200)   and speed_xc4 == 1:
        speed_xc4 = 3  
    if xc5 >=random.randint(1050,1200)   and speed_xc5 == 1:
        speed_xc5 = 3 
    if xc1 >=random.randint(700,1000) and speed_xc1 != 2.5:
        speed_xc1 = random.uniform(1.0,1.5)
    if xc2 >=random.randint(700,1000) and speed_xc2 != 2.5:
        speed_xc2 = random.uniform(1.0,1.5)
    if xc3 >=random.randint(700,1000) and speed_xc3 != 2.5:
        speed_xc3 = random.uniform(1.0,1.5)
    if xc4 >=random.randint(700,1000)  and speed_xc4 != 2.5:
        speed_xc4 = random.uniform(1.0,1.5)
    if xc5 >=random.randint(700,1000)  and speed_xc5 != 2.5:
        speed_xc5 = random.uniform(1.0,1.5)
    if xc1 >=random.randint(1050,1200) and speed_xc1 != 1:
        speed_xc1 = random.uniform(1.5,2.3)
    if xc2 >=random.randint(1050,1200)  and speed_xc2 != 1:
        speed_xc2 = random.uniform(1.5,2.3)
    if xc3 >=random.randint(1050,1200)   and speed_xc3 != 1:
        speed_xc3 = random.uniform(1.5,2.3)
    if xc4 >=random.randint(1050,1200)   and speed_xc4 != 1:
        speed_xc4 = random.uniform(1.5,2.3) 
    if xc5 >=random.randint(1050,1200)   and speed_xc5 != 1:
        speed_xc5 = random.uniform(1.5,2.3)
    if xc1 >=1920:
        print ("El ganador es la bola 1")
        speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = [0 for _ in range(5)]
        time.sleep(2)
        break



    if xc2 >=1920:
        running=False
        print ("El ganador es la bola 2")
        speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = [0 for _ in range(5)]
        time.sleep(2)
        break


    if xc3 >=1920:
        running=False
        print ("El ganador es la bola 3")
        speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = [0 for _ in range(5)]
        time.sleep(2)
        break

    if xc4 >=1920:
        running=False
        print ("El ganador es la bola 4")
        speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = [0 for _ in range(5)]
        time.sleep(2)
        break

    if xc5 >=1920:
        running=False
        print ("El ganador es la bola 5")
        speed_xc1, speed_xc2, speed_xc3, speed_xc4, speed_xc5 = [0 for _ in range(5)]
        time.sleep(2)
        break

   

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