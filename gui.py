__author__ = 'Harley'
import sys, pygame, unit
from unit import *
from pygame.sprite import Group



living_units = Group()
rect_list=[]

class GUI():

    def __init__(self,screen_rect,filestr):
        """
        Initialize the display.
        screen_rect: the bounds of the screen
        """

        # Set up the screen
        self.screen = pygame.display.set_mode((screen_rect.w, screen_rect.h))
        self.screen_rect = screen_rect
        self.background = pygame.image.load(filestr).convert()

    def load_background(self):

        #Scale image to match screensize given
        self.background =pygame.transform.scale(self.background,(self.screen_rect.w,self.screen_rect.h))
        #Place image on screen drawing from the top left
        self.screen.blit(self.background, [0,0])


    def activate_melee(self,team):
        new_melee = unit.unit_type['melee'](
                 side = team,
                 spawn = True
                 )
        rect_list.append(new_melee.rect)
        if not len(new_melee.rect.collidelistall(rect_list))>1:
            living_units.add(new_melee)

    def activate_fortress(self,team):
        new_fortress = unit.unit_type['fortress'](
            side = team,
            spawn = True
        )
        rect_list.append(new_fortress.rect)

        living_units.add(new_fortress)
    def update_units(self):
        living_units.clear(self.screen,self.background)
        for sprites in living_units:
            sprites.move(rect_list)
    def draw_units(self):
        for sprites in living_units:
            sprites.image.convert()
            sprites.image = pygame.transform.scale(sprites.image,sprites.size)
            sprites.draw_health()
            # print(sprites.rect)
        living_units.draw(self.screen)