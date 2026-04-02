# from random import randint
# import pygame as pg
# import sys
# W = 400
# H = 400
# WHITE = (255,255,255)
# class Car(pg.sprite.Sprite):
#     def __init__(self, x, filename):
#         pg.sprite.Sprite.__init__(self)
#         self.image = pg.image.load(filename).convert_alpha()
#         self.rect = self.image.get_rect(center=(x, 0))
# sc = pg.display.set_mode((W,H))
# car = Car(randint(1, W), 'car.jpg')
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#     sc.fill(WHITE)
#     sc.blit(car.image, car.rect)
#     pg.display.update()
#     pg.time.delay(20)
#     if car.rect.y <H:
#         car.rect.y += 2
#     else:
#         car.rect.y = 0


from random import randint
import pygame as pg
import sys
pg.init()
pg.time.set_timer(pg.USEREVENT, 3000)
W = 400
H = 400
WHITE = (255,255,255)
CARS = ('car1.png', 'car2.png', 'car3.png')
CARS_SURF = []
sc = pg.display.set_mode((W,H))
for i in range(len(CARS)):
    CARS_SURF.append(pg.image.load(CARS[i]).convert_alpha())