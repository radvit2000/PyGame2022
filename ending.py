import pygame as pg
from backGround import backGround
from controll import endControl
from text import redText
from base import Base

table = Base()
add = True
def endScr(score, nic):
    """прорисовка экрана проигрыша формирует таблицу рекордов
       возвращает игнал к рестарту
    """
    global add
    loose = True
    scr = pg.display.set_mode((800, 600))
    scr.fill((0, 75, 0))
    scr = backGround(scr)

    scoreText = redText(str(score))
    nicText = redText(str(nic))
    rules = redText("r - рестарт")
    scr.blit(nicText, ((800 - 17 * len(nic)) / 2, 50))
    scr.blit(scoreText, (400, 100))
    scr.blit(rules, (300, 500))
    records = table.maxFive(nic, score, add)
    for i in range (5):
        scr.blit(redText(records[i][0]), (300, 200 + i * 50))
        scr.blit(redText(records[i][1]), (500, 200 + i * 50))

    add = False
    loose = endControl()
    pg.display.flip()
    if not loose:
        add = True
    return loose
