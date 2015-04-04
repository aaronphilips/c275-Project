__author__ = 'Harley'
import pygame, unit
from pygame.sprite import Sprite, Group
from pygame.locals import *
# Temp numbers, but should be consistent for all units


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 450



class BasicUnit(pygame.sprite.Sprite):
    # Need to initialize sprite drawing stuff here
    # Set should correspond to drawing list

    def __init__(self,
                 side,
                 spawn
                 ):
        Sprite.__init__(self)



        # Unit stats:
        self.screen_x = 0
        self.screen_y = 450
        self.side = side

        self.health = None
        self.health_image  = None


    def can_attack(self):
        """
        Can the unit attack something? Depends on range, location of
        nearby enemies, and whether the unit can move or not. Movement
        should be prioritized over attacking
        Returns a boolean
        """
    def can_move(self,rect_list):
        """
        Is there a unit in front of me?
        Returns a boolean
        """

        if len(self.rect.collidelistall(rect_list))>1:
            print("Shouldn't move")
            return False

        else:
            print("Should move")
            return True

    def move(self, rect_list):
        if self.can_move(rect_list):
            if self.side:
                self.rect.x -=self.speed
            else:
                self.rect.x += self.speed


    def attack(self):
        if self.can_attack():
            # Do damage to appropriate enemy
            return "BAM!"
        else:
            return

    def draw_health(self):
        health_image = pygame.font.SysFont("comicsansms",30)
        health_text = health_image.render(str(self.health),True,(0,255,0))
         # Move the health to the bottom-right of the image.
        health_rect = health_text.get_rect()
        # Draw the health on to the image.
        self.image.blit(health_text, health_rect)





