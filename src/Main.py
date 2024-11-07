#Alright Andrew, let's do this
#Im adding this comment for a test commit
import pygame, sys
import pygame_menu
import copy
import time
from pygame.locals import *
import Board
from Board import *
import Piece
from Piece import *
from Surface import SURFACE
from Setup import *
import pickle
from pynput import keyboard


pygame.init()

#GLOBAL VARIABLES HERE
boardString=[
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*']
    ]
#Pieces
##WHITE
w_k=King(WHITE,board.board[0][2],wki,'Wking')
w_q=Queen(WHITE,board.board[0][1],wqi,'Wqueen')
w_p=Pawn(WHITE,board.board[1][2],wpi,'Wpawn')
b_q=Queen(BLACK,board.board[0][0],bqi,'Bqueen')
b_k=King(BLACK,board.board[3][0],bki,'Bking')

w_pieces=[w_k]+[w_q]+[w_p]
b_pieces=[b_q]+[b_k]

r'''
w_p=[Pawn(WHITE,board.board[0][6],wpi),Pawn(WHITE,board.board[1][6],wpi),Pawn(WHITE,board.board[2][6],wpi),Pawn(WHITE,board.board[3][6],wpi),
     Pawn(WHITE,board.board[4][6],wpi),Pawn(WHITE,board.board[5][6],wpi),Pawn(WHITE,board.board[6][6],wpi),Pawn(WHITE,board.board[7][6],wpi)]
w_n=[Knight(WHITE,board.board[1][7],wni),Knight(WHITE,board.board[6][7],wni)]
w_b=[Bishop(WHITE,board.board[2][7],wbi),Bishop(WHITE,board.board[5][7],wbi)]
w_r=[Rook(WHITE,board.board[0][7],wri),Rook(WHITE,board.board[7][7],wri)]
w_q=[Queen(WHITE,board.board[3][7],wqi)]
w_k=King(WHITE,board.board[4][7],wki)
w_k_l=[w_k]
w_pieces=w_p+w_n+w_b+w_r+w_q+w_k_l
'''

#BLACK
r'''
b_p=[Pawn(BLACK,board.board[0][1],bpi),Pawn(BLACK,board.board[1][1],bpi),Pawn(BLACK,board.board[2][1],bpi),Pawn(BLACK,board.board[3][1],bpi),
     Pawn(BLACK,board.board[4][1],bpi),Pawn(BLACK,board.board[5][1],bpi),Pawn(BLACK,board.board[6][1],bpi),Pawn(BLACK,board.board[7][1],bpi)]
b_n=[Knight(BLACK,board.board[1][0],bni),Knight(BLACK,board.board[6][0],bni)]
b_b=[Bishop(BLACK,board.board[2][0],bbi),Bishop(BLACK,board.board[5][0],bbi)]
b_r=[Rook(BLACK,board.board[0][0],bri),Rook(BLACK,board.board[7][0],bri)]
b_q=[Queen(BLACK,board.board[3][0],bqi)]
b_k=King(BLACK,board.board[4][0],bki)
b_k_l=[b_k]
b_pieces=b_p+b_n+b_b+b_r+b_q+b_k_l
'''

all_pieces=w_pieces+b_pieces #all pieces
#all_pieces=[Pawn(WHITE,board.board[3][1],wpi),Pawn(BLACK,board.board[3][6],bpi),Pawn(WHITE,board.board[4][1],wpi)]
    
def main():
    #Get board in original state
    ##game_type('traditional') #for now, all games will be traditional
    #board.test(Rook(WHITE,board.board[4][4],wri))
    board.setup(all_pieces) #add board parameter based on board selection
    for row in board.board:
        for square in row:
            if square.piece: #if there's a piece there update it from a '*' to name of color+Piece, otherwise ignore it (ie keep as '*')
                #if square.piece.color==WHITE: color='W'
                #elif square.piece.color==BLACK: color='B'
                boardString[square.row][square.col]=square.piece.string
    board.draw_board()
    pygame.display.update()
    game()
    
def select_square(turn,pos):
    piece_selected=False #is a piece selected
    while not piece_selected:
        #print(pos) #pos of click
        x=int(pos[0]/square_size)
        y=int(pos[1]/square_size)
        try:
            if board.board[x][y].get_piece() and board.board[x][y].get_piece_color()==turn:
                return board.board[x][y]
            else:
                return None
        except:
            return None
        

def move_piece(sq,moves,pos,b,returnPieceTaken=False):
    global w_pieces
    global b_pieces
    global all_pieces
    global boardString
    #pos is where you are moving the piece to 
    moved=False
    while not moved:
        col=int(pos[0]/square_size)
        row=int(pos[1]/square_size)
        current_piece=b.board[col][row].piece
        #=int(pos[0]/square_size)
        try:
            if b.board[col][row] in moves:
                #Special moves such as promotion, castling, en passant, that involve changing more than one piece (not counting captures) or image of piece (promotion)
                
                #CASTLING
                if sq.piece.type =='king' and abs(col-sq.col)>1:
                    sq.piece.set_moved() #set king moved
                    #SHORT
                    if col-sq.col>0:
                        boardString[row][5]=boardString[row][7]
                        boardString[row][6]=boardString[row][4]
                        boardString[row][7]='*'
                        boardString[row][4]='*'


                        sq.piece.set_pos(6,row) #update what position king will be on
                        b.board[7][row].piece.set_pos(5,row) #update what position rook will be on
                        b.board[7][row].piece.set_moved() #set rook moved
                        b.board[5][row].set_piece(board.board[7][row].piece)
                        b.board[7][row].set_piece(None)
                        b.board[6][row].set_piece(sq.piece)
                        sq.set_piece(None)

                    #LONG
                    else:
                        boardString[row][3]=boardString[row][0]
                        boardString[row][2]=boardString[row][4]
                        boardString[row][0]='*'
                        boardString[row][4]='*'


                        sq.piece.set_pos(2,row) #update what position king will be on
                        b.board[0][row].piece.set_pos(3,row) #update what position rook will be on
                        b.board[0][row].piece.set_moved() #set rook moved
                        b.board[3][row].set_piece(board.board[0][row].piece)
                        b.board[0][row].set_piece(None)
                        b.board[2][row].set_piece(sq.piece)
                        sq.set_piece(None)
                    return True
                #EN PASSANT
                r'''
                if ((col-1>=0 and b.board[col-1][row].piece.type=='pawn' and b.board[col-1][row].piece.lastMovedPiece==True) or 
                (col+1<=7 and b.board[col+1][row].piece.type=='pawn' and b.board[col+1][row].piece.lastMovedPiece==True)):
                    pass
                '''
                
                #PROMOTION
                if sq.piece.type=='pawn' and (row==0 or row==NUM_ROWS-1):
                    if (row==0 and sq.piece.color==WHITE) or (row==NUM_ROWS-1 and sq.piece.color==BLACK): 
                        returnVal=promotionScreen(sq.piece.color,col,row)
                        if returnVal==None:
                            return False
                        else:
                            boardString[sq.piece.y][sq.piece.x]='*'

                            all_pieces.remove(b.board[col][row].piece)
                            if sq.piece.color==WHITE:
                                b_pieces.remove(b.board[col][row].piece)
                            elif sq.piece.color==BLACK:
                                w_pieces.remove(b.board[col][row].piece)
                            b.board[col][row].set_piece(returnVal)
                            sq.set_piece(None)
                        return True
                    
                #NOT SPECIAL
                else:
                    #CAPTURING
                    if current_piece is not None:
                        if current_piece.color==WHITE:
                            w_pieces.remove(current_piece)
                        elif current_piece.color==BLACK:
                            b_pieces.remove(current_piece)
                            
                    boardString[row][col]=boardString[sq.piece.y][sq.piece.x]
                    boardString[sq.piece.y][sq.piece.x]='*'
                    sq.piece.set_moved()
                    sq.piece.set_pos(col,row) #update what position it'll be on
                    b.board[col][row].set_piece(sq.piece)
                    sq.set_piece(None)
                    


                return True
            else:
                return False
        except Exception as e:   
            return False
    return True

def promotionScreen(color,col,row):
    #INPUT: color of piece
    #ACTION: Display screen of possible promotions, including a cancel button
    #OUTPUT: selection
    #while(True):
    if(color==WHITE):
        images=[wqi,wri,wbi,wni]
    elif color==BLACK:
        images=[bqi,bri,bbi,bni]
    
    pygame.draw.rect(SURFACE,GREEN,pygame.Rect(200, 200, 400, 400))
      
    pygame.draw.rect(SURFACE,RED,pygame.Rect(215, 250, wqi.get_width()+10, wqi.get_height()+10),width=2)
    SURFACE.blit(images[0],(220,255))
        
    pygame.draw.rect(SURFACE,RED,pygame.Rect(345, 250, wri.get_width()+10, wri.get_height()+10),width=2)
    SURFACE.blit(images[1],(350,255))
        
    pygame.draw.rect(SURFACE,RED,pygame.Rect(475, 250, wbi.get_width()+10, wbi.get_height()+10),width=2)
    SURFACE.blit(images[2],(480,255))
        
    pygame.draw.rect(SURFACE,RED,pygame.Rect(215, 380, wni.get_width()+10, wni.get_height()+10),width=2)
    SURFACE.blit(images[3],(220,385))
        
    pygame.draw.rect(SURFACE,RED,pygame.Rect(345, 380, 2*(wni.get_width()+10)+20, wni.get_height()+10),width=2)
    SURFACE.blit(font.render('CANCEL',True,BLACK),(350,410))

        
    pygame.display.update()
    selectionMade=False
    while(not selectionMade):
        #TODO Optimize and account for different res sizes
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if pos[0]>=215 and pos[0]<=325 and pos[1]>=250 and pos[1]<=360:
                    return(Queen(color,board.board[col][row],images[0]))
                elif pos[0]>=345 and pos[0]<=455 and pos[1]>=250 and pos[1]<=360:
                    return(Rook(color,board.board[col][row],images[1]))
                elif pos[0]>=475 and pos[0]<=585 and pos[1]>=250 and pos[1]<=360:
                    return(Bishop(color,board.board[col][row],images[2]))
                elif pos[0]>=215 and pos[0]<=325 and pos[1]>=380 and pos[1]<=490:
                    return(Knight(color,board.board[col][row],images[3]))
                elif pos[0]>=345 and pos[0]<=575 and pos[1]>=380 and pos[1]<=490:
                    return None

def get_all_moves(): #calculates every possible move 
    global all_pieces
    all_moves={} #piece: all the moves it can make
    #should each square hold the data about who is attacking it? or just
    #what color
    for piece in all_pieces:
        all_moves[piece]=piece.get_moves(board)

def kingInCheck(color,boardStringCopy,king,pieces,step0=False,pieceIsKing=False,kingMove=None):
    r'''
    if kingMove is not None:
        print('king is at: ',kingMove.col,kingMove.row)
        kingMove=tuple([kingMove.col,kingMove.row])
    '''
    if pieceIsKing:
        kingPos=tuple([kingMove.col,kingMove.row])
    else:
        kingPos=king.get_pos()
        kingPos=tuple([kingPos[0],kingPos[1]])
    if step0:
        for p in pieces:
            for m in p.squaresAttacking:
                if tuple([m.col,m.row])==kingPos:
                    return True
        return False
    else:
        for p in pieces:
            for m in p.get_moves(board,True,boardStringCopy):
                r'''
                for b in boardStringCopy:
                    print(b)
                print(p.t,m[0],m[1])
                '''
                if m==kingPos:
                    return True
        return False

def doesThisMovePutTheKingInCheck(color,piece,moves,pieces,king,pieceIsKing=False):
    movesLegal=[]
    for move in moves: #iterate through each move that selected piece can make
        #print(type(move))
        boardStringCopy=copy.deepcopy(boardString)
        #print((piece.y,piece.x),(move.col,move.row))
        boardStringCopy[piece.y][piece.x]='*' #set old square as empty
        boardStringCopy[move.row][move.col]=piece.string #move piece to new square #THIS USED TO BE ROW THEN COL, BUT BROKE PIECES BLOCKING CHECK
        doesThisMoveResultInCheck=kingInCheck(color, boardStringCopy,king,pieces,step0=False,pieceIsKing=pieceIsKing,kingMove=move)
        if doesThisMoveResultInCheck: #if moving this piece to LOCATION results in self-check
            pass #don't add it to legal moves
        else: #otherwise
            movesLegal.append(move)  #add to legal moves

    return movesLegal

        
        
    #print(pieces)

def checkForCheck(piece,moves,color,pos,pieces,king):
    #returns moves the would not result in self-check
    r'''
    moves=doesThisMovePutTheKingInCheck(color,piece,moves, pieces, king)
    return moves
    '''
    #TODO: add checks for castling (both ways)
    fap='myBoner'
    if fap != 'myBoner':#if piece.t=='king':
        moves2=[]
        illegalSquares=[] #holds squares being attacked by other side
        for p in pieces:
            if p.squaresAttacking !=[]:
                for sA in p.squaresAttacking:
                    if sA not in illegalSquares:
                        illegalSquares.append(sA)
        for move in moves:
            if move not in illegalSquares:
                moves2.append(move)
            else:
                pass
        moves=moves2
    #if piece is a king, so when do king.get_pos() later, returns temporary position
    if piece.t=='king':
        moves=doesThisMovePutTheKingInCheck(color,piece,moves, pieces, king,True)
    #if piece not a king
    else:
        #if move happens will board state result in your color king check
        moves=doesThisMovePutTheKingInCheck(color,piece,moves, pieces, king)

    return moves
    
def on_press(key):

    if key == keyboard.Key.esc:
        try:
            sys.exit()
            quit()
        except:
            pass
            r'''print(sys.exc_info()[0])'''
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

def game():
    global w_pieces
    global b_pieces
    global all_pieces
    turn=WHITE
    king=w_k
    pieces=b_pieces

    r'''
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys
    '''
    while True:
        move_completed=False #if true, give control to other player
        #king_in_check=Piece.King.kingCheck(turn) #is the king currently in check
        #Step 0: Get move of every piece on board
        for piece in all_pieces:
            piece.get_moves(board)
            piece.get_moves(board,attack=True)
            #print(piece.color,piece.t)
            #for m in piece.squaresAttacking:
                #print(m.col,m.row)

        
        #Step 0.5: Check if own king is in check
        if kingInCheck(turn,boardString,king,pieces,True,False,None):
            if turn==pygame.Color(255,255,255):
                a='WHITE'
            else:
                a='BLACK'
            print(a,' KING IS IN CHECK')
        while not move_completed:
            valid_square_selection=False 
            valid_move_selection=False
            
            #Step 1: Loop until valid square selected to move
            while not valid_square_selection:
                for event in pygame.event.get():
                    if event.type==MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()
                        sq=select_square(turn,pos)
                        if sq: #if valid square
                            valid_square_selection=True
                            break
            #Step 2: Get moves of piece and highlight
            moves=sq.piece.squaresCanMoveTo#get_moves(board) #get moves of piece at selected square
            moves=checkForCheck(sq.piece,moves,turn,pos,pieces,king)
            sq.set_selected()
        
            if moves: #highlight
                for move in moves:
                    move.set_highlighted() #make sure to unhighlight
            board.draw_board()
            #print(boardString)
            pygame.display.update()
            loop_completed=False
            
            #sq.piece.get_attacking_squares(board)
            #sq.piece.get_attacking_pieces(board)
            #Step 3: Loop until valid square selected to move to - if invalid square selected, back to Step 1
            while not valid_move_selection and not loop_completed:
                for event in pygame.event.get():
                    if event.type==MOUSEBUTTONUP:
                        pos=pygame.mouse.get_pos()
                        valid_move_selection=move_piece(sq,moves,pos,board) #clicked valid square
                        if valid_move_selection:
                            move_completed=True
                        loop_completed=True
                        break
            if moves: #unhighlight
                for move in moves:
                    move.set_highlighted()
            sq.set_selected()
            board.draw_board()
            pygame.display.update()
            
            
            #move_piece(sq,moves)
            #move completed
        #Step 4: Switch turns
        #switch turns
        if turn==WHITE:
            turn=BLACK
            king=b_k
            pieces=w_pieces
        else:
            turn=WHITE
            king=w_k
            pieces=b_pieces
        #Step 5: Update Pieces
        all_pieces=w_pieces+b_pieces

        r'''   visualize boardString
        for row in boardString:
            print(row)
        print()
        '''
        #get where click
        #if white piece there, highlight possible moves
       


if __name__=='__main__':
    main()
    
    




#White square

#Black square
#Create squares
##Piece, space,color,image
#Create piece objects
##Pawns
##file,color,piece


#Game loop
#Whose turn is it
#Select a piece
    #Highlight available movement squares
    #Bc there might be a power up that allows you to take own pieces,  select a different piece? Esc? Figure Out
    #Each square has register for what piece is on it, get properties of that object to figure out where it can move - move/take
    #After move, check the new places that EVERY piece can move, is the enemy king hit?
    #Update board properties
    #Switch player

