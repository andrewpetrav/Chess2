from abc import ABC
import pygame
from Setup import *
from Board import *

class Piece(ABC):
    def __init__(self,color,square,t,image,tag,moved=False):
        self.x=square.col
        self.y=square.row
        self.row=self.y
        self.col=self.x
        self.color=color
        self.square=square
        self.t=t #type
        self.image=image
        self.moved=moved
        self.tag=tag
        self.squaresCanMoveTo=[] #what squares this piece can move to
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
    def get_pos(self):
        return(self.x,self.y)
    def get_attacked_by_pieces(self,piece):
        #passes piece that is moving 
        pass
    def get_moves_string(self,board,attack=False):
        #returns list of open squares in [(row, col), (row, col), ...] form
        open_squares=[]
        #print(board)
        theBoard = [list(row) for row in zip(*board)]
        #print(theBoard)
        c=None #color
        if self.color==WHITE:
            c='W'
        elif self.color==BLACK:
            c='B'
        #add a check to see if king is in check first before anything else
        #for every move, make sure it doesn't put own king in check
        if self.t=='pawn': #TODO Enpassant
            #####PROBLEM IS SOMEWHERE HERE
            if self.color==WHITE and self.y-1>-1: 
                if not attack:
                    if theBoard[self.x][self.y-1]=='*': #if nobody on square ahead of it
                        open_squares.append((self.x,self.y-1)) 
                    try:
                        if theBoard[self.x-1][self.y-1] != '*' and theBoard[self.x-1][self.y-1][0]!=c: #can take to left?
                            open_squares.append((self.x-1,self.y-1))
                    except:

                        pass
                    try:
                        if theBoard[self.x+1][self.y-1] != '*' and theBoard[self.x+1][self.y-1][0]!=c: #can take to right?
                            open_squares.append((self.x+1,self.y-1))
                    except:
                        pass


                    if self.moved==False: #if first move for pawn
                        #check if on correct square
                        if self.color==WHITE and self.y==6 or self.color==BLACK and self.y==1:
                            try:
                                if theBoard[self.x][self.y-2]=='*': #nobody two squares in front
                                    open_squares.append((self.x,self.y-2))
                            except:
                                pass
                elif attack:
                    try:
                        #attacking left?
                        if self.x-1>=0 and self.y-1>=0:#if theBoard[self.x-1][self.y-1].size: #does it exist
                            open_squares.append((self.x-1,self.y-1))
                    except:
                        pass
                    try:
                        #attacking right?
                        if self.x+1<NUM_ROWS and self.y-1>=0: #if theBoard[self.x+1][self.y-1].size: #does it exist
                            open_squares.append((self.x+1,self.y-1))
                    except:
                        pass
            if self.color==BLACK and self.y+1<NUM_ROWS:
                if not attack:
                    if theBoard[self.x][self.y+1]=='*': #if nobody on square ahead of it
                        open_squares.append((self.x,self.y+1)) 
                    try:
                        if theBoard[self.x-1][self.y+1] !='*' and theBoard[self.x-1][self.y+1][0]!=c: #can take to left?
                            open_squares.append((self.x-1,self.y+1))
                    except:
                        pass
                    try:
                        if theBoard[self.x+1][self.y+1] !='*' and theBoard[self.x+1][self.y+1][0]!=c: #can take to right?
                            open_squares.append((self.x+1,self.y+1))
                    except:
                        pass
                    if self.moved==False: #if first move for pawn
                        try:
                            if theBoard[self.x][self.y+2]=='*': #nobody two squares in front
                                open_squares.append((self.x,self.y+2))
                        except:
                            pass
                elif attack:
                    try:
                        #attacking left?
                        if theBoard[self.x-1][self.y+1].size: #does it exist
                            open_squares.append((self.x-1)(self.y-1))
                    except:
                        pass
                    try:
                        #attacking right?
                        if theBoard[self.x+1][self.y+1].size: #does it exist
                            open_squares.append((self.x+1)(self.y-1))
                    except:
                        pass     
        elif self.t=='knight':
            #open_squares=[]
            a,b,c,d,e,f,g,h=None,None,None,None,None,None,None,None
            ac,bc,cc,dc,ec,fc,gc,hc=None,None,None,None,None,None,None,None
            #left 1 up 2
            try:
                if self.x-1<0:
                    a/0
                a=theBoard[self.x-1][self.y+2]
                ac=a[0]
            except:
                pass
            #right 1 up 2
            try:
                b=theBoard[self.x+1][self.y+2]
                bc=b[0]
            except:
                pass
            #right 2 up 1
            try:
                c=theBoard[self.x+2][self.y+1]
                cc=c[0]
            except:
                pass
            #right 2 down 1
            try:
                if self.y-1<0:
                    a/0
                d=theBoard[self.x+2][self.y-1]
                dc=d[0]
            except:
                pass
            #right 1 down 2
            try:
                if self.y-2<0:
                    a/0
                e=theBoard[self.x+1][self.y-2]
                ec=e[0]
            except:
                pass
            #left 1 down 2
            try:
                if self.x-1<0 or self.y-2<0:
                    a/0
                f=theBoard[self.x-1][self.y-2]
                fc=f[0]
            except:
                pass
            #left 2 down 1
            try:
                if self.x-2<0 or self.y-1<0:
                    a/0
                g=theBoard[self.x-2][self.y-1]
                gc=g[0]
            except:
                pass
            #left 2 up 1
            try:
                if self.x-2<0:
                    a/0
                h=theBoard[self.x-2][self.y+1]
                hc=h[0]
            except:
                pass

            if a:
                if attack:
                    open_squares.append((self.x-1,self.y+2))
                elif not ac or ac!=c:
                    open_squares.append((self.x-1,self.y+2))
            if b:
                if attack:
                    open_squares.append((self.x+1,self.y+2)) 
                elif not bc or bc!=c:
                    open_squares.append((self.x+1,self.y+2))      
            if c:
                if attack:
                    open_squares.append((self.x+2,self.y+1))  
                elif not cc or cc!=c:
                    open_squares.append((self.x+2,self.y+1))  
            if d:
                if attack:
                    open_squares.append((self.x+2,self.y-1))  
                elif not dc or dc!=c:
                    open_squares.append((self.x+2,self.y-1))       
            if e:
                if attack:
                    open_squares.append((self.x+1,self.y-2))   
                elif not ec or ec!=c:
                    open_squares.append((self.x+1,self.y-2))             
            if f:
                if attack:
                    open_squares.append((self.x-1,self.y-2))   
                elif not fc or fc!=c:
                    open_squares.append((self.x-1,self.y-2))                     
            if g:
                if attack:
                    open_squares.append((self.x-2,self.y-1))      
                elif not gc or gc!=c:
                    open_squares.append((self.x-2,self.y-1))                    
            if h:
                if attack:
                    open_squares.append((self.x-2,self.y+1))   
                elif not hc or hc!=c:
                    open_squares.append((self.x-2,self.y+1))            
              
            #return open_squares
        if self.t=='bishop' or self.t=='queen':
            counter=1 #how many times thru loop (start at 1)
            #up right
            while True:
                try:
                    if(self.x+counter>-1 and self.x+counter<NUM_ROWS and self.y-counter>-1 and self.y-counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x+counter][self.y-counter]!='*'):
                            if attack:
                                open_squares.append((self.x+counter,self.y-counter))
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(theBoard[self.x+counter][self.y-counter][0]!=c):
                                    open_squares.append((self.x+counter,self.y-counter))
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                            
                        open_squares.append((self.x+counter,self.y-counter))
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
                    if(self.x-counter>-1 and self.x-counter<NUM_ROWS and self.y-counter>-1 and self.y-counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x-counter][self.y-counter]!='*'):
                            if attack:
                                open_squares.append((self.x-counter,self.y-counter))
                                counter=1
                                break
                            else:
                                if(theBoard[self.x-counter][self.y-counter][0]()!=c):
                                    open_squares.append((self.x-counter,self.y-counter))
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append((self.x-counter,self.y-counter))
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
                    if(self.x+counter>-1 and self.x+counter<NUM_ROWS and self.y+counter>-1 and self.y+counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x+counter][self.y+counter]!='*'):
                            if attack:
                                open_squares.append((self.x+counter,self.y+counter))
                                counter=1
                                break
                            else:
                                if(theBoard[self.x+counter][self.y+counter][0]!=c):
                                    open_squares.append((self.x+counter,self.y+counter))
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append((self.x+counter,self.y+counter))
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
                    if(self.x-counter>-1 and self.x-counter<NUM_ROWS and self.y+counter>-1 and self.y+counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x-counter][self.y+counter]!='*'):
                            if attack:
                                open_squares.append(self.x-counter,self.y+counter)
                                counter=1
                                break
                            else:
                                if(theBoard[self.x-counter][self.y+counter][0]!=c):
                                    open_squares.append((self.x-counter,self.y+counter))
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append((self.x-counter,self.y+counter))
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
                if(theBoard[self.x][i]!='*'): #this square holds a piece
                    if attack:
                        open_squares.append((self.x,i))
                    elif theBoard[self.x][i][0]!=c: #if it's the other player's piece
                        open_squares.append((self.x,i))
                    break #piece can't move thru pieces, so break loop if encounters another piece. add the square to open_squares if opponent's piece
                else:
                    #empty square
                    open_squares.append((self.x,i))
            for i in range(self.y+1,len(theBoard)): #how many squares down
                if(theBoard[self.x][i]!='*'): #this square holds a piece
                    if attack:
                        open_squares.append((self.x,i))
                    elif theBoard[self.x][i][0]!=c: #if it's the other player's piece
                        open_squares.append((self.x,i))
                    break
                else:
                    #empty square
                    open_squares.append((self.x,i))
            for i in range(self.x+1,len(theBoard[0])): #how many squares right
                if(theBoard[i][self.y]!='*'): #this square holds a piece
                    if attack:
                        open_squares.append((i,self.y))
                    elif theBoard[i][self.y][0]!=c: #if it's the other player's piece
                        open_squares.append((i,self.y))
                    break
                else:
                    #empty square
                    open_squares.append((i,self.y))
            for i in range(self.x-1,-1,-1): #how many squares left
                if(theBoard[i][self.y]!='*'): #this square holds a piece
                    if attack:
                        open_squares.append((i,self.y))
                    elif theBoard[i][self.y][0]!=c: #if it's the other player's piece
                         open_squares.append((i,self.y))
                    break
                else:
                    #empty square
                    open_squares.append((i,self.y))
            
            
            #return open_squares #if queen, already also got bishop moves, so can return
        elif self.t=='king': #TODO castling
            #LEFT
            if self.x-1<0: 
                pass
            else:
                #directly left
                if theBoard[self.x-1][self.y]=='*' or theBoard[self.x-1][self.y][0]!=c:
                    open_squares.append((self.x-1,self.y))
                #up left
                if self.y-1>-1:
                    if theBoard[self.x-1][self.y-1]=='*' or theBoard[self.x-1][self.y-1][0]!=c:
                        open_squares.append((self.x-1,self.y-1))
                #down left
                if self.y+1<8:
                    if theBoard[self.x-1][self.y+1]=='*' or theBoard[self.x-1][self.y+1][0]!=c:
                        open_squares.append((self.x-1,self.y+1))
            #RIGHT
            if self.x+1>NUM_ROWS-1: 
                pass
            else:
                #directly right
                if theBoard[self.x+1][self.y]=='*' or theBoard[self.x+1][self.y][0]!=c:
                    open_squares.append((self.x+1,self.y))
                #up right
                if self.y-1>-1:
                    if theBoard[self.x+1][self.y-1]=='*' or theBoard[self.x+1][self.y-1][0]!=c:
                        open_squares.append((self.x+1,self.y-1))
                #down right
                if self.y+1<8:
                    if theBoard[self.x+1][self.y+1]=='*' or theBoard[self.x+1][self.y+1][0]!=c:
                        open_squares.append((self.x+1,self.y+1))
            #DOWN
            if self.y+1>NUM_ROWS-1:
                pass
            else:
                if theBoard[self.x][self.y+1]=='*' or theBoard[self.x][self.y+1][0]!=c:
                    open_squares.append((self.x,self.y+1))
            #UP
            if self.y-1<0:
                pass
            else:
                if theBoard[self.x][self.y-1]=='*' or theBoard[self.x][self.y-1][0]!=c:
                    open_squares.append((self.x,self.y-1))
            #CASTLING 
            #TODO might need to add try except clause for potential out of bounds
            #TODO

            r'''
            if self.moved==False:
                #King Side
                if theBoard[self.x+1][self.y]=='*' and theBoard[self.x+2][self.y]=='*': #if empty spaces
                    if theBoard[self.x+3][self.y][1]=='r' and theBoard[self.x+3][self.y][0]==self.color and theBoard[self.x+3][self.y].get_piece().moved==False: #rook of same color that has not moved
                        open_squares.append(theBoard[self.x+2][self.y])
                #Queen Side
                if theBoard[self.x-1][self.y].get_piece()==None and theBoard[self.x-2][self.y].get_piece()==None and theBoard[self.x-3][self.y].get_piece()==None: #if empty spaces
                    if theBoard[self.x-4][self.y].get_piece() and theBoard[self.x-4][self.y].get_piece().t=='rook' and theBoard[self.x-4][self.y].get_piece().color==self.color and theBoard[self.x-4][self.y].get_piece().moved==False: #rook of same color that has not moved
                        open_squares.append(theBoard[self.x-2][self.y])
            '''
        return open_squares
    
    def get_moves(self,board,attack=False,boardStringCopy=None):
        if boardStringCopy==None:
            theBoard=board.board
        else:
            theBoard=boardStringCopy
            if boardStringCopy[self.y][self.x]!=self.tag: #if piece taken in this universe...
                return []
            #if just need (row, col) of each square can move
            return self.get_moves_string(theBoard,attack)
        #if attack =TRUE then return every square that the piece controls, regardless of if it can actually move there or not
        open_squares=[]
        #add a check to see if king is in check first before anything else
        
        #for every move, make sure it doesn't put own king in check
        if self.t=='pawn':
            if self.color==WHITE and self.y-1>-1: #TODO this check does not work for attack=True?
                if not attack:
                    oneInFront=theBoard[self.x][self.y-1]

                    if oneInFront.get_piece()==None: #if nobody on square ahead of it
                        open_squares.append(oneInFront) 
                    try:
                        if theBoard[self.x-1][self.y-1].get_piece() != None and theBoard[self.x-1][self.y-1].get_piece_color()!=self.color: #can take to left?
                            open_squares.append(theBoard[self.x-1][self.y-1])
                    except Exception as e:
                        pass
                    try:
                        if theBoard[self.x+1][self.y-1].get_piece() != None and theBoard[self.x+1][self.y-1].get_piece_color()!=self.color: #can take to right?
                            open_squares.append(theBoard[self.x+1][self.y-1])
                    except Exception as e:
                        pass
                    
                    #EN PASSANT
                    ###RIGHT PASANT
                    try:
                        pieceTryingToPassant=theBoard[self.x+1][self.y].get_piece()
                        if pieceTryingToPassant.type=='pawn':
                            if pieceTryingToPassant.enPassantable:
                                if pieceTryingToPassant.get_piece_color()!=self.color:
                                    open_squares.append(theBoard[self.x+1][self.y+1])
                    except Exception as e:
                        pass
                    ###LEFT PASSANT
                    try:
                        pieceTryingToPassant=theBoard[self.x-1][self.y].get_piece()
                        if pieceTryingToPassant.type=='pawn':
                            if pieceTryingToPassant.enPassantable:
                                if pieceTryingToPassant.get_piece_color()!=self.color:
                                    open_squares.append(theBoard[self.x-1][self.y+1])
                    except Exception as e:
                        pass

                    if self.moved==False: #if first move for pawn
                        #check if on correct square
                        if (self.color==WHITE and self.y==6) or (self.color==BLACK and self.y==1):
                            try:
                                if theBoard[self.x][self.y-2].get_piece()==None: #nobody two squares in front
                                    open_squares.append(theBoard[self.x][self.y-2])
                            except Exception as e:
                                pass
                elif attack: #getting what moves it is attacking
                    try:
                        #attacking left?
                        if theBoard[self.x-1][self.y-1].size: #does it exist
                            open_squares.append(theBoard[self.x-1][self.y-1])
                    except Exception as e:
                        pass
                    try:
                        #attacking right?
                        if theBoard[self.x+1][self.y-1].size: #does it exist
                            open_squares.append(theBoard[self.x+1][self.y-1])
                    except Exception as e:
                        pass
            if self.color==BLACK and self.y+1<NUM_ROWS:
                if not attack:
                    oneInFront=theBoard[self.x][self.y+1]
                    if oneInFront.get_piece()==None: #if nobody on square ahead of it
                        open_squares.append(oneInFront) 
                    try:
                        if theBoard[self.x-1][self.y+1].get_piece() != None and theBoard[self.x-1][self.y+1].get_piece_color()!=self.color: #can take to left?
                            open_squares.append(theBoard[self.x-1][self.y+1])
                    except Exception as e:
                        pass
                    try:
                        if theBoard[self.x+1][self.y+1].get_piece() != None and theBoard[self.x+1][self.y+1].get_piece_color()!=self.color: #can take to right?
                            open_squares.append(theBoard[self.x+1][self.y+1])
                    except Exception as e:
                        pass

                    #EN PASSANT
                    ###RIGHT PASANT
                    try:
                        pieceTryingToPassant=theBoard[self.x+1][self.y].get_piece()
                        if pieceTryingToPassant.type=='pawn':
                            if pieceTryingToPassant.enPassantable:
                                if pieceTryingToPassant.get_piece_color()!=self.color:
                                    open_squares.append(theBoard[self.x+1][self.y-1])
                    except Exception as e:
                        pass
                    ###LEFT PASSANT
                    try:
                        pieceTryingToPassant=theBoard[self.x-1][self.y].get_piece()
                        if pieceTryingToPassant.type=='pawn':
                            if pieceTryingToPassant.enPassantable:
                                if pieceTryingToPassant.get_piece_color()!=self.color:
                                    open_squares.append(theBoard[self.x-1][self.y-1])
                    except Exception as e:
                        pass


                    if self.moved==False: #if first move for pawn
                        try:
                            if theBoard[self.x][self.y+2].get_piece()==None: #nobody two squares in front
                                open_squares.append(theBoard[self.x][self.y+2])
                        except Exception as e:
                            pass
                elif attack: #getting what moves it is attacking
                    try:
                        #attacking left?
                        if theBoard[self.x-1][self.y+1].size: #does it exist
                            open_squares.append(theBoard[self.x-1][self.y+1])
                    except Exception as e:
                        pass
                    try:
                        #attacking right?
                        if theBoard[self.x+1][self.y-1].size: #does it exist
                            open_squares.append(theBoard[self.x+1][self.y+1])
                    except Exception as e:
                        pass
            #return open_squares
        elif self.t=='knight':
            #open_squares=[]
            a,b,c,d,ee,f,g,h=None,None,None,None,None,None,None,None
            ac,bc,cc,dc,ec,fc,gc,hc=None,None,None,None,None,None,None,None
            #left 1 up 2
            try:
                if self.x-1<0:
                    a/0
                a=theBoard[self.x-1][self.y+2]
                ac=a.get_piece_color()
            except Exception as e:
                pass
            #right 1 up 2
            try:
                b=theBoard[self.x+1][self.y+2]
                bc=b.get_piece_color()
            except Exception as e:
                pass
            #right 2 up 1
            try:
                c=theBoard[self.x+2][self.y+1]
                cc=c.get_piece_color()
            except Exception as e:
                pass
            #right 2 down 1
            try:
                if self.y-1<0:
                    a/0
                d=theBoard[self.x+2][self.y-1]
                dc=d.get_piece_color()
            except Exception as e:
                pass
            #right 1 down 2
            try:
                if self.y-2<0:
                    a/0
                ee=theBoard[self.x+1][self.y-2]
                ec=ee.get_piece_color()
            except Exception as e:
                pass
            #left 1 down 2
            try:
                if self.x-1<0 or self.y-2<0:
                    a/0
                f=theBoard[self.x-1][self.y-2]
                fc=f.get_piece_color()
            except Exception as e:
                pass
            #left 2 down 1
            try:
                if self.x-2<0 or self.y-1<0:
                    a/0
                g=theBoard[self.x-2][self.y-1]
                gc=g.get_piece_color()
            except Exception as e:
                pass
            #left 2 up 1
            try:
                if self.x-2<0:
                    a/0
                h=theBoard[self.x-2][self.y+1]
                hc=h.get_piece_color()
            except Exception as e:
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
                    
            if ee:
                if attack:
                    open_squares.append(ee)
                elif not ec or ec!=self.color:
                    open_squares.append(ee)
                    
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
                    if(self.x+counter>-1 and self.x+counter<NUM_ROWS and self.y-counter>-1 and self.y-counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x+counter][self.y-counter].get_piece()!=None):
                            if attack:
                                open_squares.append(theBoard[self.x+counter][self.y-counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(theBoard[self.x+counter][self.y-counter].get_piece_color()!=self.color):
                                    open_squares.append(theBoard[self.x+counter][self.y-counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                            
                        open_squares.append(theBoard[self.x+counter][self.y-counter])
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
                    if(self.x-counter>-1 and self.x-counter<NUM_ROWS and self.y-counter>-1 and self.y-counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x-counter][self.y-counter].get_piece()!=None):
                            if attack:
                                open_squares.append(theBoard[self.x-counter][self.y-counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(theBoard[self.x-counter][self.y-counter].get_piece_color()!=self.color):
                                    open_squares.append(theBoard[self.x-counter][self.y-counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(theBoard[self.x-counter][self.y-counter])
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
                    if(self.x+counter>-1 and self.x+counter<NUM_ROWS and self.y+counter>-1 and self.y+counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x+counter][self.y+counter].get_piece()!=None):
                            if attack:
                                open_squares.append(theBoard[self.x+counter][self.y+counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(theBoard[self.x+counter][self.y+counter].get_piece_color()!=self.color):
                                    open_squares.append(theBoard[self.x+counter][self.y+counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(theBoard[self.x+counter][self.y+counter])
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
                    if(self.x-counter>-1 and self.x-counter<NUM_ROWS and self.y+counter>-1 and self.y+counter<NUM_ROWS): #ensure no out of bounds
                        if(theBoard[self.x-counter][self.y+counter].get_piece()!=None):
                            if attack:
                                open_squares.append(theBoard[self.x-counter][self.y+counter])
                                counter=1
                                break #ARE THESE BREAK STATEMENTS PROBLEMATIC?
                            else:
                                if(theBoard[self.x-counter][self.y+counter].get_piece_color()!=self.color):
                                    open_squares.append(theBoard[self.x-counter][self.y+counter])
                                    counter=1
                                    break
                                else: #square has piece of same color, so break
                                    counter=1
                                    break
                        open_squares.append(theBoard[self.x-counter][self.y+counter])
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
                if(theBoard[self.x][i].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(theBoard[self.x][i])
                    else:    
                        if theBoard[self.x][i].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(theBoard[self.x][i])
                    break #piece can't move thru pieces, so break loop if encounters another piece. add the square to open_squares if opponent's piece
                else:
                    #empty square
                    open_squares.append(theBoard[self.x][i])
            for i in range(self.y+1,board.boardLength): #how many squares down
                if(theBoard[self.x][i].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(theBoard[self.x][i])
                    else:
                        if theBoard[self.x][i].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(theBoard[self.x][i])
                    break
                else:
                    #empty square
                    open_squares.append(theBoard[self.x][i])
            for i in range(self.x+1,board.boardWidth): #how many squares right
                if(theBoard[i][self.y].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(theBoard[i][self.y])
                    else:
                        if theBoard[i][self.y].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(theBoard[i][self.y])
                    break
                else:
                    #empty square
                    open_squares.append(theBoard[i][self.y])
            for i in range(self.x-1,-1,-1): #how many squares left
                if(theBoard[i][self.y].get_piece()!=None): #this square holds a piece
                    if attack:
                        open_squares.append(theBoard[i][self.y])
                    else:
                       if theBoard[i][self.y].get_piece_color()!=self.color: #if it's the other player's piece
                            open_squares.append(theBoard[i][self.y])
                    break
                else:
                    #empty square
                    open_squares.append(theBoard[i][self.y])
            
            
            #return open_squares #if queen, already also got bishop moves, so can return
        
        elif self.t=='king':
            #LEFT
            if self.x-1<0: 
                pass
            else:
                #directly left
                if not attack and (theBoard[self.x-1][self.y].get_piece()==None or theBoard[self.x-1][self.y].get_piece_color()!=self.color):
                    open_squares.append(theBoard[self.x-1][self.y])

                elif attack:
                    open_squares.append(theBoard[self.x-1][self.y])
                #up left
                if self.y-1>-1:
                    if not attack and (theBoard[self.x-1][self.y-1].get_piece()==None or theBoard[self.x-1][self.y-1].get_piece_color()!=self.color):
                        open_squares.append(theBoard[self.x-1][self.y-1])

                    elif attack:
                        open_squares.append(theBoard[self.x-1][self.y-1])
                #down left
                if self.y+1<NUM_ROWS:
                    if not attack and (theBoard[self.x-1][self.y+1].get_piece()==None or theBoard[self.x-1][self.y+1].get_piece_color()!=self.color):
                        open_squares.append(theBoard[self.x-1][self.y+1])

                    elif attack:
                        open_squares.append(theBoard[self.x-1][self.y+1])
            #RIGHT
            if self.x+1>NUM_ROWS-1: 
                pass
            else:
                #directly right
                if not attack and (theBoard[self.x+1][self.y].get_piece()==None or theBoard[self.x+1][self.y].get_piece_color()!=self.color):
                    open_squares.append(theBoard[self.x+1][self.y])

                elif attack:
                    open_squares.append(theBoard[self.x+1][self.y])
                #up right
                if self.y-1>-1:
                    if not attack and (theBoard[self.x+1][self.y-1].get_piece()==None or theBoard[self.x+1][self.y-1].get_piece_color()!=self.color):
                        open_squares.append(theBoard[self.x+1][self.y-1])

                    elif attack:
                        open_squares.append(theBoard[self.x+1][self.y-1])
                #down right
                if self.y+1<NUM_ROWS:
                    if not attack and (theBoard[self.x+1][self.y+1].get_piece()==None or theBoard[self.x+1][self.y+1].get_piece_color()!=self.color):
                        open_squares.append(theBoard[self.x+1][self.y+1])
                    elif attack:
                        open_squares.append(theBoard[self.x+1][self.y+1])
            #DOWN
            if self.y+1>NUM_ROWS-1:
                pass
            else:
                if not attack and (theBoard[self.x][self.y+1].get_piece()==None or theBoard[self.x][self.y+1].get_piece_color()!=self.color):
                    open_squares.append(theBoard[self.x][self.y+1])
                    
                elif attack:
                    open_squares.append(theBoard[self.x][self.y+1])
            #UP
            if self.y-1<0:
                pass
            else:
                if not attack and (theBoard[self.x][self.y-1].get_piece()==None or theBoard[self.x][self.y-1].get_piece_color()!=self.color):
                    open_squares.append(theBoard[self.x][self.y-1])
                elif attack:
                    open_squares.append(theBoard[self.x][self.y-1])
        
            #CASTLING 
            #TODO might need to add try except clause for potential out of bounds
            try:
                if not attack and self.moved==False:
                    #WHITE
                    if self.color==WHITE:
                        #King Side
                        if theBoard[self.x+1][self.y].get_piece()==None and theBoard[self.x+2][self.y].get_piece()==None:  #if not being attacked
                            if theBoard[self.x+1][self.y].isAttackedBlack==False and theBoard[self.x+2][self.y].isAttackedBlack==False: #if empty spaces
                                if theBoard[self.x+3][self.y].get_piece() and theBoard[self.x+3][self.y].get_piece().t=='rook' and theBoard[self.x+3][self.y].get_piece().color==self.color and theBoard[self.x+3][self.y].get_piece().moved==False: #rook of same color that has not moved
                                    open_squares.append(theBoard[self.x+2][self.y])
                        #Queen Side
                        if theBoard[self.x-1][self.y].get_piece()==None and theBoard[self.x-2][self.y].get_piece()==None and theBoard[self.x-3][self.y].get_piece()==None: #if empty spaces
                            if theBoard[self.x-1][self.y].isAttackedBlack==False and theBoard[self.x-2][self.y].isAttackedBlack==False and theBoard[self.x-3][self.y].isAttackedBlack==False: #if not being attacked
                                if theBoard[self.x-4][self.y].get_piece() and theBoard[self.x-4][self.y].get_piece().t=='rook' and theBoard[self.x-4][self.y].get_piece().color==self.color and theBoard[self.x-4][self.y].get_piece().moved==False: #rook of same color that has not moved
                                    open_squares.append(theBoard[self.x-2][self.y])
                    #BLACK
                    elif self.color==BLACK:
                        #King Side
                        if theBoard[self.x+1][self.y].get_piece()==None and theBoard[self.x+2][self.y].get_piece()==None:  #if not being attacked
                            if theBoard[self.x+1][self.y].isAttackedWhite==False and theBoard[self.x+2][self.y].isAttackedWhite==False: #if empty spaces
                                if theBoard[self.x+3][self.y].get_piece() and theBoard[self.x+3][self.y].get_piece().t=='rook' and theBoard[self.x+3][self.y].get_piece().color==self.color and theBoard[self.x+3][self.y].get_piece().moved==False: #rook of same color that has not moved
                                    open_squares.append(theBoard[self.x+2][self.y])
                        #Queen Side
                        if theBoard[self.x-1][self.y].get_piece()==None and theBoard[self.x-2][self.y].get_piece()==None and theBoard[self.x-3][self.y].get_piece()==None: #if empty spaces
                            if theBoard[self.x-1][self.y].isAttackedWhite==False and theBoard[self.x-2][self.y].isAttackedWhite==False and theBoard[self.x-3][self.y].isAttackedWhite==False: #if not being attacked
                                if theBoard[self.x-4][self.y].get_piece() and theBoard[self.x-4][self.y].get_piece().t=='rook' and theBoard[self.x-4][self.y].get_piece().color==self.color and theBoard[self.x-4][self.y].get_piece().moved==False: #rook of same color that has not moved
                                    open_squares.append(theBoard[self.x-2][self.y])
            except Exception as e:
                pass
                #print(e)
                r'''
                #King Side
                if theBoard[self.x+1][self.y].get_piece()==None and theBoard[self.x+2][self.y].get_piece()==None: #if empty spaces
                    if theBoard[self.x+3][self.y].get_piece() and theBoard[self.x+3][self.y].get_piece().t=='rook' and theBoard[self.x+3][self.y].get_piece().color==self.color and theBoard[self.x+3][self.y].get_piece().moved==False: #rook of same color that has not moved
                        open_squares.append(theBoard[self.x+2][self.y])
                #Queen Side
                if theBoard[self.x-1][self.y].get_piece()==None and theBoard[self.x-2][self.y].get_piece()==None and theBoard[self.x-3][self.y].get_piece()==None: #if empty spaces
                    if theBoard[self.x-4][self.y].get_piece() and theBoard[self.x-4][self.y].get_piece().t=='rook' and theBoard[self.x-4][self.y].get_piece().color==self.color and theBoard[self.x-4][self.y].get_piece().moved==False: #rook of same color that has not moved
                        open_squares.append(theBoard[self.x-2][self.y])
                '''
        r'''
        if self.color==WHITE and w_k.inCheck: #if white and white (own king) in check
            pass #doesThisStopCheck(color,open_squares)
        elif self.color==BLACK and b_k.inCheck:
            pass #doesThisStopCheck(color, open_squares)
        #doesThisMovePutOwnKingInCheck(open_squares)
        '''
        #open_squares=checkCheckSquares(open_squares,self.color,board)
        if attack==False:
            #self.squaresCanMoveTo=None
            self.squaresCanMoveTo=open_squares
        elif attack==True:
            #self.squaresAttacking=None
            self.squaresAttacking=open_squares
            return open_squares #not 100% sure why this is here
    
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
    def __init__(self,color,square,image,tag):
        self.type='pawn'
        if color==WHITE:
            self.string='Wpawn'
        else:
            self.string='Bpawn'
        self.enPassantable=False
        super().__init__(color,square,self.type,image,tag)
        
class Knight(Piece):
    def __init__(self,color,square,image,tag):
        self.type='knight'
        if color==WHITE:
            self.string='Wnight'
        else:
            self.string='Bnight'
        super().__init__(color,square,self.type,image,tag)
        
class Bishop(Piece):
    def __init__(self,color,square,image,tag):
        self.type='bishop'
        if color==WHITE:
            self.string='Wbishop'
        else:
            self.string='Bbishop'
        super().__init__(color,square,self.type,image,tag)
        
class Rook(Piece):
    def __init__(self,color,square,image,tag):
        self.type='rook'
        if color==WHITE:
            self.string='Wrook'
        else:
            self.string='Brook'
        self.moved=False
        super().__init__(color,square,self.type,image,tag)
        
class Queen(Piece):
    def __init__(self,color,square,image,tag):
        self.type='queen'
        if color==WHITE:
            self.string='Wqueen'
        else:
            self.string='Bqueen'
        super().__init__(color,square,self.type,image,tag)
        
class King(Piece):
    def __init__(self,color,square,image,tag,inCheck=False):
        self.type='king'
        if color==WHITE:
            self.string='Wking'
        else:
            self.string='Bking'
        self.inCheck=inCheck
        self.moved=False
        super().__init__(color,square,self.type,image,tag)

    
        
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)

#Create Pieces
#get game type somehow 
#for now just traditional set up







r'''
dont update/check open_squares every move
instead at beginning of game, calculate the open_squares (attacking squares)
for all pieces. e.g. b1 knight squares = a3,c3
update b1 knight's open_squares if own piece moves into one of those squares
or when b1 knight moves
different approach for pawns
'''
