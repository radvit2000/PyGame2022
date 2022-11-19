import pygame as pg
scr = pg.display.set_mode((800, 600))

headRight = pg.image.load('images/headRight.png').convert_alpha()
headLeft = pg.image.load('images/headLeft.png').convert_alpha()
headUp = pg.image.load('images/headUp.png').convert_alpha()
headDown = pg.image.load('images/headDown.png').convert_alpha()

backGroundColor = (255, 255, 255)
class Head(pg.sprite.Sprite):
    """ __init__ - создаёт объект с изображением головы змеи, создаёт его rect, и задаёт скорость по двум осям

        left, right, up, down - изменяет скорости для движения в различных направлениях

        update - изменяет изображение головы в зависимости от направления движения,
                 обеспечивает телепортация через край экрана
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.x = 20
        self.y = 0

        self.image = headRight
        self.rect = self.image.get_rect()
        self.image.set_colorkey(backGroundColor)

        self.rect.topleft = (100, 100)

    def left(self):
        if self.x != 20:
            self.x = -20
            self.y = 0
            self.update()
        else:
            self.update()

    def right(self):
        if self.x != -20:
            self.x = 20
            self.y = 0
            self.update()
        else:
            self.update()

    def up(self):
        if self.y != 20:
            self.x = 0
            self.y = -20
            self.update()
        else:
            self.update()

    def down(self):
        if self.y != -20:
            self.x = 0
            self.y = 20
            self.update()
        else:
            self.update()

    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y

        if self.x == 20:
            self.image = headRight
            self.image.set_colorkey(backGroundColor)

        elif self.x == -20:
            self.image = headLeft
            self.image.set_colorkey(backGroundColor)

        elif self.y == 20:
            self.image = headDown
            self.image.set_colorkey(backGroundColor)

        elif self.y == -20:
            self.image = headUp
            self.image.set_colorkey(backGroundColor)

        if self.rect.x > 780:
            self.rect.x = 0

        if self.rect.y > 580:
            self.rect.y = 0

        if self.rect.x < 0:
            self.rect.x = 780

        if self.rect.y < 0:
            self.rect.y = 580