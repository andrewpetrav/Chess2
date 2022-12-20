#Alright Andrew, let's do this
#Im adding this comment for a test commit
import pygame, sys
from pygame.locals import *
import Board
from Board import *
import Piece
from Piece import *
from Surface import SURFACE
from Setup import *


pygame.init()

def main():
    #Get board in original state
    ##game_type('traditional') #for now, all games will be traditional
    #board.test(Rook(WHITE,board.board[4][4],wri))
    board.setup(all_pieces) #add board parameter based on board selection
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
        

def move_piece(sq,moves,pos):
    moved=False
    while not moved:
        col=int(pos[0]/square_size)
        row=int(pos[1]/square_size)
        #=int(pos[0]/square_size)
        try:
            if board.board[col][row] in moves:
                #Special moves such as promotion, castling, en passant, that involve changing more than one piece (not counting captures) or image of piece (promotion)
                if sq.piece.type=='king' and abs(col-sq.col)>1:
                    sq.piece.set_moved() #set king moved
                    #Short castle
                    if sq.row-x<1:
                        board.board[7][y].piece.set_moved() #set rook moved
                        board.board[5][y].set_piece(board.board[7][y].piece)
                        board.board[7][y].set_piece(None)
                        board.board[6][y].set_piece(sq.piece)
                        sq.set_piece(None)
                    #Long castle
                    else:
                        board.board[0][y].piece.set_moved() #set rook moved
                        board.board[3][y].set_piece(board.board[0][y].piece)
                        board.board[0][y].set_piece(None)
                        board.board[2][y].set_piece(sq.piece)
                        sq.set_piece(None)
                else:
                    #updated Moved attribute on piece
                    sq.piece.set_moved()
                    sq.piece.set_pos(col,row) #update what position it'll be on
                    board.board[col][row].set_piece(sq.piece)
                    sq.set_piece(None)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
    return True

def get_all_moves(): #calculates every possible move 
    all_moves={} #piece: all the moves it can make
    #should each square hold the data about who is attacking it? or just
    #what color
    for piece in all_pieces:
        all_moves[piece]=piece.get_moves(board)


    
def kingInCheck(color): #checks to see if move puts/stops if OWN king is in check
    if color==WHITE:
        return w_k.inCheck
    elif color==BLACK:
        return b_k.inCheck
    
def game():
    turn=WHITE
    while True:
        move_completed=False #if true, give control to other player
        #king_in_check=Piece.King.kingCheck(turn) #is the king currently in check
        while not move_completed:
            valid_square_selection=False 
            valid_move_selection=False
            
            while not valid_square_selection:
                for event in pygame.event.get():
                    if event.type==MOUSEBUTTONDOWN:
                        pos=pygame.mouse.get_pos()
                        sq=select_square(turn,pos)
                        if sq: #if valid square
                            valid_square_selection=True
                            break
            moves=sq.piece.get_moves(board) #get moves of piece at selected square
            sq.set_selected()
            if moves: #highlight
                for move in moves:
                    move.set_highlighted() #make sure to unhighlight
            board.draw_board()
            pygame.display.update()
            loop_completed=False
            while not valid_move_selection and not loop_completed:
                for event in pygame.event.get():
                    if event.type==MOUSEBUTTONUP:
                        pos=pygame.mouse.get_pos()
                        valid_move_selection=move_piece(sq,moves,pos) #clicked valid square
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
        
        #switch turns
        if turn==WHITE:
            turn=BLACK
        else:
            turn=WHITE
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
