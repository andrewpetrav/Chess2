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
    
    def original_setup(self,w_pieces,b_pieces):
        w_p=w_pieces[0] #White pawns
        w_n=w_pieces[1] #White knights
        w_b=w_pieces[2] #White bishops
        w_r=w_pieces[3] #White rooks
        w_q=w_pieces[4] #White queen
        w_k=w_pieces[5] #White king
        b_p=b_pieces[0] #Black pawns
        b_n=b_pieces[1] #Black knights
        b_b=b_pieces[2] #Black bishops
        b_r=b_pieces[3] #Black rooks
        b_q=b_pieces[4] #Black queen
        b_k=b_pieces[5] #Black king
        for i in range(0,self.boardWidth):
            #White pawns
            self.board[i][self.boardLength-1].set_piece(w_p[i])
            #Black pawns
            self.board[i][1].set_piece(b_p[i])
        
BLACK=pygame.Color(211,139,67)
WHITE=pygame.Color(250,203,156)
RED=pygame.Color(255,0,0)
GREEN=pygame.Color(0,255,0)

white_piece_color=pygame.Color(255,255,255)
black_piece_color=pygame.Color(0,0,0)       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
