__author__ = 'Harley'
import pygame, unit
from pygame.sprite import Sprite, Group

# Temp numbers, but should be consistent for all units
UNIT_HEIGHT = 50
UNIT_WIDTH = 50
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

class BasicUnit(pygame.sprite.Sprite):
    # Need to initialize sprite drawing stuff here
    # Set should correspond to drawing list

    def __init__(self,
                 side ,
                 screen_x ,
                 screen_y ,
                 ):
        Sprite.__init__(self)

        # Setup
        self.side = side
        if side == 0 :
            self.screen_x = screen_x
        else:
            self.screen_x = SCREEN_WIDTH - UNIT_WIDTH

        self.screen_y = screen_y-UNIT_HEIGHT
        self.type = "basic_unit"
        self.active = False
        self.size = (UNIT_HEIGHT,UNIT_WIDTH)

        # Unit stats:
        self.health = None
        self.attack_damage = None
        self.attack_speed = None
        self.range = None
        self.image = None
        #Temp hardcode for 450
        self.rect = pygame.Rect(self.screen_x,self.screen_y,UNIT_WIDTH,UNIT_HEIGHT)

        #
        # if activate:
        #     self.activate()

    # Activate or deactivate the unit (for death or spawning)
    # def activate(self):
    #     if not self.active:
    #         self.active = True
    #         BasicUnit.living_units.add(self)
    # def deactivate(self):
    #     self.active = False
    #     BasicUnit.living_units.remove(self)
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

        
