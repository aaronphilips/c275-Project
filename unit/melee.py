__author__ = 'Harley'
import pygame, unit
from unit.basic_unit import BasicUnit
from unit.fortress import FORTRESS_HEIGHT, FORTRESS_WIDTH
from res import screen_y,screen_x
UNIT_HEIGHT = 200
UNIT_WIDTH = 100
SCREEN_WIDTH = screen_x
SCREEN_HEIGHT = screen_y

class melee(BasicUnit):
    sprite = pygame.image.load("media/art/melee.png")

    def __init__(self,*args,**kwargs):
        # These variables will be overwritten by the super init
        self.side = None
        self.screen_y = None
        self.screen_x = None

        # Get init values sent to baseclass
        super().__init__(**kwargs)

        # Unit specific values
        self.health = 20
        self.attack_damage = .25
        self.attack_speed = 4
        self.range = UNIT_WIDTH/2
        self.type = 'melee'
        self.image = melee.sprite
        self.speed = 4
        side = self.side

        # Set up screen positioning and unit rect dimensions
        if side == 1:
            self.screen_x = SCREEN_WIDTH - UNIT_WIDTH - FORTRESS_WIDTH
        else: self.screen_x = FORTRESS_WIDTH
        # Set constants for all units
        self.screen_y  = SCREEN_HEIGHT- UNIT_HEIGHT
        self.size = (UNIT_WIDTH, UNIT_HEIGHT)
        # Define unit rect for drawing
        self.rect = pygame.Rect(self.screen_x,self.screen_y,UNIT_WIDTH,UNIT_HEIGHT)




unit.unit_type["melee"] = melee