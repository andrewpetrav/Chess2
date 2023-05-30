import pygame
from Board import *

#Font
font = pygame.font.SysFont(None, 80)
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)
RED=pygame.Color(255,0,0)    
#Piece images
#White pieces

wpi=pygame.image.load('Pieces/White/w_p.png').convert_alpha()
wni=pygame.image.load('Pieces/White/w_n.png').convert_alpha()
wbi=pygame.image.load('Pieces/White/w_b.png').convert_alpha()
wri=pygame.image.load('Pieces/White/w_r.png').convert_alpha()
wqi=pygame.image.load('Pieces/White/w_q.png').convert_alpha()
wki=pygame.image.load('Pieces/White/w_k.png').convert_alpha()
#Black pieces
bpi=pygame.image.load('Pieces/Black/b_p.png').convert_alpha()
bni=pygame.image.load('Pieces/Black/b_n.png').convert_alpha()
bbi=pygame.image.load('Pieces/Black/b_b.png').convert_alpha()
bri=pygame.image.load('Pieces/Black/b_r.png').convert_alpha()
bqi=pygame.image.load('Pieces/Black/b_q.png').convert_alpha()
bki=pygame.image.load('Pieces/Black/b_k.png').convert_alpha()
#Re-scale images
wpi=pygame.transform.scale(wpi,(square_size,square_size))
wni=pygame.transform.scale(wni,(square_size,square_size))
wbi=pygame.transform.scale(wbi,(square_size,square_size))
wri=pygame.transform.scale(wri,(square_size,square_size))
wqi=pygame.transform.scale(wqi,(square_size,square_size))
wki=pygame.transform.scale(wki,(square_size,square_size))
bpi=pygame.transform.scale(bpi,(square_size,square_size))
bni=pygame.transform.scale(bni,(square_size,square_size))
bbi=pygame.transform.scale(bbi,(square_size,square_size))
bri=pygame.transform.scale(bri,(square_size,square_size))
bqi=pygame.transform.scale(bqi,(square_size,square_size))
bki=pygame.transform.scale(bki,(square_size,square_size))

turn=WHITE #whose turn
board=Board() 