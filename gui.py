__author__ = 'Harley'
import sys, pygame, unit
from unit import *
from pygame.sprite import Group


# Set the fonts
pygame.font.init()
FONT_SIZE = 16
BIG_FONT_SIZE = 42
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
BIG_FONT.set_bold(True)


class GUI():
    living_units = Group()
    def __init__(self,screen_rect):
        """
        Initialize the display.
        screen_rect: the bounds of the screen
        """

        # Set up the screen
        self.screen = pygame.display.set_mode((screen_rect.w, screen_rect.h))
        self.screen_rect = screen_rect


    def load_background(self,filestr):
        background = pygame.image.load(filestr).convert()
        #Scale image to match screensize given
        background =pygame.transform.scale(background,(self.screen_rect.w,self.screen_rect.h))
        #Place image on screen drawing from the top left
        self.screen.blit(background, [0,0])


    def activate_melee(self,team):
        new_melee = unit.unit_type['melee'](
                 side = team,
                 screen_x = 0,
                 #Should be from bottom left corner
                 screen_y = 450
                 )
        self.living_units.add(new_melee)
    def draw_units(self):
        for sprites in self.living_units:
            sprites.image.convert()
            sprites.image = pygame.transform.scale(sprites.image,sprites.size)
            print(sprites.rect)
        self.living_units.draw(self.screen)