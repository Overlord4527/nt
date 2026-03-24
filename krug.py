import pygame
import sys
import random
pygame.init()
FPS = 60
W = 700
H = 300
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
x = W // 2
y = H // 2
r = 50
current_color = BLUE
speed = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = random.randint(r, W - r)
                y = random.randint(r, H - r)
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if x < 0:
        x = W
    elif x > W:
        x = 0
    if y < 0:
        y = H
    elif y > H:
        y = 0
    sc.fill(WHITE)
    pygame.draw.circle(sc, current_color, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)
