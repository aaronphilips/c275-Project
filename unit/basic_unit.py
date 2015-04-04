__author__ = 'Harley'
import pygame, unit
from pygame.sprite import Sprite, Group
# Temp numbers, but should be consistent for all units
UNIT_HEIGHT = 200
UNIT_WIDTH = 100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

class BasicUnit(pygame.sprite.Sprite):
    # Need to initialize sprite drawing stuff here
    # Set should correspond to drawing list

    def __init__(self,
                 side,
                 screen_x,
                 screen_y,
                 spawn
                 ):
        Sprite.__init__(self)

        # Set which side of screen the units spawn at, depending on
        # which team they're on.
        self.side = side
        if side == 0 :
            self.screen_x = screen_x
        else:
            self.screen_x = SCREEN_WIDTH - UNIT_WIDTH

        # Set constants for all units
        self.screen_y = screen_y-UNIT_HEIGHT
        self.type = "basic_unit"
        self.size = (UNIT_WIDTH, UNIT_HEIGHT)

        # Unit stats:
        self.health = None
        self.attack_damage = None
        self.attack_speed = None
        self.range = None
        self.image = None

        # Define unit rect for drawing
        self.rect = pygame.Rect(self.screen_x,self.screen_y,UNIT_WIDTH,UNIT_HEIGHT)



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

        
