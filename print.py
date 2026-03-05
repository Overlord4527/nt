import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('рисование')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF.fill((100, 100, 100))
pygame.draw.polygon(DISPLAYSURF, (255, 255, 0), ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame. draw. line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame. draw. line(DISPLAYSURF, BLUE, (120, 60), (60, 120), 20)
pygame. draw. line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (350, 50), 20, 5)
pygame.draw.ellipse(DISPLAYSURF, RED, (0, 320, 40, 80), 1)
pygame.draw.rect (DISPLAYSURF, RED, (400, 0, 100, 50))

pixObj = pygame.PixelArray (DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj
while True:
    for even in pygame.event.get():
        if even.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()