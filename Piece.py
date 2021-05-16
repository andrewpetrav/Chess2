from abc import ABC
import pygame
from Surface import square_size
#from Main import board
#from Main import *

class Piece(ABC):
    def __int__(self,color,square,t,image,moved=False):
        self.color=color
        self.square=square
        self.t=t #type
        self.image=image
        self.moved=moved
        self.isAttacking=[] #same as open_squares+friendly pieces
        self.isAttackedBy=[] #what pieces are attacking this piece
    def get_moves(self):
        open_squares=[]
        if self.t=='pawn':
            if self.color==WHITE:
                pass
        elif self.t=='knight':
            pass
        elif self.t=='bishop':
            pass
        elif self.t=='rook':
            pass
        elif self.t=='queen':
            pass
        elif self.t=='king':
            pass


class Pawn(Piece):
    def __init__(self,color,square,image):
        super(Pawn,self).__init__(color,square,'pawn',image)

    
        
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)

