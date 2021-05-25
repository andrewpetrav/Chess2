#Alright Andrew, let's do this
#Im adding this comment for a test commit
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
    game_type('traditional') #for now, all games will be traditional
    board.setup(all_pieces) #add board parameter based on board selection
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
            if board.board[x][y] in moves:
                #Special moves such as promotion, castling, en passant
                
                #CASTLING
                if sq.piece.type=='king' and abs(x-sq.row)>1:
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
                    sq.piece.set_pos(x,y) #update what position it'll be on
                    board.board[x][y].set_piece(sq.piece)
                    sq.set_piece(None)
                return True
            else:
                return False
        except:
            return False
    return True

def get_all_moves(): #calculates every possible move 
    all_moves={} #piece: all the moves it can make
    #should each square hold the data about who is attacking it? or just
    #what color
    for piece in all_pieces:
        all_moves[piece]=piece.get_moves(board)

def game_type(t): #traditional, atomic, etc (what type of chess)
    if t=='traditional':
        #Set globality
        global w_p
        global w_n
        global w_b
        global w_r
        global w_q
        global w_k
        global w_pieces
        global b_p
        global b_n
        global b_b
        global b_r
        global b_q
        global b_k
        global b_pieces
        global all_pieces
        #Pieces
        ##WHITE
        w_p=[Pawn(WHITE,board.board[0][6],wpi),Pawn(WHITE,board.board[1][6],wpi),Pawn(WHITE,board.board[2][6],wpi),Pawn(WHITE,board.board[3][6],wpi),
             Pawn(WHITE,board.board[4][6],wpi),Pawn(WHITE,board.board[5][6],wpi),Pawn(WHITE,board.board[6][6],wpi),Pawn(WHITE,board.board[7][6],wpi)]
        w_n=[Knight(WHITE,board.board[1][7],wni),Knight(WHITE,board.board[6][7],wni)]
        w_b=[Bishop(WHITE,board.board[2][7],wbi),Bishop(WHITE,board.board[5][7],wbi)]
        w_r=[Rook(WHITE,board.board[0][7],wri),Rook(WHITE,board.board[7][7],wri)]
        w_q=[Queen(WHITE,board.board[3][7],wqi)]
        w_k=[King(WHITE,board.board[4][7],wki)]
        w_pieces=w_p+w_n+w_b+w_r+w_q+w_k
        ##BLACK
        b_p=[Pawn(BLACK,board.board[0][1],bpi),Pawn(BLACK,board.board[1][1],bpi),Pawn(BLACK,board.board[2][1],bpi),Pawn(BLACK,board.board[3][1],bpi),
             Pawn(BLACK,board.board[4][1],bpi),Pawn(BLACK,board.board[5][1],bpi),Pawn(BLACK,board.board[6][1],bpi),Pawn(BLACK,board.board[7][1],bpi)]
        b_n=[Knight(BLACK,board.board[1][0],bni),Knight(BLACK,board.board[6][0],bni)]
        b_b=[Bishop(BLACK,board.board[2][0],bbi),Bishop(BLACK,board.board[5][0],bbi)]
        b_r=[Rook(BLACK,board.board[0][0],bri),Rook(BLACK,board.board[7][0],bri)]
        b_q=[Queen(BLACK,board.board[3][0],bqi)]
        b_k=[King(BLACK,board.board[4][0],bki)]
        b_pieces=b_p+b_n+b_b+b_r+b_q+b_k
        
        all_pieces=w_pieces+b_pieces #all pieces

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


