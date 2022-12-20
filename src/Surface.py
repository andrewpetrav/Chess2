import pygame, sys
from pygame.locals import *

WINDOWWIDTH=800
WINDOWHEIGHT=800
GREEN=pygame.Color(0,255,0)
pygame.init()
SURFACE=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.RESIZABLE)
SURFACE.fill(GREEN)
