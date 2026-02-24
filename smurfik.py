import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60
WHITE = (225, 255, 255)
BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
rect_size = 50
x = WIDTH // 2
y = HEIGHT // 2
speed_x = 10
speed_y = 10
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption('Движущийся квадрат')
pygame.draw.circle(screen, BLUE, (x + rect_size//2, y + rect_size//2), rect_size//2)
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed_x
    y += speed_y
    if x + rect_size > WIDTH or x < 0:
        speed_x = -speed_x

    if y + rect_size > HEIGHT or y < 0:
        speed_y = -speed_y

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x, y, rect_size, rect_size))
    pygame.display.flip()

pygame.quit()