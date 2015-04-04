__author__ = 'Harley'
import pygame, unit
from unit.basic_unit import BasicUnit

class melee(BasicUnit):
    sprite = pygame.image.load("media/art/melee.png")

    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        self.health = 20
        self.attack_damage = 5
        self.attack_speed = 4
        self.range = 0
        self.type = 'melee'
        self.image = melee.sprite
        self.speed = 4
unit.unit_type["melee"] = melee