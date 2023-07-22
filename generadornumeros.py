import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bolas en línea recta en Pygame")

# Colores
WHITE = (255, 255, 255)

# Clase para representar una bola
class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x += self.speed

# Función para dibujar una bola en la ventana
def draw_ball(x, y):
    pygame.draw.circle(window, WHITE, (x, y), 20)

# Bucle principal del juego
def main():
    clock = pygame.time.Clock()
    balls = []

    # Generar cinco bolas con posiciones y velocidades aleatorias
    for _ in range(5):
        x = random.randint(20, window_width - 20)
        y = random.randint(20, window_height - 20)
        speed = random.randint(1, 3)
        balls.append(Ball(x, y, speed))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpiar la ventana
        window.fill((0, 0, 0))

        # Actualizar las posiciones de las bolas
        for ball in balls:
            ball.move()

        # Dibujar las bolas en sus posiciones actualizadas
        for ball in balls:
            draw_ball(int(ball.x), int(ball.y))

        # Actualizar la pantalla
        pygame.display.update()

        # Limitar la cantidad de cuadros por segundo
        clock.tick(60)

if __name__ == "__main__":
    main()
