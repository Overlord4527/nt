# import pygame as pg
# import sys
# W = 400
# H= 300
# sc = pg.display.set_mode((W,H))
# sc.fill((100,150,200))
# dog_surf = pg.image.load('animal2.bmp')
# dog_rect = dog_surf.get_rect(bottomright=(W,H))
# sc.blit(dog_surf, dog_rect)
#
#
# sun_surf = pg.image.load('sun4.png')
# sun_rect = sun_surf.get_rect()
# sc.blit(sun_surf, sun_rect)
# pg.display.update()
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#     pg.time.delay(20)


import pygame as pg
import sys
pg.init()
W = 800
H = 300
sc = pg.display.set_mode((W, H))

bg_img = pg.image.load('fon.jpg').convert()
bg_img = pg.transform.scale(bg_img, (W, H))
bg = pg.Surface((W, H))
bg.fill((100, 150, 200))
sun = pg.image.load('sun4.png').convert_alpha()
sun_rect = sun.get_rect(topleft=(0, 20))
speed = 5
clock = pg.time.Clock()
while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        sun_rect.x -= speed
    if keys[pg.K_RIGHT]:
        sun_rect.x += speed
    if keys[pg.K_UP]:
        sun_rect.y -= speed
    if keys[pg.K_DOWN]:
        sun_rect.y += speed
    sc.blit(bg_img, (0, 0))
    sc.blit(sun, sun_rect)
    pg.display.update()
    clock.tick(60)

