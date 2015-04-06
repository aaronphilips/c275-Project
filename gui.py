__author__ = 'Harley'
import sys, pygame, unit
from unit import *
from pygame.sprite import Group

pygame.font.init()
font = pygame.font.Font(None,30)


from res import screen_y,screen_x
UNIT_HEIGHT = 200
UNIT_WIDTH = 100
SCREEN_WIDTH = screen_x
SCREEN_HEIGHT = screen_y
from unit.fortress import FORTRESS_HEIGHT, FORTRESS_WIDTH


class GUI():
    team_0_cash = 100
    team_1_cash = 100
    def __init__(self,screen_rect,filestr):
        """
        Initialize the display.
        screen_rect: the bounds of the screen
        """

        # Set up the screen
        self.screen = pygame.display.set_mode((screen_rect.w, screen_rect.h))
        self.screen_rect = screen_rect
        self.background = pygame.image.load(filestr).convert()
        self.bar_rect=pygame.Rect(0,0,screen_rect.w,70)
        self.living_units = Group()
        self.unit_list=[]

    def load_background(self):
        #Scale image to match screensize given
        self.background =pygame.transform.scale(self.background,(self.screen_rect.w,self.screen_rect.h))
        #Place image on screen drawing from the top left
        self.screen.blit(self.background, [0,0])

    def can_spawn(self,unit,unit_list):

        for units in unit_list:
            if unit.side==0 and units.side==0:
                if units.screen_x==FORTRESS_WIDTH:
                    return

            if unit.side==1 and units.side==1:
                if units.screen_x==SCREEN_WIDTH - UNIT_WIDTH - FORTRESS_WIDTH:
                    return
            
        # if not len(unit.rect.collidelistall(unit_list))>0:
        self.living_units.add(unit)
        self.unit_list.append(unit)

    def activate_melee(self,team):
        new_melee = unit.unit_type['melee'](
                 side = team,
                 spawn = True
                 )

        self.can_spawn(new_melee,self.unit_list)
    def activate_archer(self,team):
        new_archer = unit.unit_type['archer'](
                 side = team,
                 spawn = True
                 )

        self.can_spawn(new_archer,self.unit_list)
    def activate_fortress(self,team):
        new_fortress = unit.unit_type['fortress'](
            side = team,
            spawn = True
        )
        self.unit_list.append(new_fortress)
        self.living_units.add(new_fortress)

    def update_units(self):
        self.living_units.clear(self.screen,self.background)
        for sprites in self.living_units:
            sprites.move(self.unit_list)
            sprites.attack(self.unit_list)
            if sprites.die():
                self.living_units.remove(sprites)
                self.unit_list.remove(sprites)
                if sprites.side: self.team_0_cash+=20
                else: self.team_1_cash+=20
    def render_info(self,info):
        info_text = font.render(str(int(info)),1, (255,0,0))
        info_rect = info_text.get_rect()
        return info_text,info_rect
    def draw_units(self):
        for sprites in self.living_units:
            sprites.image.convert()
            sprites.image = pygame.transform.scale(sprites.image,sprites.size)
            sprites.image.blit(self.render_info(sprites.health)[0],self.render_info(sprites.health)[1])
        self.living_units.draw(self.screen)
    def draw_HUD(self):
        HUD = pygame.Surface((self.bar_rect[2],self.bar_rect[3]))
        HUD.fill((125,125,125),self.bar_rect)
        self.screen.blit(HUD,(0,0))
        self.screen.blit(self.render_info(self.team_0_cash)[0], (0, 0))
        self.screen.blit(self.render_info(self.team_1_cash)[0], (self.screen_rect.w - 50,0))