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
        if (event.type == pygame.KEYDOWN and
        (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
            pygame.display.quit()
            sys.exit()
        # a key spawns a melee unit on the left side
        if (event.type == pygame.KEYDOWN and
        event.key == pygame.K_a and main_gui.team_0_cash>=10):
            main_gui.activate_melee(0)
            main_gui.team_0_cash -=10
        # l key spawns a melee unit on the right side
        if (event.type == pygame.KEYDOWN and
        event.key == pygame.K_l and main_gui.team_1_cash>=10):
            main_gui.activate_melee(1)
            main_gui.team_1_cash -=10
        if (event.type == pygame.KEYDOWN and
        event.key == pygame.K_s and main_gui.team_0_cash>=20):
            main_gui.activate_archer(0)
            main_gui.team_0_cash -=20
        if (event.type == pygame.KEYDOWN and
        event.key == pygame.K_k and main_gui.team_1_cash>=20):
            print(GUI.team_1_cash)
            main_gui.activate_archer(1)
            main_gui.team_1_cash -=20
    pygame.display.flip()
    main_gui.update_units()
    main_gui.draw_units()
    main_gui.draw_HUD()
    # print(main_gui.team_1_cash,main_gui.team_0_cash)
    print(main_gui.living_units)
    clock.tick(60)
