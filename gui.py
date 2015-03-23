__author__ = 'Harley'
import sys, pygame
# Testing out drawing images to the screen
from pygame.sprite import LayeredUpdates

# Sound names
SELECT_SOUND = "Select"
BUTTON_SOUND = "Button"

# GUI size information
MAP_WIDTH = 600
BAR_WIDTH = 200
BUTTON_HEIGHT = 50
CENTER = 100

# Set the fonts
pygame.font.init()
FONT_SIZE = 16
BIG_FONT_SIZE = 42
FONT = pygame.font.SysFont("Arial", FONT_SIZE)
BIG_FONT = pygame.font.SysFont("Arial", BIG_FONT_SIZE)
BIG_FONT.set_bold(True)

# padding for left and top side of the bar
PAD = 6

# Speed of reticle blinking
RETICLE_RATE = 0.02


# RGB colors for the GUI
FONT_COLOR = (0, 0, 0)
BAR_COLOR = (150, 150, 150)
OUTLINE_COLOR = (50, 50, 50)
BUTTON_HIGHLIGHT_COLOR = (255, 255, 255)
BUTTON_DISABLED_COLOR = (64, 64, 64)

# Names for the different teams
TEAM_NAME = {
    0: "green",
    1: "red"
}
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
class GUI(LayeredUpdates):
     # number of GUI instances
    num_instances = 0
    def __init__(self, screen_rect, bg_color):
        """
        Initialize the display.
        screen_rect: the bounds of the screen
        bg_color: the background color
        """
        LayeredUpdates.__init__(self)
        
        if GUI.num_instances != 0:
            raise Exception("GUI: can only have one instance of a simulation")
        GUI.num_instances = 1
        
        # Set up the screen
        self.screen = pygame.display.set_mode((screen_rect.w, screen_rect.h))
        self.screen_rect = screen_rect
    def load_level(self,filestr):
        background = pygame.image.load(filestr).convert()
        background =pygame.transform.scale(background,(800,600))
        #screen=pygame.display.set_mode(background)
        screen.blit(background, [0, 0])