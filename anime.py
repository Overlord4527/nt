import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 100
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 1000), 0, 32)
pygame.display.set_caption('Animation')
WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.jpg')
catx = 10
caty = 10
direction = 'right'
while True:
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 650:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 690:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 50:
            direction = 'right'
    DISPLAYSURF.blit(catImg, (catx, caty))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)


