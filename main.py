__author__ = 'Harley'
import sys, pygame
from res import screen_x,screen_y
from gui import GUI
RESOLUTION = pygame.Rect(0, 0,screen_x , screen_y)
pygame.init()

# Main_gui is an instance of the gui class. Initializes screen size
main_gui = GUI(RESOLUTION,"media/art/board.png")
main_gui.load_background()
clock = pygame.time.Clock()

# Set starting units:

main_gui.activate_fortress(0)
main_gui.activate_fortress(1)
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
        # a key spawns a melee unit on the left side
        elif (event.type == pygame.KEYDOWN and
        event.key == pygame.K_a):
            main_gui.activate_melee(0)
        # l key spawns a melee unit on the right side
        elif (event.type == pygame.KEYDOWN and
        event.key == pygame.K_l):
            main_gui.activate_melee(1)
        elif (event.type == pygame.KEYDOWN and
        event.key == pygame.K_s):
            main_gui.activate_archer(0)
        elif (event.type == pygame.KEYDOWN and
        event.key == pygame.K_k):
            main_gui.activate_archer(1)
    pygame.display.flip()
    main_gui.update_units()
    main_gui.draw_units()
    main_gui.draw_HUD()

    clock.tick(60)
