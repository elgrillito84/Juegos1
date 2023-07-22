import pygame
import sys
import random
import time
ruta_dvd = r"C:\Users\usuario\Desktop\Studio Things\JAK\dvd.png"
print("Ruta de la imagen:", ruta_dvd)
try:
    dvd = pygame.image.load(ruta_dvd)
except pygame.error as e:
    print("Error al cargar la imagen:", e)
    sys.exit()


pygame.init()

# Configuración de la ventana
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dvd")

# Colores
BLACK, DARK_BLUE, BLUE, DARK_GREEN, GREENISH_BLUE, LIGHT_TURQUOISE, GREEN, WATERY_GREEN, CYAN, RED, DARK_PINK, PINK, ORANGE, RED_PINK, MAGENTA, YELLOW, LIGHT_YELLOW, WHITE, REDDISH_BROWN, PURPLE, MUSTARD, GREENISH_BROWN, GREY, TURQUOISE = \
    (0, 0, 0), (0, 0, 100), (0, 0, 255), (0, 100, 0), (0, 100, 100), (0, 100, 255), (0, 255, 0), (0, 255, 100), \
    (0, 255, 255), (255, 0, 0), (255, 0, 100), (255, 0, 255), (255, 100, 0), (255, 100, 100), (255, 100, 255), \
    (255, 255, 0), (255, 255, 100), (255, 255, 255), (100, 0, 0), (100, 0, 100), (100, 0, 255), (100, 100, 0), \
    (100, 100, 100), (100, 100, 255)

# Define tus colores aquí...

clock = pygame.time.Clock()

ruta_dvd = r"C:\Users\usuario\Desktop\Studio Things\JAK\dvd.png"
dvd = pygame.image.load(ruta_dvd)
nuevo_ancho = int(dvd.get_width() * 0.10)
nuevo_alto = int(dvd.get_height() * 0.10)
dvd_escalada = pygame.transform.scale(dvd, (nuevo_ancho, nuevo_alto))
xc1 = random.randint(0, 1000)
yc2 = random.randint(0, 600)
speed_x = 5
speed_y = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    xc1 += speed_x
    yc2 += speed_y
    if xc1 > 1030 or xc1 < -17:
        speed_x = speed_x * -1
    if yc2 > 610 or yc2 < 0:
        speed_y = speed_y * -1

    # Dibujar
    screen.fill(WHITE)
    screen.blit(dvd_escalada, (xc1, yc2))

    # Actualizar
    pygame.display.update()
    clock.tick(60)

# Pausa para mantener la ventana abierta
time.sleep(2)  # Cambia el valor a la cantidad de segundos que desees esperar

pygame.quit()
sys.exit()