import pygame, sys
from pygame.locals import *

# run.py
pygame.init()

# Creer une fenetre de jeu
# set_mode(resolution=(width, height), flags=0, depth=0)
screen = pygame.display.set_mode((640, 480), 0, 32)

# Couleur de la fenetre
bg_color = (0, 0, 0)

# Par defaut, la fenetre sera Game Menu
pygame.display.set_caption('Game Menu')
menu_selected = True

# Initialisation des vues
menu_items = ('Start', 'Settings', 'Quit')
gm = GameMenu(screen, menu_items)
gs = GameSettings(screen)
# l ecran Game sera cree dynamiquement pour permettre le redemarrage au debut
g = None
# Par defaut, la boucle tourne a linfini.
mainloop = True

while mainloop:

    # Rafraichit l'ecran en noir a chaque boucle
    screen.fill(bg_color)

    # Demarre l'ecran menu par defaut ou apres ECHAP
    if menu_selected or g.escape_selected:
        gm.run()
        if g is not None:
            g.escape_selected = False
        gs.escape_selected = False

    # Demarre l'ecran de jeu
    if gm.start_selected:
        g = Game(screen)
        g.run()
        gm.start_selected = False
        gm.quit_select = False

    # Demarre l'ecran de configuration
    if gm.settings_selected:
        gs.run()
        gm.settings_selected = False

    # Ferme la fenetre si Quit est selectionnee
    if gm.quit_select is True:
        mainloop = False

    pygame.display.flip()