__author__ = 'Harley'
import pygame, unit
from unit import basic_unit

class melee(basic_unit):
    sprite = pygame.image.load("media/art/melee.png")

    def __init__(self):
        self._basic_image = melee.sprite
        super.__init__()
        self.health = 20
        self.attack_damage = 5
        self.attack_speed = 4
        self.range = 0








unit.unit_type["melee"] = melee