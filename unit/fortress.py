__author__ = 'Harley'
import pygame, unit
from unit.basic_unit import BasicUnit
from res import screen_y,screen_x
FORTRESS_HEIGHT = 300
FORTRESS_WIDTH = 200
SCREEN_WIDTH = screen_x
SCREEN_HEIGHT = screen_y

class fortress(BasicUnit):
    sprite = pygame.image.load("media/art/fortress.jpg")

    def __init__(self,*args,**kwargs):
        self.side = None
        self.screen_y = None
        self.screen_x = None
        super().__init__(**kwargs)
        self.health = 100
        self.attack_damage = 0
        self.attack_speed = 0
        self.range = 0
        self.type = 'fortress'
        self.image = fortress.sprite
        self.speed = 0
        side = self.side
        # Set up screen positioning and unit rect dimensions
        if side == 1:
            self.screen_x = SCREEN_WIDTH - FORTRESS_WIDTH
        # Set constants for all units
        self.screen_y =SCREEN_HEIGHT- FORTRESS_HEIGHT
        self.size = (FORTRESS_WIDTH, FORTRESS_HEIGHT)
        # Define unit rect for drawing
        self.rect = pygame.Rect(self.screen_x,self.screen_y,FORTRESS_WIDTH,FORTRESS_HEIGHT)
unit.unit_type["fortress"] = fortress