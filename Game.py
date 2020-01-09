# -*- coding: utf-8 -*-
"""
Created on Sun May 06 17:15:21 2018

@author: Mohinish
"""

import abc

class GameBase(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def executeMove( self , move, player):
        """Calculates the resultant game state after the move and returns the state."""
        return
    
    @abc.abstractmethod
    def getPossibleMoves( self ):
        """Calculates best possible moves given the game state and returns the array of moves."""
        return
        
    @abc.abstractmethod
    def generateGameStates( self, moves):
        """Calculates new states based on the current state and the list of available moves.
           Returns the array of new game states."""
        return
    
    @abc.abstractmethod
    def isGameFinished( self ):
        """Returns True if the game is either won or lost or draw, otherwise false."""
        return
    
    @abc.abstractmethod
    def calculateTerminalScore( self ):
        """Returns a score for finished game state. 
           For ex: +100 for Win, -100 for Losing and +50 for a Draw."""
        return