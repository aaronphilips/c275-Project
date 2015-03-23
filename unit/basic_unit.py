__author__ = 'Harley'
import pygame, unit
from pygame.sprite import Sprite

# Temp numbers, but should be consistent for all units
UNIT_HEIGHT = 50
UNIT_WIDTH = 50

class BasicUnit(Sprite):
    # Need to initialize sprite drawing stuff here
    # Set should correspond to drawing list
    living = []

    def __init__(self,
                 side = -1,
                 screen_x = None,
                 screen_y = UNIT_HEIGHT,
                 active = False):
        Sprite.__init__(self)

        # Setup
        self.side = side
        self.screen_x = screen_x
        self.screen_y = screen_y


        # Unit stats:
        self.health = None
        self.attack_damage = None
        self.attack_speed = None
        self.range = None

    # Activate or deactivate the unit (for death or spawning)
    def activate(self):
        if not self._active:
            self._active = True
            BasicUnit.living.add(self)
    def deactivate(self):
        self._active = False
        BasicUnit.living.remove(self)
    def can_attack(self):
        """
        Can the unit attack something? Depends on range, location of
        nearby enemies, and whether the unit can move or not. Movement
        should be prioritized over attacking
        Returns a boolean
        """
    def can_move(self):
        """
        Is there a unit in front of me?
        Returns a boolean
        """
    def attack(self):
        if self.can_attack():
            # Do damage to appropriate enemy
            return "BAM!"
        else:
            return