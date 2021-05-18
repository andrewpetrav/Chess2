from abc import ABC
import pygame
from Surface import square_size


class Piece(ABC):
    def __init__(self,color,square,t,image,moved=False):
        self.x=square.x
        self.y=square.y
        self.color=color
        self.square=square
        self.t=t #type
        self.image=image
        self.moved=moved
        self.isAttacking=[] #same as open_squares+friendly pieces
        self.isAttackedBy=[] #what pieces are attacking this piece
    def get_moves(self,board):
        open_squares=[]
        if self.t=='pawn':
            if self.color==WHITE:
                pass
        elif self.t=='knight':
            open_squares=[]
            a,b,c,d,e,f,g,h=None,None,None,None,None,None,None,None
            ac,bc,cc,dc,ec,fc,gc,hc=None,None,None,None,None,None,None,None
            #left 1 up 2
            try:
                if self.x-1<0:
                    a/0
                a=board.board[self.x-1][self.y+2]
                ac=a.get_piece_color()
            except:
                pass
            #right 1 up 2
            try:
                b=board.board[self.x+1][self.y+2]
                bc=b.get_piece_color()
            except:
                pass
            #right 2 up 1
            try:
                c=board.board[self.x+2][self.y+1]
                cc=c.get_piece_color()
            except:
                pass
            #right 2 down 1
            try:
                if self.y-1<0:
                    a/0
                d=board.board[self.x+2][self.y-1]
                dc=d.get_piece_color()
            except:
                pass
            #right 1 down 2
            try:
                if self.y-2<0:
                    a/0
                e=board.board[self.x+1][self.y-2]
                ec=e.get_piece_color()
            except:
                pass
            #left 1 down 2
            try:
                if self.x-1<0 or self.y-2<0:
                    a/0
                f=board.board[self.x-1][self.y-2]
                fc=f.get_piece_color()
            except:
                pass
            #left 2 down 1
            try:
                if self.x-2<0 or self.y-1<0:
                    a/0
                g=board.board[self.x-2][self.y-1]
                gc=g.get_piece_color()
            except:
                pass
            #left 2 up 1
            try:
                if self.x-2<0:
                    a/0
                h=board.board[self.x-2][self.y+1]
                hc=h.get_piece_color()
            except:
                pass
    
            if a and (not ac or ac!=self.color):
                open_squares.append(a)
            if b and (not bc or bc!=self.color):
                open_squares.append(b)
            if c and (not cc or cc!=self.color):
                open_squares.append(c)
            if d and (not dc or dc!=self.color):
                open_squares.append(d)
            if e and (not ec or ec!=self.color):
                open_squares.append(e)
            if f and (not fc or fc!=self.color):
                open_squares.append(f)
            if g and (not gc or gc!=self.color):
                open_squares.append(g)
            if h and (not hc or hc!=self.color):
                open_squares.append(h)
            return open_squares
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
        
class Knight(Piece):
    def __init__(self,color,square,image):
        super(Knight,self).__init__(color,square,'knight',image)
        
class Bishop(Piece):
    def __init__(self,color,square,image):
        super(Bishop,self).__init__(color,square,'bishop',image)
        
class Rook(Piece):
    def __init__(self,color,square,image):
        super(Rook,self).__init__(color,square,'rook',image)
        
class Queen(Piece):
    def __init__(self,color,square,image):
        super(Queen,self).__init__(color,square,'queen',image)
        
class King(Piece):
    def __init__(self,color,square,image):
        super(King,self).__init__(color,square,'king',image)

    
        
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)

