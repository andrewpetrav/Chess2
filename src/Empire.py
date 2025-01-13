from abc import ABC
import pygame
from Piece import *

BOARDBLACK=pygame.Color(211,139,67)
BOARDWHITE=pygame.Color(250,203,156)

class Empire(object):
    def __init__(self,color):
        self.color=color
        self.pieces=[]
        self.wins=0
        self.losses=0
        self.opp=None
        self.kings=[]
        self.queens=[]
        self.rooks=[]
        self.lightBishops=[]
        self.darkBishops=[]
        self.knights=[]
        self.pawns=[]
        self.kingCount=0
        self.queenCount=0
        self.rookCount=0
        self.lightBishopCount=0
        self.darkBishopCount=0
        self.knightCount=0
        self.pawnCount=0
    def add_piece(self,piece):
        if piece.type=='pawn':
            self.pawns.append(piece)
            self.pawnCount+=1
        elif piece.type=='knight':
            self.knights.append(piece)
            self.knightCount+=1
        elif piece.type=='bishop':
            if piece.square.color==BOARDWHITE:
                self.lightBishops.append(piece)
                self.lightBishopCount+=1
            elif piece.square.color==BOARDBLACK:
                self.darkBishops.append(piece)
                self.darkBishopCount+=1
        elif piece.type=='rook':
            self.rooks.append(piece)
            self.rookCount+=1
        elif piece.type=='queen':
            self.queens.append(piece)
            self.queenCount+=1
        elif piece.type=='king':
            self.kings.append(piece)
            self.kingCount+=1
        self.pieces.append(piece)
    def remove_piece(self,piece):
        self.pieces.remove(piece)
    def get_num_pieces(self):
        return len(self.pieces)
    def set_opp(self,otherEmpire):
        self.opp=otherEmpire
    def set_king(self,king):
        self.king=king
    def checkStalemate(self,otherEmpire):
        #King v ...
        if self.get_num_pieces==1:
            #King
            if otherEmpire.get_num_pieces==1:
                return True
            #King + Bishop
            
            #King + Knight
        #King + ... v King
            #Bishop
            #Knight
        #King + Light Square Bishop v King + Dark Square Bishop
        #King + Dark Square Bishop v King + Light Square Bishop
