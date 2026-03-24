import pygame
import sys
FPS = 60
W = 700
H = 300
WHITE = (255,255, 255)
BLUE = (0, 70, 225)
RIGHT = 'to the right'
LEFT = 'to the left'
DOWN = 'to the down'
UP = 'to the up'
STOP = 'stop'
sc = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
x = W // 2
y = x // 2
r = 50
motion = STOP
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            elif i.key == pygame.K_DOWN:
                motion = DOWN
            elif i.key == pygame.K_UP:
                motion = UP
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                motion = STOP
    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
    elif motion == DOWN:
        y += 3
    elif motion == UP:
        y -= 3
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()
    clock.tick(FPS)
