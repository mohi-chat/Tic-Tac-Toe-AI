# -*- coding: utf-8 -*-
"""
Created on Sun May 06 21:59:10 2018

@author: Mohinish

GAME BOARD :
    
 0 | 1 | 2 |
-------------
 3 | 4 | 5 |
-------------
 6 | 7 | 8 |
 
The board above represents index assignment for each box.
Computers move is denoted by 'X' and players move will be
denoted by 'O'.
 
"""

from Game import GameBase
import copy

class TicTacToe( GameBase ):
    
    def __init__( self ):
        self.state = ['', '', '', 
                      '', '', '', 
                      '', '', '']                      
        self.winner = 'O'        
        self.draw   = False
        self.bestComputerMove = ''
        self.winOrientation = ''
        self.winOrientationIndex = 0
        self.MAX_PLAYER = 'X'
        self.MIN_PLAYER = 'O'
             
    def setGameState( self , newState ):
        self.state = newState
        
    def executeMove ( self , move , player):
        # Player can either be computer or user. Computer's move : 'X', user's move : 'O'
        if self.state[ int( move ) ] == '':
            self.state[ int( move ) ] = player
            return self.state
        else:
            return False
    
    def getPossibleMoves( self ):
        possibleMoves = []
        for i in range(9):
            if self.state[i] == '':
                possibleMoves.append( str(i) )
        return possibleMoves
        
    def generateGameStates( self, moves , player):
        gameStates = []
        for i in moves:
            newGamePosition = copy.deepcopy(self)
            newGamePosition.executeMove(i,player)
            gameStates.append( newGamePosition )
        return gameStates
    
    def resetGameData( self ):
        self.state = ['', '', '', 
                      '', '', '', 
                      '', '', '']                      
        self.winner = 'O'        
        self.draw   = False
        self.bestComputerMove = ''
    
    def isGameFinished( self ):
        # Checking Rows
        for row in range(3):
            if   self.state[3*row] == self.state[3*row+1] == self.state[3*row+2] != '':
                if self.state[3*row] == 'X':
                    self.winner = 'X'
                self.winOrientation = 'row'
                self.winOrientationIndex = row
                return True
        # Checking Columns
        for col in range(3):
            if   self.state[col] == self.state[col+3] == self.state[col+6] != '':
                if self.state[col] == 'X':
                    self.winner = 'X'
                self.winOrientation = 'col'
                self.winOrientationIndex = col
                return True
        # Checking Diagonals
        if self.state[0] == self.state[4] == self.state[8] != '':
            if self.state[0] == 'X':
                self.winner = 'X'
            self.winOrientation = 'diag'
            self.winOrientationIndex = 0 # 0 for right diagonal
            return True
        elif self.state[2] == self.state[4] == self.state[6] != '':
            if self.state[2] == 'X':
                self.winner = 'X'
            self.winOrientation = 'diag'
            self.winOrientationIndex = 1 # 1 for left diagonal
            return True

        for i in range(9):
            if self.state[i] == '':
                return False
        # The case when the game is Drawn
        self.draw = True
        return True
    
    def calculateTerminalScore( self ):
        if(self.draw):
            return 0
        else:
            if self.winner == 'X':
                return 100
            elif self.winner == 'O':
                return -100