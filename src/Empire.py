from abc import ABC
import pygame
from Piece import *

class Empire(object):
    def __init__(self,color):
        self.color=color
        self.pieces=[]
        self.wins=0
        self.losses=0
        self.opp=None
        self.king=None
    def add_piece(self,piece):
        self.pieces.append(piece)
    def remove_piece(self,piece):
        self.pieces.remove(piece)
    def get_num_pieces(self):
        return len(self.pieces)
    def set_opp(self,otherEmpire):
        self.opp=otherEmpire
    def set_king(self,king):
        self.king=king
    r'''
    def checkStalemate(self,otherEmpire):
        keepChecking=False
        stalemate=True
        #Cannot move without check?
        for p in otherEmpire.pieces:
            moves=p.squaresCanMoveTo
            moves=checkForCheck(p,moves,turn,otherEmpire.pieces,self.king) #TODO: define self.king
            if moves: #if any piece has a move they can make, not a stalemate
                stalemate=False
                keepChecking=True #only keep checking if stalemate is NOT found
                break
        #In a dead position?
        if keepChecking:
            #King v ...
            if self.get_num_pieces==1:
                #King
                if otherEmpire.get_num_pieces==1:
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
        '''