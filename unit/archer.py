__author__ = 'Harley'
__author__ = 'Harley'
import pygame, unit
from unit.basic_unit import BasicUnit
from unit.fortress import FORTRESS_HEIGHT, FORTRESS_WIDTH
from unit.melee import *
from res import screen_y,screen_x
UNIT_HEIGHT = 200
UNIT_WIDTH = 100
SCREEN_WIDTH = screen_x
SCREEN_HEIGHT = screen_y

class archer(melee):
    sprite = pygame.image.load("media/art/archer.png")

    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        self.range = 4*UNIT_WIDTH
        self.type = 'archer'
        self.image = self.sprite

unit.unit_type["archer"] = archer