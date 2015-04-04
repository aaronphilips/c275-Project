__author__ = 'Harley'
import pygame, unit
from pygame.sprite import Sprite, Group
from pygame.locals import *
from res import  screen_x, screen_y

# Temp numbers, but should be consistent for all units


SCREEN_WIDTH = screen_x
SCREEN_HEIGHT = screen_y


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
        self.screen_y = screen_y
        self.side = side

        self.health = None
        self.health_image  = None
        self.range = None

    def die(self):
        if self.health<0:
            return True
        else:
            return False

    def can_attack(self,unit_list):
        """
        Can the unit attack something? Depends on range, location of
        nearby enemies.
        Returns the unit to attack

        Expects rectlist to only contain enemy rects
        """

        enemies = {}
        for unit in unit_list:
            if unit.side != self.side:
                enemies[unit] = unit.rect


        # range_rect is current unit's range
        if self.side == 0:
            range_rect = pygame.Rect(self.rect.right, self.rect.y,self.range,self.rect.h)
            target = range_rect.collidedict(enemies)
        if self.side == 1:
            range_rect = pygame.Rect(self.rect.left - self.range, self.rect.y, self.range, self.rect.h)
            target = range_rect.collidedict(enemies)
        if target is not None:
            return target[0]
        else:
            return False


    def can_move(self,unit_list):
        """
        Is there a unit in front of me?
        Returns a boolean
        """
        rect_list = []
        for units in unit_list:
            rect_list.append(units.rect)
        if len(self.rect.collidelistall(rect_list))>1:

            return False

        else:

            return True

    def move(self, unit_list):
        if self.can_move(unit_list):
            if self.side:
                self.rect.x -=self.speed
            else:
                self.rect.x += self.speed



    def attack(self,unit_list):
        can_attack = self.can_attack(unit_list)
        if can_attack== False:
            return
        else:
            can_attack.health -= self.attack_damage
            can_attack.refresh_image()

    def refresh_image(self):
        self.image = unit.unit_type[str(self.type)].sprite




