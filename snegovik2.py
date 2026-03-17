import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Уровень 3: Творчество и Прозрачность')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)

DISPLAYSURF.fill(SKY_BLUE) # Фон - небо
# --- ЗАДАНИЕ: Домик (комбинация примитивов) ---
# Основание дома (квадрат)
pygame.draw.rect(DISPLAYSURF, (200, 200, 200), (50, 200, 150, 150))
# Крыша (треугольник через polygon)
pygame.draw.polygon(DISPLAYSURF, BROWN, ((40, 200), (210, 200), (125, 120)))
# Дверь (прямоугольник)
pygame.draw.rect(DISPLAYSURF, BLACK, (100, 270, 40, 80))
# Окно (круг)
pygame.draw.circle(DISPLAYSURF, WHITE, (125, 230), 15)
# --- ЗАДАНИЕ: Работа с прозрачностью (Альфа-канал) ---
# 1. Создаем специальную поверхность такого же размера, как окно
# Флаг SRCALPHA позволяет использовать 4-е число в цвете (прозрачность)
alpha_surf = pygame.Surface((500, 400), pygame.SRCALPHA)

# 2. Рисуем два пересекающихся круга с прозрачностью (128 - это 50% прозрачности)
# Цвет: (R, G, B, Alpha)
pygame.draw.circle(alpha_surf, (255, 0, 0, 150), (100, 80), 40) # Красный
pygame.draw.circle(alpha_surf, (0, 0, 255, 150), (140, 80), 40) # Синий

# 3. Накладываем прозрачную поверхность на основное окно
DISPLAYSURF.blit(alpha_surf, (0, 0))

# --- ГЛАВНЫЙ ЦИКЛ ---
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
