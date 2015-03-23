__author__ = 'Harley'
import pygame, unit
from pygame.sprite import Sprite

# Temp numbers, but should be consistent for all units
UNIT_HEIGHT = 50
UNIT_WIDTH = 50

class BasicUnit(Sprite):
    # Need to initialize sprite drawing stuff here

    def __init__(self,
                 side = -1,
                 screen_x = None,
                 screen_y = UNIT_HEIGHT,
                 active = False):
        