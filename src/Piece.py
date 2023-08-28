from abc import ABC
import pygame
from Setup import *
from Board import *

class Piece(ABC):
    def __init__(self,color,square,t,image,moved=False):
        self.x=square.col
        self.y=square.row
        self.color=color
        #self.square=square
        self.t=t #type
        self.image=image
        self.moved=moved
        
        self.squaresAttacking=[] #what squares is this piece attacking
        self.piecesAttacking=[] #what pieces is this piece attacking (friendly included)
        self.piecesAttackedBy=[] #what pieces this piece is being attacked by (friendly included)
    def deepcopy(self):
        return(Piece(self.color,self.square,self.t,self.image,self.moved))
    def set_moved(self):
        self.moved=True
    def set_pos(self,col,row):
        self.x=col
        self.y=row
    def get_attacked_by_pieces(self,piece):
        #passes piece that is moving 
        pass
    def get_moves(self,board,attack=False):
        #if attack =TRUE then return every square that the piece controls, regardless of if it can actually move there or not
        open_squares=[]
        #add a check to see if king is in check first before anything else
        
        #for every move, make sure it doesn't put own king in check
        if self.t=='pawn':

            if self.color==WHITE and self.y-1>-1:
                if not attack:
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
                        #check if on correct square
                        if self.color==WHITE and self.y==6 or self.color==BLACK and self.y==1:
                            try:
                                if board.board[self.x][self.y-2].get_piece()==None: #nobody two squares in front
                                    open_squares.append(board.board[self.x][self.y-2])
                            except:
                                pass
                elif attack: #getting what moves it is attacking
                    try:
                        #attacking left?
                        if board.board[self.x-1][self.y-1].size: #does it exist
                            open_squares.append(board.board[self.x-1][self.y-1])
                    except:
                        pass
                    try:
                        #attacking right?
                        if board.board[self.x+1][self.y-1].size: #does it exist
                            open_squares.append(board.board[self.x+1][self.y-1])
                    except:
                        pass
            if self.color==BLACK and self.y+1<8:
                if not attack:
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
            #return open_squares
     
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

            if a:
                if attack:
                    open_squares.append(a)
                elif not ac or ac!=self.color:
                    open_squares.append(a)
            if b:
                if attack:
                    open_squares.append(b)
                elif not bc or bc!=self.color:
                    open_squares.append(b)  
                
            if c:
                if attack:
                    open_squares.append(c)
                elif not cc or cc!=self.color:
                    open_squares.append(c)
                    
            if d:
                if attack:
                    open_squares.append(d)
                elif not dc or dc!=self.color:
                    open_squares.append(d)
                    
            if e:
                if attack:
                    open_squares.append(e)
                elif not ec or ec!=self.color:
                    open_squares.append(e)
                    
            if f:
                if attack:
                    open_squares.append(f)
                elif not fc or fc!=self.color:
                    open_squares.append(f)
                     
            if g:
                if attack:
                    open_squares.append(g)
                elif not gc or gc!=self.color:
                    open_squares.append(g)
                    
            if h:
                if attack:
                    open_squares.append(h)
                elif not hc or hc!=self.color:
                    open_squares.append(h)
            
              
            #return open_squares
        
        if self.t=='bishop' or self.t=='queen':
            
            counter=1 #how many times thru loop (start at 1)
            #up right
            while True:
                try:
                    if(self.x+counter>-1 and self.x+counter<8 and self.y-counter>-1 and self.y-counter<8): #ensure no out of bounds
                        if(board.board[self.x+counter][self.y-counter].get_piece()!=None):
                            if attack:
                                open_squares.append(board.board[self.x+counter][self.y-counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(board.board[self.x+counter][self.y-counter].get_piece_color()!=self.color):
                                    open_squares.append(board.board[self.x+counter][self.y-counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(board.board[self.x+counter][self.y-counter])
                        counter+=1
                    else: 
                        counter=1
                        break
                except:
                    counter=1
                    break

            #up left
            while True:
                try:
                    if(self.x-counter>-1 and self.x-counter<8 and self.y-counter>-1 and self.y-counter<8): #ensure no out of bounds
                        if(board.board[self.x-counter][self.y-counter].get_piece()!=None):
                            if attack:
                                open_squares.append(board.board[self.x-counter][self.y-counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(board.board[self.x-counter][self.y-counter].get_piece_color()!=self.color):
                                    open_squares.append(board.board[self.x-counter][self.y-counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(board.board[self.x-counter][self.y-counter])
                        counter+=1
                    else:
                        counter=1
                        break
                except:
                    counter=1
                    break

            #down right
            while True:
                try:
                    if(self.x+counter>-1 and self.x+counter<8 and self.y+counter>-1 and self.y+counter<8): #ensure no out of bounds
                        if(board.board[self.x+counter][self.y+counter].get_piece()!=None):
                            if attack:
                                open_squares.append(board.board[self.x+counter][self.y+counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(board.board[self.x+counter][self.y+counter].get_piece_color()!=self.color):
                                    open_squares.append(board.board[self.x+counter][self.y+counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(board.board[self.x+counter][self.y+counter])
                        counter+=1
                    else:
                        counter=1
                        break
                except:
                    counter=1
                    break
            #down left
            while True:
                try:
                    if(self.x-counter>-1 and self.x-counter<8 and self.y+counter>-1 and self.y+counter<8): #ensure no out of bounds
                        if(board.board[self.x-counter][self.y+counter].get_piece()!=None):
                            if attack:
                                open_squares.append(board.board[self.x-counter][self.y+counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(board.board[self.x-counter][self.y+counter].get_piece_color()!=self.color):
                                    open_squares.append(board.board[self.x-counter][self.y+counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(board.board[self.x-counter][self.y+counter])
                        counter+=1
                    else:
                        counter=1
                        break
                except:
                    counter=1
                    break

            #if self.t=='bishop': # this is here because the queen needs both bishop and rook movess
                #return open_squares
            
        if self.t=='rook' or self.t=='queen':
            for i in range(self.y-1,-1,-1): #how many squares up
                if(board.board[self.x][i].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(board.board[self.x][i])
                    else:    
                        if board.board[self.x][i].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(board.board[self.x][i])
                    break #piece can't move thru pieces, so break loop if encounters another piece. add the square to open_squares if opponent's piece
                else:
                    #empty square
                    open_squares.append(board.board[self.x][i])
            for i in range(self.y+1,board.boardLength): #how many squares down
                if(board.board[self.x][i].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(board.board[self.x][i])
                    else:
                        if board.board[self.x][i].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(board.board[self.x][i])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[self.x][i])
            for i in range(self.x+1,board.boardWidth): #how many squares right
                if(board.board[i][self.y].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(board.board[i][self.y])
                    else:
                        if board.board[i][self.y].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(board.board[i][self.y])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[i][self.y])
            for i in range(self.x-1,-1,-1): #how many squares left
                if(board.board[i][self.y].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(board.board[i][self.y])
                    else:
                       if board.board[i][self.y].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(board.board[i][self.y])
                    break
                else:
                    #empty square
                    open_squares.append(board.board[i][self.y])
            
            
            #return open_squares #if queen, already also got bishop moves, so can return
        
        elif self.t=='king':
            #LEFT
            if self.x-1<0: 
                pass
            else:
                #directly left
                if board.board[self.x-1][self.y].get_piece()==None or board.board[self.x-1][self.y].get_piece_color()!=self.color:
                    open_squares.append(board.board[self.x-1][self.y])
                #up left
                if self.y-1>-1:
                    if board.board[self.x-1][self.y-1].get_piece()==None or board.board[self.x-1][self.y-1].get_piece_color()!=self.color:
                        open_squares.append(board.board[self.x-1][self.y-1])
                #down left
                if self.y+1<8:
                    if board.board[self.x-1][self.y+1].get_piece()==None or board.board[self.x-1][self.y+1].get_piece_color()!=self.color:
                        open_squares.append(board.board[self.x-1][self.y+1])
            #RIGHT
            if self.x+1>7: 
                pass
            else:
                #directly right
                if board.board[self.x+1][self.y].get_piece()==None or board.board[self.x+1][self.y].get_piece_color()!=self.color:
                    open_squares.append(board.board[self.x+1][self.y])
                #up right
                if self.y-1>-1:
                    if board.board[self.x+1][self.y-1].get_piece()==None or board.board[self.x+1][self.y-1].get_piece_color()!=self.color:
                        open_squares.append(board.board[self.x+1][self.y-1])
                #down right
                if self.y+1<8:
                    if board.board[self.x+1][self.y+1].get_piece()==None or board.board[self.x+1][self.y+1].get_piece_color()!=self.color:
                        open_squares.append(board.board[self.x+1][self.y+1])
            #DOWN
            if self.y+1>7:
                pass
            else:
                if board.board[self.x][self.y+1].get_piece()==None or board.board[self.x][self.y+1].get_piece_color()!=self.color:
                    open_squares.append(board.board[self.x][self.y+1])
            #UP
            if self.y-1<0:
                pass
            else:
                if board.board[self.x][self.y-1].get_piece()==None or board.board[self.x][self.y-1].get_piece_color()!=self.color:
                    open_squares.append(board.board[self.x][self.y-1])
        
            #CASTLING 
            #TODO might need to add try except clause for potential out of bounds
            if not attack and self.moved==False:
                #King Side
                if board.board[self.x+1][self.y].get_piece()==None and board.board[self.x+2][self.y].get_piece()==None: #if empty spaces
                    if board.board[self.x+3][self.y].get_piece().t=='rook' and board.board[self.x+3][self.y].get_piece().color==self.color and board.board[self.x+3][self.y].get_piece().moved==False: #rook of same color that has not moved
                        open_squares.append(board.board[self.x+2][self.y])
                #Queen Side
                if board.board[self.x-1][self.y].get_piece()==None and board.board[self.x-2][self.y].get_piece()==None and board.board[self.x-3][self.y].get_piece()==None: #if empty spaces
                    if board.board[self.x-4][self.y].get_piece().t=='rook' and board.board[self.x-4][self.y].get_piece().color==self.color and board.board[self.x-4][self.y].get_piece().moved==False: #rook of same color that has not moved
                        open_squares.append(board.board[self.x-2][self.y])
        r'''
        if self.color==WHITE and w_k.inCheck: #if white and white (own king) in check
            pass #doesThisStopCheck(color,open_squares)
        elif self.color==BLACK and b_k.inCheck:
            pass #doesThisStopCheck(color, open_squares)
        #doesThisMovePutOwnKingInCheck(open_squares)
        '''
        #open_squares=checkCheckSquares(open_squares,self.color,board)
        if attack==False:
            self.squaresAttacking=open_squares
        else:
            return open_squares

    
    def get_attacking_squares(self,board):
        r'''
         attacking=[]
         if self.t=='pawn':
             if self.color==WHITE:
                 opp_color=BLACK
                 #up left
                 if self.x-1>-1 and self.y-1>-1 and board.board[self.x-1][self.y-1].get_piece_color()==opp_color:
                     attacking.append(board.board[self.x-1][self.y-1])
                 #up right
                 if self.x+1<8 and self.y-1>-1 and board.board[self.x+1][self.y-1].get_piece_color()==opp_color:
                     attacking.append(board.board[self.x+1][self.y-1])
                 #TODO en passant
         
             else:
                 opp_color=WHITE
                 #down left
                 if self.x-1>-1 and self.y+1<8 and board.board[self.x-1][self.y+1].get_piece_color()==opp_color:
                     attacking.append(board.board[self.x-1][self.y+1])
                 #down right
                 if self.x+1<8 and self.y+1<8 and board.board[self.x+1][self.y+1].get_piece_color()==opp_color:
                     attacking.append(board.board[self.x+1][self.y+1])
                 #TODO en passant
         
             
         else:
             attacking= get_moves(self,board,True)
         '''
        self.squaresAttacking=self.get_moves(board,True)
        return self.squaresAttacking
    r'''
    def get_attacking_pieces(self,board): #get pieces 
        temp=[]
        for square in self.squaresAttacking:
            if square.piece is not None:
                temp.append(square.piece)
        self.piecesAttacking=temp
    '''
class Pawn(Piece):
    def __init__(self,color,square,image):
        self.type='pawn'
        if color==WHITE:
            self.string='Wpawn'
        else:
            self.string='Bpawn'
        super().__init__(color,square,self.type,image)
        
class Knight(Piece):
    def __init__(self,color,square,image):
        self.type='knight'
        if color==WHITE:
            self.string='Wknight'
        else:
            self.string='Bknight'
        super().__init__(color,square,self.type,image)
        
class Bishop(Piece):
    def __init__(self,color,square,image):
        self.type='bishop'
        if color==WHITE:
            self.string='Wbishop'
        else:
            self.string='Bbishop'
        super().__init__(color,square,self.type,image)
        
class Rook(Piece):
    def __init__(self,color,square,image):
        self.type='rook'
        if color==WHITE:
            self.string='Wrook'
        else:
            self.string='Brook'
        self.moved=False
        super().__init__(color,square,self.type,image)
        
class Queen(Piece):
    def __init__(self,color,square,image):
        self.type='queen'
        if color==WHITE:
            self.string='Wqueen'
        else:
            self.string='Bqueen'
        super().__init__(color,square,self.type,image)
        
class King(Piece):
    def __init__(self,color,square,image, inCheck=False):
        self.type='king'
        if color==WHITE:
            self.string='Wking'
        else:
            self.string='Bking'
        self.inCheck=inCheck
        self.moved=False
        super().__init__(color,square,self.type,image)

    
        
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)

#Create Pieces
#get game type somehow 
#for now just traditional set up




#Pieces
##WHITE
w_p=[Pawn(WHITE,board.board[0][6],wpi),Pawn(WHITE,board.board[1][6],wpi),Pawn(WHITE,board.board[2][6],wpi),Pawn(WHITE,board.board[3][6],wpi),
     Pawn(WHITE,board.board[4][6],wpi),Pawn(WHITE,board.board[5][6],wpi),Pawn(WHITE,board.board[6][6],wpi),Pawn(WHITE,board.board[7][6],wpi)]
w_n=[Knight(WHITE,board.board[1][7],wni),Knight(WHITE,board.board[6][7],wni)]
w_b=[Bishop(WHITE,board.board[2][7],wbi),Bishop(WHITE,board.board[5][7],wbi)]
w_r=[Rook(WHITE,board.board[0][7],wri),Rook(WHITE,board.board[7][7],wri)]
w_q=[Queen(WHITE,board.board[3][7],wqi)]
w_k=King(WHITE,board.board[4][7],wki)
w_k_l=[w_k]
w_pieces=w_p+w_n+w_b+w_r+w_q+w_k_l
##BLACK
b_p=[Pawn(BLACK,board.board[0][1],bpi),Pawn(BLACK,board.board[1][1],bpi),Pawn(BLACK,board.board[2][1],bpi),Pawn(BLACK,board.board[3][1],bpi),
     Pawn(BLACK,board.board[4][1],bpi),Pawn(BLACK,board.board[5][1],bpi),Pawn(BLACK,board.board[6][1],bpi),Pawn(BLACK,board.board[7][1],bpi)]
b_n=[Knight(BLACK,board.board[1][0],bni),Knight(BLACK,board.board[6][0],bni)]
b_b=[Bishop(BLACK,board.board[2][0],bbi),Bishop(BLACK,board.board[5][0],bbi)]
b_r=[Rook(BLACK,board.board[0][0],bri),Rook(BLACK,board.board[7][0],bri)]
b_q=[Queen(BLACK,board.board[3][0],bqi)]
b_k=King(BLACK,board.board[4][0],bki)
b_k_l=[b_k]
b_pieces=b_p+b_n+b_b+b_r+b_q+b_k_l


all_pieces=w_pieces+b_pieces #all pieces
#all_pieces=[Pawn(WHITE,board.board[3][1],wpi),Pawn(BLACK,board.board[3][6],bpi),Pawn(WHITE,board.board[4][1],wpi)]
    


r'''
dont update/check open_squares every move
instead at beginning of game, calculate the open_squares (attacking squares)
for all pieces. e.g. b1 knight squares = a3,c3
update b1 knight's open_squares if own piece moves into one of those squares
or when b1 knight moves
different approach for pawns
'''