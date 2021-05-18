import pygame
from Surface import square_size,SURFACE
#import Piece
#from Piece import w_pieces,b_pieces

class Square(object):
    def __init__(self,piece,color,image,powerup,highlighted=False):
        self.size=square_size
        isAttacked=False
        #isAttacking=[]
        
        self.piece=piece
        self.color=color
        self.image=image
        self.powerup=powerup
        self.highlighted=highlighted
        
        self.x,self.y=image.x,image.y
        self.x=int(self.x/self.size)
        self.y=int(self.y/self.size)
        
        self.selected=False
    
    def get_piece_image(self):
        if self.piece: #check if square has a piece before trying to return image of piece
            return self.piece.image
        else:
            return None
    def get_color(self):
        return self.color
    def get_image(self):
        return self.image
    def get_piece(self):
        return self.piece
    def set_piece(self,piece):
        self.piece=piece
    def get_isAttacked(self):
        return self.isAttacked
    def set_isAttacked(self,boolean):
        self.isAttacked=boolean
    def get_highlited(self):
        return self.highlighted
    def set_hightlighted(self):
        self.highlighted=not self.highlighted
    
    
class Board(object):
    def __init__(self,boardWidth=8,boardLength=8):
        self.boardWidth,self.boardLength=boardWidth,boardLength
        self.board=[[0 for i in range(self.boardWidth)]for j in range(self.boardLength)]
    
        self.w_attackedSquares=[] #squares being attacked BY white
        self.b_attackedSquares=[] #squares being attacked BY black
    
        clr=WHITE
        for i in range(self.boardWidth): 
            if clr==WHITE:
                clr=BLACK
            else:
                clr=WHITE
            for j in range(self.boardLength):
                image=pygame.Rect(square_size*i,square_size*j,square_size,square_size)
                #Switch color
                if clr==WHITE:
                    clr=BLACK
                else:
                    clr=WHITE
                self.board[i][j]=Square(None,clr,image,None)
    
    def draw_board(self):
        pygame.draw.line(SURFACE, black_piece_color,(0,800),(0,800))
        pygame.draw.line(SURFACE, black_piece_color, (800,0),(800,0))
        for i in range(self.boardWidth):
            for j in range(self.boardLength):
                space=self.board[i][j]
                pygame.draw.rect(SURFACE, space.get_color(),space.get_image())
                #if has piece, blit it on
                if space.get_piece_image():
                    SURFACE.blit(space.get_piece_image(), (space.x, space.y))
                    for i in range(self.boardWidth): #edit this to accomodate diff sized boards
                        pygame.draw.line(SURFACE,black_piece_color,(0,i*square_size),(800,i*square_size))
                        pygame.draw.line(SURFACE,black_piece_color,(i*square_size,0),(i*square_size,800))
    
    def setup(self,w_pieces,b_pieces):
        #Put white pieces in place
        for piece in w_pieces:
            self.board[piece.x][piece.y].set_piece(piece)
        #Put black pieces in place
        for piece in b_pieces:
            self.board[piece.x][piece.y].set_piece(piece)
        
BLACK=pygame.Color(211,139,67)
WHITE=pygame.Color(250,203,156)
RED=pygame.Color(255,0,0)
GREEN=pygame.Color(0,255,0)

white_piece_color=pygame.Color(255,255,255)
black_piece_color=pygame.Color(0,0,0)       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
