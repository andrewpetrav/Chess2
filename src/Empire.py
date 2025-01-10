from abc import ABC
import pygame
from Piece import *

class Empire(ABC):
    def __init__(self,color):
        self.color=color
        self.pieces=[]
        self.wins=0
        self.losses=0
        self.opp=None
    def add_piece(self,piece):
        self.pieces.append(piece)
    def remove_piece(self,piece):
        self.pieces.remove(piece)
    def get_num_pieces(self):
        return len(self.pieces)
    def set_opp(self,otherEmpire):
        self.opp=otherEmpire
    def checkStalemate(self,otherEmpire):
        keepChecking=False
        stalemate=True
        #Cannot move without check?
        for p in pcsSame:
            moves=p.squaresCanMoveTo
            moves=checkForCheck(p,moves,turn,pcsDiff,king)
            if moves: #if any piece has a move they can make, not a stalemate
                stalemate=False
                keepChecking=True #only keep checking if stalemate is NOT found
                break
        #In a dead position?
        if keepChecking:
            #King v ...
            if len(pcsSame)==1 and pcsSame[0].type=='king':
                #King
                if len(pcsDiff)==1 and pcsDiff[0].type=='king':
                    keepChecking=False
                #King + Bishop
                
                #King + Knight
            #King + ... v King
                #Bishop
                #Knight
            #King + Light Square Bishop v King + Dark Square Bishop
            #King + Dark Square Bishop v King + Light Square Bishop



        if stalemate:
            stalemate()