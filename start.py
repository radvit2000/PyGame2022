import pygame as pg
from backGround import backGround
from text import redText
from controll import startControl

def startScr():
    """Функция создаёт начальный экран для ввода ника игрока. Возвращает ник игрока"""
    run = True
    name = ''

    while run:
        scr = pg.display.set_mode((800, 600))
        scr = backGround(scr)
        scr.blit(redText('Как тебя зовут?'), (250, 50))
        scr.blit(redText(name), (300, 250))
        name, run = startControl(name)
        pg.display.flip()
    return name