import pygame, sys
from pygame.locals import *

WINDOWWIDTH=1000
WINDOWHEIGHT=800
GREEN=pygame.Color(0,255,0)
pygame.init()
SURFACE=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
SURFACE.fill(GREEN)
square_size=100