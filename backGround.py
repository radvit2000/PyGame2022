import pygame as pg
backGroundColor = (0, 75, 0)

def backGround(scr):
    """прорисовывает задний фон и возвращает дисплей с ним"""
    scr.fill(backGroundColor)

    for i in range(20):
        for j in range(20):
            pg.draw.rect(scr, (0, 50, 0), (i * 40, j * 40, 20, 20))
            pg.draw.rect(scr, (0, 50, 0), (20 + i * 40, 20 + j * 40, 20, 20))
    return scr