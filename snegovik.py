import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('рисование')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
DISPLAYSURF.fill((100, 255, 255))
pygame.draw.rect (DISPLAYSURF, RED, (200, 150, 100, 100))
pygame.draw.polygon(DISPLAYSURF, GREEN, ((200, 150), (250, 100), (300, 150)))
for i in range(400, 500, 20):
    pygame.draw.line(DISPLAYSURF, RED, (1, 0), (1, 100), 1)
pygame.draw.line(DISPLAYSURF, RED, (499, 0), (499, 100), 1)
for i in range(0, 120, 20):
    pygame.draw.line(DISPLAYSURF, RED, (400, 1), (500, 1), 1)
pygame.draw.rect(DISPLAYSURF, RED, (350, 200, 80, 20))
pygame.draw.rect(DISPLAYSURF, GREEN, (365, 180, 50, 20))
pygame.draw.circle(DISPLAYSURF, BLACK, (360, 220), 13, 0)
pygame.draw.circle(DISPLAYSURF, BLACK, (420, 220), 13, 0)
pygame.draw.circle(DISPLAYSURF,WHITE, (350, 300), 50)
pygame.draw.circle(DISPLAYSURF,WHITE, (350, 230), 35)
pygame.draw.circle(DISPLAYSURF,WHITE, (350, 180), 25)
pygame.draw.circle(DISPLAYSURF, BLACK, (340, 175), 3)
pygame.draw.circle(DISPLAYSURF, BLACK, (360, 175), 3)
pygame.draw.line(DISPLAYSURF, ORANGE, (350,180), (370,185), 3)
alpha_surf = pygame.Surface((500, 400), pygame.SRCALPHA)
pygame.draw.circle(alpha_surf, (255, 0, 0, 150), (100, 80), 40)
pygame.draw.circle(alpha_surf, (0, 0, 255, 150), (140, 80), 40)
DISPLAYSURF.blit(alpha_surf, (0, 0))

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