__author__ = 'Harley'
import sys, pygame
from gui import GUI
RESOLUTION = pygame.Rect(0, 0, 800, 600)
BG_COLOR = (32, 32, 32)

main_gui = GUI(RESOLUTION, BG_COLOR)
main_gui.load_level("media/art/board.png")
# The game loop
while 1:
    main_gui.update()
    main_gui.draw()
