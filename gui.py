__author__ = 'Harley'
import sys, pygame, unit
from unit import *
from pygame.sprite import Group

pygame.font.init()
font = pygame.font.Font(None,30)
living_units = Group()
unit_list=[]

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

        if not len(new_melee.rect.collidelistall(unit_list))>0:
            living_units.add(new_melee)
            unit_list.append(new_melee)

    def activate_fortress(self,team):
        new_fortress = unit.unit_type['fortress'](
            side = team,
            spawn = True
        )
        unit_list.append(new_fortress)
        living_units.add(new_fortress)

    def update_units(self):
        living_units.clear(self.screen,self.background)
        for sprites in living_units:
            sprites.move(unit_list)
            sprites.attack(unit_list)
            if sprites.die():
                living_units.remove(sprites)
                unit_list.remove(sprites)
    def draw_units(self):
        for sprites in living_units:
            sprites.image.convert()
            sprites.image = pygame.transform.scale(sprites.image,sprites.size)
            health_text = font.render(str(int(sprites.health)),1, (255,0,0))
            health_rect = health_text.get_rect()

            sprites.image.blit(health_text,health_rect)
        living_units.draw(self.screen)