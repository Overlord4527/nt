import pygame
import sys
FPS = 60
W = 700
H = 300
WHITE = (255,255, 255)
BLUE = (0, 70, 225)
sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
x = W // 2
y = x // 2
r = 50
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x,y), r)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3
    elif keys[pygame.K_DOWN]:
        y += 3
    elif keys[pygame.K_UP]:
        y -= 3
    clock.tick(FPS)
