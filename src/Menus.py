import pygame
import pygame_menu
from Surface import *

def startMenu():
    menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name :', default='John Doe')
    menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SURFACE)
    