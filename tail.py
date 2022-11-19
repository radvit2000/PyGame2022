import pygame as pg
from ending import endScr

left = pg.image.load('images/left.png').convert_alpha()
right = pg.image.load('images/right.png').convert_alpha()
up = pg.image.load('images/up.png').convert_alpha()
down = pg.image.load('images/down.png').convert_alpha()

rightUp = pg.image.load('images/rightDown.png').convert_alpha()
leftUp = pg.image.load('images/upRight.png').convert_alpha()
rightDown = pg.image.load('images/downLeft.png').convert_alpha()
leftDown = pg.image.load('images/leftUp.png').convert_alpha()

tailRight = pg.image.load('images/tailRight.png').convert_alpha()
tailLeft = pg.image.load('images/tailLeft.png').convert_alpha()
tailUp = pg.image.load('images/tailUp.png').convert_alpha()
tailDown = pg.image.load('images/tailDown.png').convert_alpha()
x = [80, 100]
y = [100, 100]

def restart():
    """Возвращает списки в изначальный вид"""
    global x, y
    x = [80, 100]
    y = [100, 100]


def tail(scr, head, len):
    """прорисовывает хвост змеи. Возвращает дисплей с отрисованным хвостом"""
    for i in range(-1, -len - 1, -1):

        if i == -1:
            if head.x == 20:
                if y[i - 1] == y[i]:
                    image = right
                elif y[i - 1] < y[i]:
                    image = leftDown
                elif y[i - 1] > y[i]:
                    image = leftUp

            elif head.x == -20:
                if y[i - 1] == y[i]:
                    image = left
                elif y[i - 1] < y[i]:
                    image = rightDown
                elif y[i - 1] > y[i]:
                    image = rightUp

            elif head.y == 20:
                if x[i - 1] == x[i]:
                    image = down
                elif x[i - 1] < x[i]:
                    image = rightUp
                elif x[i - 1] > x[i]:
                    image = leftUp

            elif head.y == -20:
                if x[i - 1] == x[i]:
                    image = up
                elif x[i - 1] < x[i]:
                    image = rightDown
                elif x[i - 1] > x[i]:
                    image = leftDown

        elif i == -len:
            if x[i + 1] == 780 and x[i] == 0:
                image = tailLeft
            elif x[i + 1] == 0 and x[i] == 780:
                image = tailRight
            elif y[i + 1] == 580 and y[i] == 0:
                image = tailUp
            elif y[i + 1] == 0 and y[i] == 580:
                image = tailDown

            elif x[i] > x[i + 1]:
                image = tailLeft
            elif x[i] < x[i + 1]:
                image = tailRight
            elif y[i] > y[i + 1]:
                image = tailUp
            elif y[i] < y[i + 1]:
                image = tailDown


        else:
            if x[i] < x[i + 1]:
                if y[i - 1] == y[i]:
                    image = right
                elif y[i - 1] < y[i]:
                    image = leftDown
                elif y[i - 1] > y[i]:
                    image = leftUp

            elif x[i] > x[i + 1]:
                if y[i - 1] == y[i]:
                    image = left
                elif y[i - 1] < y[i]:
                    image = rightDown
                elif y[i - 1] > y[i]:
                    image = rightUp

            elif y[i] < y[i + 1]:
                if x[i - 1] == x[i]:
                    image = down
                elif x[i - 1] < x[i]:
                    image = rightUp
                elif x[i - 1] > x[i]:
                    image = leftUp

            elif y[i] > y[i + 1]:
                if x[i - 1] == x[i]:
                    image = up
                elif x[i - 1] < x[i]:
                    image = rightDown
                elif x[i - 1] > x[i]:
                    image = leftDown

        scr.blit(image, (x[i], y[i]))

    x.append(head.rect.x)
    y.append(head.rect.y)
    return scr


def end(head, len, score, nik):
    """если голова врезалась в хвост запускает экран проигрыша.
       возвращает сигнал к перезапуску игры
    """
    loose = False
    newGame = False
    for i in range(-1, -len - 1, -1):
        if x[i] == head.rect.x and y[i] == head.rect.y:
            loose = True
    while loose:
        loose = endScr(score, nik)
        add = False
        if not loose:
            restart()
            newGame = True
    return newGame

def rightApple(appleX, appleY):
    """проверяет координаты находятся в хвосте или нет
       если не находятся возвращает True иначе False
    """
    global x, y
    right = True
    for i in range(len(x)):
        if appleX == x[i] and appleY == y[i]:
            right = False
    return right
