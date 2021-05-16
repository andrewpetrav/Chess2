#Alright Andrew, let's do this
import pygame, sys
from pygame.locals import *
import Board
from Board import *
import Piece
from Piece import *
from Surface import SURFACE

turn=WHITE #whose turn
board=Board()
pygame.init()


def main():
    #Get board in original state
    board.original_setup()
    board.draw_board()
    pygame.display.update()
    game()
    
def select_square(turn,pos):
    piece_selected=False #is a piece selected
    while not piece_selected:
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
        x=int(pos[0]/square_size)
        y=int(pos[1]/square_size)
        try:
            if board.board[x][y].get_highlighted()==True:
                #Special moves such as promotion, castling, en passant
                
                #CASTLING
                if sq.get_piece().type=='king' and abs(x-sq.row)>1:
                    sq.get_piece().set_moved() #set king moved
                    #Short castle
                    if sq.row-x<1:
                        board.board[7][y].get_piece().set_moved() #set rook moved
                        board.board[5][y].set_piece(board.board[7][y].get_piece())
                        board.board[7][y].set_piece(None)
                        board.board[6][y].set_piece(sq.get_piece())
                        sq.set_piece(None)
                    #Long castle
                    else:
                        board.board[0][y].get_piece().set_moved() #set rook moved
                        board.board[3][y].set_piece(board.board[0][y].get_piece())
                        board.board[0][y].set_piece(None)
                        board.board[2][y].set_piece(sq.get_piece())
                        sq.set_piece(None)
                else:
                    #updated Moved attribute on piece
                    sq.get_piece().set_moved()
                    sq.get_piece().set_pos(x,y) #update what position it'll be on
                    board.board[x][y].set_piece(sq.get_piece())
                    sq.set_piece(None)
                return True
            else:
                return False
        except:
            return False
    return True
        
             
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
                        #print(pos)
                        sq=select_square(turn,pos)
                        if sq: #if valid square
                            valid_square_selection=True
                            break
            moves=sq.get_moves(board)
            sq.set_selected()
            if moves:
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
            if moves:
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
    
#Colors
WHITE=pygame.Color(255,255,255)
BLACK=pygame.Color(0,0,0)
RED=pygame.Color(255,0,0)    
#Piece images
#White pieces
wpi=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\White\w_p.png').convert_alpha()
wni=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\White\w_n.png').convert_alpha()
wbi=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\White\w_b.png').convert_alpha()
wri=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\White\w_r.png').convert_alpha()
wqi=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\White\w_q.png').convert_alpha()
wki=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\White\w_k.png').convert_alpha()
#Black pieces
bpi=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\Black\b_p.png').convert_alpha()
bni=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\Black\b_n.png').convert_alpha()
bbi=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\Black\b_b.png').convert_alpha()
bri=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\Black\b_r.png').convert_alpha()
bqi=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\Black\b_q.png').convert_alpha()
bki=pygame.image.load(r'C:\Users\Andrew\Desktop\Chess\Pieces\Black\b_k.png').convert_alpha()
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

#Pieces
##WHITE
w_p=[Pawn(WHITE,board.board[0][6],wpi),Pawn(WHITE,board.board[1][6],wpi),Pawn(WHITE,board.board[2][6],wpi),Pawn(WHITE,board.board[3][6],wpi),
     Pawn(WHITE,board.board[4][6],wpi),Pawn(WHITE,board.board[5][6],wpi),Pawn(WHITE,board.board[6][6],wpi),Pawn(WHITE,board.board[7][6],wpi)]
w_n=[Knight(),Knight()]
w_b=[Bishop(),Bishop()]
w_r=[Rook(),Rook()]
w_q=[Queen()]
w_k=[King()]
w_pieces=[w_p,w_n,w_b,w_r,w_q,w_k]
##BLACK
b_p=[Pawn(),Pawn(),Pawn(),Pawn(),Pawn(),Pawn(),Pawn(),Pawn()]
b_n=[Knight(),Knight()]
b_b=[Bishop(),Bishop()]
b_r=[Rook(),Rook()]
b_q=[Queen()]
b_k=[King()]
b_pieces=[b_p,b_n,b_b,b_r,b_q,b_k]

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

