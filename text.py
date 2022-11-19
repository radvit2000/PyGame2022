import pygame as pg
pg.init()
font = pg.font.SysFont('serif', 48)

def redText(line):
    """подготавливает строку к прорисовке на экране и возвращает её"""
    result = font.render(str(line), False, (255, 0, 0))
    return result