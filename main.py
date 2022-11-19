import random
import time
import pygame as pg

from head import Head
from controll import controll
from backGround import backGround
from tail import tail, end, rightApple
from start import startScr

pg.init()

apple = pg.image.load('images/apple.png').convert_alpha()
WEIGHT = 800
HEIGHT = 600

scr = pg.display.set_mode((WEIGHT, HEIGHT))
head = Head()

player = pg.sprite.Group()
player.add(head)

tailLen = 2
score = 0
nic = ''
appleX = random.randint(0, 39)
appleY = random.randint(0, 29)

start = True

# основной цикл
while True:
    # принятие ника игрока
    if start:
        nic = startScr()
        start = False

    # создание заднего фона
    scr = backGround(scr)

    # движение головы от стрелок
    controll(head)

    # проверка проигрыша
    restart = end(head, tailLen, score, nic)

    # рестарт игры
    if restart:
        tailLen = 2
        score = 0

        appleX = random.randint(0, 39)
        appleY = random.randint(0, 29)

        head.rect.topleft = (100, 100)
        head.x = 20
        head.y = 0
        controll(head)

        restart = False
        start = True

    scr = tail(scr, head, tailLen)  # прорисовка хвоста
    player.draw(scr)    # прорисовка головы
    scr.blit(apple, (appleX * 20, appleY * 20))    # прорисовка яблока

    # проверка на яблоко в хвосте
    if head.rect.x == appleX * 20 and head.rect.y == appleY * 20:
        tailLen += 1
        score += 1
        right = False
        while not right:
            appleX = random.randint(0, 39)
            appleY = random.randint(0, 29)
            right = rightApple(appleX * 20, appleY * 20)

    pg.display.flip()   # обновление экрана
    time.sleep(0.1)     # задержка для стабильного FPS
