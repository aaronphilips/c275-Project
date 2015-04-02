__author__ = 'Harley'
import sys, pygame
from gui import GUI
RESOLUTION = pygame.Rect(0, 0, 800, 450)
pygame.init()

# Main_gui is an instance of the gui class. Initializes screen size
main_gui = GUI(RESOLUTION)
main_gui.load_background("media/art/board.png")
clock = pygame.time.Clock()

# Set starting units:
main_gui.activate_melee()

# The game loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        # End if q is pressed
        elif (event.type == pygame.KEYDOWN and
        (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            pygame.display.quit()
            sys.exit()
    main_gui.draw_units()
    # main_gui.update_everything()
    # main_gui.activate_crap()
    # main_gui.draw_unit()
    clock.tick(60)
