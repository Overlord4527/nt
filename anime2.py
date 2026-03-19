import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 120
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 900), 0, 32)
pygame.display.set_caption('Diagonal Animation')
BLUE = (0, 0, 255)
catImg = pygame.image.load('meegg.png')

catx, caty = 10, 10
cat2x, cat2y = 550, 550
direction = 'wwwdom'
speed = 5

while True:
    DISPLAYSURF.fill(BLUE)

    if direction == 'wwwdom':
        catx += speed
        caty += speed
        cat2x -= speed
        cat2y -= speed
        if catx >= 550: direction = 'wwwup'
    elif direction == 'wwwup':
        catx -= speed
        caty -= speed
        cat2x += speed
        cat2y += speed
        if catx <= 10:
            catx, caty = 10, 10
            cat2x, cat2y = 550, 550
            direction = 'wwwdom'
            speed += 1

    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(catImg, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            catx, caty = event.pos
            print(f"Кот прыгнул в {event.pos}")
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                catx, caty = 500, 450
                cat2x, cat2y = 500, 450
    pygame.display.update()
    fpsClock.tick(FPS)




