import pygame as pg


def controll(head):
    """управление во время основной игры"""
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_UP:
                head.up()
                break
            if i.key == pg.K_DOWN:
                head.down()
                break
            if i.key == pg.K_LEFT:
                head.left()
                break
            if i.key == pg.K_RIGHT:
                head.right()
                break

    else:
        head.update()


def endControl():
    """управение при экране проигрыша"""
    restart = True
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_r:
                restart = False
    return restart


def startControl(name):
    """управление при принятии ника игрока"""
    enter = True
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

        if i.type == pg.KEYDOWN:
            if i.key == pg.K_RETURN and len(name) != 0:
                enter = False
            elif i.key == pg.K_BACKSPACE:
                name = name[0:len(name) - 1]
            elif len(name) < 7 and i.key != pg.K_RETURN:
                name += i.unicode
    return name, enter
