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
    def set_moved(self):
        self.moved=True
    def set_pos(self,x,y):
        self.x=x
        self.y=y
    def get_moves(self,board):
        open_squares=[]
        #add a check to see if king is in check first before anything else
        
        #for every move, make sure it doesn't put own king in check
        if self.t=='pawn':
            if self.color==WHITE:
                oneInFront=board.board[self.x][self.y-1]
                if oneInFront.get_piece()==None: #if nobody on square ahead of it
                    open_squares.append(oneInFront) 
                try:
                    if board.board[self.x-1][self.y-1].get_piece() != None and board.board[self.x-1][self.y-1].get_piece_color()!=self.color: #can take to left?
                        open_squares.append(board.board[self.x-1][self.y-1])
                except:
                    pass
                try:
                    if board.board[self.x+1][self.y-1].get_piece() != None and board.board[self.x+1][self.y-1].get_piece_color()!=self.color: #can take to right?
                        open_squares.append(board.board[self.x+1][self.y-1])
                except:
                    pass
                if self.moved==False: #if first move for pawn
                    try:
                        if board.board[self.x][self.y-2].get_piece()==None: #nobody two squares in front
                            open_squares.append(board.board[self.x][self.y-2])
                    except:
                        pass
            if self.color==BLACK:
                oneInFront=board.board[self.x][self.y+1]
                if oneInFront.get_piece()==None: #if nobody on square ahead of it
                    open_squares.append(oneInFront) 
                try:
                    if board.board[self.x-1][self.y+1].get_piece() != None and board.board[self.x-1][self.y+1].get_piece_color()!=self.color: #can take to left?
                        open_squares.append(board.board[self.x-1][self.y+1])
                except:
                    pass
                try:
                    if board.board[self.x+1][self.y+1].get_piece() != None and board.board[self.x+1][self.y+1].get_piece_color()!=self.color: #can take to right?
                        open_squares.append(board.board[self.x+1][self.y+1])
                except:
                    pass
                if self.moved==False: #if first move for pawn
                    try:
                        if board.board[self.x][self.y+2].get_piece()==None: #nobody two squares in front
                            open_squares.append(board.board[self.x][self.y+2])
                    except:
                        pass
            return open_squares
     
        elif self.t=='knight':
            #open_squares=[]
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
            for i in range(self.x,board.boardLength): #how many squares up
                if(board.board[self.x][self.y-i].get_piece()): #this square holds a piece
                    if board.board[self.x][self.y-i].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x][self.y-i])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x][self.y-i])
            for i in range(self.x,0,-1): #how many squares down
                if(board.board[self.x][self.y-i].get_piece()): #this square holds a piece
                    if board.board[self.x][self.y-i].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x][self.y-i])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x][self.y-i])
            for i in range(self.y,board.boardWidth): #how many squares right
                if(board.board[self.x-i][self.y].get_piece()): #this square holds a piece
                    if board.board[self.x-i][self.y=].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x-i][self.y=])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x-i][self.y])
            for i in range(self.y,0,-1): #how many squares left
                if(board.board[self.x-i][self.y].get_piece()): #this square holds a piece
                    if board.board[self.x-i][self.y=].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x-i][self.y=])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x-i][self.y])
            return open_squares
        elif self.t=='queen':
            #up down left right
            for i in range(self.x,board.boardLength): #how many squares up
                if(board.board[self.x][self.y-i].get_piece()): #this square holds a piece
                    if board.board[self.x][self.y-i].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x][self.y-i])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x][self.y-i])
            for i in range(self.x,0,-1): #how many squares down
                if(board.board[self.x][self.y-i].get_piece()): #this square holds a piece
                    if board.board[self.x][self.y-i].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x][self.y-i])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x][self.y-i])
            for i in range(self.y,board.boardWidth): #how many squares right
                if(board.board[self.x-i][self.y].get_piece()): #this square holds a piece
                    if board.board[self.x-i][self.y=].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x-i][self.y=])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x-i][self.y])
            for i in range(self.y,0,-1): #how many squares left
                if(board.board[self.x-i][self.y].get_piece()): #this square holds a piece
                    if board.board[self.x-i][self.y=].get_piece_color()!=self.color: #if it's the other player's piece
                        open_squares.append(board.board[self.x-i][self.y=])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x-i][self.y])
            # diagonals
            
            
            return open_squares
        elif self.t=='king':
            pass


class Pawn(Piece):
    def __init__(self,color,square,image):
        self.type='pawn'
        super().__init__(color,square,self.type,image)
        
class Knight(Piece):
    def __init__(self,color,square,image):
        self.type='knight'
        super().__init__(color,square,self.type,image)
        
class Bishop(Piece):
    def __init__(self,color,square,image):
        self.type='bishop'
        super().__init__(color,square,self.type,image)
        
class Rook(Piece):
    def __init__(self,color,square,image):
        self.type='rook'
        super().__init__(color,square,self.type,image)
        
class Queen(Piece):
    def __init__(self,color,square,image):
        self.type='queen'
        super().__init__(color,square,self.type,image)
        
class King(Piece):
    def __init__(self,color,square,image):
        self.type='king'
        super().__init__(color,square,self.type,image)

    
        
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)

